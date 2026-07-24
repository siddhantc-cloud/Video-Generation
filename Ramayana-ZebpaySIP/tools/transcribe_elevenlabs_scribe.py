#!/usr/bin/env python3
"""Transcribe one review asset with ElevenLabs Scribe without logging secrets."""

from __future__ import annotations

import argparse
import json
import mimetypes
import os
from pathlib import Path

import requests


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--model", default="scribe_v2")
    parser.add_argument("--language-code", default="en")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    api_key = os.environ.get("ELEVENLABS_API_KEY")
    if not api_key:
        raise RuntimeError("ELEVENLABS_API_KEY is not available in this process.")
    mime_type = mimetypes.guess_type(args.input.name)[0] or "application/octet-stream"
    with args.input.open("rb") as audio:
        response = requests.post(
            "https://api.elevenlabs.io/v1/speech-to-text",
            headers={"xi-api-key": api_key},
            files={"file": (args.input.name, audio, mime_type)},
            data={
                "model_id": args.model,
                "language_code": args.language_code,
                "tag_audio_events": "false",
                "diarize": "false",
                "timestamps_granularity": "word",
            },
            timeout=600,
        )
    response.raise_for_status()
    payload = response.json()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(payload, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    print(
        json.dumps(
            {
                "output": str(args.output),
                "model": args.model,
                "language_code": payload.get("language_code"),
                "language_probability": payload.get("language_probability"),
                "text": payload.get("text"),
            },
            indent=2,
            ensure_ascii=False,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
