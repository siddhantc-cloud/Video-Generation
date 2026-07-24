---
name: script-video-production
description: Orchestrate a cinematic social-video project from an initial idea through script, keyframes, animatic, costed generative motion, deterministic graphics, audio, review, and delivery. Use when starting an ad, short, reel, mythology film, branded story, or other complete video workflow and the user wants the whole repeatable process rather than one isolated production task.
---

# Script Video Production

Use this as the high-level entry point. It routes work to atomic production skills and agents; it
does not let one context create, spend, edit, and certify its own output.

## Checklist

| Requirement | Pass condition | Evidence | Owner | Status |
|---|---|---|---|---|
| Canonical recipe | The idea-to-film recipe is read before planning | Recipe path in work log | Producer | Required |
| Atomic routing | Each stage uses the narrowest skill and agent | Stage checklist | Producer | Required |
| Human gates | Script, animatic, spend, and final promotion have explicit owners | Approval records | Human / producer | Required |
| Current provider truth | Schema and credits are rechecked before each paid job | Live preflight | Prompt reviewer | Required |
| Independent review | Creators do not certify their own output | Review record | Reviewer | Required |

## Workflow

1. Read `../../../.agent-harness/recipes/idea-to-cinematic-social-video.md` completely.
2. Start the clean project with `$script-video-bootstrap`.
3. Freeze the idea contract, then route narration and shooting-script work through the
   `script-rewriter` agent.
4. Use `$script-video-plan`; route shot feasibility through `assistant-director`.
5. Use `$script-video-continuity` for characters, locations, props, visual laws, and provider
   Elements.
6. Use `$script-video-animatic` to prove the complete film before paid motion.
7. Have `scene-expectations` write the per-shot rubric before takes exist.
8. Have `prompt-reviewer` audit each immutable packet, live schema, quote, and approval.
9. Use `$script-video-generate` for one approved job at a time.
10. Use `$script-video-review` and the independent `video-reviewer` for keeper decisions.
11. Use `$script-video-motion-graphics` for exact graphs, text, numbers, captions, and logos.
12. Use `$script-video-post` and `video-editor` for frame-locked assembly and audio.
13. Promote reusable evidence with `$script-video-learn`.

## State and cost rules

- Keep the checklist and evidence paths in the project, not in chat.
- Price the generated source seconds, not the final runtime.
- Estimate attempts as a multiplier on the one-pass source plan.
- Use 480p only as an experiment tier when the approved model supports it. A later 1080p run is a
  fresh take unless the provider exposes a verified seed/re-render mechanism.
- Preserve rejected takes and provider IDs; monitor an existing job rather than recreating it.
- Keep narration and music separate from native diegetic SFX.
- Salvage usable source ranges before buying another roll.
- Render all exact content deterministically.

## Completion

Finish with the current objective, changed artifacts, verification evidence, spend versus cap,
unresolved human/legal/brand gates, and the exact next atomic stage. Never call a review cut final
without explicit promotion.
