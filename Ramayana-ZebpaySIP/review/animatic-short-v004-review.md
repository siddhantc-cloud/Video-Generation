# Animatic short v004 — self-review

## Review checklist

| Requirement | Pass condition | Evidence | Owner | Status |
|---|---|---|---|---|
| Decode | Full file decodes without an FFmpeg error | Null decode on 2026-07-23 | Editor | Pass |
| Frame lock | Output contains exactly 1,566 frames at 30 fps | v004 EDL and FFprobe | Editor | Pass |
| Stream sync | Audio/video drift is less than one frame | 0.001667 s measured drift | Editor | Pass |
| Semantic sync | Each visual cut is within half a frame of its matching word boundary | 13.5 ms maximum error | Editor | Pass |
| Boundary review | Every transition is inspected before/after the cut | `boundary-pairs.png` | Editor | Pass |
| Flash correction | K10→G11 has no internal black/navy flash | `K10-G11-boundary-fixed.png` | Editor | Pass |
| Continuity | Keyframes pass character, geography, palette, and crop review | `keyframes-short-v004-review.md` | Continuity | Pass |
| Investment safety | Graphics explain regularity without a return promise | SIP metaphor clip and copy audit | Brand/Editor | Pass |
| Brand determinism | Logo and CTA are post-produced, not generated inside imagery | End-card clip and source | Editor | Pass |
| Human playback | Human accepts image quality, semantic timing, pacing, and graphic direction | v004 review cut | Human | Pending |

## Verdict

**TECHNICAL / EDITORIAL SELF-REVIEW PASS. HUMAN PLAYBACK PENDING.**

Review cut:
`deliverables/review-cuts/animatic-short/ZebPay_Squirrel_SHORT_ANIMATIC_v004.mp4`

This is the first version in the short-form series with both stream sync and phrase-level semantic
sync. It remains an animatic with scratch narration, not a final master.

## Verified output

- Runtime: 52.200 seconds.
- Raster: 1080×1920 vertical.
- Frame rate: 30 fps constant.
- Video: H.264, yuv420p.
- Audio: AAC, 48 kHz stereo.
- Frames: 1,566 exactly.
- Video duration: 52.198333 seconds.
- Audio duration: 52.200000 seconds.
- Measured stream drift: 0.001667 seconds.
- Decode: pass.

## Semantic-sync evidence

The narration was synthesized once. The same Edge TTS request produced 105 word-boundary events.
Each cut was snapped to the nearest whole 30 fps frame.

- Maximum visual-cut error, excluding intentional opening pre-roll: 13.5 ms.
- One frame at 30 fps: 33.3 ms.
- Final spoken word ends at 50.820 seconds.
- Deterministic end-card hold after the final word: 1.380 seconds.

The opening visual begins 102 ms before “An,” which is intentional pre-roll rather than a semantic
error.

## Boundary review

Evidence:

- `edit/verify/animatic-short-v004/boundary-pairs.png`
- `edit/verify/animatic-short-v004/K10-G11-boundary-fixed.png`
- `edit/verify/animatic-short-v004/sequence-contact-sheet.png`

One issue was found during self-review: the first SIP-graphic build faded from solid navy for ten
frames, causing a dark flash at K10→G11. The fade was removed, both graphic clips were rebuilt, the
master was rerendered, and the boundary was rechecked. No blank frame, duplicate transition frame,
or unintentional flash remains in the reviewed master.

## Copy and safety audit

Visible deterministic copy is limited to:

- THE MARKET MOVES
- SAME AMOUNT. REGULARLY.
- THROUGH UPS AND DOWNS
- MARKET PATH
- EQUAL CONTRIBUTIONS
- ZebPay
- START YOUR SIP

The cut contains no promise of returns, no predicted outcome, no “India's oldest crypto exchange”
claim, and no like/share/subscribe copy. The graph path moves both up and down while identical
contribution markers continue at fixed intervals.

## v003 → v004 comparison

| Dimension | v003 | v004 |
|---|---|---|
| Human status | Rejected | Pending playback |
| Runtime | 57.900 s | 52.200 s |
| Narration construction | Eight separately synthesized blocks | One continuous performance |
| Picture timing | Percentage weights inside narration blocks | First-word boundary per visual idea |
| Semantic timing error | Unmeasured/arbitrary | 13.5 ms maximum |
| Story imagery | Repetitive amber poster treatment | Eleven newly directed, continuity-grounded plates |
| Calm/rough contrast | Multiple same-look stills | Matched geography with explicit calm/storm pair |
| SIP section | Three static presentation cards | One continuous bridge-based animated metaphor |
| Brand card | Clean but basic static card | Animated deterministic premium card |
| Stream drift | 0.000 s | 0.001667 s |

## Remaining work

1. Human playback and taste verdict.
2. Any image or pacing notes from that playback.
3. Final narration casting/performance.
4. Diegetic SFX, ambience, music, and captions.
5. Brand/legal review before release.
6. Only after the animatic is locked: paid motion generation for the selected beats.
