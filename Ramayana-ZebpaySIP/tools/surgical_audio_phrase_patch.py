#!/usr/bin/env python3
"""Replace one frame-owned narration phrase and rebuild its word boundaries."""

from __future__ import annotations

import argparse
import json
import subprocess
from pathlib import Path

import numpy as np
import soundfile as sf


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--base-audio", type=Path, required=True)
    parser.add_argument("--base-word-timings", type=Path, required=True)
    parser.add_argument("--replacement-audio", type=Path, required=True)
    parser.add_argument("--replacement-scribe", type=Path, required=True)
    parser.add_argument("--replacement-display-text", required=True)
    parser.add_argument("--beat-id", required=True)
    parser.add_argument("--start-frame", type=int, required=True)
    parser.add_argument("--end-frame", type=int, required=True)
    parser.add_argument("--trim-start-seconds", type=float, default=0.0)
    parser.add_argument("--fps", type=int, default=30)
    parser.add_argument("--sample-rate", type=int, default=48_000)
    parser.add_argument("--fade-ms", type=float, default=30.0)
    parser.add_argument("--output-audio", type=Path, required=True)
    parser.add_argument("--output-word-timings", type=Path, required=True)
    parser.add_argument("--metadata", type=Path, required=True)
    args = parser.parse_args()

    if args.end_frame <= args.start_frame:
        raise ValueError("End frame must be greater than start frame")
    samples_per_frame = args.sample_rate // args.fps
    if samples_per_frame * args.fps != args.sample_rate:
        raise ValueError("Sample rate must divide evenly by fps")

    base, rate = sf.read(args.base_audio, dtype="float64", always_2d=True)
    if rate != args.sample_rate or base.shape[1] != 1:
        raise ValueError("Base narration must be mono at the requested sample rate")

    start_sample = args.start_frame * samples_per_frame
    end_sample = args.end_frame * samples_per_frame
    target_samples = end_sample - start_sample
    target_seconds = target_samples / args.sample_rate

    scribe = json.loads(args.replacement_scribe.read_text(encoding="utf-8-sig"))
    source_duration = float(scribe["audio_duration_secs"]) - args.trim_start_seconds
    tempo = source_duration / target_seconds
    fade_seconds = args.fade_ms / 1000.0
    fade_out_start = max(0.0, target_seconds - fade_seconds)
    filter_graph = (
        f"aresample={args.sample_rate},"
        f"rubberband=tempo={tempo:.12f},"
        f"apad,atrim=end_sample={target_samples},"
        f"afade=t=in:st=0:d={fade_seconds:.6f},"
        f"afade=t=out:st={fade_out_start:.6f}:d={fade_seconds:.6f}"
    )
    command = [
        "ffmpeg",
        "-v",
        "error",
        "-ss",
        f"{args.trim_start_seconds:.6f}",
        "-i",
        str(args.replacement_audio),
        "-af",
        filter_graph,
        "-ar",
        str(args.sample_rate),
        "-ac",
        "1",
        "-f",
        "f64le",
        "-",
    ]
    replacement_bytes = subprocess.check_output(command)
    replacement = np.frombuffer(replacement_bytes, dtype="<f8")
    if len(replacement) != target_samples:
        raise RuntimeError(
            f"Replacement has {len(replacement)} samples; expected {target_samples}"
        )

    patched = base[:, 0].copy()
    patched[start_sample:end_sample] = replacement
    args.output_audio.parent.mkdir(parents=True, exist_ok=True)
    sf.write(args.output_audio, patched, args.sample_rate, subtype="PCM_24")

    timing = json.loads(args.base_word_timings.read_text(encoding="utf-8-sig"))
    old_words = timing["words"]
    before = [word for word in old_words if word.get("beat_id") != args.beat_id]
    replacement_words = []
    slot_start = args.start_frame / args.fps
    for word in scribe["words"]:
        if word.get("type") != "word":
            continue
        source_start = max(0.0, float(word["start"]) - args.trim_start_seconds)
        source_end = max(source_start, float(word["end"]) - args.trim_start_seconds)
        replacement_words.append(
            {
                "text": word["text"],
                "start_sec": slot_start + source_start / tempo,
                "end_sec": min(
                    args.end_frame / args.fps,
                    slot_start + source_end / tempo,
                ),
                "beat_id": args.beat_id,
            }
        )
    words = sorted(before + replacement_words, key=lambda word: word["start_sec"])
    for index, word in enumerate(words):
        word["index"] = index

    timing["source"] = "elevenlabs-surgical-phrase-repair"
    timing["audio"] = str(args.output_audio)
    timing["words"] = words
    timing["word_count"] = len(words)
    timing["text"] = timing["text"].replace(
        "A SIP lets you invest the same amount regularly",
        args.replacement_display_text,
    )
    timing["repair"] = {
        "replaced_beat": args.beat_id,
        "output_start_frame": args.start_frame,
        "output_end_frame_exclusive": args.end_frame,
        "source_candidate": str(args.replacement_audio),
        "source_text": scribe["text"],
        "display_text": args.replacement_display_text,
        "trim_start_seconds": args.trim_start_seconds,
        "tempo": tempo,
        "pitch_preserved": True,
    }
    args.output_word_timings.parent.mkdir(parents=True, exist_ok=True)
    args.output_word_timings.write_text(
        json.dumps(timing, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )

    metadata = {
        "schema": 1,
        "base_audio": str(args.base_audio),
        "replacement_audio": str(args.replacement_audio),
        "output_audio": str(args.output_audio),
        "beat_id": args.beat_id,
        "start_frame": args.start_frame,
        "end_frame_exclusive": args.end_frame,
        "target_samples": target_samples,
        "target_seconds": target_seconds,
        "trim_start_seconds": args.trim_start_seconds,
        "tempo": tempo,
        "pitch_preserved": True,
        "fade_ms": args.fade_ms,
        "replacement_display_text": args.replacement_display_text,
    }
    args.metadata.parent.mkdir(parents=True, exist_ok=True)
    args.metadata.write_text(
        json.dumps(metadata, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    print(json.dumps(metadata, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
