#!/usr/bin/env python
"""Render one continuous Edge TTS track and record word-boundary metadata.

The audio stream and timing metadata are emitted by the same synthesis request.
This makes phrase-to-picture cuts inspectable without dividing a narration line
by arbitrary image percentages.
"""

from __future__ import annotations

import argparse
import asyncio
import json
from pathlib import Path

import edge_tts


TICKS_PER_SECOND = 10_000_000


async def render(
    text: str,
    audio_path: Path,
    timing_path: Path,
    voice: str,
    rate: str,
    pitch: str,
    volume: str,
) -> None:
    audio_path.parent.mkdir(parents=True, exist_ok=True)
    timing_path.parent.mkdir(parents=True, exist_ok=True)

    communicate = edge_tts.Communicate(
        text,
        voice,
        rate=rate,
        pitch=pitch,
        volume=volume,
        boundary="WordBoundary",
    )
    boundaries: list[dict[str, object]] = []

    with audio_path.open("wb") as audio_file:
        async for chunk in communicate.stream():
            if chunk["type"] == "audio":
                audio_file.write(chunk["data"])
            elif chunk["type"] == "WordBoundary":
                offset_ticks = int(chunk["offset"])
                duration_ticks = int(chunk["duration"])
                boundaries.append(
                    {
                        "index": len(boundaries),
                        "text": chunk["text"],
                        "offset_ticks": offset_ticks,
                        "duration_ticks": duration_ticks,
                        "start_sec": round(offset_ticks / TICKS_PER_SECOND, 6),
                        "end_sec": round(
                            (offset_ticks + duration_ticks) / TICKS_PER_SECOND, 6
                        ),
                    }
                )

    payload = {
        "schema": 1,
        "source": "edge-tts-word-boundary",
        "voice": voice,
        "rate": rate,
        "pitch": pitch,
        "volume": volume,
        "text": text,
        "word_count": len(boundaries),
        "words": boundaries,
    }
    timing_path.write_text(
        json.dumps(payload, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--text-file", type=Path, required=True)
    parser.add_argument("--audio", type=Path, required=True)
    parser.add_argument("--timings", type=Path, required=True)
    parser.add_argument("--voice", default="en-IN-PrabhatNeural")
    parser.add_argument("--rate", default="-4%")
    parser.add_argument("--pitch", default="+0Hz")
    parser.add_argument("--volume", default="+0%")
    args = parser.parse_args()

    text = args.text_file.read_text(encoding="utf-8").strip()
    if not text:
        raise SystemExit("Narration text is empty.")
    asyncio.run(
        render(
            text,
            args.audio,
            args.timings,
            args.voice,
            args.rate,
            args.pitch,
            args.volume,
        )
    )


if __name__ == "__main__":
    main()
