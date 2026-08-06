# Project continuity (shared across Claude Code, Codex, Cursor)

Native chat history is **not** interchangeable across hosts. This folder is the
automated bridge: any host reads it at start and appends before ending meaningful work.

## Files

| Path | Purpose |
|------|---------|
| `CONTINUITY.md` | Rolling human-readable state (source of truth for "where we are") |
| `transcript.jsonl` | Append-only machine log of turns/handoffs |
| `handoffs/` | Structured handoff packets when switching hosts mid-task |
| `STATUS.json` | Latest compact status for scripts/hooks |

## Automations (installed with mythyaverse-agent-setup)

1. User-level `CLAUDE.md` / `AGENTS.md` require read-on-start + append-on-finish.
2. Cursor skill `agent-conversation` + `/continue-conversation`.
3. CLI: `scripts/agent-convo.ps1` / `scripts/agent-convo.sh`.

## Init in a project

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File <setup-repo>/scripts/agent-convo.ps1 init -ProjectRoot .
```

```bash
bash <setup-repo>/scripts/agent-convo.sh init --project-root .
```
