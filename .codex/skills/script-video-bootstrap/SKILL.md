---
name: script-video-bootstrap
description: Create a clean, repeatable production workspace from an idea or approved script. Use when starting a new short, reel, ad, explainer, or cinematic video project before planning shots or generating media.
---

# Script Video Bootstrap

Create the project before creating media. The workspace is the source of truth, not chat history.

## Workflow

1. Read `video-production-system/PRODUCTION_SYSTEM.md` and
   `docs/video-production-workflow.md`.
2. Confirm the project name, idea or approved source script, aspect ratio, frame rate, experiment
   resolution, primary platform, target runtime, and human approval owner.
3. Run `tools/New-VideoProject.ps1`. Never overwrite an existing project.
4. If a script is already approved, copy it unchanged into `scripts/source-script.md` and mark it
   frozen. If the input is only an idea, preserve it verbatim in `project/brief.md`; create and
   approve the narration before freezing `scripts/source-script.md`.
5. Populate `project/brief.md`, `project/production-decisions.md`, and `project/cost-plan.md`.
6. Record each initial requirement as a checklist row with requirement, pass condition, evidence, owner, and status.
7. Verify all canonical directories and `project-settings.json` exist.

## Command

```powershell
powershell -ExecutionPolicy Bypass -File tools/New-VideoProject.ps1 `
  -ProjectName "Project-Name" `
  -ScriptPath "D:\path\approved-script.md" `
  -AspectRatio "9:16" `
  -Fps 30 `
  -Resolution "480x854"
```

Omit `ScriptPath` only when the script will be entered immediately afterward.

## Rules

- Preserve the frozen source. Proposed rewrites go in `scripts/shooting-script.md` with a change log.
- Use safe names containing letters, numbers, periods, underscores, or hyphens.
- Keep unrelated campaigns, caches, provider downloads, and old experiments outside the active project.
- Do not generate media, spend provider credits, or imply creative approval.
- Stop if the target exists or resolves outside the workspace.

## Completion

Report the project path, preserved idea/script source, settings, unresolved brief fields, and next
skill: `$script-video-production` for the whole workflow or `$script-video-plan` for planning only.
