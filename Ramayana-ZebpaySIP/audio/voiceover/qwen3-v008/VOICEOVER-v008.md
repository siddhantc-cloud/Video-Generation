# Qwen3-TTS local voiceover v008

## Checklist

| Requirement | Pass condition | Evidence | Owner | Status |
|---|---|---|---|---|
| Original voice | Voice is designed from text instruction without cloning or imitating a real person | `voice-instruction.txt` | Voice producer | Pass |
| Local runtime | CUDA generation succeeds in the isolated Python 3.12 environment | Generation metadata | Operator | Pass |
| Benchmark | Two seeds test Vanaras, Ram Setu, SIP, and ZebPay | Benchmark WAV metadata and Scribe v2 JSON | Voice producer | Pass |
| Copy fidelity | Full raw and encoded review contain all 105 approved words | Raw/final Scribe v2 results | Audio QC | Pass |
| Acronym evidence | Both encoded SIP spans are materially longer than the rejected 60 ms occurrence | Final word timing: 0.860 s and 1.221 s | Audio QC | Pass; human listening still required |
| Frame sync | Phrase-locked narration is exactly 1,566 frames / 52.200 seconds | EDL and FFprobe | Editor | Pass |
| Human voice approval | Owner accepts identity, accent, terms, pacing, and mix | Complete captioned v008 playback | Human | Pending |

## Selection

The chosen route is Qwen3-TTS 1.7B VoiceDesign, not a claim that it is universally the best TTS.
It is the strongest first fit here because the official open-source model supports natural-language
voice and prosody design, runs inside the available 16 GB GPU, and does not require a cloned
real-person reference.

- Model: `Qwen/Qwen3-TTS-12Hz-1.7B-VoiceDesign`
- Package: `qwen-tts==0.1.1`
- PyTorch: `2.11.0+cu128`
- Attention: SDPA
- GPU: NVIDIA GeForce RTX 5060 Ti, 15.928 GiB reported
- License/source: <https://github.com/QwenLM/Qwen3-TTS>
- Selected seed: `240726`

Indian English is not an official Qwen3-TTS language/dialect guarantee, so the exact project terms
were benchmarked rather than assumed.

## Voice direction

The source of truth is `voice-instruction.txt`: a mature Indian English male narrator, deep
resonant baritone, reverent premium mythology-documentary tone, warm authority, restrained emotion,
medium-slow pace, clean close-mic sound, and no real-person imitation.

Synthesis uses pronunciation orthography in `full-narration-text.txt`:

| Display copy | Synthesis input |
|---|---|
| `SIP` | `S. I. P.` |
| `ZebPay` | `Zeb Pay` |

Captions and semantic checks use `full-narration-display-text.txt`; phonetic spelling never appears
on screen.

## Benchmark

| Seed | Duration | Peak allocated VRAM | Scribe result | Decision |
|---|---:|---:|---|---|
| `240726` | 10.000 s | 4.188 GiB | Vanaras, Ram Setu, both SIP occurrences, ZebPay recovered | Selected |
| `240727` | 10.320 s | 4.198 GiB | Scribe heard `Annaras` instead of Vanaras | Rejected |

Scribe normalizes pronounced initials into `SIP`, so transcript spelling alone is insufficient.
The selected benchmark's article-plus-acronym span was 1.000 second and its final SIP span was
0.600 second. Human listening remains the pronunciation authority.

## Full generation

- Raw WAV: `Ramayana-ZebPaySIP_NARRATION_v008_qwen3_raw_seed-240726.wav`
- Metadata: `Ramayana-ZebPaySIP_NARRATION_v008_qwen3_raw_seed-240726.metadata.json`
- Raw Scribe timing:
  `Ramayana-ZebPaySIP_NARRATION_v008_qwen3_raw_seed-240726-scribe-v2.json`
- Raw SHA-256: `E2ECFFA8A8408D2F65BF86BA532DBC388B2592769EF0346CF3EA31D872CC69A4`
- Raw format: 24 kHz, mono, 24-bit PCM
- Raw duration: 47.600 seconds
- Cached model load: 15.331 seconds
- Synthesis: 260.831 seconds
- Peak allocated VRAM: 4.640 GiB
- Hosted TTS generation credits: zero

The raw transcript recovered all 105 approved words with English probability 1.0. Its SIP spans
were 1.299 seconds and 1.200 seconds.

## Phrase lock and mix

- Phrase-locked WAV:
  `../../edit/audio/qwen3-v008/narration-phrase-locked-v001.wav`
- Phrase-lock EDL:
  `../../edit/audio/qwen3-v008/narration-phrase-locked-v001-edl.json`
- Word timing:
  `../../edit/audio/qwen3-v008/narration-word-boundaries-v001.json`
- Exact output: 2,505,600 samples / 52.200 seconds / 1,566 frames
- Maximum phrase onset after picture cut: 30 ms
- Pitch-safe compression: K10 1.030x; G12 1.120x; all other phrases natural speed
- Audio master:
  `../../edit/audio/qwen3-v008/Ramayana-ZebPaySIP_AUDIO_MASTER_v008.wav`
- Master SHA-256: `A214D87B6B07C6317FAE1DB777E2FC49D4BE127F2F26F9115CC8D90B4791CEE8`
- Encoded mix: -16.3 LUFS integrated / -2.0 dBTP

The v006 native-SFX stem is reused unchanged and remains independently replaceable. No music was
added.

## Verification usage

Local Qwen synthesis has no provider generation charge after installation. Four Scribe v2 checks
were used: two 10-second benchmarks, one 47.6-second raw narration, and one 52.2-second encoded
review. The account key cannot read reliable currency totals here, so no currency cost is claimed.

## Verdict

`NEEDS HUMAN`. Technical, semantic, timing, loudness, caption, and encoded-file checks pass. The
owner must listen to the entire captioned v008 cut and explicitly accept or reject the voice,
accent, exact spoken initials, mythology terms, pacing, phrase compression, and SFX balance.
