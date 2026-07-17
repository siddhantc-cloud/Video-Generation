# Pre-Generation Gate Report — Clear Gut "Ingredient Army" (v5 AI-FRIENDLY variant)

**Reviewer:** prompt-reviewer (pre-generation gate) · **Date:** 2026-06-14
**Engine:** Veo 3.1 (`veo3_1`, native audio) + Nano Banana 2 (`nano_banana_2`) keyframes + 1 ffmpeg card
**Files under review:** `prompts/v5_aifriendly.md` (EDITED in-place) vs
`00_input_script_HUMAN.md` (frozen truth) modulo `01_script_v5_AIFRIENDLY.md` (sanctioned rewrite)

---

## 1. VERDICT

**GATE: BLOCKED — 0 unresolved regressions (5 prompt-level defects found and ALL auto-fixed) · 1 creative micro-decision flagged for human · awaiting spend approval.**

No regression remains in the prompt file. The gate is BLOCKED only on the two things a reviewer
cannot self-approve: (a) the explicit **spend approval** (~614 cr), and (b) one optional creative
micro-decision (S12 voiced dose tail — does not block, see §6). Every spoken line is
character-identical to the sanctioned v5 script, dash-free, quote-free, single-line-per-shot, with a
correct ambient bed; every duration is engine-legal.

I distinguish two categories of finding:
- **Defects I fixed** (5 edits): internal prompt contradictions that would have caused a *regression
  at generation time* (silhouette dropped / a second mouth animated / Veo hallucinating a music bed).
  These were NOT line/intent regressions — the words and beats were faithful — but they were
  prompt-craft faults that put fidelity at risk, so I repaired them. They are listed in the table.
- **Sanctioned deltas** (many): every place the prompt differs from the raw human script is traced to
  a specific change-log line and is NOT a regression.

---

## 2. REGRESSION / DEFECT TABLE

Legend — Sanctioned = authorized by the v5 change-log (not a regression). Defect = prompt-craft fault
that risked a generation-time regression; fixed in-place.

