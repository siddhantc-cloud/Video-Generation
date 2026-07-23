# Short v004 motion first-pass review

## Acceptance checklist

| Requirement | Pass condition | Evidence | Owner | Status |
|---|---|---|---|---|
| Submission integrity | One persisted job and one matching charge exist for every approved packet | `storyboard/short-v004/motion-shot-manifest.json`; account ledger | Producer/Operator | Pass |
| Model and cost lock | Seedance 2.0 Standard, 480p, High, Sound On, one candidate; charges equal quotes | Job records; account balance 3854.03 | Producer/Operator | Pass |
| Technical validity | Every output decodes with H.264 video and stereo AAC audio | FFprobe matrix below | Operator | Pass |
| Continuous motion | No output contains a detected structural cut | Contact sheets; zero scene hits above 0.35 for K02-K10/K14 | Director/Operator | Pass |
| Story continuity | Every selected range preserves its required subject, location stage, and direction | Visual review matrix below | Director/Operator | Pass with K03 range restriction |
| Immutable selects | Every promoted select is byte-identical to its raw generation | SHA-256 copy verification | Operator | Pass |
| Editorial fallback | Any invalid range is excluded without a blind reroll | K03 uses only the pebble-valid opening range | Editor | Locked |

## Verdict matrix

| Shot | Output | Motion verdict | Native-audio mean/peak | Review note |
|---|---|---|---:|---|
| K01 v002 | 6.060 s | Keeper | -25.6/-11.6 dB | Continuous Rama-to-workforce reveal; generative first-frame recomposition recorded separately |
| K02 v001 | 4.063 s | Keeper | -21.3/-2.0 dB | Squirrel stays tiny and stable while the background workforce moves |
| K03 v001 | 4.063 s | **Partial keeper: use 0.00-1.50 s only** | -26.2/-2.8 dB | Pebble is intact in the opening walk, then disappears; slow only the valid range to fill its edit cell |
| K04 v001 | 4.063 s | Keeper | -25.7/-9.8 dB | Lead vanara maintains the boulder and gives a restrained glance; squirrel remains composed |
| K05 v001 | 4.063 s | Keeper | -19.8/-6.0 dB | Strong, readable size contrast with stable squirrel, pebble, boulder, and legs |
| K06 v001 | 4.063 s | Keeper | -42.8/-23.0 dB | Stable quiet recognition between Rama and squirrel; supplement very quiet ambience in post |
| K07 v001 | 4.063 s | Keeper | -32.0/-4.8 dB | Calm return movement and bridge geography remain stable |
| K08 v001 | 4.063 s | Keeper | -22.2/-5.0 dB | Strong storm motion; squirrel remains planted and anatomically stable |
| K09 v001 | 5.062 s | Keeper | -31.0/-7.3 dB | Packed pebble seam remains coherent with subtle water/grit motion |
| K10 v001 | 4.063 s | Keeper | -35.7/-17.5 dB | Clean completed causeway glide; no generated words or symbols |
| K14 v001 | 6.060 s | Keeper | -48.9/-30.3 dB | Stable completed bridge and squirrel end tableau; supplement quiet ambience in post |

All K02-K10/K14 files are H.264 496x864 at 24 fps with stereo 44.1 kHz AAC. Four-second
requests return 4.063 seconds, K09 returns 5.062, and six-second K14 returns 6.060.

## Spend summary

- Rejected K01 v001 learning take: 18 credits.
- Accepted K01 v002 correction: 18 credits.
- K02-K10/K14 first pass: 129 credits.
- Total new short-v004 learning and production spend: **165 credits**.
- Account balance after the pass: **3854.03 credits**.
- No K10/K14 charge was created by the first `rate_limit_reached` response; each was submitted once
  only after capacity reopened.

## Evidence

- Raw video and companion records: `../footage/generated/`
- Immutable promoted copies: `../footage/selects/`
- Extracted native SFX: `../audio/sfx/generated/`
- 2 fps contact sheets: `frames/K*_2fps_contact.png`
- K03 detail audit: `qc-frames/K03_v001_squirrel-detail.png`
- K01 corrected review: `K01_v002-review.md`
