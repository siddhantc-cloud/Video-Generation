#!/usr/bin/env python3
"""Conform one timestamped narration to an integer-frame phrase map.

The input performance remains continuous: this tool partitions it only in the
silence between mapped phrases. A segment that overruns its existing picture
slot is accelerated with Rubber Band without changing pitch. A shorter segment
keeps its natural delivery and receives silence at the tail. Every output slot
therefore has exactly the sample count implied by its frame range. ElevenLabs
character alignment remains the default input; Scribe word timing is accepted
when the canonical display text is supplied separately.
"""

from __future__ import annotations

import argparse
import json
import math
import re
import subprocess
from pathlib import Path
from typing import Any


WORD_RE = re.compile(r"\b[\w]+(?:['’][\w]+)?\b", re.UNICODE)


def run(command: list[str]) -> None:
    subprocess.run(command, check=True)


def probe_duration(path: Path) -> float:
    result = subprocess.run(
        [
            "ffprobe",
            "-v",
            "error",
            "-show_entries",
            "format=duration",
            "-of",
            "default=noprint_wrappers=1:nokey=1",
            str(path),
        ],
        check=True,
        capture_output=True,
        text=True,
    )
    return float(result.stdout.strip())


def normalized_token(value: str) -> str:
    return "".join(character.lower() for character in value if character.isalnum())


def load_scribe_words(
    payload: dict[str, Any], canonical_text: str
) -> list[dict[str, Any]]:
    canonical_matches = list(WORD_RE.finditer(canonical_text))
    canonical_tokens = [normalized_token(match.group(0)) for match in canonical_matches]
    scribe_words = [
        word
        for word in payload.get("words", [])
        if word.get("type") == "word" and normalized_token(str(word.get("text", "")))
    ]
    scribe_tokens = [normalized_token(str(word["text"])) for word in scribe_words]
    canonical_stream = "".join(canonical_tokens)
    scribe_stream = "".join(scribe_tokens)
    if canonical_stream != scribe_stream:
        raise ValueError(
            "Scribe transcript does not match the canonical narration after "
            "case/punctuation/word-boundary normalization. Reject or repair the take "
            "before conforming it."
        )

    scribe_spans: list[dict[str, Any]] = []
    cursor = 0
    for word, token in zip(scribe_words, scribe_tokens):
        scribe_spans.append(
            {
                "start_offset": cursor,
                "end_offset": cursor + len(token),
                "start_sec": float(word["start"]),
                "end_sec": float(word["end"]),
            }
        )
        cursor += len(token)

    def offset_to_time(offset: int, boundary: str) -> float:
        if boundary not in {"start", "end"}:
            raise ValueError(f"Unsupported boundary direction: {boundary}")
        if offset == len(scribe_stream):
            return float(scribe_spans[-1]["end_sec"])
        for span in scribe_spans:
            span_start = int(span["start_offset"])
            span_end = int(span["end_offset"])
            contains_offset = (
                span_start <= offset < span_end
                if boundary == "start"
                else span_start < offset <= span_end
            )
            if contains_offset:
                token_length = int(span["end_offset"]) - int(span["start_offset"])
                fraction = (offset - int(span["start_offset"])) / token_length
                return float(span["start_sec"]) + fraction * (
                    float(span["end_sec"]) - float(span["start_sec"])
                )
        raise ValueError(f"Unable to map canonical character offset {offset}.")

    words: list[dict[str, Any]] = []
    cursor = 0
    for index, (match, token) in enumerate(zip(canonical_matches, canonical_tokens)):
        start_offset = cursor
        end_offset = cursor + len(token)
        words.append(
            {
                "index": index,
                "text": match.group(0),
                "start_sec": offset_to_time(start_offset, "start"),
                "end_sec": offset_to_time(end_offset, "end"),
            }
        )
        cursor = end_offset
    return words


def load_words(
    payload: dict[str, Any], canonical_text: str | None = None
) -> list[dict[str, Any]]:
    if "alignment" not in payload:
        if canonical_text is None:
            raise ValueError(
                "Scribe timing input requires --canonical-text so provider word "
                "boundaries can be mapped to the approved display script."
            )
        return load_scribe_words(payload, canonical_text)

    text = payload["text"]
    alignment = payload["alignment"]
    characters = alignment["characters"]
    starts = alignment["character_start_times_seconds"]
    ends = alignment["character_end_times_seconds"]

    if len(characters) != len(text):
        raise ValueError(
            f"Alignment has {len(characters)} characters but source text has {len(text)}."
        )

    words: list[dict[str, Any]] = []
    for index, match in enumerate(WORD_RE.finditer(text)):
        last_character = match.end() - 1
        words.append(
            {
                "index": index,
                "text": match.group(0),
                "start_sec": float(starts[match.start()]),
                "end_sec": float(ends[last_character]),
            }
        )
    return words


