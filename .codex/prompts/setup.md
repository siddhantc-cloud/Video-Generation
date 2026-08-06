Set up or repair this machine so it can produce the repository films.

Read `docs/SOP-00-SETUP.md` first. It is the human source of truth. The canonical agent instructions
are in `.codex/skills/script-video-setup/SKILL.md`. Follow that skill, or invoke it directly as
`$script-video-setup`.

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
   and the next document to read, which is `docs/SOP-01-STORY-FILM.md` or
   `docs/SOP-02-PRODUCT-EXPLAINER.md`.

To make this available as `/setup` in Codex, copy this file once:

    New-Item -ItemType Directory -Force -Path "$env:USERPROFILE\.codex\prompts" | Out-Null
    Copy-Item .codex\prompts\setup.md "$env:USERPROFILE\.codex\prompts\setup.md" -Force
