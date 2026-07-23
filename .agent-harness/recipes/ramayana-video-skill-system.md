# Ramayana video skill system recipe

## Checklist

| Requirement | Pass condition | Evidence | Owner | Status |
|---|---|---|---|---|
| Cost control | Every paid iteration has a live quote, cap, approval, actual charge, and verdict | `Ramayana-ZebpaySIP/project/production-learning-and-cost-plan.md` | Human/Producer | Complete |
| Stage separation | Planning, continuity, generation, review, and post each have a focused skill | `.codex/skills/ramayana-*` | Operator | Complete: seven skills |
| Navigation memory | Each newly inspected Cinema Studio page updates the detailed runbook and concise navigation skill | Runbook plus `ramayana-cinema-navigation` | Operator | Complete |
| Learning command | `/learn` promotes only verified, durable findings from source evidence | `.claude/commands/learn.md` and `ramayana-learn` | Human/Operator | Complete |
| Cross-host parity | Codex skill sources and Claude mirrors are byte-equivalent | `tools/sync-ramayana-video-skills.ps1 -Check` | Operator | Complete; validator passed on both hosts |
| No false certainty | Estimates are labelled; live prices and generated quality are never guaranteed | Cost plan and skill rules | Producer/Operator | Complete |

## Purpose

Create a project-local operating layer that lets Codex, Claude, or a human repeat the Ramayana-ZebPay video workflow without reconstructing it from chat. The project documents remain the source of truth. Skills contain only triggers, decision rules, and repeatable procedures.

## Skill set

| Skill | Responsibility |
|---|---|
| `ramayana-cinema-navigation` | Navigate and map Higgsfield Cinema Studio; update the runbook after each new page or state |
| `ramayana-video-plan` | Build shot packets, iteration budgets, approval caps, and cost forecasts |
| `ramayana-elements-continuity` | Prepare and register Characters, Locations, Props, and continuity references |
| `ramayana-shot-generate` | Stage, price, approve, submit once, monitor, and download a Higgsfield shot |
| `ramayana-video-review` | Run technical, visual, temporal, continuity, and audio QC; decide keeper/reject |
| `ramayana-video-post` | Assemble selects, narration, native SFX, music, graphics, captions, and masters |
| `ramayana-learn` | Extract verified lessons and update the runbook, cost plan, recipes, and skill rules |

## Host layout

- Canonical editable skills: `.codex/skills/<skill>/`.
- Claude mirrors: `.claude/skills/<skill>/`.
- Claude slash wrapper: `.claude/commands/learn.md`.
- Codex invocation: `$ramayana-learn` or plain-language use of that skill.
- Mechanical parity helper: `tools/sync-ramayana-video-skills.ps1`.

The Claude command and Codex skill are equivalent entry points; Codex does not receive a fabricated `/learn` command surface.

## Learning sources, in precedence order

1. Current generated media, FFprobe/FFmpeg evidence, screenshots, job/account records, and human verdicts.
2. Per-shot generation and review records.
3. `project/higgsfield-cinema-studio-navigation-runbook.md`.
4. `project/production-learning-and-cost-plan.md` and `project/production-decisions.md`.
5. Project recipes and skills.
6. Chat recollection only when it is also anchored to one of the sources above.

## Update rule

For every newly inspected Cinema Studio page or state:

1. Record starting state, exact action, confirmed result, stop condition, cost/destructive boundary, and evidence in the navigation runbook.
2. Update `ramayana-cinema-navigation` only when the observation changes a reusable navigation law.
3. Run `/learn` after a meaningful batch or a generation/review verdict, not after every click.
4. Sync host copies and run structural validation.

Do not paste screenshots, full prompts, job payloads, or long histories into a skill. Link the authoritative project record instead.

## Validation

1. Run the skill-creator `quick_validate.py` against every canonical and mirrored skill.
2. Run `powershell -ExecutionPolicy Bypass -File tools/sync-ramayana-video-skills.ps1 -Check`.
3. Confirm every path referenced by the skills exists.
4. Confirm `/learn` does not spend credits, generate media, delete assets, or promote a select.
