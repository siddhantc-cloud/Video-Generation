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

## Session 6 - 2026-07-24

| Requirement | Pass condition | Evidence | Owner | Status |
|---|---|---|---|---|
| ElevenLabs provider truth | Mythology availability and current API entitlement are verified live | Voice Library/API evidence in `VOICEOVER-v006.md` | Voice producer | Complete |
| Voice identity | One rights-safe Indian-English narrator is selected and versioned | Account-owned `NarratorZebPay` Voice Design voice | Voice producer | Complete |
| Pronunciation | Vanaras, Ram Setu, Rama, SIP, and ZebPay survive the final mixed output | Dictionary r2 and final Scribe transcript | Audio QC | Pass |
| Phrase lock | New performance preserves every approved picture/graph/logo beat | v006 phrase-lock EDL; max onset 30 ms | Editor | Pass |
| SFX architecture | Approved native SFX remain separate and intelligible under narration | v006 SFX stem and -16.01 LUFS mix | Sound/QC | Pass |
| Encoded review | Clean/captioned cuts decode, match duration, and retain identical audio | v006 review QC | Editor/QC | Pass |
| Human voice approval | Owner accepts the full voice performance | Captioned v006 review cut | Human | Pending |

**Strategy:** Check the live Higgsfield and ElevenLabs catalogs before synthesis. Prefer an exact
mythology library voice only when the current account can legally and technically use it through the
chosen surface; otherwise use the account-owned original Voice Design narrator. Generate one
continuous timestamped performance, phrase-lock it to the approved 1,566-frame picture, rebuild
captions from the conformed word timings, and preserve the reviewed native SFX architecture.

**Decisions:** ElevenLabs hosts exact Hindu-mythology voices, but the current free/API entitlement
returns HTTP 402 for Voice Library TTS. Higgsfield exposes only generic voice IDs and does not expose
those mythology labels. The selected `NarratorZebPay` voice is an original generated Indian-English
documentary narrator already in the account. Dictionary r2 uses `Zeb Pay` rather than the rejected
hyphenated alias. The new mix retains approved shot-local SFX at -10 dB and requires no limiter.

**Evidence:** `audio/voiceover/elevenlabs-v006/VOICEOVER-v006.md`;
`edit/timelines/final-short-v006-elevenlabs.json`;
`review/final-short-v006-elevenlabs-qc.md`; captioned review cut under
`deliverables/review-cuts/final-short-v006/`.

**Outstanding:** Human playback of v006. Do not overwrite or demote the approved v005 final until
the owner accepts voice tone, pace, and pronunciation. Brand/legal release remains separate.

## Session 7 - 2026-07-24

| Requirement | Pass condition | Evidence | Owner | Status |
|---|---|---|---|---|
| Local voice runtime | Open-source TTS runs on the available 16 GB GPU without hosted synthesis credits | Qwen v008 metadata; 4.640 GiB peak allocated | Voice producer | Pass |
| Exact terms | Vanaras, Ram Setu, Rama, both SIP occurrences, and ZebPay survive the encoded mix | v008 Scribe v2 transcript | Audio QC | Pass |
| SIP correction evidence | Acronym timing is materially longer than the rejected 60 ms v006 occurrence | Encoded v008 SIP spans 0.860 s and 1.221 s | Audio QC | Pass; human listening pending |
| Phrase lock | Continuous local take preserves every approved picture beat | v008 EDL; max onset 30 ms; max tempo 1.120x | Editor | Pass |
| Encoded review | Clean/captioned cuts decode, match duration, and share identical audio | v008 review QC | Editor/QC | Pass |
| Human voice approval | Owner accepts voice, accent, pronunciation, pace, and mix | Captioned v008 review cut | Human | Pending |

**Strategy:** Benchmark the exact difficult terms before generating a full local voice. Select the
seed by transcript/timing evidence, generate one continuous take, map synthesis orthography back to
approved display copy, phrase-lock with pitch-safe local compression, reuse the independent native
SFX stem, and rebuild captions from the conformed Qwen timing.

**Decisions:** Qwen3-TTS 1.7B VoiceDesign is isolated in a project Python 3.12 environment and uses
PyTorch SDPA on the RTX 5060 Ti. Seed `240726` was selected because Scribe recovered `Vanaras`;
seed `240727` was rejected after `Annaras`. Synthesis uses `S. I. P.` and `Zeb Pay`, while captions
retain `SIP` and `ZebPay`. The raw local take is 47.600 seconds. Only K10 and G12 overrun their
picture slots, at 1.030x and 1.120x.

**Evidence:** `audio/voiceover/qwen3-v008/VOICEOVER-v008.md`;
`edit/timelines/final-short-v008-qwen3-local.json`;
`review/final-short-v008-qwen3-local-qc.md`; review cuts under
`deliverables/review-cuts/final-short-v008/`.

**Outstanding:** Human listening is still authoritative because Scribe normalizes initialisms.
Keep v005 as the approved final until the owner accepts the complete v008 performance. Brand/legal
release remains separate.

## Session 8 - 2026-07-24

| Requirement | Pass condition | Evidence | Owner | Status |
|---|---|---|---|---|
| v008 disposition | Human feedback overrides automated voice checks | `review/final-short-v008-human-rejection.md` | Human/Reviewer | Rejected |
| Indian-English route | Current Sarvam model, voices, controls, dictionary, and price are verified | Sarvam v009 voice record | Voice producer | Pass |
| Cheap selection | Difficult terms are tested before full synthesis | Four voice/temperature auditions | Voice producer | Pass |
| Pronunciation lock | SIP and ZebPay survive the encoded review | Final Scribe and dictionary `p_2811321e` | Audio QC | Pass; listening required |
| Phrase lock | New voice preserves all 1,566 picture frames | v009 EDL; 30 ms max onset; 1.200x max tempo | Editor | Pass |
| Encoded review | Clean/captioned cuts decode, match duration, and share audio | v009 QC | Editor/QC | Pass |
| Human voice approval | Owner accepts accent, naturalness, terms, compression, and mix | Captioned v009 review | Human | Pending |

**Strategy:** Replace the rejected foreign-sounding local voice with Sarvam Bulbul v3 Indian
English. Compare short real-script auditions, use a provider pronunciation dictionary instead of
visible phonetic spelling, select native pace plus warm temperature, generate one continuous take,
and phrase-lock it to the unchanged v005 picture.

**Decisions:** `mani` at pace 1.0 and temperature 0.75 was selected over faster `ratan` and `shubh`
auditions. Dictionary `p_2811321e` maps SIP to `S I P` and ZebPay to `Zebb Pay`. A same-voice closing
phrase retest was comped into the selected full performance. Five phrases require pitch-safe local
compression; the maximum is K01 at 1.200x. Native SFX remains a separate stem at -10 dB.

**Evidence:** `audio/voiceover/sarvam-v009/VOICEOVER-v009.md`;
`edit/timelines/final-short-v009-sarvam.json`;
`review/final-short-v009-sarvam-qc.md`; review cuts under
`deliverables/review-cuts/final-short-v009/`.

**Outstanding:** Human playback must judge whether the first article plus S-I-P cadence sounds
natural, whether ZebPay is exact, and whether K01/K14 compression is perceptible. v005 remains the
approved final. Brand/legal release remains separate.
