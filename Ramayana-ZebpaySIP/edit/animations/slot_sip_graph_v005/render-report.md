# SIP Graph v005 render report

## Checklist

| Requirement | Pass condition | Evidence | Owner | Status |
|---|---|---|---|---|
| Approved composition | Human approved the Studio/contact-sheet direction before render | Conversation approval | Human | Complete |
| Storyboard | Three animated cards match the phrase map and total duration | `STORYBOARD.md` + Studio board | Codex | Complete |
| HyperFrames gate | No lint, runtime, layout, motion, contrast, or caption-zone failures | Final `npm run check` | Codex | Complete |
| Exact output | 1080 × 1920, 30 fps, 319 frames, 10.633333 s | FFprobe | Codex | Complete |
| Codec compatibility | H.264 High, yuv420p | FFprobe | Codex | Complete |
| Decode integrity | Every frame decodes; no black interval detected | FFmpeg decode + blackdetect | Codex | Complete |
| Phrase ownership | Local frames 133 and 245 are the first frames of their new visual phrases | `r3-boundary-contact.png` | Codex | Complete |
| Master safety | Existing v003 masters remain untouched | Output isolated under this slot | Codex | Complete |

## Selected render

`renders/sip-graph-v005_r3_1080x1920_30fps_hq.mp4`

- Codec: H.264 High
- Pixel format: yuv420p
- Dimensions: 1080 × 1920
- Frame rate: 30/1
- Duration: 10.633333 seconds
- Frames declared/read: 319/319
- File size: 10,934,430 bytes
- Decode check: pass
- Blackdetect: none

## Self-correction history

1. Initial render preserved exact duration but the outgoing and incoming headlines overlapped for 2–3 frames at both phrase boundaries.
2. Repair 2 removed the overlap but advanced each new headline by one frame.
3. Repair 3 derives transition times as `133 / 30` and `245 / 30`. The actual rendered boundary frames now preserve exact phrase ownership:

   - frame 132: outgoing beat 1;
   - frame 133: incoming beat 2;
   - frame 244: outgoing beat 2;
   - frame 245: incoming beat 3;
   - frame 318: resolved final state.

The first two renders remain preserved as QC evidence. The selected asset is repair 3.

## Review evidence

- `verify/render-v005/r3-hero-contact.png`
- `verify/render-v005/r3-boundary-contact.png`
