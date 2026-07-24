#!/usr/bin/env python3
"""Create Sarvam pronunciation dictionaries and documented Bulbul v3 WAV takes.

The helper uses only the Python standard library. It loads SARVAM_API_KEY from
the process environment or an explicitly resolved .env file, never prints the
credential, and records reproducible non-secret request metadata.
"""

from __future__ import annotations

import argparse
import base64
import hashlib
import json
import os
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
import uuid
import wave
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


API_ROOT = "https://api.sarvam.ai"
DEFAULT_MODEL = "bulbul:v3"
DEFAULT_LANGUAGE = "en-IN"
DEFAULT_PRICE_INR_PER_10K = 30.0


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--env-file",
        type=Path,
        default=Path(__file__).resolve().parents[2] / ".env",
        help="Ignored dotenv file used only when SARVAM_API_KEY is absent.",
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    dictionary = subparsers.add_parser("create-dictionary")
    dictionary.add_argument("--dictionary-file", required=True, type=Path)
    dictionary.add_argument("--metadata", required=True, type=Path)

    update_dictionary_parser = subparsers.add_parser("update-dictionary")
    update_dictionary_parser.add_argument("--dictionary-file", required=True, type=Path)
    update_dictionary_parser.add_argument("--dict-id", required=True)
    update_dictionary_parser.add_argument("--metadata", required=True, type=Path)

    synthesize = subparsers.add_parser("synthesize")
    text_group = synthesize.add_mutually_exclusive_group(required=True)
    text_group.add_argument("--text")
    text_group.add_argument("--text-file", type=Path)
    synthesize.add_argument("--output", required=True, type=Path)
    synthesize.add_argument("--metadata", required=True, type=Path)
    synthesize.add_argument("--model", default=DEFAULT_MODEL)
    synthesize.add_argument("--language", default=DEFAULT_LANGUAGE)
    synthesize.add_argument("--speaker", default="ratan")
    synthesize.add_argument("--pace", type=float, default=1.0)
    synthesize.add_argument("--temperature", type=float, default=0.75)
    synthesize.add_argument("--sample-rate", type=int, default=48000)
    synthesize.add_argument("--codec", default="wav")
    synthesize.add_argument("--dict-id")
    synthesize.add_argument(
        "--price-inr-per-10k",
        type=float,
        default=DEFAULT_PRICE_INR_PER_10K,
    )
    synthesize.add_argument("--dry-run", action="store_true")
    return parser.parse_args()


def load_dotenv_value(path: Path, name: str) -> str | None:
    if not path.exists():
        return None
    result: str | None = None
    for raw_line in path.read_text(encoding="utf-8-sig").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue
        if line.startswith("export "):
            line = line[7:].lstrip()
        if "=" not in line:
            continue
        key, value = line.split("=", 1)
        if key.strip() != name:
            continue
        value = value.strip()
        if len(value) >= 2 and value[0] == value[-1] and value[0] in "\"'":
            value = value[1:-1]
        result = value
    return result


def load_api_key(env_file: Path) -> str:
    value = os.environ.get("SARVAM_API_KEY") or load_dotenv_value(
        env_file.resolve(), "SARVAM_API_KEY"
    )
    if not value:
        raise RuntimeError(
            "SARVAM_API_KEY is absent from the process environment and env file."
        )
    return value


def read_text(inline: str | None, source: Path | None) -> tuple[str, str]:
    if inline is not None:
        value = inline
        label = "inline"
    elif source is not None:
        value = source.read_text(encoding="utf-8-sig")
        label = str(source.resolve())
    else:
        raise ValueError("Text input is required.")
    value = value.strip()
    if not value:
        raise ValueError("Text input cannot be empty.")
    return value, label


