# Production workflow: "The Squirrel in Ram Setu" (ZebPay SIP ad)

Concrete instance of the master pipeline in `../AI_VIDEO_WORKFLOW.md`. This binds the pluggable slots to THIS job and classifies every shot. **Status: PLAN for human review. No credits spent yet.** Once approved, production starts at Gate 0.

Source script: `The Squirrel in Ram Setu (Small Investments Create Big Wealth).md` (7 scenes).

---

## 1. The brief (distilled from the script)

- **Brand:** ZebPay ("India's oldest crypto exchange").
- **Message:** SIP / consistent small investing beats timing the market. The Ramayana squirrel places one pebble again and again, regardless of the tide, and helps build Ram Setu. "You don't need to time the market. You need to keep showing up, same amount, every time. That's SIP."
- **Form:** narrated mythological allegory, 7 scenes, single narrator voiceover, ends on a ZebPay logo card.
- **Tone:** grand and reverent at the open, warm and playful in the middle, plainspoken and direct at the SIP payoff.

---

## 2. The key structural finding (why this is more tractable than our caricature ads)

**Every line is NARRATOR voiceover. No character speaks on camera anywhere in the script.** Consequences:
- We **skip the entire multi-speaker lip-sync failure mode** (hard rule 4 is not even triggered, no moving mouths to sync).
- Audio is **one VO track** (recorded or TTS) plus timed captions. This is the audio-decision-node "no visible speaking mouth" branch.
- Generation risk collapses to two things: **(a) character identity consistency across scenes** (Rama, the squirrel) and **(b) environment continuity** (the growing bridge). Both are handled by the still-first + reference-lock + keyframe method, not by lip-sync tricks.

This is the single biggest reason to be confident this video can come out well.

---

## 3. Requirements to confirm (decisions for your review)

These are not in the script and change the pipeline. **All R1 to R7 now resolved (2026-07-07). One loose end: the Sarvam API key is NOT in `.env` (only `ELEVEN_LABS_API_KEY` is), so VO defaults to ElevenLabs until the key is added. Not a blocker.**

| # | Decision | Options / note | My recommendation |
|---|---|---|---|
| R1 | **Art style** | photoreal cinematic epic · stylized 3D animated · 2D illustrated · painterly Amar-Chitra-Katha | **DECIDED: PHOTOREAL** (your call). Flag, not an overrule: this is the highest-drift, most expensive path. Consistency mitigations are intensified in Section 4a. |
| R2 | **Aspect ratio** | 9:16 · 16:9 · 1:1 | **DECIDED: 9:16 vertical** (mobile reel). |
| R3 | **Target duration** | VO-driven | **DECIDED: script-natural length** (no hard cap; set by the VO runtime, est. ~60 to 90s). Timed once the VO is generated. |
| R4 | **Narration language + voice** | English (script is English) · Hindi · Hinglish | **DECIDED: English, Indian-style, via Sarvam Bulbul TTS** (storytelling voice); ElevenLabs is the already-wired fallback. See Section 4a. |
| R5 | **Scene 7 "direct to camera"** | VO tone vs a real on-camera presenter | **DECIDED: no presenter.** Still + VO + Mode B animations (Remotion/HyperFrames rendered, assembled in video-use). See Section 4a. |
| R6 | **Music / SFX** | generate vs stock | **DECIDED: generate with ElevenLabs `compose_music`** (already wired), a to-brief orchestral myth bed; ambient SFX via ElevenLabs `text_to_sound_effects` or stock. **Higgsfield's only music model (Sonilo) is game-pipeline-only, so it cannot score this ad.** |
| R7 | **The squirrel-stripe beat** | it is a VISUAL beat, not audio | **CLARIFIED + INCLUDED (subtle).** The Indian palm squirrel's three pale stripes are mythologically Rama's finger-marks; they appear softly at Scene 4d when Rama strokes its back. Zero extra cost (part of the still/animation design), not an audio/SFX element. Veto if unwanted. |

