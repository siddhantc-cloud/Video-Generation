---
name: ramayana-video-review
description: Review Ramayana-ZebpaySIP generated video and audio for technical validity, identity, anatomy, objects, continuity, motion, cuts, performance, and native sound. Use after every generation and before any file is promoted to footage/selects.
---

# Ramayana video review

Read the shot packet and `Ramayana-ZebpaySIP/review/criteria/expectations.md`. Review the full clip in motion; still frames alone cannot close temporal criteria.

## Review checklist

1. Use FFprobe to record codec, dimensions, frame rate, duration, and audio streams.
2. Verify file hashes and preserve the raw take.
3. Inspect start, middle, end, and any suspicious transition/contact region.
4. Check identity, face/filter integrity, anatomy, costume, props, location, and performance.
5. Check the intended single camera move, unwanted cuts, background resets, jitter, and temporal drift.
6. Extract and inspect native audio; measure loudness and silence, then require human listening for content acceptance.
7. Mark every applicable criterion PASS, FAIL, or NEEDS HUMAN with timestamped evidence.
8. Classify a reject as structural or stochastic using the controlled reason vocabulary.
9. For deterministic motion graphics, inspect the actual encoded MP4 at frame `n-1` and frame `n`
   for every semantic or editorial boundary. Browser/Studio snapshots do not close this criterion.
10. For a film-to-brand transformation, compare the outgoing master frame with local frame 0 and
    inspect the final encoded frame for unintended fade, missing CTA, or weakened logo hierarchy.

## Verdict rules

- A blocker or required major failure means REJECT.
- Never copy a rejected file into `footage/selects/`.
- A file existing is not approval.
- Keeper promotion requires a written review verdict and human/director acceptance where specified.
- Recommend one-variable iteration for structural failures; recommend batch-and-select only after enough evidence shows stochastic variance.

S1-a v002 is the reference failure example: continuity anchors passed, but an extra cut/background reset at 6.375 seconds failed the uninterrupted Dolly In.
