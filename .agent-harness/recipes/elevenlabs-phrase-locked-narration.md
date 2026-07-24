# Recipe: ElevenLabs phrase-locked narration replacement

## Checklist

| Requirement | Pass condition | Evidence | Owner | Status |
|---|---|---|---|---|
| Voice rights and entitlement | The selected voice is account-owned or the current plan permits API use; no real-person imitation is introduced | Voice metadata and one short audition result | Producer / operator | Required |
| Pronunciation lock | Brand, acronym, character, and place names survive synthesis and ASR verification | Versioned pronunciation dictionary metadata and transcript | Sound editor | Required |
| Continuous performance | One complete narration request returns audio and character timing metadata | Immutable raw narration and alignment JSON | Sound editor | Required |
| Phrase map | Every narration phrase owns a whole-frame visual slot from the approved picture | Versioned timeline/EDL | Editor | Required |
| Pitch-safe conform | Natural silence is retained; only overrun phrases are time-compressed without pitch shift | Phrase-lock EDL with per-phrase ratios | Editor | Required |
| Separate sound architecture | Narration, diegetic SFX, music, and graphics remain independently replaceable | Versioned stems and mix manifest | Sound editor | Required |
| Encoded technical QC | Runtime, frame count, decode, stream drift, loudness, peak, and black-frame checks pass | Probe and QC report | Reviewer | Required |
| Semantic QC | ASR recovers the complete script and key pronunciations from the encoded review cut | Final mixed-media transcript | Reviewer | Required |
| Human listening gate | A human accepts performance, pronunciations, pacing, and mix on the encoded review cut | Explicit approval | Human | Required before final promotion |

## When to use

Use this recipe when picture timing is already approved but scratch narration must be replaced with
a production voice. It is also appropriate before picture lock when exact phrase slots already own
the storyboard. Do not globally stretch a continuous narration when the measured phrase drift would
break semantic sync.

## Inputs

- Approved narration text.
- Approved picture or whole-frame phrase timeline.
- Current ElevenLabs voice catalog and account entitlement evidence.
- Required pronunciation list.
- Separate SFX and music sources.
- Output fps, runtime, and loudness target.

## Output structure

```text
<project>/
  audio/voiceover/<version>/
    <narration>-raw.mp3
    <narration>-alignment.json
    pronunciation-dictionary.json
    VOICEOVER.md
  edit/audio/<version>/
    narration-phrase-locked.wav
    narration-phrase-locked-edl.json
    narration-word-boundaries.json
    sfx-phrase-locked.wav
    audio-master.wav
  edit/timelines/<version>.json
  edit/<version>.srt
  edit/verify/<version>/
  review/<version>-qc.md
  deliverables/review-cuts/<version>-clean.mp4
  deliverables/review-cuts/<version>-captioned.mp4
```

## Steps

1. Inspect the live voice catalog and the current account entitlement. A catalog match is not proof
   that the current account may synthesize it through the API.
2. Prefer an account-owned, rights-safe voice when a shared-library voice is unavailable. Generate
   only a short pronunciation audition before the full take.
3. Create a versioned pronunciation dictionary for ambiguous names and acronyms. Preserve IDs and
   rules, never credentials.
4. Generate the entire narration in one request with timing metadata. Keep the raw audio and
   character alignment immutable.
5. Run ASR on the raw result. Reject or revise it if required names, numbers, or the complete text
   are not recovered.
6. Compare every narration phrase against its approved whole-frame slot. Retain natural delivery
   plus tail silence when a phrase fits.
7. Time-compress only phrases that overrun their slots, using a pitch-preserving transform. Record
   the ratio for every changed phrase and reject conspicuous compression.
8. Rebuild diegetic SFX into their original visual slots from approved stems. Do not bake narration
   into generative footage or overwrite the source picture.
9. Mix narration and SFX as separate stems. Measure integrated loudness and true peak; do not hide a
   poor performance with aggressive dynamic processing.
10. Rebuild captions from the conformed word boundaries and omit copy already rendered
    deterministically when duplication would be distracting.
11. Mux clean and captioned review cuts from the same picture and audio master.
12. Verify decode, exact duration/frame count, stream parity, black frames, captions, phrase
    boundaries, loudness, peaks, and ASR on the encoded artifact.
13. Mark the result `NEEDS HUMAN` until a person listens to the complete encoded review cut. Do not
    replace the approved final before that approval.

## Host rows

| Host | Execution surface | Credential rule | Parity rule |
|---|---|---|---|
| Codex | ElevenLabs official API or configured MCP; FFmpeg/FFprobe; project Python conformer | Read the user environment at runtime; never print or persist the key | Follow this shared recipe and canonical project skill |
| Claude | ElevenLabs configured MCP or official API; FFmpeg/FFprobe; same project Python conformer | Same | Follow this shared recipe and mirrored project skill |

## Verified reference run

- Project: `Ramayana-ZebpaySIP`
- Version: v006 review
- Date: 2026-07-24
- Voice: account-owned `NarratorZebPay`
- Runtime: 52.200 seconds
- Picture: unchanged approved v005 clean picture, 1,566 frames at 30 fps
- Conform: only three overrun phrases accelerated; maximum ratio 1.210x; pitch preserved
- Encoded audio: approximately -16.0 LUFS integrated and -3.3 dBTP
- Semantic check: ASR recovered all 105 narration words and all required names
- Promotion status: technical pass, human listening approval still required