---

## 4. Bound slots (proposed defaults, finalized at the spend gate)

| Slot | Bound (finalized 2026-07-07) |
|---|---|
| Style / format | photoreal cinematic mythological allegory; aspect ratio pending R2 (assume 9:16) |
| Skill lane | `caricature-talking-ad` staging method adapted (scene-focused keyframes, no lip-sync) + `audio-first-reel` / `video-use` for VO + caption + assembly |
| Still model (Phase 1) | `chatgpt-imagegen` (free) for concept + reference exploration; Higgsfield Nano Banana Pro for the LOCKED canonical character + per-shot keyframe stills (photoreal fidelity) |
| Motion model (Phase 2) | **Seedance 2.0** (most consistency control: start+end keyframes + image_references, silent mode). Fallbacks: Kling v3.0, Cinema Studio 3.0. See Section 4a. |
| Audio source | single VO track: **ElevenLabs (active, key present)**; Sarvam Bulbul is the preferred tonal fit but its key is NOT in `.env` yet. Music via ElevenLabs `compose_music`. NOT per-shot native audio; `generate_audio=false` on all clips |
| Outro / overlays (Mode B) | **Remotion or HyperFrames** for the ZebPay card, kinetic text, motion overlays; **video-use** for assembly/grade/captions |
| Caption style | `video-captions-karaoke` if styled captions wanted; language English |
| Reference assets | Rama, squirrel, lead vanara, baby vanara, bridge-state refs (see Section 6) |

---

## 4a. Model, VO, and Mode-B tooling decision (verified live 2026-07-07)

**Video engine: Seedance 2.0 (primary).** I checked the live Higgsfield model list, and the intuition "Veo gives the most control so drift does not happen" is backwards for this job on two counts:
- **No engine makes drift "not happen." It is structural** (verified in our own research). Control REDUCES drift; it never removes it. Photoreal makes any residual drift MORE visible than a stylized look would.
- **On Higgsfield, Veo 3.1 exposes only a single `start_image`** (no end-frame, no reference images). Its real edge is native audio + raw photoreal polish, but native audio is useless here (our VO is a separate track, no on-camera lips). So Veo actually gives the LEAST consistency control of the shortlist.
- **Seedance 2.0 exposes the MOST consistency control:** `start_image` + `end_image` (keyframe endpoints) AND `image_references` (multi-image identity conditioning), and is explicitly built for "consistent identity." Up to 4k, cinematic "epic" genre, 4 to 15s. Set `generate_audio=false` (silent) since VO is separate, which also cuts credits. It also topped the independent with-audio arena in our earlier research.
- **Gemini Omni Flash** (the "Gemini Omni" you named) is real and on Higgsfield, but exposes `image_references` ONLY, no start/end keyframes, 720p / 10s max. Good reference conditioning, weaker endpoint control, a fast/cheap tier, not a control leader.

**So do not pick purely on price.** For a consistency-critical PHOTOREAL job, control beats a small price delta, and Seedance 2.0 has the most control. Cost levers (not a model downgrade): iterate cheaply on **Seedance 2.0 Mini / `fast` mode / low-res**, render finals on **Seedance 2.0 `std`** at 1080p or 4k, audio off throughout. Per-shot fallbacks if a shot fights Seedance: **Kling v3.0** (start+end, cinematic) or **Cinema Studio 3.0** (Higgsfield cinema-grade, start+end). **Exact per-shot credit cost is confirmed at the spend gate** (prompt-reviewer, live data), not guessed here.

**Photoreal drift mitigation (since R1 = photoreal):** lock a strong Rama and squirrel reference sheet; pass `image_references` on every shot they appear in; keyframe endpoints (`start_image`/`end_image`) so the face is pinned at cut points; keep shots short; re-lock identity at each reappearance; accept a residual drift ceiling and spend the 3-attempt re-roll budget on the hardest shots (4c above all).

