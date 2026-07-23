# Animatic production-readiness audit

## Audit checklist

| Requirement | Pass condition | Evidence | Owner | Status |
|---|---|---|---|---|
| Legacy recovery | The previous ZebPay storyboard, keyframes, animatic, EDL, audio mix, and end card are preserved in the clean workspace | SHA-256 comparison against `zebpay/` | Editor | PASS |
| Editorial sync | The animatic is frame-locked and its technical properties match the EDL | `edit/edl/animatic.json`; FFprobe | Editor | PASS: 4999 frames, 166.633 seconds, 0.0003 seconds drift |
| Story coverage | Every narration beat has an assigned visual in film order | `edit/timelines/animatic.json` | Director/Editor | PASS: 24 timed rows |
| Keyframe inventory | The recovered clean set matches the earlier set | Hash comparison of `zebpay/keyframes/` and `keyframes/` | Art/Editor | PASS: all 30 files identical |
| Runtime approval | The human approves the 166.633-second cut or a shorter alternative before broad paid generation | Human review note | Human/Editor | PENDING |
| Generation conformance | Every image used as a start/end input is exact 9:16 and reviewed after crop/outpaint | Dimension report plus conformed-image review | Art/Director | FAIL: 15 images are 1024x1536 and only S1-a has a dedicated 1080x1920 conform |
| Endpoint safety | A proposed start/end pair preserves identity, scale, hand/prop geometry, and reachable motion | Pairwise visual review | Director/Continuity | FAIL for the current S4-c pair |
| Identity continuity | Rama, squirrel, and lead vanara keyframes match their canonical assets closely enough to animate | Visual comparison against `assets/characters/` | Director/Continuity | NEEDS REVISION for S4-c end; otherwise usable as planning frames |
| Deterministic sections | Still pushes, investing graphics, sacred text, captions, and sponsor card stay outside paid generation | Shooting script and expectations | Editor | PASS in plan |
| Moving-footage conform | Approved moving selects replace animatic slides without changing the approved narration clock | Final replacement EDL | Editor | PENDING |

## Verified recovery

The previous workflow was already completed and then copied into the clean workspace. It should not
be rebuilt.

- `zebpay/animatic/ZebPay_Squirrel_ANIMATIC.mp4` and
  `deliverables/review-cuts/animatic/ZebPay_Squirrel_ANIMATIC.mp4` are byte-identical.
- The old and clean EDL files, scratch audio mixes, and deterministic end cards are byte-identical.
- `zebpay/storyboard.html` and `storyboard/index.html` are byte-identical.
- All 30 old and clean keyframe files are byte-identical.
- The final recovered animatic is H.264/AAC, 1080x1920, 30 fps, 4999 frames, and 166.633 seconds.
- A twelve-sample visual overview is retained at `review/frames/animatic-overview.png`.

The animatic contains 298 spoken words across 24 timed rows. It is a valid editorial prototype, but
its existence is not approval of its runtime.

## Visual findings

### Strong enough to retain

- The warm golden-hour visual law is coherent across the film.
- S1-a and S4-a read as the same Rama closely enough for planning, although the final generation
  must still bind the canonical Rama assets.
- S3-b and S3-c preserve the lead vanara well, and the group-laugh frame belongs to the same visual
  world.
- The bridge and squirrel story remain understandable from stills alone.

### Must be fixed before animation

1. **Fifteen keyframes are 1024x1536 (2:3), not 9:16.** A deterministic center crop to
   864x1536 would remove 80 pixels from each side, but every resulting crop must be reviewed.
   Do not let the Higgsfield composer make an unobserved crop.
2. **The current S4-c endpoint pair is not interpolation-safe.** `S4-c_start.png` contains one open
   palm and a standing squirrel. `S4-c_end.png` changes to two cupped hands, a different contact
   geometry, different squirrel scale, and a more mascot-like eye/body treatment. Feeding these as
   literal endpoints encourages finger morphing, body rescaling, and identity drift.
