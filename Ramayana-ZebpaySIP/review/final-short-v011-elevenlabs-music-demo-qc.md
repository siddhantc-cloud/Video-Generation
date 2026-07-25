# Final short v011 ElevenLabs + demo music QC

## Review checklist

| Requirement | Pass condition | Evidence | Owner | Status |
|---|---|---|---|---|
| Source safety | Approved v005 final and prior reviews remain unchanged | New v011 review paths | Editor | Pass |
| Surgical voice repair | Only G12 narration changes from v006 | Patch metadata | Editor | Pass |
| SIP intelligibility | Encoded ASR recovers `SIP lets you invest` without a preceding article | Final Scribe v2 transcript | Audio QC | Pass; human cadence accepted |
| Mix preservation | Narration/SFX use v006 coefficients; no full-mix normalization or limiter | Mix metadata | Sound editor | Pass |
| Demo music rights | Track and license are recorded and marked non-final | `audio/music/demo-v011/SOURCE.md` | Producer | Pass |
| Music separation | Music is independently replaceable and ducked 6 dB under detected speech | Duck stem and mix metadata | Sound editor | Pass |
| Stream lock | Both variants are 1,566 frames, 52.200 seconds, 1080×1920 at 30 fps | FFprobe | QC | Pass |
| Audio identity | Clean and captioned variants contain the same AAC stream | MD5 `c601bde7540f0585612040174888e336` | Audio QC | Pass |
| Loudness | Speech-led demo mix retains headroom without aggressive processing | -16.5 LUFS, 4.2 LU LRA, -3.2 dBTP | Audio QC | Pass |
| Decode | Full video and audio decode reports no error | FFmpeg exit 0 for both variants | QC | Pass |
| Black-frame check | No black interval of 0.10 seconds or longer | Blackdetect returned zero intervals | QC | Pass |
| Captions | Approved v005 caption geometry is reused and G15 remains subtitle-free | Final contact sheets | Editor/QC | Pass |
| Human playback | Owner accepts narrator, both SIP uses, ZebPay, demo music, and SFX balance | Owner conversation, 2026-07-24; reconfirmed 2026-07-25 | Human | Pass |

## Technical evidence

- Timeline: `edit/timelines/final-short-v011-elevenlabs-music-demo.json`
- Voice record: `audio/voiceover/elevenlabs-v011/VOICEOVER-v011.md`
- Patch metadata:
  `edit/audio/elevenlabs-v011-demo/narration-phrase-locked-v005-sip-at-start.metadata.json`
- Mix metadata:
  `edit/audio/elevenlabs-v011-demo/Ramayana-ZebPaySIP_AUDIO_MASTER_v011_demo-music.metadata.json`
- Encoded transcript:
  `edit/audio/elevenlabs-v011-demo/scribe-final-mix/Ramayana-ZebPaySIP_REVIEW_v011_elevenlabs-sip-at-start_music-demo_captioned.json`
- Overview contact: `edit/verify/final-short-v011/overview-caption-contact-final.png`
- SIP/caption contact: `edit/verify/final-short-v011/v011-caption-37.6-final.png`

The final Scribe transcript is:

> An army of Vanaras was building Ram Setu, boulder by boulder. At the edge of the shore, a tiny
> squirrel carried one pebble at a time. The others laughed. What difference could something so
> small make? But Rama saw what they missed. The squirrel kept showing up, whether the tide was calm
> or rough. And with every return, another gap was filled. Investing can work the same way. You do
> not need to predict the perfect market moment. SIP lets you invest the same amount regularly
> through the ups and downs. Small steps, repeated consistently, can build something bigger. Start
> your SIP with Zebpay.

## Outputs

- Clean review:
  `deliverables/review-cuts/final-short-v011/Ramayana-ZebPaySIP_REVIEW_v011_elevenlabs-sip-at-start_music-demo_clean.mp4`
  - SHA-256: `80CE2F3322830FD4F0E91F5B7430308E32F33C014CA7507667A4A184E8C89091`
  - 50,463,540 bytes
- Captioned review:
  `deliverables/review-cuts/final-short-v011/Ramayana-ZebPaySIP_REVIEW_v011_elevenlabs-sip-at-start_music-demo_captioned.mp4`
  - SHA-256: `7CD0003E9318DBA1BAD640A4E8552B2D991D401097B1D8AEC69BE164F201705B`
  - 44,218,578 bytes

## Verdict

`PASS — HUMAN CREATIVE APPROVED`. Technical QC and complete owner playback passed. v011 remains a
review cut, not a promoted campaign final: the demo track must be replaced or explicitly cleared
for final use, commercial voice entitlement must be confirmed, and brand, legal, regulatory, and
explicit promotion approvals remain separate.
