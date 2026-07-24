# Script-to-video production system

The canonical from-idea execution recipe is
`.agent-harness/recipes/idea-to-cinematic-social-video.md`. This file defines the compact system
contract and project structure.

## Checklist

| Requirement | Pass condition | Evidence | Owner | Status |
|---|---|---|---|---|
| Frozen input | The human script is saved verbatim before adaptation | `scripts/source-script*` | Director | Required |
| Shot classification | Every shot is assigned deterministic, turnkey, or generative mode | Shooting script | Director | Required |
| Still-first gate | Generative shots have approved keyframes before video spend | Keyframe review | Human / director | Required |
| Whole-film gate | A phrase-locked storyboard and timed animatic are approved | Animatic review | Human | Required |
| Spend gate | Every paid job has an exact packet, live quote, cap, and immediate approval | Shot record | Human / producer | Required |
| Evidence review | Every take has a timestamped keeper/reject verdict | Review record | Reviewer | Required |
| Frame-locked post | Picture, narration, SFX, graphics, and captions follow an integer-frame manifest | Timeline manifest | Editor | Required |
| Delivery QC | Decode, boundaries, audio, captions, legal copy, hashes, and human playback pass | QC report | QC / human | Required |
| Learning | Reusable evidence updates the generic recipe or skill; incident detail stays project-local | Learning record | Director | Required |

## Core production law

1. Freeze the original script.
2. Rewrite only with a change log and human approval.
3. Classify every shot:

   - **Deterministic:** text, graphs, UI, captions, logos, still moves, and editing.
   - **Turnkey:** a provider's reliable template or avatar happy path.
   - **Generative:** novel cinematic motion that cannot be rendered deterministically.

4. Spend in this order: planning → stills → animatic → one pilot → approved batch → post.
5. Use one subject and one primary action per generative shot.
6. Use a three-attempt cap, then redesign or fall back.
7. Treat the approved narration as the master clock and quantize every boundary to whole frames.
8. Make each spoken phrase own the visual shown during that phrase.
9. Add deterministic text, charts, captions, logos, and legal copy in post.
10. Re-perceive the encoded output. Logs and browser previews are not final evidence.

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

## Gate sequence

| Gate | Decision |
|---|---|
| Script | Is the frozen input preserved and the adaptation approved? |
| Design | Are character, location, prop, brand, and visual-law anchors approved? |
| Animatic | Does the complete film read, pace, and synchronize correctly before paid motion? |
| Spend | Is the exact model, mode, duration, reference, and cost packet approved? |
| Pilot | Does one representative generation prove the chosen surface? |
| Keeper | Does each take pass technical, continuity, temporal, and audio review? |
| Picture lock | Are only approved ranges present on an integer-frame timeline? |
| Delivery | Do encoded media, captions, sound, claims, boundaries, and hashes pass? |

## Tool routing

- Higgsfield: cinematic generative shots and Cinema Studio Elements.
- ChatGPT ImageGen or another approved still engine: look-lock, references, and keyframes.
- HyperFrames or Remotion: deterministic motion graphics.
- FFmpeg/FFprobe through video-use: conform, assembly, captions, audio, QC, and delivery.
- Resolve Free: optional supervised finishing after picture lock, never a required dependency.

Provider features, pricing, limits, and model quality are time-sensitive. Inspect current schemas and
live quotes before use; never turn one project's dated result into a universal default.

Price generative work from billed source seconds and expected attempts, not final runtime.
Deterministic graph, copy, caption, logo, hold, and reusable-select intervals do not belong in the
provider-seconds total.
