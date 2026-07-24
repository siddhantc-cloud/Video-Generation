#!/usr/bin/env python3
"""Build a frame-locked narration + SFX + music mix without master normalization.

The v006 narration/SFX relationship is the reference:

    narration: +0.2 dB
    native SFX: -10.0 dB, followed by the same +0.2 dB

Music is added as a third, independently controlled stem. It is ducked only by
the narration activity envelope. If the resulting sample peak exceeds the
requested ceiling, only the music is reduced; narration and SFX remain fixed.
"""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

import numpy as np
import soundfile as sf


def db_to_gain(db: float) -> float:
    return 10.0 ** (db / 20.0)


def gain_to_db(gain: float) -> float:
    return 20.0 * math.log10(max(gain, 1e-12))


def read_audio(path: Path, expected_rate: int) -> np.ndarray:
    audio, rate = sf.read(path, dtype="float64", always_2d=True)
    if rate != expected_rate:
        raise ValueError(f"{path}: expected {expected_rate} Hz, found {rate} Hz")
    return audio


def stereo(audio: np.ndarray) -> np.ndarray:
    if audio.shape[1] == 1:
        # Match FFmpeg's equal-power mono-to-stereo rematrix used by the
        # approved v006 master: each output channel receives mono / sqrt(2).
        return np.repeat(audio / math.sqrt(2.0), 2, axis=1)
    if audio.shape[1] == 2:
        return audio
    raise ValueError(f"Expected mono or stereo audio, found {audio.shape[1]} channels")


def speech_duck_envelope(
    narration: np.ndarray,
    sample_rate: int,
    threshold_dbfs: float,
    duck_db: float,
    attack_ms: float,
    release_ms: float,
) -> np.ndarray:
    """Return a seek-safe gain envelope using a 20 ms narration RMS detector."""

    mono = narration.mean(axis=1)
    hop = max(1, round(sample_rate * 0.020))
    frame_count = math.ceil(len(mono) / hop)
    padded = np.pad(mono, (0, frame_count * hop - len(mono)))
    rms = np.sqrt(np.mean(padded.reshape(frame_count, hop) ** 2, axis=1) + 1e-12)
    active = 20.0 * np.log10(rms) >= threshold_dbfs
    target_frames = np.where(active, db_to_gain(duck_db), 1.0)
    target = np.repeat(target_frames, hop)[: len(mono)]

    attack_coeff = math.exp(-1.0 / max(1.0, sample_rate * attack_ms / 1000.0))
    release_coeff = math.exp(-1.0 / max(1.0, sample_rate * release_ms / 1000.0))
    envelope = np.empty_like(target)
    current = 1.0
    for index, requested in enumerate(target):
        coeff = attack_coeff if requested < current else release_coeff
        current = requested + coeff * (current - requested)
        envelope[index] = current
    return envelope


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--narration", type=Path, required=True)
    parser.add_argument("--sfx", type=Path, required=True)
    parser.add_argument("--music", type=Path, required=True)
    parser.add_argument("--music-output", type=Path)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--metadata", type=Path, required=True)
    parser.add_argument("--sample-rate", type=int, default=48_000)
    parser.add_argument("--narration-gain-db", type=float, default=0.2)
    parser.add_argument("--sfx-gain-db", type=float, default=-9.8)
    parser.add_argument("--music-gain-db", type=float, default=-15.42)
    parser.add_argument("--music-duck-db", type=float, default=-6.0)
    parser.add_argument("--speech-threshold-dbfs", type=float, default=-45.0)
    parser.add_argument("--attack-ms", type=float, default=30.0)
    parser.add_argument("--release-ms", type=float, default=350.0)
    parser.add_argument("--peak-ceiling-dbfs", type=float, default=-2.0)
    args = parser.parse_args()

    narration = stereo(read_audio(args.narration, args.sample_rate))
    sfx = stereo(read_audio(args.sfx, args.sample_rate))
    music = stereo(read_audio(args.music, args.sample_rate))
    sample_count = min(len(narration), len(sfx), len(music))
    if len({len(narration), len(sfx), len(music)}) != 1:
        narration = narration[:sample_count]
        sfx = sfx[:sample_count]
        music = music[:sample_count]

    narration_gain = db_to_gain(args.narration_gain_db)
    sfx_gain = db_to_gain(args.sfx_gain_db)
    reference_bus = narration * narration_gain + sfx * sfx_gain

    envelope = speech_duck_envelope(
        narration,
        args.sample_rate,
        args.speech_threshold_dbfs,
        args.music_duck_db,
        args.attack_ms,
        args.release_ms,
    )

    selected_music_gain_db = args.music_gain_db
    ceiling = db_to_gain(args.peak_ceiling_dbfs)
    while True:
        music_gain = db_to_gain(selected_music_gain_db)
        ducked_music = music * envelope[:, None] * music_gain
        mixed = reference_bus + ducked_music
        peak = float(np.max(np.abs(mixed)))
        if peak <= ceiling:
            break
        selected_music_gain_db -= 0.5
        if selected_music_gain_db < -60:
            raise RuntimeError("Unable to meet peak ceiling by reducing only the music stem")

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.metadata.parent.mkdir(parents=True, exist_ok=True)
    sf.write(args.output, mixed, args.sample_rate, subtype="PCM_24")
    if args.music_output:
        args.music_output.parent.mkdir(parents=True, exist_ok=True)
        sf.write(args.music_output, ducked_music, args.sample_rate, subtype="PCM_24")

    metadata = {
        "schema": 1,
        "narration": str(args.narration),
        "sfx": str(args.sfx),
        "music": str(args.music),
        "ducked_music_output": str(args.music_output) if args.music_output else None,
        "output": str(args.output),
        "sample_rate": args.sample_rate,
        "channels": 2,
        "samples": sample_count,
        "duration_seconds": sample_count / args.sample_rate,
        "mix": {
            "master_normalization": "none",
            "limiter": "none",
            "narration_gain_db": args.narration_gain_db,
            "narration_mono_to_stereo": "equal-power; -3.0103 dB per channel",
            "sfx_gain_db": args.sfx_gain_db,
            "music_requested_gain_db": args.music_gain_db,
            "music_selected_gain_db": selected_music_gain_db,
            "music_duck_db_during_speech": args.music_duck_db,
            "speech_threshold_dbfs": args.speech_threshold_dbfs,
            "duck_attack_ms": args.attack_ms,
            "duck_release_ms": args.release_ms,
            "peak_ceiling_dbfs": args.peak_ceiling_dbfs,
            "measured_sample_peak_dbfs": gain_to_db(peak),
            "peak_safety_action": "reduce-music-only",
        },
    }
    args.metadata.write_text(json.dumps(metadata, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(metadata, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
