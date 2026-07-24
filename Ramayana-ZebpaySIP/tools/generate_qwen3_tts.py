#!/usr/bin/env python3
"""Generate a documented Qwen3-TTS VoiceDesign narration take.

The script keeps model caches outside the virtual environment, writes a
24-bit WAV, and records enough metadata to reproduce and review the take.
It intentionally uses PyTorch SDPA rather than FlashAttention on Windows.
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.metadata
import json
import os
import platform
import random
import sys
import time
from datetime import datetime, timezone
from pathlib import Path


DEFAULT_MODEL = "Qwen/Qwen3-TTS-12Hz-1.7B-VoiceDesign"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    text_group = parser.add_mutually_exclusive_group(required=True)
    text_group.add_argument("--text")
    text_group.add_argument("--text-file", type=Path)
    instruct_group = parser.add_mutually_exclusive_group(required=True)
    instruct_group.add_argument("--instruct")
    instruct_group.add_argument("--instruct-file", type=Path)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--metadata", type=Path)
    parser.add_argument("--model", default=DEFAULT_MODEL)
    parser.add_argument("--language", default="English")
    parser.add_argument("--seed", type=int, default=240726)
    parser.add_argument("--temperature", type=float, default=0.9)
    parser.add_argument("--top-p", type=float, default=0.95)
    parser.add_argument("--top-k", type=int, default=50)
    parser.add_argument("--repetition-penalty", type=float, default=1.05)
    parser.add_argument("--max-new-tokens", type=int, default=4096)
    parser.add_argument(
        "--cache-dir",
        type=Path,
        default=Path(__file__).resolve().parents[2] / "_cache" / "huggingface",
    )
    return parser.parse_args()


def read_value(inline: str | None, source: Path | None) -> str:
    if inline is not None:
        value = inline
    elif source is not None:
        value = source.read_text(encoding="utf-8")
    else:
        raise ValueError("An inline value or source file is required.")
    value = value.strip()
    if not value:
        raise ValueError("Text and instruction values cannot be empty.")
    return value


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main() -> int:
    args = parse_args()
    text = read_value(args.text, args.text_file)
    instruct = read_value(args.instruct, args.instruct_file)
    cache_dir = args.cache_dir.resolve()
    cache_dir.mkdir(parents=True, exist_ok=True)

    # These must be set before importing Transformers/Hugging Face libraries.
    os.environ["HF_HOME"] = str(cache_dir)
    os.environ["HF_HUB_DISABLE_TELEMETRY"] = "1"
    os.environ["TOKENIZERS_PARALLELISM"] = "false"

    import numpy as np
    import soundfile as sf
    import torch
    from qwen_tts import Qwen3TTSModel

    if not torch.cuda.is_available():
        raise RuntimeError("CUDA is required for this production workflow.")

    random.seed(args.seed)
    np.random.seed(args.seed)
    torch.manual_seed(args.seed)
    torch.cuda.manual_seed_all(args.seed)
    torch.cuda.empty_cache()
    torch.cuda.reset_peak_memory_stats()

    started = time.perf_counter()
    model = Qwen3TTSModel.from_pretrained(
        args.model,
        device_map="cuda:0",
        dtype=torch.bfloat16,
        attn_implementation="sdpa",
        low_cpu_mem_usage=True,
    )
    loaded = time.perf_counter()
    wavs, sample_rate = model.generate_voice_design(
        text=text,
        instruct=instruct,
        language=args.language,
        do_sample=True,
        temperature=args.temperature,
        top_p=args.top_p,
        top_k=args.top_k,
        repetition_penalty=args.repetition_penalty,
        max_new_tokens=args.max_new_tokens,
    )
    generated = time.perf_counter()

    if len(wavs) != 1:
        raise RuntimeError(f"Expected one waveform, received {len(wavs)}.")
    waveform = np.asarray(wavs[0], dtype=np.float32)
    if waveform.ndim != 1:
        waveform = np.squeeze(waveform)
    if waveform.ndim != 1:
        raise RuntimeError(f"Expected mono audio, received shape {waveform.shape}.")

    args.output.parent.mkdir(parents=True, exist_ok=True)
    sf.write(args.output, waveform, sample_rate, subtype="PCM_24")
    duration_seconds = len(waveform) / sample_rate
    peak = float(np.max(np.abs(waveform))) if len(waveform) else 0.0
    rms = float(np.sqrt(np.mean(np.square(waveform)))) if len(waveform) else 0.0

    metadata_path = args.metadata or args.output.with_suffix(".metadata.json")
    metadata_path.parent.mkdir(parents=True, exist_ok=True)
    metadata = {
        "schema_version": 1,
        "created_utc": datetime.now(timezone.utc).isoformat(),
        "status": "unreviewed",
        "human_listening_required": True,
        "model": args.model,
        "model_mode": "voice_design",
        "language": args.language,
        "text": text,
        "instruction": instruct,
        "generation": {
            "seed": args.seed,
            "do_sample": True,
            "temperature": args.temperature,
            "top_p": args.top_p,
            "top_k": args.top_k,
            "repetition_penalty": args.repetition_penalty,
            "max_new_tokens": args.max_new_tokens,
            "attention": "sdpa",
            "dtype": "bfloat16",
        },
        "runtime": {
            "python": platform.python_version(),
            "torch": torch.__version__,
            "qwen_tts": importlib.metadata.version("qwen-tts"),
            "platform": platform.platform(),
            "gpu": torch.cuda.get_device_name(0),
            "gpu_total_vram_gib": round(
                torch.cuda.get_device_properties(0).total_memory / (1024**3), 3
            ),
            "gpu_peak_allocated_gib": round(
                torch.cuda.max_memory_allocated() / (1024**3), 3
            ),
            "model_load_seconds": round(loaded - started, 3),
            "generation_seconds": round(generated - loaded, 3),
            "cache_dir": str(cache_dir),
        },
        "audio": {
            "path": str(args.output.resolve()),
            "sha256": sha256(args.output),
            "sample_rate": sample_rate,
            "channels": 1,
            "subtype": "PCM_24",
            "samples": len(waveform),
            "duration_seconds": round(duration_seconds, 6),
            "peak_linear": round(peak, 8),
            "rms_linear": round(rms, 8),
        },
    }
    metadata_path.write_text(
        json.dumps(metadata, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )

    print(json.dumps(metadata, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
