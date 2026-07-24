# Recipe: local Qwen3-TTS narration and phrase-locked post-production

## Checklist

| Requirement | Pass condition | Evidence | Owner | Status |
|---|---|---|---|---|
| Rights-safe voice | The instruction designs an original voice and does not imitate a real person | Versioned instruction text and model/license record | Producer | Required |
| Isolated runtime | Python 3.12 environment, CUDA PyTorch, and `qwen-tts` are project-local; caches are ignored and live on the spacious drive | Environment path, package versions, and GPU smoke test | Operator | Required |
| Short benchmark | At least two inexpensive seeds test every difficult name, acronym, and brand term before a full take | Benchmark WAV metadata and transcripts | Voice producer | Required |
| Pronunciation evidence | ASR recovers the complete benchmark and timing shows the acronym was not collapsed into a near-instant word | Scribe word timing plus human listening | Audio reviewer | Required |
| Continuous performance | One full-script request produces a complete immutable raw take | Raw WAV, generation metadata, and transcript | Voice producer | Required |
| Frame-locked conform | Approved display words map exactly to provider timing; every phrase slot contains an integer sample count | Phrase-lock EDL and word-boundary JSON | Editor | Required |
| Separate mix | Narration, native SFX, music, and picture remain independently replaceable | Versioned stems and mix manifest | Sound editor | Required |
| Encoded QC | Runtime, frames, decode, streams, loudness, peak, black frames, captions, and final ASR pass | Review report and encoded artifacts | Reviewer | Required |
| Human listening | A person accepts voice identity, accent, terms, pace, compression, and SFX balance | Explicit approval | Human | Required before promotion |

## When to use

Use this route when a rights-clean original narrator and free-form voice direction are more
important than access to a hosted voice catalog. It is suitable for a 16 GB NVIDIA GPU and for
iteration after the model is cached. Do not assume an Indian accent or mythology-name pronunciation
from the model description: benchmark the exact script terms first.

Use a hosted TTS fallback when the local benchmark fails the required accent or phoneme gate. Do
not clone a public or real-person voice without documented rights.

## Reference model and host

- Model: `Qwen/Qwen3-TTS-12Hz-1.7B-VoiceDesign`
- Code/package: `qwen-tts`
- License source: Apache-2.0 in the official Qwen3-TTS repository/model publication
- Host reference: Windows 11, Python 3.12, RTX 5060 Ti 16 GB
- Attention: PyTorch SDPA; do not add FlashAttention on this Windows workflow
- Canonical generator: `<project>/tools/generate_qwen3_tts.py`
- Phrase conformer: `<project>/tools/build_elevenlabs_phrase_locked_audio.py`
  (backward-compatible ElevenLabs alignment plus Scribe word-timing input)

## Output structure

```text
<project>/
  .venv-qwen3-tts/                       # ignored
  audio/voiceover/<version>/
    benchmark-text.txt
    voice-instruction.txt
    benchmark-<seed>.wav                 # ignored raw media
    benchmark-<seed>.metadata.json
    benchmark-<seed>-scribe-v2.json
    full-narration-text.txt              # pronunciation orthography
    full-narration-display-text.txt      # approved visible copy
    <narration>-raw.wav                   # ignored raw media
    <narration>-raw.metadata.json
    <narration>-raw-scribe-v2.json
    VOICEOVER.md
  edit/audio/<version>/
    narration-phrase-locked.wav
    narration-phrase-locked-edl.json
    narration-word-boundaries.json
    audio-master.wav
    scribe-final-mix/<review>.json
  edit/<version>.srt
  edit/timelines/<version>.json
  review/<version>-qc.md
  deliverables/review-cuts/<version>/
```

## Install

Keep the virtual environment inside the film project and both caches at repository root on `D:`.
The cache directories must remain ignored.

```powershell
uv venv --python 3.12 <project>/.venv-qwen3-tts
uv --cache-dir <repo>/_cache/uv pip install `
  --python <project>/.venv-qwen3-tts/Scripts/python.exe `
  torch==2.11.0+cu128 torchaudio==2.11.0+cu128 `
  --index-url https://download.pytorch.org/whl/cu128
uv --cache-dir <repo>/_cache/uv pip install `
  --python <project>/.venv-qwen3-tts/Scripts/python.exe qwen-tts==0.1.1
```

