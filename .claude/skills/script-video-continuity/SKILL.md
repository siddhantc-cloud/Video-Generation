---
name: script-video-continuity
description: Build and audit reusable characters, locations, props, brand assets, and keyframes. Use when preparing visual references or preventing identity and environment drift across shots.
---

# Script Video Continuity

Treat reusable visual elements as controlled assets. A good prompt cannot repair inconsistent references.

## Workflow

1. Read the approved brief, shooting script, shot tracker, and visual expectations.
2. Inventory required characters, locations, props, wardrobe states, and brand assets.
3. Create one canonical record per element under `assets/`.
4. Separate stable invariants from shot-specific state:
   - invariants: identity, anatomy, proportions, color, costume, material;
   - state: pose, expression, lighting, dirt, damage, camera, action.
5. Prefer clean neutral references with an unobstructed silhouette and consistent crop.
6. Remove accidental text, watermarks, logos, hands, extra limbs, and irrelevant background clutter.
7. Register provider-side elements only after local visual approval.
8. Record element name, category, local source, provider identifier, invariant description, and approval evidence.
9. Audit every shot packet against the canonical records.

## Reference policy

- Use a canonical reference for the first appearance.
- Use the previous approved ending frame for direct continuation.
- Use an explicit end keyframe only when composition or action landing matters.
- Do not stack weak references. Fewer clean references beat many conflicting ones.
- Brand marks and readable copy are deterministic overlays unless intentional physical integration is essential.

## Guardrails

Do not alter the frozen script, submit paid generations, approve continuity from thumbnails, or overwrite original assets.

Completion means every referenced element is identifiable, locally recoverable, provider-addressable when needed, and linked from the shot tracker.
