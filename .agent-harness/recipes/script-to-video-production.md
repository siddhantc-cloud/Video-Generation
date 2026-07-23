# Recipe: Script-to-video production

## Checklist

| Requirement | Pass condition | Evidence | Owner | Status |
|---|---|---|---|---|
| Frozen source | Original approved script is preserved unchanged | `scripts/source-script.md` | Human / producer | Required |
| Delivery contract | Runtime, aspect ratio, fps, platform, and experiment resolution are explicit | `project/project-settings.json` and brief | Producer | Required |
| Frame-locked plan | Every beat owns a whole-frame interval and production mode | `scripts/shot-tracker.md` | Director / editor | Required |
| Continuity controls | Reusable characters, locations, props, and brand sources are approved | `assets/` records and contact sheet | Continuity | Required |
| Free animatic | Story, timing, crop, and transitions pass before paid motion | Versioned review cut | Human | Required before generation |
| Spend boundary | Each provider job has a live quote and exact approved packet | Job ledger and approval evidence | Human | Required per job |
| Independent review | Every generated take has a timestamped verdict against prior expectations | `review/` report | Reviewer | Required |
| Deterministic graphics | Exact text, numbers, graphs, logos, and captions are rendered in post | Motion source and encoded render | Motion designer | Required |
| Master QC | Encoded master passes probe, frame, boundary, audio, and human playback checks | Delivery record | Editor / human | Required |
| Reusable learning | Evidence-backed cross-project lessons are promoted and host parity passes | Recipe/skill diff and checks | Partner agent | Required |

## Inputs

- An approved source script.
- Delivery platform and format.
- Brand assets and legal constraints.
- Available narration, image, video, motion-graphics, and editing tools.
- A human owner for creative and spend approvals.

## Output

A canonical project scaffold created from `video-production-system/templates/project`, with immutable raw media, versioned working files, timestamped reviews, and one explicitly promoted final.

## Workflow

1. **Bootstrap** with `$script-video-bootstrap`.
2. **Rewrite only if needed.** Preserve the source and obtain human approval for the shooting-script change log.
3. **Plan** with `$script-video-plan`; classify each beat as deterministic, turnkey, or generative.
4. **Prepare continuity** with `$script-video-continuity`.
5. **Build and approve the free animatic** with `$script-video-animatic`.
6. **Set measurable expectations** before seeing generated takes.
7. **Stage one approved provider job** and use `$script-video-generate`.
8. **Review each take independently** with `$script-video-review`.
9. **Create exact graphics** with `$script-video-motion-graphics`.
10. **Assemble and master** with `$script-video-post`.
11. **Promote learning** with `$script-video-learn`.

## Production laws

- One narration performance is the audio master unless the project records a different clock.
- One phrase owns one exact whole-frame visual interval.
- One generative shot should express one subject, one main action, and one camera idea.
- Generate stills and approve an animatic before paid motion.
- Native diegetic SFX may be generated with the shot; narration and music stay separate.
- Text, claims, data, graphs, logos, and captions are deterministic post-production.
- Current provider schema and quote override memory.
- A submitted job is monitored, not recreated.
- The actual encoded MP4 is evidence; browser previews are not.
- Inspect deterministic transitions at `n-1`, `n`, and `n+1`.

## Host rows

| Host | Skill surface | Agent surface | Parity rule |
|---|---|---|---|
| Codex | `.codex/skills/script-video-*` | Shared definitions under `video-production-system/agents/`; Codex may execute them directly | Canonical skills |
| Claude | `.claude/skills/script-video-*` | `.claude/agents/*.md` | Byte-equivalent mirrors |

File-based Claude agent discovery has no identical Codex project surface. The shared canonical definitions and checklist contracts are the intentional Codex mapping.

## Evidence destination

Project evidence stays in `<project>/review/`, `<project>/project/`, and provider job ledgers. Cross-project verified rules stay in this recipe and `video-production-system/`.
