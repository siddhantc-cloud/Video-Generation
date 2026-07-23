# Ramayana-ZebPaySIP final short v005

## Delivery checklist

| Requirement | Pass condition | Evidence | Owner | Status |
|---|---|---|---|---|
| Approved source | Promoted bytes match the human-approved captioned v005 review cut | Matching SHA-256 | Human / editor | Pass |
| Technical master | H.264/AAC, 1080×1920, 30 fps, 1,566 frames, 52.200 s, 48 kHz stereo | FFprobe | QC | Pass |
| Decode and boundary QC | Full decode, black-frame, graph, logo, caption, and transition checks pass | `../../review/final-short-v005-premium-graphics-qc.md` | QC | Pass |
| Human playback | Owner approved the complete captioned cut with sound | Conversation, 2026-07-24 | Human | Pass |
| Git delivery | Final is represented by a Git LFS pointer and uploaded with the commit | Git/LFS verification | Partner agent | Pending until push |
| Legal release | Any required advertiser, platform, or legal approval is documented outside operator QC | Release record | Human / brand / legal | Pending |

## Primary deliverable

| File | Purpose | SHA-256 | Bytes |
|---|---|---|---:|
| `Ramayana-ZebPaySIP_FINAL_v005_1080x1920_captioned.mp4` | Primary Shorts/Reels master with premium SIP graph, ZebPay logo close, and burned captions | `DBB08C1682CFCB45CDA8DE90C53DEDA9319DF862F0C099A123991F855B899B47` | 47,805,218 |

The final is a byte-identical copy of
`../review-cuts/final-short-v005/Ramayana-ZebPaySIP_REVIEW_v005_premium-graphics_captioned.mp4`.
It was not re-encoded during promotion.

## Source and QC

- Timeline: `../../edit/timelines/final-short-v005-premium-graphics.json`
- Final QC: `../../review/final-short-v005-premium-graphics-qc.md`
- Graph source: `../../edit/animations/slot_sip_graph_v005/`
- Logo source: `../../edit/animations/slot_zebpay_logo_v005/`

This file records creative and technical promotion. It does not invent legal or regulatory release
approval.
