# Recipe: Sarvam Bulbul v3 Indian-English narration

## Checklist

| Requirement | Pass condition | Evidence | Owner | Status |
|---|---|---|---|---|
| Credential safety | `SARVAM_API_KEY` is read at runtime from the environment or an ignored `.env`; it is never printed or persisted | Credential-presence check and Git ignore check | Operator | Required |
| Current provider contract | Model, voices, controls, limits, and price are verified against current official Sarvam documentation | Dated source links in the voiceover record | Voice producer | Required |
| Low-cost audition | Short takes compare at least the language-recommended voice and one credible alternative on every difficult term | Audition WAV metadata and transcripts | Voice producer | Required |
| Pronunciation lock | A Bulbul v3 dictionary explicitly controls ambiguous acronyms and brand names | Versioned dictionary JSON, provider dictionary ID, and audition evidence | Sound editor | Required |
| Natural performance | Pace stays near the voice's native rate and temperature permits natural prosody; no aggressive control is used to hide a poor voice | Selected settings and human listening verdict | Voice producer / human | Required |
| Continuous narration | The approved script fits one provider request and returns one immutable raw take | Raw WAV, request ID, hash, and metadata | Sound editor | Required |
| Frame-locked conform | Provider or ASR timing maps the approved display words into whole-frame phrase slots without pitch shift | Phrase-lock EDL and word-boundary JSON | Editor | Required |
| Separate sound architecture | Narration, diegetic SFX, music, graphics, and picture remain independently replaceable | Versioned stems and mix manifest | Sound editor | Required |
| Encoded QC | Runtime, frame count, decode, stream drift, loudness, peak, black frames, captions, and final ASR pass | Review report and encoded artifacts | Reviewer | Required |
| Human listening gate | A person accepts Indian accent, mythological names, acronym cadence, brand pronunciation, pacing, and mix | Explicit approval | Human | Required before promotion |

## When to use

Use this route for Indian-language or Indian-English narration when a hosted, India-focused voice is
preferable to a generic international TTS voice. It is especially suitable for financial acronyms,
Indian names, and code-mixed material that needs an explicit pronunciation dictionary.

Do not choose Bulbul v2 merely to gain pitch or loudness controls. Start with the higher-quality
Bulbul v3 voice, select the right speaker, and direct natural performance with punctuation, pace,
temperature, and a pronunciation dictionary. Use post-production for gain and dynamics.

## Verified provider contract

Verify these values again before a later production because provider behavior and price can change.
The following were current on 2026-07-24:

- REST endpoint: `POST https://api.sarvam.ai/text-to-speech`
- Authentication header: `api-subscription-key`
- Model: `bulbul:v3`
- Indian English: `en-IN`
- REST input limit: 2,500 characters
- English-recommended voices: male `ratan`, female `ishita`
- Useful male alternatives: `mani` for low pronunciation error and `shubh` as the default voice
- Pace: 0.5 to 2.0; start at `1.0`
- Temperature: use approximately 0.7 to 0.8 for warm storytelling; low values can sound controlled
- Pitch and loudness: not supported by Bulbul v3
- Pronunciation dictionaries: Bulbul v3 only; one dictionary per request
- High-quality REST output: WAV at 48 kHz is supported
- Price: ₹30 per 10,000 characters, beta price

Official sources:

- `https://docs.sarvam.ai/api/getting-started/models/bulbul`
- `https://docs.sarvam.ai/api/api-guides-tutorials/text-to-speech/how-to/change-the-speaker-voice`
- `https://docs.sarvam.ai/api/api-guides-tutorials/text-to-speech/pronunciation-dictionary`
- `https://docs.sarvam.ai/api/api-guides-tutorials/text-to-speech/best-practices`
- `https://docs.sarvam.ai/api/getting-started/pricing`

## Output structure

