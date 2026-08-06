---
description: Set up or repair this machine so it can produce the repository films
argument-hint: [optional focus such as credentials, mcp, skills, lfs, or ramayana/cryptopack]
---

Use the project-local `script-video-setup` skill. Follow `docs/SOP-00-SETUP.md`.

Requirements:

1. Confirm the working directory is a clone of this repository. If it is not, stop and give the clone
   and `git lfs pull` commands. Cloning is a human action.
2. Run `powershell -ExecutionPolicy Bypass -File tools/setup-video-repo.ps1` and show the real
   output.
3. Split the result into machine fixes, human actions, and optional items.
4. Ask before running `-Install`. Then re-run the read-only check and show the new summary.
5. Never run a provider login, never print a credential value, never buy credits, and never submit a
   paid job.
6. Never install Qwen3-TTS. It needs explicit owner approval.
7. End with: what changed, the current pass and fail counts, the numbered human actions that remain,
   and the next document to read, which is `docs/SOP-01-RAMAYANA-ZEBPAY-SIP.md` or
   `docs/SOP-02-CRYPTOPACK-REBALANCING.md`.

If the user gave a focus argument, still run the full check, then explain that area in detail.
