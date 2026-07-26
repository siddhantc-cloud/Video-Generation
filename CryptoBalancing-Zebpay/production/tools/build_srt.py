#!/usr/bin/env python3
"""Convert HyperFrames caption groups into an exact sidecar SRT."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


def stamp(seconds: float) -> str:
    milliseconds = max(0, round(seconds * 1000))
    hours, milliseconds = divmod(milliseconds, 3_600_000)
    minutes, milliseconds = divmod(milliseconds, 60_000)
    whole_seconds, milliseconds = divmod(milliseconds, 1000)
    return f"{hours:02d}:{minutes:02d}:{whole_seconds:02d},{milliseconds:03d}"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--groups", required=True)
    parser.add_argument("--out", required=True)
    args = parser.parse_args()
    groups = json.loads(Path(args.groups).read_text(encoding="utf-8"))["groups"]
    blocks = []
    for index, group in enumerate(groups, start=1):
        blocks.append(
            f"{index}\n{stamp(group['start'])} --> {stamp(group['end'])}\n{group['text']}"
        )
    output = Path(args.out)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text("\n\n".join(blocks) + "\n", encoding="utf-8")
    print(f"Wrote {len(groups)} captions to {output}.")


if __name__ == "__main__":
    main()
