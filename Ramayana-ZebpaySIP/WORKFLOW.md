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
| Voice and demo-music candidate | SIP, ZebPay, accent, music, and SFX balance pass complete human playback | `review/final-short-v011-elevenlabs-music-demo-qc.md` | Human | v011 creative playback passed |
| Release | Music rights plus brand, legal, and regulatory approval are documented | Release records | Human / brand / legal | Pending |

## Current version authority

- **Promoted final:** v005 captioned master. Its delivery record documents human playback and Git
  LFS promotion; legal release remains pending.
- **Newest creative-approved review:** v011 clean and captioned cuts. Technical QC and owner
  playback passed. The demo music is not final-campaign approved, and commercial voice
  entitlement plus brand, legal, and regulatory release remain separate gates.
- **Promotion rule:** keep v005 unchanged until the owner explicitly selects a replacement whose
  final music, voice entitlement, brand, legal, and regulatory approvals are documented.

## Local storage state

- **Retained media:** the two creative-approved v011 review cuts and the promoted v005 captioned
  final used by the presentation.
- **Removed on 2026-07-25:** all pre-v011 encoded review media and work renders, rejected Qwen v008
  WAV/review media, the `.venv-qwen3-tts` environment, and the dedicated repository Hugging Face/UV
  caches.
- **Retained evidence:** tracked timelines, metadata, QC/rejection records, contact sheets, source
  code, original assets, approved generated selects, and Git history.
- **Reinstallation rule:** do not recreate or download Qwen3-TTS without explicit owner approval.

## Project-specific operating evidence

- Manual Higgsfield generation:
  `project/higgsfield-manual-generation-operating-spec.md`.
- Cost and iteration ledger: `project/production-learning-and-cost-plan.md`.
- Audio/frame-lock system: `edit/AV_SYNC_SYSTEM.md`.
- Current promoted delivery: `deliverables/final/DELIVERY-v005.md`.
- Current audio review: `review/final-short-v011-elevenlabs-music-demo-qc.md`.
