#!/usr/bin/env python
"""Build compact phrase-timed social captions from the locked word-boundary source."""

from __future__ import annotations

import argparse
import json
import math
import re
from pathlib import Path


PROJECT = Path(__file__).resolve().parents[1]
TIMELINE = PROJECT / "edit/timelines/final-short-v001-phrase-map.json"
OUTPUT = PROJECT / "edit/master-short-v001.srt"


def timestamp(seconds: float) -> str:
    total_ms = max(0, round(seconds * 1000))
    hours, remainder = divmod(total_ms, 3_600_000)
    minutes, remainder = divmod(remainder, 60_000)
    secs, millis = divmod(remainder, 1000)
    return f"{hours:02d}:{minutes:02d}:{secs:02d},{millis:03d}"


def chunk_sizes(word_count: int, maximum: int = 5) -> list[int]:
    groups = max(1, math.ceil(word_count / maximum))
    base, extra = divmod(word_count, groups)
    return [base + (1 if index < extra else 0) for index in range(groups)]


def phrase_tokens(phrase: str, expected: int) -> list[str]:
    tokens = phrase.split()
    if len(tokens) == expected:
        return tokens
    return [re.sub(r"\s+", " ", token).strip() for token in tokens][:expected]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--timeline", type=Path, default=TIMELINE)
    parser.add_argument("--word-boundaries", type=Path)
    parser.add_argument("--output", type=Path, default=OUTPUT)
    args = parser.parse_args()

    timeline = json.loads(args.timeline.read_text(encoding="utf-8-sig"))
    timing_path = (
        args.word_boundaries
        if args.word_boundaries
        else PROJECT / timeline["narration"]["word_boundaries"]
    )
    words = json.loads(timing_path.read_text(encoding="utf-8"))["words"]
    beats = timeline["beats"]
    entries: list[tuple[float, float, str]] = []

    for beat_index, beat in enumerate(beats):
        # G15 already renders the spoken CTA verbatim as deterministic brand copy. Burning the
        # same sentence as a subtitle overlaps the approved card, so accessibility text is
        # represented by the card itself for this final beat.
        if beat["id"] == "G15":
            continue
        first = int(beat["first_word_index"])
        last_exclusive = (
            int(beats[beat_index + 1]["first_word_index"])
            if beat_index + 1 < len(beats)
            else len(words)
        )
        count = last_exclusive - first
        tokens = phrase_tokens(str(beat["phrase"]), count)
        if len(tokens) != count:
            tokens = [str(word["text"]) for word in words[first:last_exclusive]]

        beat_start = int(beat["start_frame"]) / int(timeline["fps"])
        beat_end = int(beat["end_frame"]) / int(timeline["fps"])
        cursor = 0
        sizes = chunk_sizes(count)
        for group_index, size in enumerate(sizes):
            chunk_first = first + cursor
            chunk_last = chunk_first + size - 1
            start = max(beat_start, float(words[chunk_first]["start_sec"]) - 0.05)
            if group_index + 1 < len(sizes):
                next_first = chunk_last + 1
                end = min(beat_end, float(words[next_first]["start_sec"]) - 0.05)
            else:
                end = beat_end
            text = " ".join(tokens[cursor : cursor + size])
            entries.append((start, max(start + 0.15, end), text))
            cursor += size

    blocks = []
    for index, (start, end, text) in enumerate(entries, 1):
        blocks.append(
            f"{index}\n{timestamp(start)} --> {timestamp(end)}\n{text}\n"
        )
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text("\n".join(blocks), encoding="utf-8")
    print(
        json.dumps(
            {
                "entries": len(entries),
                "output": str(args.output),
                "first": entries[0],
                "last": entries[-1],
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
