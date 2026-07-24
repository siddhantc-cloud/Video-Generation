# Recipe: Script-to-video production compatibility route

## Checklist

| Requirement | Pass condition | Evidence | Owner | Status |
|---|---|---|---|---|
| Canonical route | The complete process is read from the single canonical document | `docs/video-production-workflow.md` | Operator | Required |
| Supported entrypoint | Execution uses `$script-video-production` | Skill work log | Operator | Required |

This filename is retained for older prompts and links. It contains no independent workflow.

- Canonical human-readable process: `docs/video-production-workflow.md`.
- Machine-routing recipe: `.agent-harness/recipes/idea-to-cinematic-social-video.md`.
- Project structure and tool routing: `video-production-system/PRODUCTION_SYSTEM.md`.

Do not add gates, prompts, costs, or production laws here; update the canonical document through
`$script-video-learn`.
