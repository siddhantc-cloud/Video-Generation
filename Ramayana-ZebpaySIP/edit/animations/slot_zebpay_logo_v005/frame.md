# ZebPay Logo v005 — normative frame

## Checklist

| Requirement | Pass condition | Evidence | Owner | Status |
|---|---|---|---|---|
| Exact story timing | Exactly 100 frames at 30 fps (3.333333 s) | FFprobe after render | Codex | Complete |
| Incoming continuity | Frame 0 reproduces global frame 1465 before the transition begins | Boundary contact sheet | Codex | Complete |
| Brand fidelity | The supplied ZebPay logo asset is used unmodified and remains legible | Source + rendered frames | Codex | Complete |
| CTA ownership | `START YOUR SIP` is the only large call to action | Render inspection | Codex | Complete |
| Closing hold | The complete lockup holds without fading through frame 99 | Rendered frame 99 | Codex | Complete |
| Mobile readability | Brand name ≥150 px and CTA ≥63 px | Source + layout audit | Codex | Complete |
| Caption policy | No redundant G15 subtitle is burned over the deterministic CTA | `edit/master-short-v001.srt` | Codex | Complete |

## Visual system

- Canvas: 1080 × 1920, 30 fps.
- Source transition: exact outgoing K14 frame from the existing v003 clean master.
- Supplied logo background blue: sampled from the asset as `#2072EF`.
- Palette: ink `#020817`, navy `#061733`, brand blue `#2072EF`, light blue `#79AEFF`, warm white `#F4F7FF`, muted blue `#B6C8E6`, Ram Setu amber `#E9B96E`.
- Display type: Montserrat 900. Technical microtype: Space Mono 700.
- Geometry: bridge-perspective rails converge into the brand mark, linking the Ram Setu metaphor to the sponsor reveal.
- No unapproved exchange-age claim, return promise, price, rate, or extra product feature.

## Motion beats

1. Frames 0–17: preserve the outgoing Ram Setu image while three light paths travel along the bridge toward its horizon.
2. Frames 18–47: a cobalt horizon flare transforms the film world into the ZebPay brand field; the official mark and wordmark resolve.
3. Frames 48–99: `START YOUR SIP` locks in and holds as the final readable state. No end fade.

The final state intentionally occupies the full closing beat. Captions omit G15 because the card already renders the spoken CTA verbatim.