def sha256_bytes(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def request_json(
    method: str,
    path: str,
    api_key: str,
    payload: bytes | None = None,
    content_type: str | None = None,
) -> dict[str, Any]:
    headers = {"api-subscription-key": api_key}
    if content_type:
        headers["Content-Type"] = content_type
    request = urllib.request.Request(
        f"{API_ROOT}{path}",
        data=payload,
        headers=headers,
        method=method,
    )
    try:
        with urllib.request.urlopen(request, timeout=120) as response:
            return json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as error:
        body = error.read().decode("utf-8", errors="replace")
        raise RuntimeError(
            f"Sarvam API request failed with HTTP {error.code}: {body[:1000]}"
        ) from error


def multipart_file(field_name: str, path: Path) -> tuple[bytes, str]:
    boundary = f"----codex-sarvam-{uuid.uuid4().hex}"
    content = path.read_bytes()
    chunks = [
        f"--{boundary}\r\n".encode(),
        (
            f'Content-Disposition: form-data; name="{field_name}"; '
            f'filename="{path.name}"\r\n'
        ).encode(),
        b"Content-Type: application/json\r\n\r\n",
        content,
        b"\r\n",
        f"--{boundary}--\r\n".encode(),
    ]
    return b"".join(chunks), f"multipart/form-data; boundary={boundary}"


def wav_metadata(path: Path) -> dict[str, Any]:
    try:
        with wave.open(str(path), "rb") as handle:
            frames = handle.getnframes()
            sample_rate = handle.getframerate()
            return {
                "channels": handle.getnchannels(),
                "sample_width_bytes": handle.getsampwidth(),
                "sample_rate": sample_rate,
                "frames": frames,
                "duration_seconds": round(frames / sample_rate, 6),
            }
    except wave.Error:
        return {"container_probe": "unsupported_by_python_wave"}


def create_dictionary(args: argparse.Namespace, api_key: str) -> dict[str, Any]:
    source = args.dictionary_file.resolve()
    dictionary = json.loads(source.read_text(encoding="utf-8-sig"))
    pronunciations = dictionary.get("pronunciations")
    if not isinstance(pronunciations, dict) or not pronunciations:
        raise ValueError("Dictionary must contain a non-empty pronunciations object.")
    payload, content_type = multipart_file("file", source)
    started = time.perf_counter()
    response = request_json(
        "POST",
        "/text-to-speech/pronunciation-dictionary",
        api_key,
        payload,
        content_type,
    )
    dictionary_id = response.get("dictionary_id")
    if not dictionary_id:
        raise RuntimeError("Sarvam response did not contain dictionary_id.")
    metadata = {
        "schema_version": 1,
        "created_utc": datetime.now(timezone.utc).isoformat(),
        "provider": "Sarvam AI",
        "operation": "create_pronunciation_dictionary",
        "dictionary_id": dictionary_id,
        "source": str(source),
        "source_sha256": sha256_bytes(source.read_bytes()),
        "languages": sorted(pronunciations),
        "entry_counts": {
            language: len(entries) if isinstance(entries, dict) else None
            for language, entries in pronunciations.items()
        },
        "request_seconds": round(time.perf_counter() - started, 3),
    }
    args.metadata.parent.mkdir(parents=True, exist_ok=True)
    args.metadata.write_text(
        json.dumps(metadata, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    return metadata


def update_dictionary(args: argparse.Namespace, api_key: str) -> dict[str, Any]:
    source = args.dictionary_file.resolve()
    dictionary = json.loads(source.read_text(encoding="utf-8-sig"))
    pronunciations = dictionary.get("pronunciations")
    if not isinstance(pronunciations, dict) or not pronunciations:
        raise ValueError("Dictionary must contain a non-empty pronunciations object.")
    payload, content_type = multipart_file("file", source)
    started = time.perf_counter()
    response = request_json(
        "PUT",
        (
            "/text-to-speech/pronunciation-dictionary?dict_id="
            f"{urllib.parse.quote(args.dict_id, safe='')}"
        ),
        api_key,
        payload,
        content_type,
    )
    dictionary_id = response.get("dictionary_id")
    if dictionary_id != args.dict_id:
        raise RuntimeError("Sarvam response did not confirm the requested dictionary ID.")
    metadata = {
        "schema_version": 1,
        "created_utc": datetime.now(timezone.utc).isoformat(),
        "provider": "Sarvam AI",
        "operation": "update_pronunciation_dictionary",
        "dictionary_id": dictionary_id,
        "source": str(source),
        "source_sha256": sha256_bytes(source.read_bytes()),
        "languages": sorted(pronunciations),
        "entry_counts": {
            language: len(entries) if isinstance(entries, dict) else None
            for language, entries in pronunciations.items()
        },
        "updated_pronunciations": response.get("updated_pronunciations"),
        "request_seconds": round(time.perf_counter() - started, 3),
    }
    args.metadata.parent.mkdir(parents=True, exist_ok=True)
    args.metadata.write_text(
        json.dumps(metadata, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    return metadata


def synthesize(args: argparse.Namespace, api_key: str) -> dict[str, Any]:
    text, text_source = read_text(args.text, args.text_file)
    if args.model == "bulbul:v3" and len(text) > 2500:
        raise ValueError("Bulbul v3 REST input exceeds 2,500 characters.")
    if not 0.5 <= args.pace <= 2.0:
        raise ValueError("Bulbul v3 pace must be between 0.5 and 2.0.")
    if not 0.01 <= args.temperature <= 2.0:
        raise ValueError("Bulbul v3 temperature must be between 0.01 and 2.0.")

    payload: dict[str, Any] = {
        "text": text,
        "target_language_code": args.language,
        "speaker": args.speaker,
        "pace": args.pace,
        "speech_sample_rate": args.sample_rate,
        "model": args.model,
        "output_audio_codec": args.codec,
        "temperature": args.temperature,
    }
    if args.dict_id:
        payload["dict_id"] = args.dict_id

    estimated_cost = len(text) * args.price_inr_per_10k / 10000
    metadata: dict[str, Any] = {
        "schema_version": 1,
        "created_utc": datetime.now(timezone.utc).isoformat(),
        "status": "dry_run" if args.dry_run else "unreviewed",
        "human_listening_required": True,
        "provider": "Sarvam AI",
        "endpoint": "POST /text-to-speech",
        "request": {
            "model": args.model,
            "target_language_code": args.language,
            "speaker": args.speaker,
            "pace": args.pace,
            "temperature": args.temperature,
            "speech_sample_rate": args.sample_rate,
            "output_audio_codec": args.codec,
            "dict_id": args.dict_id,
            "text_source": text_source,
            "text_characters": len(text),
            "text_sha256": sha256_bytes(text.encode("utf-8")),
        },
        "cost": {
            "price_inr_per_10000_characters": args.price_inr_per_10k,
            "estimated_inr": round(estimated_cost, 6),
            "pricing_as_of": "2026-07-24",
            "pricing_source": "https://docs.sarvam.ai/api/getting-started/pricing",
        },
    }
    if args.dry_run:
        return metadata

    started = time.perf_counter()
    response = request_json(
        "POST",
        "/text-to-speech",
        api_key,
        json.dumps(payload, ensure_ascii=False).encode("utf-8"),
        "application/json",
    )
    encoded_parts = response.get("audios")
    if not isinstance(encoded_parts, list) or not encoded_parts:
        raise RuntimeError("Sarvam response did not contain audio data.")
    audio_bytes = base64.b64decode("".join(encoded_parts))
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_bytes(audio_bytes)
    metadata.update(
        {
            "request_id": response.get("request_id"),
            "request_seconds": round(time.perf_counter() - started, 3),
            "audio": {
                "path": str(args.output.resolve()),
                "bytes": len(audio_bytes),
                "sha256": sha256_bytes(audio_bytes),
                **wav_metadata(args.output),
            },
        }
    )
    args.metadata.parent.mkdir(parents=True, exist_ok=True)
    args.metadata.write_text(
        json.dumps(metadata, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    return metadata


def main() -> int:
    args = parse_args()
    try:
        api_key = load_api_key(args.env_file)
        if args.command == "create-dictionary":
            metadata = create_dictionary(args, api_key)
        elif args.command == "update-dictionary":
            metadata = update_dictionary(args, api_key)
        else:
            metadata = synthesize(args, api_key)
        print(json.dumps(metadata, indent=2, ensure_ascii=False))
        return 0
    except Exception as error:
        print(f"ERROR: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
