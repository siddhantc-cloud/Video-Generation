# Final short v005 premium-graphics QC

## Review checklist

| Requirement | Pass condition | Evidence | Owner | Status |
|---|---|---|---|---|
| Source safety | Locked v003 clean and captioned masters retain their published SHA-256 hashes | Hash verification | Codex | Pass |
| Picture map | Only frames 983–1301 and 1466–1565 are replaced | `edit/timelines/final-short-v005-premium-graphics.json` | Editor/QC | Pass |
| Stream lock | Both variants contain 1,566 frames and 52.200-second video/audio streams | FFprobe | QC | Pass |
| Audio preservation | Original AAC elementary stream is copied without alteration | Matching MD5 `09db2492eab6ae63ba8d6295f08f9511` | Sound/QC | Pass |
| Decode | Full video and audio decode reports no error | FFmpeg full decode | QC | Pass |
| Black-frame check | No black interval of 0.10 seconds or longer | FFmpeg blackdetect | QC | Pass |
| Graph phrase ownership | Graph begins at frame 983; local beat boundaries remain 133 and 245 | Caption/graphics contact sheet | Editor/QC | Pass |
| Logo continuity | Frame 1466 reproduces the outgoing K14 picture before the logo transformation | Clean boundary sheet | Editor/QC | Pass |
| Logo hold | The full lockup remains present through frame 1565 | Clean boundary sheet | Brand/QC | Pass |
| Caption order | Captions are burned after picture assembly and occupy the lower safe band | Caption/graphics contact sheet | Editor/QC | Pass |
| CTA duplication | No final subtitle duplicates `START YOUR SIP` | SRT plus final frames | Editor/QC | Pass |
| Human playback | Human watches the complete captioned review cut with sound | Owner approval in conversation, 2026-07-24 | Human | Pass |
| Brand/legal release | Human/brand owner approves final ZebPay presentation | Review cut | Human/Brand | Pending |

## Operator verdict

The cut is technically ready for human playback. The SIP graph and closing logo are frame-exact,
visually continuous, readable at vertical feed scale, and free of black flashes. The captions were
repositioned from the graph focal curve into the lower safe band before the selected captioned
render. The outgoing master frame and encoded logo frame 0 measure `0.990158` overall SSIM. The
original narration, native SFX, and mix are not re-encoded.

## Review evidence

- Clean transition pairs: `edit/verify/final-short-v005/boundary-pairs-clean.png`
- Graph/caption/logo frames: `edit/verify/final-short-v005/graphics-caption-contact.png`
- Five-second overview: `edit/verify/final-short-v005/overview-5sec-contact.png`
- Logo render audit:
  `edit/animations/slot_zebpay_logo_v005/verify/render-v005/logo-render-contact.png`

## Review deliverables

- Captioned:
  `deliverables/review-cuts/final-short-v005/Ramayana-ZebPaySIP_REVIEW_v005_premium-graphics_captioned.mp4`
  - SHA-256: `DBB08C1682CFCB45CDA8DE90C53DEDA9319DF862F0C099A123991F855B899B47`
  - 47,805,218 bytes
- Clean:
  `deliverables/review-cuts/final-short-v005/Ramayana-ZebPaySIP_REVIEW_v005_premium-graphics_clean.mp4`
  - SHA-256: `0696E4B7F4F3474B0D8B90B15B34A5313E820A8FB0E232003934D512E05225E4`
  - 50,394,436 bytes

The captioned review cut was approved by the owner and promoted byte-for-byte to
`deliverables/final/Ramayana-ZebPaySIP_FINAL_v005_1080x1920_captioned.mp4` on 2026-07-24. The clean
cut remains a review asset. Any required brand/legal release remains a separate pending sign-off.
