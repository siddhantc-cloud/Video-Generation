# Script-to-video production system

## Checklist

| Requirement | Pass condition | Evidence | Owner | Status |
|---|---|---|---|---|
| Canonical process | Operators use one complete production procedure | `docs/video-production-workflow.md` | Operator | Required |
| Canonical structure | New projects use the folder contract below | Scaffold output | Producer | Required |
| Current routing | Provider and media tools are selected from current capabilities | Tool preflight | Operator | Required |

This file owns only the reusable project structure and tool-routing contract. The complete
idea-to-delivery process, prompts, gates, and cost method live in
`docs/video-production-workflow.md`.

## Canonical project structure

```text
<project>/
  assets/
    brand/
    characters/
    locations/
    props/
    references/
  audio/
    narration/
    music/
    sfx/
  deliverables/
    review-cuts/
    final/
  edit/
    animations/
    captions/
    timelines/
    verify/
  footage/
    raw/
    selects/
  keyframes/
    look-lock/
    shots/
  project/
    brief.md
    cost-plan.md
    production-decisions.md
    project-settings.json
  review/
    criteria/
    takes/
  scripts/
    source-script.md
    shooting-script.md
    shot-tracker.md
  storyboard/
  tools/
  WORKFLOW.md
```

Create it with:

```powershell
powershell -ExecutionPolicy Bypass -File tools/New-VideoProject.ps1 `
  -ProjectName <project-folder> -ScriptPath <script-file>
```

## Tool routing

- Higgsfield: cinematic generative shots and Cinema Studio Elements.
- ChatGPT ImageGen or another approved still engine: look-lock, references, and keyframes.
- HyperFrames or Remotion: exact deterministic motion graphics.
- FFmpeg/FFprobe through video-use: conform, assembly, captions, audio, QC, and delivery.
- Resolve Free: optional supervised finishing after picture lock, never a required dependency.

Provider capabilities, schemas, prices, and limits are time-sensitive. Inspect them immediately
before use. The canonical workflow explains how to classify shots, control spend, review encoded
evidence, and promote learning.
