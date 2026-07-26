#!/usr/bin/env python3
"""Build the six small deterministic interface cues used by the review cut."""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import random
import wave
from array import array
from pathlib import Path


SR = 48_000
TAU = math.tau


def render(path: Path, duration: float, sampler) -> str:
    rng = random.Random(path.name)
    samples = array("h")
    total = int(duration * SR)
    for index in range(total):
        t = index / SR
        value = max(-1.0, min(1.0, sampler(t, duration, rng)))
        sample = int(value * 32767)
        samples.extend((sample, sample))
    with wave.open(str(path), "wb") as handle:
        handle.setnchannels(2)
        handle.setsampwidth(2)
        handle.setframerate(SR)
        handle.writeframes(samples.tobytes())
    return hashlib.sha256(path.read_bytes()).hexdigest()


def whoosh(t, duration, rng):
    phase = t / duration
    envelope = math.sin(math.pi * phase) ** 1.7
    frequency = 160 + 760 * phase * phase
    return envelope * (
        0.13 * math.sin(TAU * frequency * t) + 0.035 * rng.uniform(-1, 1)
    )


def tick_pair(t, duration, rng):
    local = t % 0.24
    envelope = math.exp(-24 * local)
    frequency = 760 if t < 0.24 else 1040
    return 0.15 * envelope * math.sin(TAU * frequency * t)


def ping(t, duration, rng):
    envelope = math.exp(-7.5 * t)
    return envelope * (
        0.15 * math.sin(TAU * 880 * t) + 0.06 * math.sin(TAU * 1320 * t)
    )


def scroll_ping(t, duration, rng):
    phase = t / duration
    envelope = math.sin(math.pi * phase) * math.exp(-1.8 * phase)
    return envelope * (
        0.055 * rng.uniform(-1, 1) + 0.075 * math.sin(TAU * (420 + 240 * phase) * t)
    )


def settle(t, duration, rng):
    envelope = math.exp(-10 * t)
    frequency = 170 - 65 * min(1.0, t / duration)
    pop = 0.17 * envelope * math.sin(TAU * frequency * t)
    accent_t = max(0.0, t - 0.18)
    accent = 0.09 * math.exp(-16 * accent_t) * math.sin(TAU * 620 * accent_t)
    return pop + (accent if t >= 0.18 else 0.0)


def press(t, duration, rng):
    attack = 0.13 * math.exp(-32 * t) * rng.uniform(-1, 1)
    release_t = max(0.0, t - 0.12)
    release = (
        0.12
        * math.exp(-9 * release_t)
        * (math.sin(TAU * 540 * release_t) + 0.45 * math.sin(TAU * 810 * release_t))
    )
    return attack + (release if t >= 0.12 else 0.0)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--project", required=True)
    parser.add_argument("--audio-meta", default="audio_meta.json")
    args = parser.parse_args()
    project = Path(args.project).resolve()
    output_dir = project / "assets/audio/sfx"
    output_dir.mkdir(parents=True, exist_ok=True)

    definitions = [
        ("01-reveal-whoosh.wav", 0.72, whoosh, 1, 2.35, 0.34),
        ("02-rebalance-ticks.wav", 0.52, tick_pair, 2, 4.65, 0.36),
        ("03-research-ping.wav", 0.52, ping, 3, 4.80, 0.31),
        ("04-history-scroll-ping.wav", 0.62, scroll_ping, 4, 5.25, 0.28),
        ("05-control-settle.wav", 0.48, settle, 5, 2.30, 0.32),
        ("06-enable-press.wav", 0.50, press, 6, 3.00, 0.38),
    ]

    cues = []
    hashes = {}
    for name, duration, sampler, frame, offset, volume in definitions:
        path = output_dir / name
        hashes[name] = render(path, duration, sampler)
        cues.append(
            {
                "frame": frame,
                "file": path.relative_to(project).as_posix(),
                "offset_s": offset,
                "duration_s": duration,
                "volume": volume,
            }
        )

    meta_path = (project / args.audio_meta).resolve()
    audio_meta = json.loads(meta_path.read_text(encoding="utf-8"))
    audio_meta["sfx"] = cues
    meta_path.write_text(json.dumps(audio_meta, indent=2), encoding="utf-8")
    (output_dir / "sfx-v001-metadata.json").write_text(
        json.dumps(
            {
                "provenance": "Original deterministic local synthesis",
                "sample_rate": SR,
                "channels": 2,
                "files": hashes,
            },
            indent=2,
        ),
        encoding="utf-8",
    )
    print(f"Wrote {len(cues)} deterministic SFX cues.")


if __name__ == "__main__":
    main()