Verify a real GPU tensor before downloading the model. On the reference host, the isolated
environment measured 4.74 GB and the completed Hugging Face model cache measured 4.21 GB. The UV
package cache measured 6.32 GB after an interrupted install and can contain recoverable temporary
data; do not present the model headline weight as the complete disk requirement.

## Workflow

1. Write one versioned voice instruction: identity, age range, accent, pitch/timbre, pace,
   emotional restraint, recording character, pronunciation requirements, and explicit exclusions.
2. Write a short benchmark containing every ambiguous project term. Use explicit synthesis
   orthography such as `S. I. P.` and `Zeb Pay`; keep approved display copy in a separate file.
3. Generate at least two seeded benchmark WAVs with `generate_qwen3_tts.py`. Preserve metadata for
   model, seed, sampling controls, runtime, VRAM peak, duration, and hash.
4. Transcribe the benchmarks. Reject a seed that loses a required word. Duration evidence can
   expose a collapsed acronym, but ASR spelling alone never replaces human listening.
5. Generate the complete narration in one request using the selected instruction and seed. Keep
   the raw WAV immutable.
6. Transcribe the raw take. The approved display script and the normalized ASR character stream
   must match exactly before conforming.
7. Phrase-lock the raw performance against the approved whole-frame map. Use Scribe timing plus
   `--canonical-text` when the synthesis orthography changes word boundaries. Pad shorter phrase
   tails; use Rubber Band only for overruns; record every ratio.
8. Rebuild captions from the conformed word timing. Do not display phonetic synthesis spelling.
9. Mix the narration with separately approved SFX/music. Measure a first loudness pass and render a
   second pass; preserve at least 1.5 dB true-peak headroom after AAC encoding.
10. Stream-copy the locked picture into a clean review when possible. Burn captions last and
    stream-copy the clean cut's audio into the captioned variant.
11. Verify exact frame/sample duration, elementary audio identity, full decode, black intervals,
    encoded loudness/peak, caption contacts, boundary frames, and ASR on the encoded review.
12. Mark the result `NEEDS HUMAN`. The local take cannot replace an approved master until a person
    listens to the complete encoded cut.

## Cost model

- Qwen generation after installation: no provider generation credits; local electricity and
  machine time only.
- Model/package download: one-time bandwidth and disk cost.
- Scribe verification: hosted usage if ElevenLabs is used; record seconds and do not invent plan or
  currency cost when the key cannot read subscription totals.
- Repeated scripts reuse the environment, model cache, generator, benchmark pattern, and post
  pipeline. Only script-specific voice tests and renders recur.

## Windows notes

- `qwen_tts` may print a missing-SoX warning during import. The verified VoiceDesign WAV path uses
  `soundfile` and completed without SoX; do not add a new binary unless a required operation proves
  it needs one.
- The package may recommend FlashAttention. The verified RTX 5060 Ti run uses SDPA and requires no
  FlashAttention build.
- Hugging Face can warn that Windows symlinks and optional Xet acceleration are unavailable.
  Ordinary HTTPS completed successfully. Enable Developer Mode or add `hf_xet` only as a deliberate
  environment change, not as a reaction to a non-blocking warning.
- Interrupted UV downloads can leave ignored `.tmp*` cache directories. Verify that no UV process
  is active and resolve the exact cache target before any manual cleanup.

## Host rows

| Host | Execution surface | Credential rule | Parity rule |
|---|---|---|---|
| Codex | Project Python, CUDA/SDPA, FFmpeg/FFprobe, optional ElevenLabs Scribe verifier | Read the user environment at runtime; never print or persist a key | Follow this recipe and canonical project skill |
| Claude | Same project environment and scripts | Same | Follow this shared recipe and mirrored skill |

## Verified reference run

- Project/version: `Ramayana-ZebpaySIP` v008 review
- Date: 2026-07-24
- Selected seed: `240726`
- Raw duration: 47.600 seconds
- GPU peak allocated: 4.640 GiB
- Cached model load: 15.331 seconds
- Full synthesis: 260.831 seconds
- Phrase map: 1,566 frames / 52.200 seconds / 2,505,600 samples
- Maximum phrase onset: 30 ms
- Pitch-safe overrun ratios: K10 1.030x; G12 1.120x
- Encoded audio: -16.3 LUFS integrated, -2.0 dBTP
- Encoded semantic check: 105 words; Vanaras, Ram Setu, Rama, both SIP occurrences, and ZebPay
- Promotion: technical pass; human listening pending
