---
name: script-video-setup
description: Set up or repair this machine so it can produce the repository films. Use for /setup, a new operator, a new computer, a failed environment check, missing skills or MCP servers, or before the first paid job.
---

# Script Video Setup

Bring a machine from an empty state to a verified video-production workspace. Report evidence. Never
run a login. Never spend money.

## Workflow

1. Read `README.md`, then `docs/SOP-00-SETUP.md`. The README is the operator front door and the
   SOP is the detail. Do not repeat their content into chat. Refer to them.
2. Confirm the operator is inside a clone of this repository. If not, stop and give the clone
   commands from SOP step 1. Cloning is a human action.
3. Run the checker:

   ```powershell
   powershell -ExecutionPolicy Bypass -File tools/setup-video-repo.ps1
   ```

4. Read every row. Group the results into three lists:
   - machine fixes an agent may run;
   - human actions;
   - optional items.
5. Ask the operator to approve the automated repairs, then run:

   ```powershell
   powershell -ExecutionPolicy Bypass -File tools/setup-video-repo.ps1 -Install
   ```

6. Re-run the read-only check and show the new result.
7. Print the remaining human actions as a numbered list. State plainly that you cannot do them.
8. Point at the next document: `docs/SOP-01-STORY-FILM.md` or
   `docs/SOP-02-PRODUCT-EXPLAINER.md`.

## What an agent must never do here

- Do not run `higgsfield auth login` or any other interactive provider login.
- Do not create, read back, print, or copy a credential value.
- Do not write a key into `.mcp.json`, a skill, a recipe, a commit, or a chat message.
- Do not buy credits, upgrade a plan, or submit a paid job.
- Do not install Qwen3-TTS. The owner removed it on 2026-07-25. It needs explicit owner approval.
- Do not edit a mirrored skill or agent file as if it were canonical.

## Interpreting failures

| Row | Meaning | Action |
|---|---|---|
| `git-lfs-media` FAIL | Videos are still pointer text | Run `git lfs install` then `git lfs pull` |
| `dotenv-ignored` FAIL | `.env` could be committed | Stop. Restore the ignore rule before any key exists. |
| `mcp-no-secrets` FAIL | A key-shaped value is in `.mcp.json` | Stop. Tell the human to rotate that credential now. |
| `mcp:ElevenLabs` FAIL | The command path belongs to another machine | Set it to this machine's `uvx` path |
| `credential:*` HUMAN | A key or login is missing | Hand the exact SOP step to the human |
| `parity:*` FAIL | A mirror drifted from canonical | Run the matching sync script without `-Check` |
| `host-skill:*` HUMAN | Provider skills are missing | Give the install list from SOP step 5, then ask for a host restart |

## Rules

- Verification first. Report the actual command output, not an expectation.
- Report a partial pass as a partial pass. Never call a machine ready while a required row fails.
- Keep credential handling to presence checks only.
- End with: what changed, the current check summary, the human actions left, and the next document.