3. **S4-c should use a repaired endpoint or no end frame.** The safest next design is the existing
   start frame plus a very small settle/lift motion, with the canonical squirrel reference. If an
   endpoint is required, edit a new end frame that preserves the same hand, camera, scale, and
   squirrel identity.
4. **S6 is still a placeholder visual treatment.** Its 20.5-second timing works, but the calm ocean
   still should be replaced by the planned deterministic investment/SIP motion-graphic sequence
   before picture lock.

## Animatic-to-moving-footage conform

The animatic remains the editorial source of truth. Each paid take is coverage used to replace one
or more approved animatic cells. The keyframe images establish the intended composition; they are
not automatically valid Seedance endpoints.

Candidate full-production grouping after the representative pilots pass:

| Candidate job | Animatic coverage | Billed duration at current integer controls | Method | Important condition |
|---|---|---:|---|---|
| J01 | S1-a | 10 s | Single continuous shot | Must cover the known 6.375-second cut-failure window |
| J02 | S1-b | 10 s | Single aerial reveal | Crowd remains distant |
| J03 | S1-c | 6 s | Single action | Boulder and splash survive |
| J04 | S1-d | 6 s | Moving background plus deterministic inscription | No generated text |
| J05 | S2-a | 8 s | Single arrival shot | Establish canonical squirrel scale |
| J06 | S2-b + S2-c | 7 s | Intentional two-shot sequence | Same squirrel/location; name the internal cut |
| J07 | S3-a | 5 s | Single action | Pebble remains visible |
| J08 | S3-b + S3-c/group laugh | 9 s | Intentional multi-shot sequence | Same lead vanara; maximum two internal cuts |
| J09 | S3-d | 6 s | Single tracking shot | Baby vanara and stone stay stable |
| J10 | S3-e | 4 s | Isolated high-risk contact/action shot | Do not group; use cutaway fallback after structural failure |
| J11 | S4-a + S4-b | 9 s | Intentional two-shot Rama sequence | Canonical Rama assets own identity |
| J12 | S4-c | 7 s | Isolated high-risk contact shot | Repair endpoint strategy first |
| J13 | S4-d | 7 s | Isolated macro contact shot | Stable stripes; reveal in post |
| J14 | S4-e | 5 s | Reaction coverage | Separate reference packet from S4-d |
| J15 | S5-a + S5-b + S5-c | 11 s | Intentional three-beat montage | Attempt only after isolated S5-b physics pilot passes |
| J16 | S5-d | 9 s | Single bridge pan | Structure reveals but does not morph |
| Mode B | S5-e | 13.333 s edit cell | Deterministic still push | Zero Higgsfield generation |
| Mode B | S6 | 20.5 s edit cell | Deterministic SIP graphics | Redesign placeholder while keeping approved timing |
| J17 | S7-a | 14 s | Near-static payoff shot | Completed bridge and squirrel remain locked |
| Mode B | S7-b | 10 s edit cell | Existing deterministic end card | Brand/legal approval still required |

This candidate map is 17 paid jobs and about 133 billed seconds. At the dated no-reference 480p
Standard quote of 3 credits per second, it is about 399 credits before reference-price effects.
That is only 12 credits below the existing 411-credit one-pass estimate. Grouping reduces jobs and
rounding waste; it does not materially reduce a duration-priced bill and does not remove the
intentional visual cuts.

The largest cost lever is therefore **editing the 166.633-second animatic before animation**, not
packing every beat into 15-second generations.

## Recommended next gate

Before another paid generation:

1. Review the existing animatic and choose whether 166.633 seconds is approved.
2. If not, create a shorter keyframe-only animatic using the same stills and a revised scratch VO.
3. Conform every retained keyframe non-destructively to exact 1080x1920.
4. Repair S4-c endpoint geometry and squirrel identity.
5. Replace the S6 placeholder with a deterministic design in the approved timing.
6. Rebuild the animatic and require `SYNC LOCKED`.
7. Only then stage the three representative 480p Standard pilots.