def phrase_boundaries(
    beats: list[dict[str, Any]],
    words: list[dict[str, Any]],
    source_duration: float,
    fade_seconds: float,
) -> list[float]:
    boundaries = [
        max(0.0, float(words[0]["start_sec"]) - fade_seconds)
    ]
    for beat in beats[1:]:
        first = int(beat["first_word_index"])
        previous_end = float(words[first - 1]["end_sec"])
        phrase_start = float(words[first]["start_sec"])
        gap = max(0.0, phrase_start - previous_end)
        pre_roll = min(fade_seconds, gap / 2.0)
        boundaries.append(phrase_start - pre_roll)
    boundaries.append(source_duration)
    return boundaries


def escape_concat_path(path: Path) -> str:
    return path.resolve().as_posix().replace("'", r"'\''")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("source_audio", type=Path)
    parser.add_argument("alignment_json", type=Path)
    parser.add_argument("phrase_map_json", type=Path)
    parser.add_argument("output_wav", type=Path)
    parser.add_argument("--segments-dir", type=Path, required=True)
    parser.add_argument("--edl", type=Path, required=True)
    parser.add_argument("--word-timings", type=Path)
    parser.add_argument(
        "--canonical-text",
        type=Path,
        help="Approved display text; required when alignment_json is Scribe word timing.",
    )
    parser.add_argument("--sample-rate", type=int, default=48_000)
    parser.add_argument("--fade-ms", type=float, default=30.0)
    args = parser.parse_args()

    alignment_payload = json.loads(args.alignment_json.read_text(encoding="utf-8-sig"))
    phrase_map = json.loads(args.phrase_map_json.read_text(encoding="utf-8-sig"))
    beats = phrase_map["beats"]
    fps = int(phrase_map["fps"])
    canonical_text = (
        args.canonical_text.read_text(encoding="utf-8-sig").strip()
        if args.canonical_text
        else None
    )
    words = load_words(alignment_payload, canonical_text)
    alignment_source = (
        "scribe-word-timing" if "alignment" not in alignment_payload else "elevenlabs-alignment"
    )
    resolved_text = canonical_text or alignment_payload["text"]

    expected_words = max(int(beat["first_word_index"]) for beat in beats) + 1
    if len(words) < expected_words:
        raise ValueError(
            f"Only {len(words)} aligned words are available for a map requiring "
            f"at least {expected_words}."
        )

    source_duration = probe_duration(args.source_audio)
    fade_seconds = args.fade_ms / 1000.0
    boundaries = phrase_boundaries(beats, words, source_duration, fade_seconds)
    args.segments_dir.mkdir(parents=True, exist_ok=True)
    args.output_wav.parent.mkdir(parents=True, exist_ok=True)
    args.edl.parent.mkdir(parents=True, exist_ok=True)

    samples_per_frame = args.sample_rate / fps
    if not samples_per_frame.is_integer():
        raise ValueError(
            f"{args.sample_rate} Hz does not produce an integer sample count at {fps} fps."
        )

    concat_lines: list[str] = []
    records: list[dict[str, Any]] = []
    word_records: list[dict[str, Any]] = []

    for index, beat in enumerate(beats):
        source_start = boundaries[index]
        source_end = boundaries[index + 1]
        source_seconds = source_end - source_start
        frames = int(beat["end_frame"]) - int(beat["start_frame"])
        target_samples = int(frames * samples_per_frame)
        target_seconds = target_samples / args.sample_rate
        tempo = source_seconds / target_seconds if source_seconds > target_seconds else 1.0
        pad_seconds = max(0.0, target_seconds - source_seconds)
        segment_path = args.segments_dir / f"{index:02d}_{beat['id']}.wav"

        filters = [
            f"atrim=start={source_start:.9f}:end={source_end:.9f}",
            "asetpts=PTS-STARTPTS",
            f"aresample={args.sample_rate}",
        ]
        if tempo > 1.000001:
            filters.append(f"rubberband=tempo={tempo:.9f}:pitch=1.0")
            pad_seconds = 0.0
        filters.extend(
            [
                f"apad=whole_len={target_samples}",
                f"atrim=end_sample={target_samples}",
                "asetpts=N/SR/TB",
            ]
        )

        effective_fade = min(fade_seconds, target_seconds / 4.0)
        filters.extend(
            [
                f"afade=t=in:st=0:d={effective_fade:.6f}",
                (
                    "afade=t=out:"
                    f"st={target_seconds - effective_fade:.6f}:d={effective_fade:.6f}"
                ),
            ]
        )

        run(
            [
                "ffmpeg",
                "-y",
                "-hide_banner",
                "-loglevel",
                "error",
                "-i",
                str(args.source_audio),
                "-af",
                ",".join(filters),
                "-ar",
                str(args.sample_rate),
                "-ac",
                "1",
                "-c:a",
                "pcm_s24le",
                str(segment_path),
            ]
        )

        actual_seconds = probe_duration(segment_path)
        tolerance = 1.0 / args.sample_rate
        if abs(actual_seconds - target_seconds) > tolerance:
            raise RuntimeError(
                f"{beat['id']} is {actual_seconds:.9f}s, expected {target_seconds:.9f}s."
            )

        first_word = int(beat["first_word_index"])
        phrase_onset_in_slot = float(words[first_word]["start_sec"]) - source_start
        if tempo > 1.000001:
            phrase_onset_in_slot /= tempo

        last_word_exclusive = (
            int(beats[index + 1]["first_word_index"])
            if index + 1 < len(beats)
            else len(words)
        )
        output_start_seconds = int(beat["start_frame"]) / fps
        for word in words[first_word:last_word_exclusive]:
            local_start = float(word["start_sec"]) - source_start
            local_end = float(word["end_sec"]) - source_start
            if tempo > 1.000001:
                local_start /= tempo
                local_end /= tempo
            word_records.append(
                {
                    "index": int(word["index"]),
                    "text": word["text"],
                    "start_sec": output_start_seconds + max(0.0, local_start),
                    "end_sec": min(
                        output_start_seconds + target_seconds,
                        output_start_seconds + max(0.0, local_end),
                    ),
                    "beat_id": beat["id"],
                }
            )

        concat_lines.append(f"file '{escape_concat_path(segment_path)}'")
        records.append(
            {
                "id": beat["id"],
                "phrase": beat["phrase"],
                "output_start_frame": int(beat["start_frame"]),
                "output_end_frame_exclusive": int(beat["end_frame"]),
                "frames": frames,
                "target_samples": target_samples,
                "target_seconds": target_seconds,
                "source_start_seconds": source_start,
                "source_end_seconds": source_end,
                "source_seconds": source_seconds,
                "tempo": tempo,
                "tail_pad_seconds_before_fades": pad_seconds,
                "phrase_onset_in_slot_seconds": phrase_onset_in_slot,
                "segment": segment_path.as_posix(),
            }
        )

    concat_path = args.segments_dir / "concat.txt"
    concat_path.write_text("\n".join(concat_lines) + "\n", encoding="utf-8")
    run(
        [
            "ffmpeg",
            "-y",
            "-hide_banner",
            "-loglevel",
            "error",
            "-f",
            "concat",
            "-safe",
            "0",
            "-i",
            str(concat_path),
            "-ar",
            str(args.sample_rate),
            "-ac",
            "1",
            "-c:a",
            "pcm_s24le",
            str(args.output_wav),
        ]
    )

    total_frames = sum(record["frames"] for record in records)
    total_samples = int(total_frames * samples_per_frame)
    expected_seconds = total_samples / args.sample_rate
    actual_seconds = probe_duration(args.output_wav)
    if abs(actual_seconds - expected_seconds) > 1.0 / args.sample_rate:
        raise RuntimeError(
            f"Master is {actual_seconds:.9f}s, expected {expected_seconds:.9f}s."
        )

    edl = {
        "schema": 1,
        "source_audio": args.source_audio.as_posix(),
        "alignment": args.alignment_json.as_posix(),
        "alignment_source": alignment_source,
        "canonical_text": args.canonical_text.as_posix() if args.canonical_text else None,
        "phrase_map": args.phrase_map_json.as_posix(),
        "fps": fps,
        "sample_rate": args.sample_rate,
        "fade_ms": args.fade_ms,
        "source_duration_seconds": source_duration,
        "output_frames": total_frames,
        "output_samples": total_samples,
        "output_duration_seconds": actual_seconds,
        "sync_locked": math.isclose(
            actual_seconds,
            expected_seconds,
            abs_tol=1.0 / args.sample_rate,
        ),
        "segments": records,
    }
    args.edl.write_text(json.dumps(edl, indent=2) + "\n", encoding="utf-8")
    if args.word_timings:
        args.word_timings.parent.mkdir(parents=True, exist_ok=True)
        word_timing_payload = {
            "schema": 1,
            "source": f"{alignment_source}-phrase-locked",
            "text": resolved_text,
            "word_count": len(word_records),
            "fps": fps,
            "sample_rate": args.sample_rate,
            "audio": args.output_wav.as_posix(),
            "words": word_records,
        }
        args.word_timings.write_text(
            json.dumps(word_timing_payload, indent=2) + "\n",
            encoding="utf-8",
        )
    print(
        f"SYNC LOCKED: {total_frames} frames, {total_samples} samples, "
        f"{actual_seconds:.3f}s"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
