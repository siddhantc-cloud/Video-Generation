# Ramayana-ZebPaySIP workflow status

Canonical production procedure: `../docs/video-production-workflow.md`.

This file records Ramayana-ZebPaySIP status only. Project evidence overrides generic examples and
no review cut becomes a final merely because its technical QC passed.

## Checklist

| Stage | Pass condition | Evidence | Owner | Status |
|---|---|---|---|---|
| Brief and source | Campaign idea, message, format, and original script are preserved | `project/brief.md`, `scripts/original-script.md` | Human / creative | Built; explicit source approval record absent |
| Visual plan | Shooting plan, continuity assets, storyboard, and keyframes are reviewable | `scripts/`, `assets/`, `storyboard/`, `keyframes/` | Director / producer | Built |
| Animatic | Complete phrase-locked film passes human story and timing review | v004 animatic, phrase map, and EDL | Human / editor | Passed at 52.2 seconds |
| Narrative motion | Every used source range has generation and review evidence | `footage/generated/`, `footage/selects/`, `review/short-v004-motion-first-pass-review.md` | Production / reviewer | Complete |
| Promoted master | Premium graph/logo picture, captions, sound, playback, hash, and Git LFS delivery are recorded | `deliverables/final/DELIVERY-v005.md` | Human / editor / QC | v005 promoted; legal release pending |
| Voice and demo-music candidate | SIP, ZebPay, accent, music, and SFX balance pass complete human playback | `review/final-short-v011-elevenlabs-music-demo-qc.md` | Human | v011 technically passed; human playback pending |
| Release | Music rights plus brand, legal, and regulatory approval are documented | Release records | Human / brand / legal | Pending |

## Current version authority

- **Promoted final:** v005 captioned master. Its delivery record documents human playback and Git
  LFS promotion; legal release remains pending.
- **Newest review candidate:** v011 clean and captioned cuts. Technical QC passed, but the demo
  music is not final-campaign approved and human listening remains the acceptance authority.
- **Promotion rule:** keep v005 unchanged until v011 passes human playback and separately receives
  music, brand, legal, and regulatory approval.

## Project-specific operating evidence

- Manual Higgsfield generation:
  `project/higgsfield-manual-generation-operating-spec.md`.
- Cost and iteration ledger: `project/production-learning-and-cost-plan.md`.
- Audio/frame-lock system: `edit/AV_SYNC_SYSTEM.md`.
- Current promoted delivery: `deliverables/final/DELIVERY-v005.md`.
- Current audio review: `review/final-short-v011-elevenlabs-music-demo-qc.md`.
