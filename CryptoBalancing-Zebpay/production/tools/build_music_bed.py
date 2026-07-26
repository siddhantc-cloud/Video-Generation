#!/usr/bin/env python3
"""Create the deterministic, rights-clean CryptoPack technology underscore."""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import random
import wave
from array import array
from datetime import datetime, timezone
from pathlib import Path


SAMPLE_RATE = 48_000
TEMPO = 112.0
BEAT = 60.0 / TEMPO
BAR = BEAT * 4.0
TAU = math.tau
PROGRESSION = [
    (146.83, (293.66, 369.99, 440.00)),  # D
    (110.00, (220.00, 293.66, 369.99)),  # G
    (123.47, (246.94, 329.63, 440.00)),  # A
    (98.00, (196.00, 261.63, 329.63)),   # F
]
PLUCK_SCALE = (587.33, 659.25, 739.99, 880.00, 739.99, 659.25, 587.33, 493.88)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--project", required=True)
    parser.add_argument("--duration", type=float, required=True)
    parser.add_argument("--audio-meta", default="audio_meta.json")
    args = parser.parse_args()

    project = Path(args.project).resolve()
    output_dir = project / "assets/audio/music"
    output_dir.mkdir(parents=True, exist_ok=True)
    output = output_dir / "music-v001-original.wav"
    rng = random.Random(20260726)
    noise_table = [rng.uniform(-1.0, 1.0) for _ in range(4096)]

    total_samples = math.ceil(args.duration * SAMPLE_RATE)
    pcm = array("h")
    block_size = 4096
    for block_start in range(0, total_samples, block_size):
        block_end = min(total_samples, block_start + block_size)
        for sample_index in range(block_start, block_end):
            t = sample_index / SAMPLE_RATE
            bar_index = int(t / BAR)
            beat_phase = (t % BEAT) / BEAT
            eighth = BEAT / 2.0
            eighth_phase = (t % eighth) / eighth
            root, chord = PROGRESSION[bar_index % len(PROGRESSION)]

            fade_in = min(1.0, t / 1.4)
            fade_out = min(1.0, max(0.0, (args.duration - t) / 1.8))
            section = 0.84 if t < 8.669 else 1.0
            if 27.132 <= t < 36.076:
                section = 0.90
            if t >= 41.637:
                section = 1.08
            master = fade_in * fade_out * section

            # Warm pad: a restrained three-note field with slow phase movement.
            pad = sum(
                math.sin(TAU * frequency * t + voice * 0.7)
                + 0.18 * math.sin(TAU * frequency * 2.0 * t + voice)
                for voice, frequency in enumerate(chord)
            ) / (3.0 * 1.18)
            pad *= 0.105

            # Rounded bass on beats one and three.
            beat_in_bar = int((t % BAR) / BEAT)
            bass_env = math.exp(-5.2 * beat_phase) if beat_in_bar in (0, 2) else 0.0
            bass = (
                math.sin(TAU * root * 0.5 * t)
                + 0.22 * math.sin(TAU * root * t)
            ) * 0.08 * bass_env

            # Glassy two-note pluck figure; octave pattern keeps it playful.
            step = int(t / eighth)
            pluck_frequency = PLUCK_SCALE[step % len(PLUCK_SCALE)]
            pluck_env = math.exp(-7.8 * eighth_phase)
            pluck = (
                math.sin(TAU * pluck_frequency * t)
                + 0.28 * math.sin(TAU * pluck_frequency * 2.01 * t)
            ) * 0.045 * pluck_env

            # Very soft pulse and deterministic brushed hat for forward motion.
            kick_env = math.exp(-12.0 * beat_phase)
            kick = math.sin(TAU * (64.0 - 20.0 * beat_phase) * t) * 0.036 * kick_env
            hat_env = math.exp(-18.0 * eighth_phase)
            noise = noise_table[sample_index % len(noise_table)]
            hat = noise * 0.012 * hat_env

            mono = (pad + bass + pluck + kick + hat) * master
            pan = 0.09 * math.sin(TAU * 0.07 * t)
            left = max(-1.0, min(1.0, mono * (1.0 - pan)))
            right = max(-1.0, min(1.0, mono * (1.0 + pan)))
            pcm.append(int(left * 32767))
            pcm.append(int(right * 32767))

    with wave.open(str(output), "wb") as handle:
        handle.setnchannels(2)
        handle.setsampwidth(2)
        handle.setframerate(SAMPLE_RATE)
        handle.writeframes(pcm.tobytes())

    meta_path = (project / args.audio_meta).resolve()
    audio_meta = json.loads(meta_path.read_text(encoding="utf-8"))
    audio_meta["bgm"] = {
        "path": output.relative_to(project).as_posix(),
        "volume": 0.24,
        "query": "light playful technology underscore; optimistic and restrained",
        "duration_s": round(args.duration, 3),
    }
    meta_path.write_text(json.dumps(audio_meta, indent=2), encoding="utf-8")

    metadata = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "title": "CryptoPack Rebalancing technology underscore v001",
        "provenance": "Original deterministic local synthesis; no catalog or generative music provider",
        "seed": 20260726,
        "sample_rate": SAMPLE_RATE,
        "channels": 2,
        "duration_s": round(args.duration, 3),
        "tempo_bpm": TEMPO,
        "file": output.relative_to(project).as_posix(),
        "sha256": sha256(output),
    }
    (output_dir / "music-v001-metadata.json").write_text(
        json.dumps(metadata, indent=2), encoding="utf-8"
    )
    print(f"Wrote {output} ({args.duration:.3f}s, SHA-256 {metadata['sha256']}).")


if __name__ == "__main__":
    main()
