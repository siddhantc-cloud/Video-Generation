# Animatic short v003 — human rejection audit

## Audit checklist

| Requirement | Pass condition | Evidence | Owner | Status |
|---|---|---|---|---|
| Preserve evidence | v003 remains untouched and reviewable | `deliverables/review-cuts/animatic-short/ZebPay_Squirrel_SHORT_ANIMATIC_v003.mp4` | Editor | Complete |
| Record human verdict | v003 is no longer described as a keeper candidate | User feedback on 2026-07-23 and this audit | Human/Editor | Complete |
| Separate sync types | Stream sync and semantic sync receive separate verdicts | v003 EDL and timing audit below | Editor | Complete |
| Identify visual failure | Rebuild requirements are specific and testable | Contact sheet and visual audit below | Editor | Complete |

## Verdict

**REJECTED by human review on 2026-07-23.**

The file is technically synchronized but not semantically synchronized. Video and audio both end at
57.900 seconds with zero measured stream drift, yet most picture changes were allocated by percentage
inside a narration paragraph. They were not tied to the first spoken word of the idea shown on screen.

## Timing diagnosis

- Q1, Q2, Q3, Q4, and Q5 split one narration recording across several images using fixed weights.
- The split points therefore cannot reliably land on “boulder by boulder,” “The others laughed,”
  “calm,” “rough,” or “another gap was filled.”
- Q6 repeats the same problem across three cards. The cards begin at 32.900, 37.833, and 42.767
  seconds because of 34/34/32 weights, not because the narration reaches the matching clause.
- The proper fix is one continuous narration track with word-boundary metadata and visual transitions
  snapped to the relevant phrase boundary.

## Visual diagnosis

Evidence: `edit/verify/animatic-short-v003-human-rejection/contact-sheet-v003.png`.

- The mythological section repeats the same orange sunset, centered subject, and shallow-depth portrait
  treatment. This makes different story beats feel like variants of one prompt instead of deliberate
  coverage from a directed scene.
- Rama, the squirrel, and the vanaras often appear separately. The emotional relationship is described
  by narration rather than staged inside the frame.
- Several stills have the polished-but-synthetic “AI epic poster” look: excessive amber, crunchy
  micro-detail, overly perfect rays, and insufficiently tactile coastal weather.
- The SIP section changes visual language completely and becomes a set of wordy presentation cards.
  Those cards are useful timing placeholders but not cinema-quality imagery.
- The payoff frame is clearer than the cards, but it repeats the same frontal golden causeway image
  and therefore does not feel earned as a new visual climax.

## v004 acceptance conditions

1. Every visual transition is linked to a word-boundary or an intentional silent beat.
2. The story coverage includes an epic wide, scale contrast, mockery reaction, Rama–squirrel
   recognition, calm/rough persistence, structural payoff, and bridge completion.
3. Character identity is grounded in the canonical Rama, squirrel, and lead-vanara references.
4. Location progression uses the clean first, half-built, and completed bridge references.
5. Color is sun-faded and naturalistic, not uniformly orange; weather and shot scale vary by beat.
6. The SIP explanation is one continuous visual metaphor with restrained deterministic graphics,
   not three static text cards.
7. Brand text and the official ZebPay logo remain deterministic post-production assets.
