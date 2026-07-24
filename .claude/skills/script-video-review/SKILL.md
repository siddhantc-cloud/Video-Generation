---
name: script-video-review
description: Review encoded video and audio takes against measurable expectations. Use for technical QC, continuity, motion, timing, sound, graphics, and keeper decisions.
---

# Script Video Review

Review the actual encoded artifact, not a thumbnail, browser preview, or generation narrative.

## Inputs

Read the shot tracker, expectation rows, continuity records, prompt packet, provider metadata, and file hashes. Probe the candidate with FFprobe before creative review.

## Review passes

1. **Technical:** decodability, duration, frame rate, dimensions, codec, missing or corrupt streams.
2. **Visual:** identity, anatomy, object integrity, temporal stability, composition, lighting, camera, unintended text.
3. **Temporal:** action completes, entrance and exit states are usable, no dead tail, no abrupt event before narration meaning.
4. **Continuity:** compare first and last frames with adjacent approved shots and canonical elements.
5. **Audio:** native SFX relevance, clipping, silence, artifacts, speech leakage, music leakage.
6. **Graphics:** exact copy, logo integrity, safe margins, legibility, data truthfulness.
7. **Full playback:** watch the encoded file with sound at delivery scale.

For any failed take, record the longest usable frame range and whether deterministic salvage can
cover the approved phrase interval. Explicitly test for unintended internal cuts in prompts that
asked for a continuous shot.

For deterministic boundaries inspect frames `n-1`, `n`, and `n+1`.

## Verdict

Return exactly one:

- `PASS`: meets all must criteria and can be promoted.
- `FAIL`: misses a must criterion; specify the smallest useful retry change.
- `NEEDS HUMAN`: evidence cannot settle a subjective, legal, or brand decision.

Write timestamped findings with severity and evidence paths under `review/`. Do not edit, regenerate, or silently waive criteria.
