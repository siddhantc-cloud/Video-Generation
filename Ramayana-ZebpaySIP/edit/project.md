# Edit project memory

## Session 1 - 2026-07-23

| Requirement | Pass condition | Evidence | Owner | Status |
|---|---|---|---|---|
| Short-form strategy | A sub-60-second structure is approved before editing | `project/short-form-cut-strategy.md` | Human/Editor | Complete |
| Deterministic preview | Existing keyframes and free scratch TTS produce a reviewable cut without Higgsfield | v003 review cut | Editor | Complete |
| Technical verification | The cut is frame-locked and reviewed at every boundary | v003 EDL and `edit/verify/animatic-short-v003/` | Editor | Complete |
| Human playback | Human reviews pacing and story clarity | v003 review cut | Human | Pending |

**Strategy:** Condense the 166.633-second story to one 57.900-second vertical animatic. Reuse the
strongest existing keyframes, remove redundant setup and mockery beats, preserve Rama's recognition
without the unsafe pickup endpoint, and render the SIP explanation and ZebPay CTA deterministically.

**Decisions:** The short script is 105 words. Scratch narration uses `en-IN-PrabhatNeural` at -4%.
The empty S6 placeholder was replaced with three SIP cards. The legacy end card was rejected because
it contained unapproved copy; v003 uses a clean CTA card.

**Reasoning log:** v001 and v002 remain preserved as self-review evidence. v003 is the keeper
candidate because it passes duration, sync, decode, boundary, copy, and source-preservation checks.

**Outstanding:** Human playback; final narration direction; music/SFX/captions; brand/legal approval;
then a revised paid-motion seconds map if the human locks this animatic.

## Session 2 - 2026-07-23

| Requirement | Pass condition | Evidence | Owner | Status |
|---|---|---|---|---|
| Human feedback recorded | v003 is marked rejected for semantic timing and visual quality | `review/animatic-short-v003-human-rejection.md` | Editor | Complete |
| Visual rebuild | A new directed, continuity-controlled keyframe set replaces the v003 selections | `keyframes/short-v004/` | Image/Continuity | Complete |
| Semantic sync | Visual transitions follow spoken phrase boundaries | v004 phrase map and EDL | Editor | Complete |
| Graphic rebuild | SIP and CTA sections no longer use primitive static cards | v004 animation clips | Editor | Complete |
| Self-review | Full decode, frame count, stream drift, boundary pairs, copy, and continuity pass | `review/animatic-short-v004-review.md` | Editor | Complete |
| Human playback | Human accepts v004 as the new animatic baseline | v004 review cut | Human | Pending |

**Strategy:** Preserve the approved 105-word script but rebuild its directing logic. Synthesize the
scratch narration once, capture word-boundary metadata from the same request, snap each picture idea
to the matching first word, generate a new naturalistic coastal keyframe set, and keep the story and
SIP metaphor in one visual world.

**Decisions:** v004 uses eleven new generated plates, one continuous bridge-based SIP graphic, and a
deterministic animated ZebPay card. The first K02 variant was replaced because the workers looked
human rather than vanara. A ten-frame fade at K10→G11 was removed after boundary review exposed a
dark flash.

**Reasoning log:** Technical stream sync is necessary but insufficient. Phrase-level semantic sync
is now measured separately and must remain within half a frame for this workflow.

**Outstanding:** Human playback and taste notes; final narration; SFX/ambience/music/captions;
brand/legal approval; then paid motion only for approved beats.

## Session 3 - 2026-07-23

| Requirement | Pass condition | Evidence | Owner | Status |
|---|---|---|---|---|
| Motion production | Every approved v004 motion cell has one reviewed 480p Seedance take or a documented range repair | Motion manifest and first-pass review | Producer/Director | Complete |
| Picture conform | Motion sources preserve all 1,566 phrase-locked frames | Final phrase map and EDL | Editor | Complete |
| SFX architecture | Reviewed native audio is mixed as shot-local stems with boundary fades | Picture/VO/SFX review cut | Sound/Editor | Complete |
| Caption craft | Caption blocks remain compact, safe, and above all graphics | v003 QC contact sheets | Editor/QC | Complete |
| Delivery | Captioned master, clean master, and poster decode and match their hashes | `deliverables/final/DELIVERY-v003.md` | Editor/QC | Complete |
| Human release | Final playback and brand/legal release are recorded | Delivery review | Human/Brand | Pending |

**Strategy:** Replace the approved v004 keyframe cells with reviewed Seedance motion while preserving
the exact phrase map. Use the valid opening range of K03 only, keep all native ambience as separate
stems under the approved narration, and retain deterministic SIP graphics and ZebPay card.