**Voice-over: verified, but key status corrected.** Sarvam's Bulbul TTS is purpose-built for Indian languages and Indian-accented English, handles code-mixed Hinglish, and has a dedicated Storytelling / Advertising voice category (ideal for this narrated myth). **Key status (checked 2026-07-07): `.env` contains only `ELEVEN_LABS_API_KEY`, there is NO Sarvam key.** So VO runs on **ElevenLabs** (it has Indian-English voices) unless you add `SARVAM_API_KEY` to `.env`, in which case we switch to Sarvam for the better tonal match. VO is one track rendered once, so either works and this does not block us.

**Music: ElevenLabs `compose_music` (wired), NOT Higgsfield.** I checked Higgsfield's audio models: its only music generator (Sonilo) is flagged game-pipeline-only, so it cannot score this ad. We generate a to-brief orchestral myth bed with ElevenLabs `compose_music` (licensed royalty-free stock is the alternative); ambient SFX (waves, construction thuds) via ElevenLabs `text_to_sound_effects` or stock.

**Outro + "animations over a still": Mode B, exactly as you said.** The ZebPay logo card, kinetic text/CTA, and light motion-graphic overlays render deterministically with **Remotion or HyperFrames** (zero generation credits), and the whole film is assembled, graded, and captioned in **video-use** (already installed here). For subtle life in a photoreal still (Scene 6's calm space, Ken-Burns / parallax on hero stills), Remotion does camera/parallax moves on a still for free; reserve a paid image-to-video pass only for a still that genuinely needs organic motion.

## 5. Per-scene shot breakdown and A/B/C classification

Mode key: **C** = generative AI video (paid), **B** = programmatic/deterministic (near-free), **A** = turnkey (none here). Every C shot obeys the four hard rules: one subject/action per shot, still-first, 3-attempt cap then fallback, and (not triggered here) no multi-speaker lip-sync.

| Scene | Shot | Mode | Subject / action | Key risk | Notes |
|---|---|---|---|---|---|
| 1 Purpose | 1a Rama at shore gazing to horizon | C | Rama, still hero pose, wind in hair | **Establishes Rama canonical look** (identity lock for scenes 4, 7) | This still IS the Rama reference. Get it perfect first. |
| 1 | 1b Vanara sena gathered behind Rama | C | crowd of vanaras, determined | crowd coherence | wide shot; crowd can be loose |
| 1 | 1c First boulder hurled into sea, big splash | C | one boulder, one action, splash | water physics | single action, keyframe the splash moment |
| 2 Squirrel arrives | 2a Squirrel appears at shore, watching | C | squirrel, small, watching | **Establishes squirrel canonical look** (identity lock for all later scenes) | This still IS the squirrel reference. |
| 2 | 2b Squirrel carries pebble, places it in a gap | C | squirrel + pebble, one action | squirrel identity through motion | image-first; keyframe start (pick up) and end (place) |
| 3 Mockery | 3a Squirrel tries to place pebble | C | squirrel, one action | consistency vs 2b | reuse squirrel ref |
| 3 | 3b Vanara hoists boulder, flexes, looks at squirrel | C | one vanara, one action | vanara look | **establishes lead vanara** |
| 3 | 3c Vanara grins holding two boulders | C | same vanara | identity vs 3b | keep same ref |
| 3 | 3d Baby vanara strolls past carrying a stone | C | baby vanara, one action | new minor character | low stakes, brief |
| 3 | 3e Vanara flicks the pebble away | C | vanara hand + pebble | interaction with squirrel | keep squirrel out-of-focus or separate beat |
| 4 Rama notices | 4a Rama watching, eyes land on squirrel | C | Rama (match 1a) | **Rama identity must match Scene 1** | reuse Rama ref, this is where drift shows |
| 4 | 4b Rama walks over, laughter fades | C | Rama walking | identity through motion | keyframe |
| 4 | 4c Rama kneels, lifts squirrel into palm | C | Rama + squirrel, contact | **hardest shot: two characters, physical contact** | keyframe both endpoints; expect re-rolls; fallback = two-shot cutaway |
| 4 | 4d Rama strokes squirrel's back (stripe beat, R7) | C | Rama fingers + squirrel back | delicate motion | optional stripe reveal here |
| 5 Bridge completed | 5a Montage: squirrel returns in calm and rough seas | C ×N + B assembly | squirrel, repeated returns | continuity across cuts | several short C clips, assembled Mode B |
| 5 | 5b Bridge growing: boulders + lengthening pebble line | C | environment, no character | **bridge-state continuity** | environment evolution shot |
| 5 | 5c Camera push into the gap, pebbles now load-bearing | C | macro push-in on pebbles | detail | strong single-motion shot |
| 6 Parallel | 6a Clean transition, NO mythology, calm space for SIP thought | **B** | typographic / abstract calm | none (deterministic) | **Mode B: render this, do not generate.** Kinetic type or calm abstract for the VO to land. Cheap + on-brand. |
| 7 Outro | 7a Completed bridge, golden light, squirrel on its own pebble | C | hero wide, squirrel | payoff beauty | the money hero shot |
| 7 | 7b ZebPay logo card, minimal, bottom corner | **B** | brand card | none | **Mode B: render, do not generate.** |

**Rough scope: ~18 generative (C) shots + 2 deterministic (B) segments + captions + assembly.** Scene 4c (Rama holding the squirrel) and any squirrel-through-motion shots are the re-roll hotspots; every one has a listed fallback.

---

## 6. Character + environment bible (the identity-lock feeder stage)

Lock these as reference stills BEFORE any animation (cheap, via `chatgpt-imagegen` then Nano Banana for the final locks):

- **Rama:** divine warrior-prince, Dhanush (bow), flowing hair, serene. Appears scenes 1, 4, 7. Canonical set from shot 1a. Highest cross-scene consistency requirement.
- **Squirrel:** Indian palm squirrel, small, expressive. Appears scenes 2 to 7 (the most-repeated character). Canonical set from shot 2a. Optional three-stripe reveal after 4d (R7).
- **Lead vanara:** boastful, muscular. Scenes 3 to 4. Canonical from 3b.
- **Baby vanara:** scene 3 only, minor.
- **Bridge states:** empty sea → first boulders → half-built with pebble line → completed golden bridge. Environment continuity refs so the bridge reads as the same structure evolving.

---

## 7. Phase plan and gates for this video

Follows `../AI_VIDEO_WORKFLOW.md`. Because it is all-VO, the flow is unusually clean:

1. **Gate 0 (THE FIRST STEP):** freeze the script (`00_input_script_HUMAN.md`, done), then run `script-rewriter` to produce `01_script_AIFRIENDLY.md` + a change-log: shot decomposition (esp. Scene 3's ~5 actions), re-spec of the hard shots (4c two-character contact, 5c macro push-in), the resolved decisions (no presenter, stripe beat at 4d), and VO pacing / pause beats. No dialogue to fix (all VO). **The human approves this rewrite BEFORE a single per-shot keyframe is generated, so keyframes are built against the final decomposed shot list, not the draft.**
2. **Classify (done above):** ~18 C, 2 B.
3. **Gate A (C shots):** `assistant-director` audit of the mythology shots vs the chosen engine's failure modes; `scene-expectations` writes the per-shot bar (esp. Rama and squirrel identity criteria).
4. **Phase 1 keyframes + Gate B (done):** character bible + 4-state bridge + multi-angle Rama/squirrel sheets built (shot-agnostic). Then ONE locked keyframe still per C shot (~23), **against the APPROVED rewrite's shot list** (this is why the rewrite comes first). Reviewed on-model / composition / no-stray-text BEFORE animating. Cheap; most iteration happened here.
5. **Storyboard + animatic gate (done):** all locked keyframes assembled into (a) a static film-order board (`storyboard.html`, published as an artifact) with each shot's VO + camera + mode/status, and (b) a timed **animatic** (`animatic/ZebPay_Squirrel_ANIMATIC.mp4`: the keyframes cut to a free Edge-TTS Indian-English scratch VO with Ken-Burns moves and a ZebPay end card, all local and free). The human reviews the whole film flow, pacing, and timing before any spend. The last free checkpoint before money. Shareable with the ZebPay team. The animatic is built by the frame-locked audio-master tool (`tools/av_sync_render.py` + `zebpay/animatic/manifest.json`): it verified **SYNC LOCKED at 0.0 ms drift** and wrote an EDL. Method: `../AV_SYNC_SYSTEM.md`.
6. **Gate A.5 SPEND GATE:** `prompt-reviewer` checks prompts vs the frozen script, picks the motion model, verifies cost, defines the AV review method. Human approves spend. **First credits spent here.**
7. **Phase 2 animate:** keyframe-driven, one subject/action per shot, 3-attempt cap, fallback per shot. Pilot S1-a and 4c first (Gate C).
8. **Record/generate the single VO** and time it; **render Mode B** segments (6a, 7b, the राम overlays, the stripe overlay) and captions.
9. **Phase 3 assemble:** lay VO as the spine, cut visuals to it, music bed, transitions, burn captions last.
10. **Phase 4 verify:** re-transcribe VO in order, frame-check identity/continuity, spend audit. Gate D human approves.

---

## 8. Spend posture

- **Phases 0, 1, Mode B, captions: near-zero credits** (scripting, `chatgpt-imagegen` stills, code render, VO TTS).
- **Only Phase 2 (animate ~18 C shots) spends real credits**, and only after stills are approved. Firm number is set at the spend gate once the motion model is chosen (engine choice swings cost a lot). Plan for each C shot to cost its base rate times up to 3 attempts; 4c and squirrel-motion shots will use their re-roll budget, most wide/static shots will not.
- Cheapest large lever: keep Scene 6 and the end card in Mode B, and keep the VO as one track rather than per-shot native audio.

---

## 9. Open risks specific to this video

1. **Rama identity drift across scenes 1 → 4 → 7** is the main quality risk (structural, per research). Mitigation: strong locked reference, reuse it every shot, keep Rama shots composed similarly, accept the drift ceiling and re-lock at each appearance.
2. **Squirrel-through-motion** (carrying/placing pebbles) repeats many times; small identity wobble is visible. Mitigation: lock a strong squirrel ref; prefer keyframed short actions.
3. **Scene 4c physical contact** (Rama's palm holding the squirrel) is the single hardest shot. Mitigation: pilot it first; fallback is a two-shot (Rama's face + a separate insert of the squirrel in a palm).
4. **Bridge-state continuity** across scenes 2, 5, 7. Mitigation: environment reference set.
5. **Photoreal (R1, chosen) multiplies the identity risks above.** Mitigated by Seedance's keyframe + reference control (Section 4a), strong reference locks, short shots, and the 3-attempt re-roll budget; a residual drift ceiling is accepted. A stylized look would have shrunk this, but photoreal is the creative call.

---

## 10. Recommended next step

All creative decisions R1 to R7 are now resolved: photoreal · 9:16 mobile reel · script-natural length · ElevenLabs (or Sarvam once keyed) Indian-English VO · ElevenLabs-generated music · stripe beat included · no presenter, Mode B outro · **Seedance 2.0** engine. **The one loose end: the Sarvam key is not in `.env`, so VO uses ElevenLabs unless you add `SARVAM_API_KEY`; this does not block us.**

**Production order (locked):** (1) freeze [done] → (2) character bible, shot-agnostic [done] → (3) **script-rewrite [running now]**, you approve it → (4) per-shot keyframes generated against the APPROVED shot list → (5) Gate B still review → (6) Gate A.5 spend gate → first Seedance credits. Everything through step 5 is zero credit spend, so you approve the decomposed script AND the photoreal keyframes before any paid generation.