| Shot | Axis | Human-script intent | What the prompt encoded | Sanctioned? (change-log) | Regression? | Severity | Fix applied / decision | Residual risk |
|---|---|---|---|---|---|---|---|---|
| **S1** | Cast/staging — mouth guard | King looms over the sad bloated stomach (S1 VISUAL); only King speaks | Body described a faceless turned-away stomach silhouette **but** the guard said "no other character is visible" — a self-contradiction Veo could resolve by dropping the silhouette OR by animating it | n/a (prompt-craft) | **Would-be regression** (lost the scripted stomach OR a 2nd mouth) | major | **FIXED** `prompts/v5_aifriendly.md` S1 Veo: guard now "ONLY the King speaks and ONLY the King's mouth moves; the stomach silhouette has NO visible face and its mouth never moves; no other character speaks." | Veo may still raise the silhouette's prominence; verify at video-review (still-checkable: face not visible) |
| **S2** | Cast/staging — mouth guard | Same King frame, gesturing to his gang; only King speaks | Same contradiction as S1 | n/a (prompt-craft) | **Would-be regression** | major | **FIXED** S2 Veo: same guard rewrite as S1 | same as S1 |
| **S9** | Brand/safety — audio bed | Team-up swell (mood); per rule #8 + Cast block, music is POST, never asked of Veo | Prompt body said "Heroic uplifting swell" while `[NEG]` said "no music" → contradiction → Veo may hallucinate a music/laugh bed (the exact rule-#8 failure) | n/a (prompt-craft) | **Would-be regression** (un-scripted music bed) | major | **FIXED** S9 Veo: "(Mood is heroic and uplifting; the music swell is added in POST, do NOT generate any music.)" | low; confirm with ASR/ear at review that bed is clean room-tone only |
| **S10** | Brand/safety — audio bed | Product reveal spectacle; music/SFX POST | "Magical golden shimmer." standalone read as an audio cue vs `[NEG]` no-music | n/a (prompt-craft) | **Would-be regression** | minor | **FIXED** S10 Veo: "(Visual: magical golden shimmer only; any chime or music is POST, do NOT generate any music.)" | low |
| **S11** | Brand/safety — audio bed | Resolution + tagline; chime is POST | "Bright uplifting, soft chime." vs `[NEG]` no-music | n/a (prompt-craft) | **Would-be regression** | major | **FIXED** S11 Veo: "(Visual is bright and uplifting; the soft chime is added in POST, do NOT generate any music or chime.)" | low |
| S1 laugh | Dialogue — laugh count | `Hahaha!` (raw) | `हा हा।` (2 beats) in prompt | **Sanctioned** ("S1 laugh count": 3→2 beats, matches what Veo voices) | No | — | caption MUST be cut from ACTUAL Whisper audio, not this text (fixlist #2) |
| S1/S2 | Beat split | King's 6-line monologue + BOOM | split across S1+S2 solos; BOOM→POST SFX | **Sanctioned** ("S1 two characters + 6-line speech") | No | — | none |
| S3 | Beat/staging | Stomach's cry for help (raw S1 tail, in King's frame) | Stomach SOLO, King out of frame, lens-facing, mouth moves | **Sanctioned** ("S3 raw stomach line") | No | — | none |
| S4–S7 | Dialogue/intent | 4 hero intros (Amla/Ajwain/Saunf/Haritaki), each verbatim-meaning | 4 SOLO dialogue shots, Latin→Devanagari, `!`/`…`→`।`, Anglicism smoothing | **Sanctioned** (per-hero change-log rows) | No | — | S4=22w / S10=21w at the 8s ceiling (flagged in v5 itself); lip-sync stays needs-human |
| S5/S7/S8 | Dialogue — King taunts | 3 per-hero King taunts (raw) | CUT; only the final reaction kept as S8 solo | **Sanctioned** ("S2→S5 King taunts" — the biggest creative trade, flagged + human-approved in v5) | No | — | banter rhythm reduced (the v5 gate already surfaced this; human approved) |
| S6 | Voice gender | Saunf (female herb) | "smooth gentle calm **FEMALE** Hindi voice" | matches Cast block | No | — | Veo may still guess; needs-ear confirm |
| S7 | Good/evil read | Haritaki = trusted herb, warm | "benevolent good guy, NOT menacing", warm gold, kind eyes | matches rule #3 (anti-leakage) | No | — | Haritaki bible ref is itself fierce (expectations.md note) — verify warm at review |
| S9 | Multi-mouth collapse | 4 heroes each speak + BOOM (raw S6) | collapsed to NARRATOR VO, heroes HARD profile, mouths closed | **Sanctioned** ("S6 FOUR heroes" blocker) | No | — | recurring lens-facing failure — verify hard-profile holds (fixlist #4) |
| S9/S10/S11 | Narrator split | raw 5-sentence narrator block | split across the 3 narrated shots | **Sanctioned** ("S7 Narrator 5 sentences") | No | — | same narrator voice across all 3 — verify continuity |
| S8 | Scream cut | `Nahiiiiiii!` (raw S8) | King blast → POST visual/SFX, no spoken scream | **Sanctioned** ("BOOM/Nahiiiiiii interjections") | No | — | none |
| S11 | Stomach happy line | `Ab lag raha hai pet halka hai!` (raw, spoken) | narrated joy ("पेट हल्का"), stomach HARD profile mouth-closed | **Sanctioned** ("S8 3 speakers + scream"; lighter-touch alt offered) | No | — | if human wants stomach to SPEAK it, that is a new solo shot (see §6 option) |
| S10/S11 | Label in motion | product reveal | S10 "label need NOT be legible"; S11 "label kept sharp" but not relied on; legible payoff = S12 card | matches rule #9 | No | — | S11 "label sharp" is aspirational not demanded — acceptable; brand truth on S12 |
| S12 | Brand close | dose + tagline + brand (raw S8 narrator tail) | on-card POST text; optional voiced narrator tail | **Sanctioned** ("S8 dose 10-15 drops") | No | — | **needs-human micro-decision** (§6): voice the tail or card-only? |

**Net: 0 line/speaker/laugh/duration/claim regressions. 5 prompt-craft defects, all fixed in-place.**

---

## 3. PER-SCENE FIDELITY CONFIRMATION (coverage, not just problems)

Verified programmatically (char-exact diff of every spoken line vs the sanctioned v5 line — all 11
`identical=True`, dash-free, quote-free; `[NEG]` present on all 11; all durations in {4,6,8}):

- **S1 King (8s)** — PASS after fix. Line verbatim, 2-beat laugh, comedic-menace, silhouette guard repaired.
- **S2 King (8s)** — PASS after fix. Acidity/bloating gag intact as own beat, silhouette guard repaired.
- **S3 Stomach (6s)** — PASS clean. SOLO speaker, lens-facing, King out of frame. (Distinct from S11.)
- **S4 Amla (8s)** — PASS clean. Warm hero, full pitch verbatim (22w, sanctioned at ceiling).
- **S5 Ajwain (6s)** — PASS clean. Bright energetic, tightened line (sanctioned), warm.
- **S6 Saunf (8s)** — PASS clean. Explicit FEMALE voice; calm; line verbatim.
- **S7 Haritaki (8s)** — PASS clean. Warm gold + anti-villain-leakage guard; swagger line kept.
- **S8 King (6s)** — PASS clean. The one kept reaction; cowering, still gross-not-sympathetic.
- **S9 team (NARRATOR, 6s)** — PASS after fix. Heroes HARD profile / mouths closed; King tiny/dark; music-conflict repaired.
- **S10 reveal (NARRATOR, 8s)** — PASS after fix. No characters; bottle still, label-not-required; music-conflict repaired.
- **S11 resolution (NARRATOR, 8s)** — PASS after fix. Stomach HARD profile mouth-closed (fixlist #4 fix); benefit+tagline verbatim; music-conflict repaired.
- **S12 card (ffmpeg, free)** — PASS clean. Pixel-perfect brand close from real PNG; optional voiced tail flagged (§6).

The four AD-flagged staging calls, resolved:
1. **S3 (speaks) vs S11 (narrated):** cleanly distinct — S3 lens-facing + mouth moves; S11 hard profile + mouth closed + "NO character moves their mouth." Not blurred. **PASS.**
2. **S1/S2 silhouette vs "no other character visible":** was a real contradiction → **FIXED** (guard now keys on *who speaks/whose mouth moves*, silhouette stays present, face not visible). **RESOLVED.**
3. **S10 dual refs (`bottle` + `clear_gut_product`):** both files exist (`bible/bottle.png`, `assets/clear_gut_product.png`); used as colorway/shape refs only, stylized. **PASS.**
4. **S12 voiced dose tail:** genuine creative choice → **flagged for human (§6)**, non-blocking.

---

## 4. MODEL + COST PLAN (live-verified)

### Model choice per step
| Step | Model | Why |
|---|---|---|
| Keyframes (12; S12 needs none → 11) | `nano_banana_2` (Nano Banana 2 / "Pro") | multi-image-ref array → locks character identity from bible refs; 9:16 supported; needed for the per-character ID consistency this ad depends on |
| Video, dialogue shots S1–S8 | `veo3_1`, `veo-3-1-preview`, `--quality high` | native audio + same-pass lip-sync; speaker-dominant solo framing is the only reliable lip-sync path (per v5 research + memory) |
| Video, narrated shots S9–S11 | `veo3_1` (same tier) | native narrator VO over mouth-closed staging; no lip-sync needed but same engine/tier for grade continuity |
| S12 product card | ffmpeg Ken-Burns (no model) | guarantees pixel-perfect, word-perfect label — FREE, 0 credits |

### Schema — VERIFIED live (`higgsfield model get` + `models_explore`, 2026-06-14)
- **veo3_1:** `duration` ∈ {4,6,8} (string enum); `aspect_ratio` ∈ {16:9, 9:16}; `quality` ∈ {basic, high, ultra}; `model` ∈ {veo-3-1-preview, veo-3-1-fast}; `medias` = start_image ×**1** (single start-image — matches the one-keyframe-per-clip design). All 11 prompt durations are legal; all 9:16.
- **nano_banana_2:** `resolution` ∈ {1k,2k,4k}; `input_images` = array (multi-ref OK); aspect includes 9:16. No per-image hard cap surfaced in schema; prior runs used up to 5 refs (S9) without error.

### Cost — VERIFIED from live transaction log (actual charges, not memory)
- **Veo 3.1:** every charge in `account transactions` is a flat **−58 cr** (18 occurrences, all identical), corresponding to the tier the prior run used: `--duration 8 --quality high --model veo-3-1-preview`.
  - **UNVERIFIED:** whether 4s/6s clips cost *less* than 8s at this tier. The log only contains 8s/high/preview charges, all flat 58. **Conservative planning uses 58 cr for every Veo clip regardless of duration.** If shorter durations are cheaper, the real spend is lower — this is a ceiling, not a floor.
- **Nano Banana (Pro):** **−2 cr** per image (verified, multiple occurrences).
- **ffmpeg card:** **0 cr.**

| Step | Unit cost (verified) | Qty | Subtotal |
|---|---|---|---|
| Keyframes (`nano_banana_2`) | 2 cr | 11 | **22 cr** |
| Veo clips (`veo3_1`, high/preview) | 58 cr (ceiling) | 11 | **638 cr** |
| S12 card (ffmpeg) | 0 cr | 1 | **0 cr** |
| **TOTAL (clean first pass, no re-rolls)** | | | **660 cr** |

> If short clips (S3/S5/S8/S9 at 6s) bill below 58, total drops; treat 660 cr as the **upper bound** for one clean pass.

**Re-roll reality (from fixlist):** lip-sync (S1–S5), the recurring lens-facing failure (S9/S11), and gender/leakage checks routinely force re-rolls. Budget a realistic **1.3–1.5× Veo** for re-rolls → **~830–960 cr** to a finished cut. The prior produced run overspent ~640 cr on a now-guardrailed CLI duplicate-id bug — re-confirm `--wait`/id-parse guardrails before submitting.

### SPEND GATE
- **Total estimated (clean pass, upper bound): ~660 cr.** Keyframes 22 cr + Veo 638 cr.
- **Realistic to-finished (with re-rolls): ~830–960 cr.**
- **Current balance: 647.4 cr (Ultra plan).**
- **The first clean pass (~660 cr) marginally EXCEEDS the current 647.4 cr balance**, and a re-roll
  budget exceeds it substantially. **A top-up is likely required before a complete pass.**
- **No `generate` call may run until the human explicitly approves the spend.** I do not generate and
  do not spend. Generation proceeds only on the human's go.

---

## 5. AV REVIEW METHOD FOR THIS VIDEO (what the video-reviewer runs post-generation)

Tied to this ad's four known failure modes: **(a) laugh-count**, **(b) dash-garble**, **(c) lens-facing
narrated character**, **(d) label drift**.

**Eyes (frame-checkable, Higgsfield `video_analysis` per clip + 1fps frame timeline):**
- Per clip: motion/composition/camera/qualitative lip-sync read; re-extract the timeline from the EXACT file under review (process-bug #7 guard).
- S1/S2: stomach silhouette present but **face not visible**; only King animates. (defect-fix verification)
- S3: stomach lens-facing, mouth moving (it SHOULD here). S4–S8: solo speaker dominant, others absent.
- **S9/S11 (failure mode c):** narrated characters in **HARD profile, mouths CLOSED, not lens-facing**. This is the #1 re-roll trigger — verify on interior frames, expect re-rolls, never auto-PASS.
- **S7:** Haritaki reads warm/good, NOT a second villain (anti-leakage); good/evil read holds across the reel.
- **G-no-burned-text:** scan every second — no Veo-burned subtitles/captions (Devanagari or Latin).
- **(failure mode d) label:** S10 label may be soft (OK); S11 not relied on; **S12 card = the one guaranteed-legible BLUMELIFE + blue "Clear Gut" + "पेट हल्का। दिन हल्का।"** — verify pixel-sharp, no typo, correct colorway (amber glass / white cap).
- Bottle does not morph (S10/S11 "still, no morph"); no character identity drift vs bible refs.

**Ears — content (Whisper + ElevenLabs):**
- Whisper transcription: all 11 lines present, in order, each in its window, correct Hindi, none swapped/dropped/duplicated.
- **(failure mode a) laugh count:** count "हा हा" beats from ACTUAL Whisper audio (NOT from script). Caption is cut from the ACTUAL audio — never from the prompt text (fixlist #2 guard).
- **(failure mode b) dash-garble:** confirm no garbage/dash artifact in S3/S6/S7 audio (the v5 audio carried dashes; the prompts are now dash-free — verified char-clean — so a fresh gen should be clean; confirm by ear/ASR).
- ElevenLabs `speech_to_text` / `isolate_audio`: isolate the voice before scoring; confirm S6 reads FEMALE; confirm no hallucinated music bed (the §2 defect-fix verification) — bed should be clean room-tone only.

**Ears — quality (UTMOS, RELATIVE only):**
- UTMOS is English-TTS-trained → on Hindi/character/ambient it reads low absolutely. Use RELATIVE ranking + re-roll trend; isolate the voice first; flag the lowest outliers (v5 lowest was S3 Ajwain 1.46), do NOT threshold absolutely.

**Stays needs-human (cannot pass on stills/ASR alone):**
- Frame-exact lip-sync offset (S1–S5 confirmed weak in v5 — never auto-PASS).
- Calibrated-absolute Hindi MOS / subjective voice quality.
- Motion smoothness, final subjective polish, karaoke timing.

Each check maps to `expectations.md` IDs (G-no-burned-text, G-good-evil-read, G-lines-in-order,
BRAND-S9-legible, CAP-*). An unconfirmed blocker-severity needs-human item blocks delivery.

---

## 6. NEEDS-HUMAN (non-blocking creative micro-decision)

**S12 voiced dose tail.** The raw human S8 narrator block voices "Sirf 10-15 drops. Subah aur raat."
The v5 rewrite (sanctioned) moves the dose/brand list to the S12 on-card POST text and marks a voiced
narrator tail OPTIONAL. The prompt offers both. Decide:
- **(A) Card-only (recommended for the tightest cut):** dose/brand appear as on-card text; no extra audio. Cleanest, no extra spend.
- **(B) Voice the tail:** add a POST off-card VO line `सिर्फ़ दस से पंद्रह बूँदें, सुबह और रात।` (no Veo gen — TTS/narrator in post). Restores the human's spoken dose CTA. ~0 Veo cr (post audio).

This does NOT block the gate; it can be decided at edit time. I flag it rather than guess because the
human script DID voice it and the rewrite made it optional — a genuine intent ambiguity.

(Two further sanctioned-but-optional restorations the v5 gate already offered the human, listed for
completeness, not required: ONE extra King taunt micro-shot after Amla [+58 cr, +1 clip]; a Stomach
SOLO speaking shot for "अब लग रहा है पेट हल्का है।" [+58 cr, +1 clip]. Both are clean solos if wanted.)

---

## 7. EDITS APPLIED TO `prompts/v5_aifriendly.md` (5 edits, 5 prompts)

1. **S1 Veo** — replaced guard "Only the King's mouth moves; no other character is visible." → "ONLY the King speaks and ONLY the King's mouth moves; the stomach silhouette has NO visible face and its mouth never moves; no other character speaks." (resolves silhouette-vs-no-character contradiction)
2. **S2 Veo** — same guard rewrite as S1.
3. **S9 Veo** — "Heroic uplifting swell." → "(Mood is heroic and uplifting; the music swell is added in POST, do NOT generate any music.)" (resolves prompt-body music vs `[NEG]` no-music)
4. **S10 Veo** — "Magical golden shimmer." → "(Visual: magical golden shimmer only; any chime or music is POST, do NOT generate any music.)"
5. **S11 Veo** — "Bright uplifting, soft chime." → "(Visual is bright and uplifting; the soft chime is added in POST, do NOT generate any music or chime.)"

Post-edit re-verification: all 11 spoken Devanagari lines remain char-identical to v5; all `[NEG]` intact (11 Veo blocks); no spoken-line touched.

---

## 8. GATE

**GATE: BLOCKED — prompts are fidelity-clean (0 unresolved regressions, 5 defects fixed). Awaiting:
(1) SPEND APPROVAL (~660 cr clean pass / ~830–960 cr with re-rolls vs 647.4 cr balance — top-up
likely needed), and (2) optional S12 dose-tail decision (non-blocking).**

**APPROVE to proceed to generation (spend ~660 cr, top-up likely) / tell me what to revise.**
Nothing generates until the human approves. I have not generated and have not spent.