**Decisions:** The first pass produced ten full keepers and one partial K03 keeper. K03 is slowed
from its valid 0.00-1.50-second range and held to fill four seconds. Captions use 3-5-word
word-boundary chunks. The redundant final subtitle is omitted because the branded card already
contains the spoken CTA verbatim.

**Reasoning log:** v001 and v002 final renders are preserved as self-QC evidence. v003 is the
operator-QC master after fixing both excessive caption coverage and end-card overlap. ElevenLabs
music returned HTTP 402 before generation, so the final mix intentionally uses narration plus
Seedance-native SFX without an invented substitute.

**Outstanding:** Human playback and brand/legal release approval.

## Session 4 - 2026-07-23

| Requirement | Pass condition | Evidence | Owner | Status |
|---|---|---|---|---|
| Premium SIP motion | The graph reads as cinematic motion design inside the Ram Setu world | HyperFrames v005 hero contact | Motion/Creative | Complete |
| Storyboard | Three animated cards match the approved narration beats and exact duration | `edit/animations/slot_sip_graph_v005/STORYBOARD.md` | Motion/Editor | Complete |
| Phrase lock | Visual beat 2 begins at local frame 133 and beat 3 at frame 245 | r3 boundary contact | Editor/QC | Complete |
| Technical delivery | 319 decoded frames, 30 fps, 1080×1920, no black interval | `render-report.md` | Editor/QC | Complete |
| Master integration | A new review cut replaces G11-G13 without changing the locked v003 master | New timeline/review cut | Editor | Pending |

**Strategy:** Replace only the primitive SIP graph section with a deterministic HyperFrames
composition. Preserve the K10 Ram Setu plate, express volatility with one uneven market curve, and
express SIP discipline with equal contribution markers on a fixed bridge cadence.

**Decisions:** The board has three animated cards at 4.433333 s, 3.733333 s, and 2.466667 s. The
selected MP4 is `sip-graph-v005_r3_1080x1920_30fps_hq.mp4`. HyperFrames rendered the exact 319-frame
duration natively, so no quality-reducing conform re-encode was performed.

**Reasoning log:** The first render exposed a 2-3-frame headline overlap that automated checks
reported only as informational. The second repair removed overlap but advanced the new phrase by one
frame. The third and selected pass derives boundaries from integer frame arithmetic (`133 / 30` and
`245 / 30`), proving that actual rendered-frame inspection remains mandatory.

**Outstanding:** Insert the approved standalone graph into a new review cut; then address the logo
animation, narration, and other audio work separately.

## Session 5 - 2026-07-23

| Requirement | Pass condition | Evidence | Owner | Status |
|---|---|---|---|---|
| Premium ZebPay close | The bridge world transforms into the supplied mark and a strong CTA | Logo render contact | Motion/Brand | Complete |
| Exact logo slot | Closing animation is 100 frames at 30 fps with no end fade | Logo render report | Editor/QC | Complete |
| Premium graph integration | Selected 319-frame graph replaces only G11–G13 | v005 timeline manifest | Editor | Complete |
| Picture and audio lock | Review variants remain 1,566 frames; existing AAC is byte-identical | FFprobe and audio MD5 | Editor/QC | Complete |
| Caption-safe finish | Captions are burned last, below the graph focal curve, and omit G15 | Caption contact sheet | Editor/QC | Complete |
| Human review | Human watches the complete captioned cut and approves brand treatment | v005 review cut | Human/Brand | Pending |

**Strategy:** Finish the motion-graphics pass without reopening the approved film or audio. Replace
only the two deterministic picture ranges, preserve every phrase boundary, copy the v003 AAC stream
unchanged, and create new review outputs rather than overwriting the locked masters.

**Decisions:** The logo transition starts from the exact global frame 1465 image, sends blue/amber
light along Ram Setu, and resolves into the supplied ZebPay mark and `START YOUR SIP`. The final
state holds through frame 99. The initial caption burn crossed the graph curve; it was rejected and
rebuilt in the lower safe band before the selected output. G15 remains subtitle-free because the
card itself renders the spoken CTA.

**Reasoning log:** Browser snapshots passed, but the actual 100-frame render and assembled boundary
pairs remained the authority. Frame 1465 and new frame 1466 are visually continuous because local
logo frame 0 uses the exact outgoing picture. Both review variants decode fully, blackdetect finds
no interval, and their audio elementary streams match the v003 source MD5.

**Outputs:** `deliverables/review-cuts/final-short-v005/`; timeline and hash manifest at
`edit/timelines/final-short-v005-premium-graphics.json`; full operator QC at
`review/final-short-v005-premium-graphics-qc.md`.

**Outstanding:** Human playback and ZebPay brand/legal approval. Narration, music, and SFX remain a
separate future pass; no audio change was made here.
