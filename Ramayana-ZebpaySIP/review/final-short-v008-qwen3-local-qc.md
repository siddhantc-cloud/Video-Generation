# Final short v008 local Qwen3-TTS voiceover QC

## Review checklist

| Requirement | Pass condition | Evidence | Owner | Status |
|---|---|---|---|---|
| Source safety | Approved v005 final remains unchanged | v005 source remains the picture source; final was not overwritten | Editor | Pass |
| Voice provenance | Original voice is designed locally without a real-person reference | Qwen instruction and metadata | Voice producer | Pass |
| Copy fidelity | Encoded review contains all 105 approved words | Final Scribe v2 transcript, English probability 1.0 | Audio QC | Pass |
| Required terms | Encoded ASR recovers Vanaras, Ram Setu, Rama, both SIP occurrences, and ZebPay | Final word-timing JSON | Audio QC | Pass |
| Acronym timing | Neither SIP occurrence collapses to the rejected near-instant duration | Encoded spans: 0.860 s and 1.221 s | Audio QC | Pass; listening required |
| Semantic timing | Each phrase begins within the accepted picture tolerance | Maximum phrase onset after cut: 30 ms | Editor/QC | Pass |
| Pitch-safe conform | Only overruns are accelerated and maximum is below the 1.21x prior reference | K10 1.030x; G12 1.120x | Editor/QC | Pass |
| Stream lock | Both variants are 1,566 frames with 52.200-second video/audio | FFprobe | QC | Pass |
| Audio identity | Clean and captioned variants contain the same AAC stream | MD5 `cfb431ab17da7f85bd4cbb8a7ddd7e52` | Audio QC | Pass |
| Loudness | Speech-led social mix is near -16 LUFS and below -1.5 dBTP | -16.3 LUFS, -2.0 dBTP after AAC | Audio QC | Pass |
| Decode | Full video and audio decode reports no error | FFmpeg exit 0 for both variants | QC | Pass |
| Black-frame check | No black interval of 0.10 seconds or longer | FFmpeg blackdetect returned zero intervals | QC | Pass |
| Caption order | Captions are rebuilt from v008 timing and burned last | v008 SRT and encoded contacts | Editor/QC | Pass |
| Graph/logo safety | Captions remain readable and G15 is subtitle-free | Overview and boundary contacts | Brand/QC | Pass |
| Human listening | Owner accepts voice identity, accent, mythology terms, SIP initials, pace, and mix | Complete captioned v008 playback | Human | Fail: foreign accent; SIP controlled/robotic |

## Technical evidence

- Timeline/audio manifest: `edit/timelines/final-short-v008-qwen3-local.json`
- Voice record: `audio/voiceover/qwen3-v008/VOICEOVER-v008.md`
- Phrase-lock EDL: `edit/audio/qwen3-v008/narration-phrase-locked-v001-edl.json`
- Overview contact: `edit/verify/final-short-v008/overview-caption-contact.png`
- Boundary contact: `edit/verify/final-short-v008/boundary-caption-contact.png`
- Encoded transcript:
  `edit/audio/qwen3-v008/scribe-final-mix/Ramayana-ZebPaySIP_REVIEW_v008_qwen3-local_captioned.json`

ASR normalization can write `SIP` whether the sound is spoken as a word or as initials. The
substantially longer spans are useful rejection evidence against the prior 60 ms failure, but only
human listening can certify the exact phonemes.

## Outputs

- Clean review:
  `deliverables/review-cuts/final-short-v008/Ramayana-ZebPaySIP_REVIEW_v008_qwen3-local_clean.mp4`
  - SHA-256: `8501B8EE5ED45A64C9C55FB3C78657856841836CB4F70670107775E65FC1A772`
  - 50,445,083 bytes
- Captioned review:
  `deliverables/review-cuts/final-short-v008/Ramayana-ZebPaySIP_REVIEW_v008_qwen3-local_captioned.mp4`
  - SHA-256: `82E9FADC92D95635DBBAE5276DF677375D6C2D5403986B41B6B2F71513FDCAA3`
  - 47,924,918 bytes

## Verdict

`REJECTED BY HUMAN`. The measurable checks remain valid, but owner playback found the accent too
foreign and the SIP delivery too controlled and robotic. See `final-short-v008-human-rejection.md`.
v008 is not a replacement final.
