# Recipe: Idea to cinematic social video

## Checklist

| Requirement | Pass condition | Evidence | Owner | Status |
|---|---|---|---|---|
| Canonical procedure | The operator reads the complete workflow without relying on this routing file for production detail | `docs/video-production-workflow.md` | Operator | Required |
| Correct entrypoint | Work begins through `$script-video-production` and the narrow skill selected for the current stage | Skill work log | Operator | Required |
| Project evidence | Campaign-specific state stays in the project workspace and its `WORKFLOW.md` | Project records | Operator | Required |

## Authority and routing

- Human-readable production process, prompt packets, review gates, and dated cost example:
  `docs/video-production-workflow.md`.
- Project scaffold and tool-routing contract: `video-production-system/PRODUCTION_SYSTEM.md`.
- New-project orchestration: `$script-video-production`.
- Verified reusable learning: `$script-video-learn`.

Read the canonical workflow completely before execution. Do not copy its phases, prompts, or cost
tables into this recipe, skills, agent prompts, or project status files.

## Host rows

| Host | Entry surface | Shared authority |
|---|---|---|
| Codex | `.codex/skills/script-video-production/SKILL.md` | `docs/video-production-workflow.md` |
| Claude | `.claude/skills/script-video-production/SKILL.md` | `docs/video-production-workflow.md` |

Project evidence belongs under the active project. Cross-project evidence may update the canonical
workflow only after `$script-video-learn` verifies it.
