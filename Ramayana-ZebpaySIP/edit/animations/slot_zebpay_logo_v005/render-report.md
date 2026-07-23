# ZebPay Logo v005 render report

## Checklist

| Requirement | Pass condition | Evidence | Owner | Status |
|---|---|---|---|---|
| Authorized composition | Human requested the premium ZebPay logo and review cut | Conversation request | Human | Complete |
| Storyboard | Three cards sum to 3.333333 seconds | `STORYBOARD.md` | Codex | Complete |
| HyperFrames gate | Lint, runtime, 84-sample layout, motion, frame, and contrast checks pass | Final `hyperframes check` | Codex | Complete |
| Exact output | 1080 × 1920, 30 fps, 100 frames, 3.333333 seconds | FFprobe | Codex | Complete |
| Codec compatibility | H.264 High, yuv420p | FFprobe | Codex | Complete |
| Decode integrity | Every frame decodes; no black interval is detected | FFmpeg decode and blackdetect | Codex | Complete |
| Boundary continuity | Local frames 0 and 1 preserve the outgoing K14 picture before transformation | `verify/render-v005/logo-render-contact.png` | Codex | Complete |
| Closing hold | Frame 99 contains the complete logo and CTA; there is no end fade | `verify/render-v005/logo-render-contact.png` | Codex | Complete |
| Master safety | Existing v003 masters remain byte-identical | Final SHA-256 verification | Codex | Complete |

## Selected render

`renders/zebpay-logo-v005_1080x1920_30fps_hq.mp4`

- SHA-256: `4E6EF7704FF493D1EB81EC57D20B1CFC7BBBC784A6EC70D52FD286DB7DFF4C66`
- Size: 1,874,511 bytes
- Codec/profile: H.264 High
- Pixel format: yuv420p
- Dimensions: 1080 × 1920
- Frame rate: 30/1
- Duration: 3.333333 seconds
- Frames declared/read: 100/100
- Decode check: pass
- Blackdetect: none
- Outgoing master frame 1465 vs local frame 0 SSIM: `0.990158` after H.264 encoding

## Creative result

The exact outgoing K14 frame remains visible at local frame 0. Three restrained light paths then
travel along Ram Setu toward the horizon, which blooms into the sampled ZebPay blue (`#2072EF`).
The supplied logo asset resolves without being redrawn or distorted. `START YOUR SIP` remains fully
readable through frame 99; no exchange-age claim, return promise, or end fade is present.

## Review evidence

- `preview/zebpay-logo-v005-contact.png`
- `verify/render-v005/logo-render-contact.png`
