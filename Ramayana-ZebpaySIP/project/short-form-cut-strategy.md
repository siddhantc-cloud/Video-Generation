# Short-form cut strategy

## Approval checklist

| Requirement | Pass condition | Evidence | Owner | Status |
|---|---|---|---|---|
| Distribution fit | One vertical master works as a YouTube Short, Instagram Reel, Instagram boost, and Instagram-to-Facebook boosted Reel | Official platform references below | Producer | Verified |
| Creative runtime | Primary master lands between 55 and 58 seconds, including the ZebPay end card | `deliverables/review-cuts/animatic-short/ZebPay_Squirrel_SHORT_ANIMATIC_v003.mp4` | Human/Editor | Complete: 57.900-second review cut |
| Message clarity | The squirrel story, consistency lesson, SIP parallel, and ZebPay CTA remain understandable | `scripts/short-script-v001.md`; v003 review cut | Creative/Human | Ready for human review |
| Cost reduction | Paid motion is limited to shots that need motion; graphics, still pushes, contact payoff, and end card remain deterministic | v003 timeline and graphics sources | Producer/Editor | Animatic completed with zero Higgsfield credits |
| Source preservation | The 166.633-second animatic and original script remain unchanged as historical sources | Original animatic SHA-256 `1A299D194D42C5B0572E5B48F395226C4FE756F0CFEF5D370D88AA1D4F794DF1` | Editor | Verified preserved |
| Cut authorization | No short timeline, new narration, or render is produced until the human approves this strategy | User request on 2026-07-23 | Human | Approved for deterministic animatic |

## Verdict

A one-minute ceiling is the right production choice, but it is not the current organic platform
limit. YouTube Shorts can be up to three minutes. Instagram can create and edit longer Reels, while
Reels over three minutes are not recommended to new audiences. Instagram-only boosted Reels must be
under 90 seconds, and the Instagram-to-Facebook boost flow allows up to 60 seconds.

Use **58 seconds** as the primary creative target. It preserves all of those routes, leaves a small
technical margin under 60 seconds, improves completion potential, and materially reduces Higgsfield
spend. Produce a 25-to-30-second performance cutdown later from the same approved footage; it should
not require new generated shots.

Official references checked 2026-07-23:

- [YouTube Help: three-minute Shorts](https://support.google.com/youtube/answer/15424877?hl=en)
- [Instagram Help: create a Reel](https://www.facebook.com/help/instagram/225190788256708)
- [Instagram Help: boost an Instagram Reel](https://www.facebook.com/help/instagram/570215404599013)
- [Instagram Help: boost a Reel shared to Facebook](https://www.facebook.com/help/instagram/5557385897683570/)

## Proposed 58-second beat map

| Time | Story beat | Visual plan | Paid motion |
|---:|---|---|---:|
| 0:00-0:06 | Ram Setu scale and purpose | Rama, sea, bridge construction; immediate visual hook | 6 s |
| 0:06-0:15 | The squirrel contributes | One coherent pebble-carry/placement action, supported by existing keyframes | 7 s |
| 0:15-0:21 | Mockery | One vanara reaction; remove the baby-vanara detour and repeated boasting | 5 s |
| 0:21-0:32 | Rama recognizes the effort | Rama notices the squirrel; use a locked palm/recognition still for the fragile contact payoff | 7 s |
| 0:32-0:42 | Consistency through conditions | One persistence shot plus a short calm/rough-tide edit from existing assets | 8 s |
| 0:42-0:53 | SIP parallel | Deterministic motion graphics and typography in FFmpeg/video-use | 0 s |
| 0:53-0:58 | Emotional payoff and ZebPay CTA | Locked bridge hero still, then deterministic ZebPay end card | 0 s |
| **Total** | **Seven concise beats** | **33 generated seconds plus 25 deterministic seconds** | **33 s** |

The five initial moving units are deliberately fewer than the current approximately 22 generative
units. Each unit still contains one coherent action. Fewer cuts do not justify overloading a
15-second generation with unrelated beats.

## Proposed narration

> An army of vanaras was building Ram Setu, boulder by boulder. At the edge of the shore, a tiny
> squirrel carried one pebble at a time. The others laughed. What difference could something so
> small make? But Rama saw what they missed. The squirrel kept showing up, whether the tide was calm
> or rough. And with every return, another gap was filled. Investing can work the same way. You do
> not need to predict the perfect market moment. A SIP lets you invest the same amount regularly,
> through the ups and downs. Small steps, repeated consistently, can build something bigger. Start
> your SIP with ZebPay.

This is 105 words. At approximately 125 words per minute it occupies about 50 seconds, leaving roughly
eight seconds for deliberate pauses, the visual hook, and the final brand hold.

## What changes

- Collapse the long battle setup into one visual sentence.
- Keep one clear contribution beat and one mockery beat.
- Keep Rama's recognition, but avoid paying to generate the highest-risk hand-to-squirrel pickup.
- Collapse three tide/repetition explanations into one line and one short montage.
- State the investment parallel once.
- Remove the unapproved "India's oldest crypto exchange" claim.
- Remove "Like, share, and subscribe"; use the direct product CTA instead.

## Indicative experiment economics

At the dated no-reference 480p Standard quote of 3 credits per generated second, 33 generated seconds
would indicate about **99 credits for one candidate pass**, before any media-reference pricing effect.
That is approximately 76% below the current 411-credit one-pass planning estimate. It is not a live
quote or spend authorization. Every fully staged shot still requires a current preflight, exact
reference quote, one-candidate cap, and human approval.

## Approval gate

Approval of this document authorizes creation of a **new versioned short script and 58-second
frame-locked timeline**. It does not authorize paid Higgsfield generation. The existing
166.633-second animatic remains untouched.

Execution result: v003 was rendered on 2026-07-23 at 57.900 seconds with 1,737 frames and zero
audio/video drift. It is a review animatic with scratch narration, not picture lock or paid-generation
authorization.
