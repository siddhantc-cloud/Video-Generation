# Ramayana–ZebPay SIP

Production workspace for one film: **“The Squirrel in Ram Setu.”** It is a vertical ZebPay SIP ad
that uses the Ramayana squirrel story to show how small, repeated contributions create something large.

## Current checklist

| Requirement | Pass condition | Evidence | Owner | Status |
|---|---|---|---|---|
| Story and message | Human script is frozen | `scripts/original-script.md` | Human/Creative | Complete |
| Shooting plan | Every beat is decomposed into filmable shots | `scripts/shooting-script.md` | Director | Complete |
| Visual assets | Character, environment, brand, and reference assets are organized | `assets/` | Art | Complete |
| Storyboard | Film can be reviewed in sequence | `storyboard/index.html` | Director/Human | Built; approval not recorded |
| Keyframes | Planned shot frames are available | `keyframes/` | Art | Complete |
| Animatic | Timed review cut with scratch narration exists | `deliverables/review-cuts/animatic/` | Editor/Human | Built; approval not recorded |
| Production footage | Approved moving footage exists for every shot | `footage/` | Production | In progress: two pilot shots only |
| Final audio | Approved VO, music, and SFX stems exist | `audio/` | Sound/Human | Pending |
| Final edit | Picture, sound, graphics, captions, and grade are locked | `edit/` | Editor | Pending |
| Delivery | Final masters and platform versions pass QC | `deliverables/final/` | Editor/Human | Pending |

## Work in this order

1. Read `project/brief.md`.
2. Review the original and shooting scripts in `scripts/`.
3. Check the visual bible in `assets/`.
4. Review `storyboard/index.html`, then the timed animatic.
5. Approve or revise keyframes before producing more footage.
6. Put new raw shots in `footage/generated/`; move approved versions to `footage/selects/`.
7. Build picture, sound, titles, captions, and color in `edit/`.
8. Record review evidence in `review/`.
9. Export review cuts, then approved masters to `deliverables/`.

The full manual production method and current stage gates are in `WORKFLOW.md`.
The current Higgsfield shot-generation method, including native SFX with separate narration, is in
`project/higgsfield-manual-generation-operating-spec.md`.
The iteration budget, actual spend ledger, scale forecast, and cheaper-repeat strategy are in
`project/production-learning-and-cost-plan.md`.

## Folder map

| Folder | Manual-film equivalent | What belongs here |
|---|---|---|
| `project/` | Creative brief and production book | Objective, audience, constraints, decisions, status |
| `scripts/` | Script department | Original script, shooting script, shot tracker |
| `assets/` | Art department | Character bible, locations/environments, props, brand, reference stills |
| `storyboard/` | Storyboard department | Film-order visual board |
| `keyframes/` | Approved shot designs | Start/end frames used to create or judge footage |
| `audio/` | Sound department | Voiceover, music, SFX, and mixes |
| `footage/` | Camera/production dailies | Raw generated shots and approved selects |
| `edit/` | Post-production | Timelines, EDLs, graphics, working renders, sync method |
| `review/` | Director/producer/QC | Acceptance criteria, audits, QC frames, review notes |
| `deliverables/` | Distribution | Review cuts and final masters |
| `tools/` | Technical support | Reproducible local assembly utility |

## Key files to open

- Creative brief: `project/brief.md`
- Higgsfield manual generation spec: `project/higgsfield-manual-generation-operating-spec.md`
- Cinema Studio navigation runbook: `project/higgsfield-cinema-studio-navigation-runbook.md`
- Production learning and cost plan: `project/production-learning-and-cost-plan.md`
- Shooting script: `scripts/shooting-script.md`
- Shot status: `scripts/shot-tracker.md`
- Storyboard: `storyboard/index.html`
- Animatic: `deliverables/review-cuts/animatic/ZebPay_Squirrel_ANIMATIC.mp4`
- Pilot reel: `deliverables/review-cuts/pilots/PILOTS_REEL.mp4`
- Review criteria: `review/criteria/expectations.md`

Project-local production skills are mirrored under `.codex/skills/ramayana-*` and `.claude/skills/ramayana-*`. Claude can run `/learn`; Codex can invoke `$ramayana-learn`. The command updates only verified production knowledge and never spends credits.

## House rules

- One shot ID must have one clear source keyframe, one current select, and one review verdict.
- Raw footage is never overwritten; revisions get a new version.
- Only approved footage moves into `footage/selects/`.
- Text, captions, the `राम` inscription, stripe reveal, and ZebPay branding are finished in post.
- The narrator is one continuous external voice, not a different voice per shot.
- Final financial and brand claims require human/legal approval before delivery.
- Temporary caches do not belong in this workspace; they can be regenerated from the timelines.

## Snapshot

Reorganized on 2026-07-21 from the existing film artifacts. The original repository folders remain
untouched and serve as recovery copies.
