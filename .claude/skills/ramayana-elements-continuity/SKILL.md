---
name: ramayana-elements-continuity
description: Prepare, clean, register, audit, and reuse Characters, Locations, Props, and identity references for the Ramayana-ZebpaySIP film. Use when creating Higgsfield Elements, preventing character or location drift, choosing reference roles, or checking continuity before generation.
---

# Ramayana Elements and continuity

Read `Ramayana-ZebpaySIP/project/global-visual-law.md`, the relevant assets, and Steps 7-16 of `project/higgsfield-cinema-studio-navigation-runbook.md`.

## Decide the Element type

- **Character:** stable identity, body, fur/skin, costume, and signature carried object.
- **Location:** character-free geography, construction state, light direction, and environment.
- **Prop:** create only when an object needs an exact recurring design. Do not create Props for one-off pebbles, generated text, or deterministic brand graphics.

## Prepare the reference

1. Preserve the source file.
2. Remove baked-in people or characters from Location plates into a new file.
3. Keep Character descriptions compact and invariant-only. Exclude action, camera, emotion, and temporary pose.
4. Verify the intended media preview and category before Create.

## Register through Cinema Studio

1. Open Elements in the Ramayana project and choose New Element.
2. Enter the stable name and compact description.
3. Click the visible category and confirm the closed field.
4. Attach exactly one approved reference after clearing persistent picker selections.
5. Click Create once and wait for `Element created.` plus the exact handle/category.

The verified library contains four Characters and four Locations. CLI uploads are not Cinema Studio Elements. Record new inventory in the runbook and use `$ramayana-learn` when a new reusable continuity rule is discovered.

## Choose references by shot relationship

- **Fresh shot:** exact start keyframe + canonical character/body reference + correct location/bridge state. Add an end keyframe only when a precise reachable endpoint matters.
- **Direct continuation:** accepted previous clip as video context + its inspected final frame as the next start where possible + canonical character and location references. Describe only the next action. Cap chains at two continuations, hard ceiling three, then re-anchor from originals.
- **Camera/motion borrowing:** previous or purpose-shot video supplies motion/camera only. State that role explicitly; current canonical images still own identity, wardrobe, location, light, and style.
- **New scene or normal edit:** do not attach the previous clip by default. Re-anchor from canonical assets and create continuity through matching action, eyeline, screen direction, light, and grade.

Do not attach start frame, end frame, and previous video automatically. Conflicting anchors over-constrain the generation. An end frame must be close enough in framing, scale, placement, and contact state to interpolate without a layout teleport.
