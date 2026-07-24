# Final short v006 ElevenLabs voiceover QC

## Review checklist

| Requirement | Pass condition | Evidence | Owner | Status |
|---|---|---|---|---|
| Source safety | Approved v005 final remains unchanged | v005 published SHA-256 remains `DBB08C...B47` | Editor | Pass |
| Voice provenance | Narrator is owned/generated or otherwise authorized | Account-owned Voice Design voice `NarratorZebPay` | Voice producer | Pass |
| Copy fidelity | Mixed output contains all 105 approved words | Final-mix Scribe transcript, English probability 1.0 | Audio QC | Pass |
| Pronunciation | Mythology, SIP, and ZebPay terms remain intelligible | Scribe recovers Vanaras, Ram Setu, Rama, SIP, Zebpay | Audio QC | Pass |
| Semantic timing | Each phrase begins with its approved picture beat | Maximum phrase onset after cut is 30 ms | Editor/QC | Pass |
| Stream lock | Both variants are 1,566 frames with 52.200-second video/audio | FFprobe | QC | Pass |
| Audio identity | Clean and captioned variants contain the same AAC stream | MD5 `fdb5cc91a7730c73a655f5190c5fdf81` | Audio QC | Pass |
| Loudness | Speech-led social mix is near -16 LUFS and below -1.5 dBTP | -16.01 LUFS, -3.28 dBTP | Audio QC | Pass |
| Decode | Full video and audio decode reports no error | FFmpeg exit 0 for both variants | QC | Pass |
| Black-frame check | No black interval of 0.10 seconds or longer | FFmpeg blackdetect returned zero intervals | QC | Pass |
| Caption order | Captions are rebuilt from v006 timing and burned last | v006 SRT and encoded contact sheets | Editor/QC | Pass |
| Graph/logo safety | Captions do not obscure the CTA and G15 remains subtitle-free | Boundary and overview contact sheets | Brand/QC | Pass |
| Human listening | Owner accepts tone, pace, mythological authority, and brand pronunciation | Complete captioned v006 playback | Human | Pending |

## Technical evidence

- Picture source:
  `deliverables/review-cuts/final-short-v005/Ramayana-ZebPaySIP_REVIEW_v005_premium-graphics_clean.mp4`
- Timeline/audio manifest: `edit/timelines/final-short-v006-elevenlabs.json`
- Voice record: `audio/voiceover/elevenlabs-v006/VOICEOVER-v006.md`
- Overview contact: `edit/verify/final-short-v006/overview-caption-contact.png`
- Boundary contact: `edit/verify/final-short-v006/boundary-caption-contact.png`
- Final mixed-audio transcript:
  `edit/audio/elevenlabs-v006/scribe-final-mix/transcripts/Ramayana-ZebPaySIP_REVIEW_v006_elevenlabs_captioned.json`

## Outputs

- Clean review:
  `deliverables/review-cuts/final-short-v006/Ramayana-ZebPaySIP_REVIEW_v006_elevenlabs_clean.mp4`
  - SHA-256: `B6A326787D76617440C3D4F110AD0801B3CE4BAA5A5AD1AB982AE0EE0D015924`
  - 50,423,639 bytes
- Captioned review:
  `deliverables/review-cuts/final-short-v006/Ramayana-ZebPaySIP_REVIEW_v006_elevenlabs_captioned.mp4`
  - SHA-256: `31BB76427D5978A76F698AF0D52506BEB501DF101C6C8033495989631CA7FA0E`
  - 43,593,119 bytes

## Verdict

`NEEDS HUMAN`. All measurable criteria pass. This is a new review version, not a replacement final.
The remaining criterion is subjective listening: accept or reject the voice’s reverence, warmth,
pace, and exact spoken treatment of Vanaras, Ram Setu, Rama, SIP, and ZebPay. Do not promote v006
until the owner closes that criterion.
