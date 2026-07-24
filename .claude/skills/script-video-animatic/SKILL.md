---
name: script-video-animatic
description: Build a frame-locked storyboard and audio-master animatic before paid motion. Use for keyframe timing, narration sync, shot-boundary approval, and low-cost concept validation.
---

# Script Video Animatic

The animatic is the first complete film. It proves story, timing, composition, and continuity before generative motion costs money.

## Workflow

1. Read `.agent-harness/recipes/phrase-locked-animatic.md`.
2. Produce or select one approved narration performance.
3. Probe the exact audio duration; make it the master clock.
4. Map narration phrases to integer-frame boundaries.
5. Generate or select storyboard keyframes that match the actual script beats.
6. Assign one visual owner per phrase and list any deliberate overlap.
7. Build a timed still sequence with simple deterministic motion only.
8. Add temporary labels only when they help review; do not fake final graphics.
9. Render an encoded MP4.
10. Inspect every transition at frames `n-1`, `n`, and `n+1`, then review the full video with sound.
11. Record human approval before any paid motion generation.
12. Record which intervals will remain deterministic, which require generative source seconds, and
    which can use a hold or reused partial take.

## Acceptance

- Audio and picture have identical intended runtime.
- No sentence changes image before its meaning lands.
- No shot is present only because a keyframe already exists.
- Every shot transition occurs on a whole frame.
- The final frame resolves the call to action or story ending.
- The billed-source estimate excludes deterministic graph, copy, caption, and logo intervals.
- Approval evidence is recorded in `review/`.

## Guardrails

Do not create provider jobs, replace narration midway without remapping all boundaries, or judge timing from an editor preview alone.

When approved, update `scripts/shot-tracker.md` and hand generative rows to `$script-video-generate`.