```text
<project>/
  audio/voiceover/<version>/
    audition-text.txt
    pronunciation-dictionary.json
    pronunciation-dictionary.metadata.json
    audition-<speaker>-<settings>.wav
    audition-<speaker>-<settings>.metadata.json
    full-narration-display-text.txt
    <narration>-raw.wav
    <narration>-raw.metadata.json
    <narration>-raw-asr.json
    VOICEOVER.md
  edit/audio/<version>/
    narration-phrase-locked.wav
    narration-phrase-locked-edl.json
    narration-word-boundaries.json
    audio-master.wav
  edit/timelines/<version>.json
  edit/<version>.srt
  review/<version>-qc.md
  deliverables/review-cuts/<version>/
```

## Workflow

1. Confirm that `.env` is ignored and contains `SARVAM_API_KEY`, or provide the key through the
   process environment. Never echo the value.
2. Recheck the official model, voice, parameter, input-limit, and price pages.
3. Freeze approved display copy. Keep pronunciation substitutions in the provider dictionary, not
   in captions or visible script text.
4. Build one `en-IN` pronunciation dictionary containing only terms that need control. For an
   initial English financial pass, use exact replacements such as `SIP` to `S I P`; test brand
   pronunciation in the selected speaker before adding more rules.
5. Write a short audition containing every ambiguous term in natural sentences. Compare the
   English-recommended voice with one or two credible alternatives at native pace. For storytelling,
   compare temperature near 0.7 or 0.8; avoid flattening the take with a compliance-style value.
6. Transcribe and measure the auditions. Reject missing or collapsed words. ASR spelling and
   duration are evidence, but a person must still judge accent, acronym cadence, and naturalness.
7. Generate the complete narration in one REST request when it is under 2,500 characters. Preserve
   the raw WAV, request ID, settings, character count, estimated cost, and hashes.
8. Transcribe the raw take, then map the approved display words to whole-frame phrase slots. Pad
   phrases that finish early and pitch-preserve only genuine overruns.
9. Mix narration with separately approved SFX and music. Use post-production gain, EQ, compression,
   and loudness normalization; Bulbul v3 has no pitch or loudness synthesis controls.
10. Build captions from the conformed display-word boundaries. Never expose dictionary replacement
    spelling such as `S I P` in visible copy.
11. Mux clean and captioned review cuts from the same picture and audio master.
12. Verify the encoded review artifact and mark it `NEEDS HUMAN`. Do not replace an approved final
    until a person listens to the complete encoded cut.

## Cost control

Bulbul v3 cost is character based:

```text
estimated INR = input characters × current INR price per 10,000 characters / 10,000
```

Short auditions are inexpensive and prevent waste on unsuitable full performances. Reuse the same
pronunciation dictionary, selected voice, generator, phrase map, SFX stem, and rendering workflow
across later revisions. Recheck beta pricing before quoting future jobs.

## Host rows

| Host | Execution surface | Credential rule | Parity rule |
|---|---|---|---|
| Codex | Project Sarvam generator, official REST API, FFmpeg/FFprobe, and project timing tools | Read `SARVAM_API_KEY` at runtime from the environment or ignored `.env`; never print or persist it | Follow this shared recipe and canonical project skill |
| Claude | Same project generator and timing tools | Same | Follow this shared recipe and mirrored project skill |

## Verified reference run

- Project/version: `Ramayana-ZebpaySIP` v009 review
- Date: 2026-07-24
- Model/voice: Bulbul v3, `en-IN`, `mani`
- Controls: pace 1.0, temperature 0.75, 48 kHz WAV
- Dictionary: `SIP` to `S I P`; `ZebPay` to `Zebb Pay`
- Experiment TTS cost: ₹7.656 estimated for nine requests / 2,552 characters
- Selected comped raw duration: 50.372 seconds
- Phrase lock: 1,566 frames / 52.200 seconds / 2,505,600 samples
- Maximum phrase onset: 30 ms
- Maximum pitch-safe tempo: 1.200x
- Encoded audio: -16.06 LUFS / -2.46 dBTP
- Promotion: technical review pass; human accent, phoneme, pacing, and mix approval pending
