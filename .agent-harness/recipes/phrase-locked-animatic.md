# Recipe: phrase-locked keyframe animatic

## Checklist

| Requirement | Pass condition | Evidence | Owner | Status |
|---|---|---|---|---|
| Continuous narration | One audio file and word-boundary JSON come from the same synthesis request | Project `edit/audio/<version>/` | Editor | Required |
| Phrase map | Every visual beat names its matching first word and whole-frame start | Versioned timeline JSON | Editor | Required |
| Image continuity | Keyframes use canonical character/location references and survive delivery crop | Contact sheet and review | Image/Continuity | Required |
| Deterministic text | Logos, claims, captions, and CTA copy are added in post | Graphic source/render | Editor | Required |
| Frame lock | Video frame count equals timeline frame count and A/V drift is under one frame | Output EDL and FFprobe | Editor | Required |
| Semantic lock | Cut-to-word error is at most half a frame | Timing audit | Editor | Required |
| Boundary review | Pre/post frames at every transition contain no blank, flash, or wrong state | Boundary-pair sheet | Editor | Required |
| Human approval | Human accepts timing, visual quality, pacing, and brand direction | Review cut | Human | Required before paid motion |

## When to use

Use this recipe when one narration performance owns several distinct visual ideas. Do not use
percentage image weights as proof of semantic sync.

Canonical generic implementation:
`video-production-system/templates/project/edit/AV_SYNC_SYSTEM.md`.

Project implementations may add stricter constraints. The verified reference below is evidence, not
a requirement to copy its story, brand, duration, or shot count.

## Inputs

- Plain narration text.
- Canonical character, location, prop, and brand references.
- Phrase-level storyboard.
- Output fps, resolution, and maximum runtime.

## Output structure

```text
<project>/
  scripts/<narration-version>.txt
  keyframes/<version>/
  storyboard/<version>/shot-plan.md
  edit/audio/<version>/
  edit/timelines/<version>-phrase-map.json
  edit/animations/<version>/
  edit/verify/<version>/
  review/<version>-review.md
  deliverables/review-cuts/<version>.mp4
```

## Steps

1. Write the phrase-level shot plan before generating images.
2. Render narration once with word boundaries from the same request.
3. Generate a small look-lock set and review identity, geography, lighting, anatomy, and crop.
4. Generate the remaining approved keyframes; keep provider outputs immutable and copy project-bound
   selections into the versioned keyframe folder.
5. Add all copy and logos deterministically in post.
6. Snap each visual start to the nearest whole frame to the matching first-word boundary.
7. Render each visual segment to its exact integer frame count; concatenate video losslessly.
8. Pad the single continuous narration only at the end, then mux.
9. Verify frame count, decode, stream drift, semantic cut error, and final-word hold.
10. Inspect before/after frames at every cut. Fix and rerender any flash or wrong graphic state.
11. Write the comparison/review record and wait for human playback before paid motion.

## Verified reference run

- Project: `Ramayana-ZebpaySIP`
- Version: v004
- Date: 2026-07-23
- Runtime: 52.200 s
- Frames: 1,566 at 30 fps
- Stream drift: 1.667 ms
- Maximum semantic cut error: 13.5 ms
- Corrective learning: an internal fade in the SIP clip caused a dark boundary flash despite perfect
  A/V sync; boundary-pair inspection caught it and the fade was removed.
