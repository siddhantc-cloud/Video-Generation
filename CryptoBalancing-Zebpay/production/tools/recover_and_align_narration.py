#!/usr/bin/env python3
"""Recover one existing ElevenLabs take into frame WAVs and exact-copy word timings.

This tool never calls a provider. It splits the immutable recovered master at
documented paragraph silences and uses the locally cached faster-whisper model
only to time the approved words.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
from datetime import datetime, timezone
from pathlib import Path

from faster_whisper import WhisperModel


FRAME_BOUNDARIES = [0.0, 8.669, 17.119, 27.132, 36.076, 41.637, 46.486349]
# Whole-program ASR on the encoded v001 review cut found that Whisper's
# prompted per-segment alignment stretched the first word back across the
# leading paragraph silence. Later word boundaries were already aligned.
# These frame-relative onsets preserve the exact audio while preventing an
# early karaoke highlight at each reset.
FIRST_WORD_ONSETS = {1: 0.0, 2: 0.651, 3: 0.701, 4: 0.288, 5: 0.344, 6: 0.463}


def parse_script(path: Path) -> list[tuple[int, str]]:
    frames: list[tuple[int, str]] = []
    current_frame: int | None = None
    current_text: list[str] = []

    def flush() -> None:
        nonlocal current_frame, current_text
        if current_frame is not None and current_text:
            frames.append((current_frame, " ".join(current_text).strip()))
        current_text = []

    for line in path.read_text(encoding="utf-8").splitlines():
        heading = re.match(r"^##\s+Line\s+\d+.*?\(Frame\s+(\d+)\)", line, re.I)
        if heading:
            flush()
            current_frame = int(heading.group(1))
            continue
        spoken = re.match(r"^(?: {4,}|\t)(.+)$", line)
        if current_frame is not None and spoken:
            current_text.append(spoken.group(1).strip())
    flush()
    return frames


def run(command: list[str]) -> str:
    result = subprocess.run(command, check=True, capture_output=True, text=True)
    return result.stdout.strip()


def norm(value: str) -> str:
    return re.sub(r"[^a-z0-9]", "", value.lower())


def align_words(approved_text: str, hypothesis: list[dict], duration: float) -> list[dict]:
    approved = re.findall(r"\S+", approved_text)
    if not hypothesis:
        step = duration / max(1, len(approved))
        return [
            {
                "id": f"w{index + 1}",
                "text": token,
                "start": round(index * step, 3),
                "end": round((index + 1) * step, 3),
            }
            for index, token in enumerate(approved)
        ]

    output: list[dict] = []
    hyp_index = 0
    for index, token in enumerate(approved):
        wanted = norm(token)
        start_index = min(hyp_index, len(hypothesis) - 1)
        combined = ""
        end_index = start_index
        while end_index < len(hypothesis):
            combined += norm(hypothesis[end_index]["text"])
            if combined == wanted or len(combined) >= len(wanted):
                break
            end_index += 1

        if combined != wanted:
            # Keep sequence progress even when the recognizer chooses a synonym.
            end_index = start_index

        start = float(hypothesis[start_index]["start"])
        end = float(hypothesis[min(end_index, len(hypothesis) - 1)]["end"])
        output.append(
            {
                "id": f"w{index + 1}",
                "text": token,
                "start": round(max(0.0, start), 3),
                "end": round(min(duration, max(start + 0.03, end)), 3),
            }
        )
        hyp_index = min(end_index + 1, len(hypothesis))

    # If recognizer/token grouping ran out early, spread remaining words through
    # the final spoken interval without changing approved copy.
    for index in range(1, len(output)):
        if output[index]["start"] < output[index - 1]["end"] - 0.02:
            output[index]["start"] = round(output[index - 1]["end"], 3)
        if output[index]["end"] <= output[index]["start"]:
            output[index]["end"] = round(min(duration, output[index]["start"] + 0.08), 3)
    return output


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--project", required=True)
    parser.add_argument("--script", default="SCRIPT.md")
    parser.add_argument(
        "--master", default="assets/audio/voice/narration-v001-provider-master.mp3"
    )
    parser.add_argument("--history-item-id", required=True)
    args = parser.parse_args()

    project = Path(args.project).resolve()
    script_path = (project / args.script).resolve()
    master_path = (project / args.master).resolve()
    output_dir = project / "assets/audio/voice"
    output_dir.mkdir(parents=True, exist_ok=True)

    frames = parse_script(script_path)
    if len(frames) != 6:
        raise SystemExit(f"Expected 6 script frames, found {len(frames)}")

    model = WhisperModel("small.en", device="cpu", compute_type="int8")
    voices: list[dict] = []
    segments_meta: list[dict] = []

    for index, (frame, approved_text) in enumerate(frames):
        start = FRAME_BOUNDARIES[index]
        end = FRAME_BOUNDARIES[index + 1]
        output = output_dir / f"{frame:02d}-narration-v001.wav"
        run(
            [
                "ffmpeg",
                "-hide_banner",
                "-loglevel",
                "error",
                "-y",
                "-ss",
                str(start),
                "-to",
                str(end),
                "-i",
                str(master_path),
                "-ac",
                "2",
                "-ar",
                "48000",
                "-c:a",
                "pcm_s24le",
                str(output),
            ]
        )
        duration = float(
            run(
                [
                    "ffprobe",
                    "-v",
                    "error",
                    "-show_entries",
                    "format=duration",
                    "-of",
                    "csv=p=0",
                    str(output),
                ]
            )
        )
        transcription, info = model.transcribe(
            str(output),
            language="en",
            beam_size=5,
            word_timestamps=True,
            initial_prompt=approved_text,
            vad_filter=False,
        )
        hypothesis = []
        transcript_text = []
        for segment in transcription:
            transcript_text.append(segment.text.strip())
            for word in segment.words or []:
                hypothesis.append(
                    {
                        "text": word.word.strip(),
                        "start": float(word.start),
                        "end": float(word.end),
                    }
                )
        timed_words = align_words(approved_text, hypothesis, duration)
        if timed_words:
            timed_words[0]["start"] = FIRST_WORD_ONSETS[frame]
        rel_path = output.relative_to(project).as_posix()
        voices.append(
            {
                "frame": frame,
                "path": rel_path,
                "duration_s": round(duration, 3),
                "words": [
                    {**word, "id": f"f{frame}-{word['id']}"} for word in timed_words
                ],
            }
        )
        segments_meta.append(
            {
                "frame": frame,
                "approved_text": approved_text,
                "local_transcript": " ".join(transcript_text),
                "language_probability": round(float(info.language_probability), 5),
                "source_start_s": start,
                "source_end_s": end,
                "duration_s": round(duration, 3),
                "file": rel_path,
                "sha256": sha256(output),
            }
        )

    (project / "audio_meta.json").write_text(
        json.dumps({"bgm": None, "voices": voices, "sfx": []}, indent=2),
        encoding="utf-8",
    )
    metadata = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "provider": "ElevenLabs",
        "recovery_mode": "history audio download; no second synthesis",
        "history_item_id": args.history_item_id,
        "voice_id": "cgSgspJ2msm6clMCkdW9",
        "voice_name": "Jessica - Playful, Bright, Warm",
        "model_id": "eleven_multilingual_v2",
        "submitted_characters": sum(len(text) for _, text in frames) + 2 * (len(frames) - 1),
        "source_script": script_path.relative_to(project).as_posix(),
        "provider_master": master_path.relative_to(project).as_posix(),
        "provider_master_sha256": sha256(master_path),
        "frame_boundaries_s": FRAME_BOUNDARIES,
        "boundary_method": "midpoints of paragraph-level silences measured with ffmpeg silencedetect at -36 dB / 0.20 s",
        "word_timing_method": "local faster-whisper small.en; approved copy retained exactly",
        "segments": segments_meta,
    }
    (output_dir / "narration-v001-metadata.json").write_text(
        json.dumps(metadata, indent=2), encoding="utf-8"
    )
    print(
        f"Recovered {len(voices)} frame WAVs; total {sum(v['duration_s'] for v in voices):.3f}s."
    )


if __name__ == "__main__":
    main()
