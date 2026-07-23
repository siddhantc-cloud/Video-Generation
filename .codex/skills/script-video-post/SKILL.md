---
name: script-video-post
description: Assemble approved selects into a frame-locked master with narration, SFX, music, graphics, and captions. Use for editorial, review cuts, mastering, and delivery QC.
---

# Script Video Post

Editorial starts from approved ranges and an integer-frame manifest. Narration owns the clock unless the project explicitly chooses another master.

## Workflow

1. Read the approved shot tracker, phrase map, review verdicts, and `edit/AV_SYNC_SYSTEM.md`.
2. Create a render manifest with source hashes, exact in/out frames, timeline start/end frames, layer order, audio routing, and transforms.
3. Assemble only approved selects. Preserve raw generations unchanged.
4. Lock picture against the approved narration performance.
5. Mix native SFX, designed SFX, ambience, and music on separate stems; keep speech intelligible and prevent clipping.
6. Replace exact text, data, graph, and logo sections with deterministic renders.
7. Add captions last from the locked narration timing.
8. Render a versioned review cut.
9. Probe duration, dimensions, frame count, frame rate, streams, loudness, and peak level.
10. Inspect boundary frames and watch the entire encoded file with sound.
11. If audio was intended to pass unchanged, verify elementary audio-stream MD5 before and after muxing.
12. Promote only the human-approved cut into `deliverables/final/`.

## Delivery

Record filename, version, SHA-256, runtime, frame count, dimensions, audio properties, source review cut, approval evidence, and unresolved legal/brand status.

Git delivery policy belongs to the repo: keep raw and review media ignored; use Git LFS only for an explicitly promoted final when the owner requests version control.
