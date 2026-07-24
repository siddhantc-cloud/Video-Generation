---
name: script-video-plan
description: Convert an approved script into a cost-aware shot plan and approval packet. Use for beat maps, shot lists, iteration budgets, generation routing, and production sequencing.
---

# Script Video Plan

Plan from message and timing first. More shots are not automatically better; every cut must earn its place.

Read `docs/video-production-workflow.md` for the canonical idea-to-film sequence and reusable
prompt packets.

## Required inputs

Read:

- `project/brief.md`
- `scripts/source-script.md`
- `scripts/shooting-script.md`
- `review/criteria/expectations.md`
- `project/production-decisions.md`
- `project/cost-plan.md`

## Workflow

1. Freeze the delivery constraint: platform, runtime, aspect ratio, frame rate, and experiment resolution.
2. Build a narration phrase map. Each phrase owns an exact whole-frame interval.
3. Reduce redundant copy before shortening shot duration.
4. Classify every beat:
   - **Deterministic**: text, logo, graph, captions, compositing.
   - **Turnkey**: a model or app with predictable bounded output.
   - **Generative**: cinematic or organic motion where variation is acceptable.
5. Choose the longest coherent shot that preserves one clear subject, action, and camera idea.
6. Define reference roles explicitly: canonical identity, `start_image`, optional `end_image`, and
   previous accepted video only for true continuation or motion reference. Define native diegetic
   SFX intent and narration relationship.
7. Build a free still/keyframe animatic before paid motion.
8. Estimate quote ranges and iteration tiers: experiment, keeper, final.
9. Write the plan to `scripts/shot-tracker.md` and the budget to `project/cost-plan.md`.

## Cost policy

- Experiment on the lowest supported resolution without changing the approved model.
- Price from the provider's live quote immediately before submission.
- Price generated source seconds, not final runtime. Keep exact graphics and holds out of the
  provider-seconds total.
- Budget by attempts, not just duration. Show one-pass cost and a 1.5–2-pass practical reserve;
  retain a hard three-attempt cap per generative shot unless the project records a stricter cap.
- Promote only reviewed keepers. Do not upscale failed composition.
- Treat a higher-resolution rerun as a fresh take unless the live provider exposes a verified
  seed/re-render mechanism.

## Approval packet

For each paid shot include shot ID, duration, model, resolution, references, exact prompt, sound instruction, live quote, attempt number, and expected pass conditions.

Do not submit a paid generation. Hand approved packets to `$script-video-generate`.
