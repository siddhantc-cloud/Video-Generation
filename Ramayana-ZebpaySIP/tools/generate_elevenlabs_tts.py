#!/usr/bin/env python3
"""Generate ElevenLabs speech with character timestamps without exposing credentials."""

from __future__ import annotations

import argparse
import base64
import json
import os
from pathlib import Path

import requests


def load_api_key(repo_root: Path) -> str:
    for name in ("ELEVENLABS_API_KEY", "ELEVEN_LABS_API_KEY"):
        value = os.environ.get(name)
        if value:
            return value
    env_file = repo_root / ".env"
    if env_file.exists():
        for line in env_file.read_text(encoding="utf-8-sig").splitlines():
            if "=" not in line or line.lstrip().startswith("#"):
                continue
            name, value = line.split("=", 1)
            if name.strip() in ("ELEVENLABS_API_KEY", "ELEVEN_LABS_API_KEY"):
                return value.strip().strip('"').strip("'")
    raise RuntimeError("ElevenLabs API key was not found in the environment or ignored repo .env")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--text-file", type=Path, required=True)
    parser.add_argument("--audio-output", type=Path, required=True)
    parser.add_argument("--alignment-output", type=Path, required=True)
    parser.add_argument("--voice-id", required=True)
    parser.add_argument("--voice-name", default="")
    parser.add_argument("--model-id", default="eleven_v3")
    parser.add_argument("--language-code", default="en")
    parser.add_argument("--output-format", default="mp3_44100_128")
    parser.add_argument("--seed", type=int)
    parser.add_argument("--stability", type=float, default=0.5)
    parser.add_argument("--similarity-boost", type=float, default=0.82)
    parser.add_argument("--style", type=float, default=0.12)
    parser.add_argument("--speed", type=float, default=1.08)
    parser.add_argument("--speaker-boost", action=argparse.BooleanOptionalAction, default=True)
    parser.add_argument("--dictionary-id")
    parser.add_argument("--dictionary-version")
    args = parser.parse_args()

    repo_root = Path(__file__).resolve().parents[2]
    api_key = load_api_key(repo_root)
    text = args.text_file.read_text(encoding="utf-8-sig").strip()
    voice_settings = {
        "stability": args.stability,
        "similarity_boost": args.similarity_boost,
        "style": args.style,
        "use_speaker_boost": args.speaker_boost,
        "speed": args.speed,
    }
    payload: dict[str, object] = {
        "text": text,
        "model_id": args.model_id,
        "language_code": args.language_code,
        "voice_settings": voice_settings,
    }
    if args.seed is not None:
        payload["seed"] = args.seed
    if args.dictionary_id or args.dictionary_version:
        if not (args.dictionary_id and args.dictionary_version):
            raise ValueError("Dictionary ID and version must be provided together")
        payload["pronunciation_dictionary_locators"] = [
            {
                "pronunciation_dictionary_id": args.dictionary_id,
                "version_id": args.dictionary_version,
            }
        ]

    url = (
        "https://api.elevenlabs.io/v1/text-to-speech/"
        f"{args.voice_id}/with-timestamps?output_format={args.output_format}"
    )
    response = requests.post(
        url,
        headers={"xi-api-key": api_key, "Content-Type": "application/json"},
        json=payload,
        timeout=600,
    )
    response.raise_for_status()
    result = response.json()
    audio = base64.b64decode(result["audio_base64"])

    args.audio_output.parent.mkdir(parents=True, exist_ok=True)
    args.alignment_output.parent.mkdir(parents=True, exist_ok=True)
    args.audio_output.write_bytes(audio)
    metadata = {
        "schema": 1,
        "provider": "ElevenLabs",
        "model_id": args.model_id,
        "voice_id": args.voice_id,
        "voice_name": args.voice_name,
        "language_code": args.language_code,
        "seed": args.seed,
        "voice_settings": voice_settings,
        "pronunciation_dictionary_id": args.dictionary_id,
        "pronunciation_dictionary_version": args.dictionary_version,
        "source_script": str(args.text_file),
        "text": text,
        "alignment": result.get("alignment"),
        "normalized_alignment": result.get("normalized_alignment"),
    }
    args.alignment_output.write_text(
        json.dumps(metadata, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    print(
        json.dumps(
            {
                "audio_output": str(args.audio_output),
                "alignment_output": str(args.alignment_output),
                "characters": len(text),
                "model_id": args.model_id,
                "voice_name": args.voice_name,
            },
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
