# Short v004 motion-generation plan

## Execution checklist

| Requirement | Pass condition | Evidence | Owner | Status |
|---|---|---|---|---|
| Picture lock | Motion replaces the approved v004 keyframe cells without changing narration timing | `shot-plan.md`; `edit/edl/animatic-short-v004.json` | Director/Editor | Complete |
| Explicit start role | Every generative shot uses its approved conformed frame as `start_image`, never a generic image reference | `motion-shot-manifest.json`; K01 v001 review | Operator | Locked |
| Model policy | Actual Seedance 2.0 Standard, 480p, High bitrate, Sound On, one candidate | Manifest plus job records | Producer/Operator | Locked |
| Duration policy | Each request covers the complete beat, rounded up to Seedance's integer/minimum duration | Timing table below | Director | Complete |
| Continuity | Only the visible canonical characters and matching bridge stage are attached | Manifest reference lists | Continuity | Complete |
| Paid control | Exact cost is read before each submission; every returned job ID is persisted and duplicate submission is prevented | CLI cost/job/account records | Producer/Operator | Exact first-pass quotes complete; submission active |
| Keeper gate | A rejected generated cell falls back to its approved keyframe animation until a diagnosed correction passes | `review/short-v004-motion-first-pass-review.md` | Director/Editor | Complete for first pass; K03 range-restricted |
| Final delivery | Keeper motion, deterministic graphics, narration, native SFX, captions, and end card form one QC-passed master; any unavailable optional music is documented | Final timeline and `review/final-short-v003-qc.md` | Editor/Human | Operator QC complete; human/brand release pending |

## Request durations and first-pass budget

| Shot | Edit duration | Seedance request | First-pass credits at verified 3 credits/s |
|---|---:|---:|---:|
| K01 | 5.867 s | 6 s | 18 |
| K02 | 1.900 s | 4 s | 12 |
| K03 | 4.000 s | 4 s | 12 |
| K04 | 2.100 s | 4 s | 12 |
| K05 | 3.633 s | 4 s | 12 |
| K06 | 2.767 s | 4 s | 12 |
| K07 | 3.567 s | 4 s | 12 |
| K08 | 1.567 s | 4 s | 12 |
| K09 | 4.300 s | 5 s | 15 |
| K10 | 3.067 s | 4 s | 12 |
| K14 | 5.467 s | 6 s | 18 |
| **Motion pass total** | **34.233 s used** | **49 s billed** | **147** |

The rejected K01 v001 generic-image experiment adds 18 sunk credits, so a successful K01 v002 plus
one first pass of every remaining motion cell would place total new v004 learning spend at 165
credits. G11-G13 and G15 remain deterministic and consume no Higgsfield credits.

All fully referenced first-pass packets were re-priced on 2026-07-23. K01/K14 quote 18 credits,
K09 quotes 15, and every four-second K02-K08/K10 packet quotes 12. K01 v002 is a reviewed keeper.
The remaining approved first-pass submission cap is therefore **129 credits**.

The account currently permits eight concurrent `seedance_2_0` jobs. A K09/K10/K14 submission batch
accepted K09 as the eighth active job and rejected K10/K14 with `rate_limit_reached` before creating
jobs or charges. Wait for capacity and submit only the manifest rows without a persisted job ID.
After K03 and K05 completed, K10 and K14 were submitted once. All remaining first-pass jobs now have
persisted IDs and the account charge for K02-K10/K14 totals exactly 129 credits.

## Edit policy

- Generated media is immutable raw footage under `footage/generated/`.
- Only reviewed keepers are copied or linked into `footage/selects/`.
- The final timeline trims each request to the existing v004 cell boundaries; narration timing never
  stretches to accommodate a generation.
- A failed motion cell does not block assembly. The approved v004 keyframe move remains the safe
  fallback, preserving the complete film while the failed class is diagnosed.
- Narration remains separate. Native Seedance audio supplies diegetic SFX/ambience only; music and
  loudness balancing happen in post.
