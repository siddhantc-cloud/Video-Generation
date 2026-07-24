---
name: script-video-motion-graphics
description: Create premium deterministic graphs, logos, typography, and transitions. Use when building or reviewing HyperFrames, Remotion, or FFmpeg motion-graphics sections.
---

# Script Video Motion Graphics

Use deterministic rendering for anything that must be exact: copy, numbers, graphs, logos, captions, and brand geometry.

## Routing

- Read the `hyperframes` skill first for HyperFrames work.
- Use Remotion for programmatic React compositions and reusable branded systems.
- Use FFmpeg for final compositing, stream-safe muxing, and simple deterministic transforms.

## Workflow

1. Read `.agent-harness/recipes/hyperframes-motion-graphics.md` and the deterministic lane in
   `docs/video-production-workflow.md`.
2. Confirm exact frame interval, dimensions, frame rate, safe area, copy, data, logo source, and incoming/outgoing visual state.
3. Create `frame.md` before code: hierarchy, palette, typography, grid, depth, and motion beats.
4. Build all motion as a pure function of frame number. Avoid wall-clock state and nondeterministic randomness.
5. Preserve exact first-frame continuity when replacing a section.
6. Render the real encoded output, not only a browser or editor preview.
7. Inspect a contact sheet plus frames `start-1`, `start`, `start+1`, `end-1`, `end`, `end+1`.
8. Check the full section with narration and adjacent shots.
9. Add captions only after picture and narration are locked.

## Quality bar

Motion must have hierarchy, intentional easing, restrained depth, readable dwell time, and a clean landing frame. Never ask a generative model to render exact financial data, legal copy, captions, or logos.

Do not overwrite approved renders. Version every candidate and send it to `$script-video-review`.
