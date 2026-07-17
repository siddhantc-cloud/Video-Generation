# Pre-Generation Gate — Clear Gut "Ingredient Army" — FAITHFUL variant

**Reviewer:** prompt-reviewer (the pre-generation gate)
**Date:** 2026-06-14
**Reviewed:** `prompts/v5_faithful.md` (18 Veo prompts + 18 keyframes + S18 ffmpeg card)
**Reference of truth:** `00_input_script_HUMAN.md` (frozen, 8 scenes)
**Sanctioned rewrite:** `01_script_v5_FAITHFUL.md` (engine-forced changes only)

---

## 1. VERDICT

**GATE: BLOCKED — awaiting spend approval.**
**1 true regression found and fixed (R1), 2 prompt-safety fixes applied (R2/R3), 0 need a human creative call.**
**1 human-accepted risk to re-acknowledge (S17b lens-facing speaking stomach) and 1 cost correction (cheaper than the script claimed) + 1 hard blocker (balance < cost).**

The prompts are faithful to the human script (modulo the sanctioned engine splits). Fidelity is good. The gate is BLOCKED only on (a) spend approval and (b) an insufficient credit balance — not on creative content.

---

## 2. REGRESSION TABLE

| ID | Scene | Axis | Human intent | Prompt encoded (before) | Sanctioned? (change-log) | Regression? | Severity | Fix applied | Residual risk |
|----|-------|------|--------------|-------------------------|--------------------------|-------------|----------|-------------|---------------|
| R1 | S17b | Dialogue — punctuation | Stomach happy line (raw S8 `...pet halka hai!`) | spoken line ended in `!` : `...हल्का है!` | NO — change-log Rule 6 + S8 row mandate `!`→`।`; `!` leaks/voices in Veo | **YES** | minor | Edited Veo S17b: `हल्का है!` → `हल्का है।` | none |
| R2 | S1 | Staging — mouth-guard contradiction | King looms over the stomach; stomach present, silent (raw S1 VISUAL) | body keeps the stomach silhouette in frame, yet guard said "no other character is visible" (self-contradiction; weakens the guard) | the silhouette itself IS sanctioned (S1 row: faceless turned-away shape); the *contradiction* was an authoring slip | NO (slip, fixed) | minor | Rewrote S1 guard: "Only the King speaks and only the King's mouth moves; the stomach silhouette is faceless, has no visible mouth and stays silent and still; no other mouth is in frame." | Veo could still try to animate the silhouette — faceless/turned-away/no-mouth minimizes it; video-reviewer must confirm no mouth appears |
| R3 | S2 | Staging — mouth-guard contradiction | Same S1 staging continues | same contradiction as S1 | same as R2 | NO (slip, fixed) | minor | Same guard rewrite applied to S2 | same as R2 |

**No other regressions.** Specifically verified clean (see §3): every spoken line is byte-verbatim to the script table, zero dashes/hyphens anywhere, zero quotes wrapping any spoken line, all durations legal {4,6,8}, laugh "हा हा" = exactly 2 beats (S1/S5), no spoken BOOM/scream, label deferred to S18, soft Ayurvedic claims, no un-scripted additions.

---

## 3. PER-SCENE FIDELITY CONFIRMATION (coverage, not just problems)

Every one of the human script's 8 scenes / all lines map forward. Mapping + verdict:

| Prompt shot | Dur | Maps to human | Verdict |
|---|---|---|---|
| S1 King | 8 | raw S1 KING lines 1–3 | PASS (after R2 guard fix) |
| S2 King | 8 | raw S1 KING lines 4–6 ("acidity my friend, bloating my brother" gag) | PASS (after R3 guard fix) |
| S3 Stomach | 6 | raw S1 STOMACH cry ("...मेरी हेल्प कर सके?") | PASS |
| S4 Amla | 8 | raw S2 AMLA identity+function | PASS (22-word length note, F2) |
| S5 King | 4 | raw S2 KING taunt #1 ("एक अकेला...? हा हा।") | PASS — King SOLO, smug |
| S6 Ajwain | 6 | raw S3 AJWAIN | PASS |
| S7 King | 4 | raw S3 KING taunt #2 | PASS — King SOLO, scoffing |
| S8 Saunf | 8 | raw S4 SAUNF — explicit FEMALE voice | PASS |
| S9 King | 4 | raw S4 KING taunt #3 | PASS — King SOLO, forced bravado |
| S10 Haritaki | 8 | raw S5 HARITAKI | PASS — WARM/golden, explicitly NOT menacing |
| S11 King | 4 | raw S5 KING taunt #4 | PASS — King SOLO, confidence breaks |
| S12 Amla | 4 | raw S6 AMLA ("एक मिनट।") | PASS |
| S13 Ajwain | 4 | raw S6 AJWAIN | PASS |
| S14 Saunf | 4 | raw S6 SAUNF — FEMALE voice | PASS |
| S15 Haritaki | 4 | raw S6 HARITAKI; "BOOM!" = POST SFX only | PASS — no spoken BOOM |
| S16 Narrator | 8 | raw S7 narrator sentences 1–3 (merge reveal) | PASS (23-word VO, F2) |
| S17a Narrator | 8 | raw S7 narrator sentences 4–5; King blast = POST visual/SFX | PASS — no spoken scream (23-word VO, F2) |
| S17b Stomach | 6 | raw S8 STOMACH happy line | PASS (after R1 fix; F1 risk) |
| S18 card (ffmpeg) | ~4 | raw S8 narrator dose/brand list + tagline | PASS — post card, pixel-sharp label, no Veo |

**The four authoring-flagged items, resolved:**
- **S17b speaking stomach (F1):** authored correctly — clean SOLO dialogue shot, one mouth to lens, 6-word line, no other mouth in frame. Risk documented in both the script flag and the prompt-file flag; the narrated fallback is *noted but NOT silently substituted* (the human chose speaking for this variant). Correct.
- **S1/S2 silhouette vs mouth-guard:** WAS self-contradictory; FIXED (R2/R3). Now reconciles: silhouette stays in frame (faithful to "King sitting on the stomach"), but is faceless/mouthless/silent so Veo cannot mis-assign a line to it.
- **S16 dual-ref:** header `(ref: bottle, clear_gut_product)` and body "image 1 bottle ref and image 2 product ref" — both refs present and mapped (bible/bottle.png + assets/clear_gut_product.png). Correct.
- **King taunt arc S5/S7/S9/S11:** each is King SOLO ("ALONE… Only this one character in frame"), no hero in frame, and the escalating-then-deflating arc is explicitly encoded (smug → scoffing → forced-bravado/sweat → wide-eyed break). Correct.

**Flags acknowledged (NOT regressions, no fix):**
- **F2 over-budget lines:** S4 = 22 words, S16 = 23, S17a = 23 (vs ~≤20 budget). These are *verbatim-faithful* so kept as-is. S16/S17a are VO (forgiving). **S4 is the single highest lip-sync risk** (22-word on-camera hero in 8s) — flag it for extra re-roll budget. Trimming would be a fidelity downgrade and is a human call, not a regression fix.

---

## 4. MODEL + COST PLAN (verified LIVE 2026-06-14 via `higgsfield` CLI)

### Models per step
| Step | Model | Why | Verified schema |
|---|---|---|---|
| Keyframes (18) | `nano_banana_2` (Nano Banana Pro) | Multi-image-ref character-ID lock; `input_images` array + 9:16 + 2k | aspect `9:16`✓, resolution `2k`✓, `input_images` array✓ |
| Video (18 clips) | `veo3_1` (Google Veo 3.1) | Native audio + same-pass lip-sync; single start-image/clip; same engine as the validated prior run | aspect `9:16`✓, duration enum `["4","6","8"]`✓, `quality` `["basic","high","ultra"]`, `model` `["veo-3-1-preview","veo-3-1-fast"]`, start_image max 1✓ |
| S18 card | ffmpeg (local) | Pixel-perfect legible label; no model call, no spend | n/a |

**Priced tier:** `--model veo-3-1-preview --quality high` (the tier the prior validated production run used; transaction history shows a flat 58cr at 8s).
**VERIFIED unit costs** (`generate cost`, read-only, no job created): **Veo 8s = 58cr · 6s = 43.5cr · 4s = 29cr** (price SCALES with duration). nano_banana_2 9:16 2k = **2cr/image**.
Alt tiers (verified, NOT recommended): veo-3-1-fast 8s = 22cr (lower quality, weaker lip-sync); ultra 8s = 87cr.

### Line-item table (clean single pass)
| Shot | Model | Dur | Credits |
|---|---|---|---|
| S1 | veo3_1 | 8s | 58 |
| S2 | veo3_1 | 8s | 58 |
| S3 | veo3_1 | 6s | 43.5 |
| S4 | veo3_1 | 8s | 58 |
| S5 | veo3_1 | 4s | 29 |
| S6 | veo3_1 | 6s | 43.5 |
| S7 | veo3_1 | 4s | 29 |
| S8 | veo3_1 | 8s | 58 |
| S9 | veo3_1 | 4s | 29 |
| S10 | veo3_1 | 8s | 58 |
| S11 | veo3_1 | 4s | 29 |
| S12 | veo3_1 | 4s | 29 |
| S13 | veo3_1 | 4s | 29 |
| S14 | veo3_1 | 4s | 29 |
| S15 | veo3_1 | 4s | 29 |
| S16 | veo3_1 | 8s | 58 |
| S17a | veo3_1 | 8s | 58 |
| S17b | veo3_1 | 6s | 43.5 |
| **Veo subtotal** | — | 106s | **768.5** |
| Keyframes 18 × 2cr | nano_banana_2 | — | **36** |
| S18 card | ffmpeg | — | 0 |
| **CLEAN-PASS TOTAL** | — | — | **804.5 cr** |

### Cost correction vs the script
The script quoted **~930 cr** (flat 58cr/clip × ~16 clips). **Verified actual = 804.5 cr** despite **18** clips, because Veo price scales with duration and the 8 four-second micro-shots are only 29cr each (not 58). So the FAITHFUL clean pass is **~126cr CHEAPER than the script's own estimate**, and the clip count is **18, not 16** (S17a + S17b are both Veo). It is still materially more than the AI-friendly cut — that comparison is correct in direction, just not in magnitude.

### Spend gate (BLOCKER)
- **Clean pass:** 804.5 cr
- **Re-roll cushion:** +150–350 cr (4 King taunts + 4 freeze quips + lens-facing S17b + 22-word S4 = elevated re-roll surface; ~3–6 Veo re-rolls @ 29–58cr + a few keyframe re-rolls). Realistic need ≈ **1,000–1,150 cr**.
- **Current balance: 647.4 cr (Ultra plan).**
- **HARD BLOCKER:** the clean pass (804.5cr) already **exceeds the balance (647.4cr) by ~157cr**, before any re-roll. **A top-up is required before a full faithful run is even possible.** This is a stronger blocker than for the AI-friendly cut and is itself a reason the human may prefer the lean variant or a trimmed hybrid.
- **No generation and no spend were performed in this review** — all costs came from the read-only `generate cost` estimator and transaction history.

---

## 5. AV REVIEW METHOD FOR THIS VIDEO (per-scene, post-generation)

**Eyes (Higgsfield `video_analysis` + ffmpeg frame timeline, per clip):**
- Dialogue shots (S1–S15, S17b): the **named speaker's mouth moves AND no other mouth animates**.
- S1/S2: stomach silhouette stays **faceless/mouthless/silent** (no mouth ever appears on it).
- King taunts S5/S7/S9/S11: King **SOLO**, no hero leaks into frame; arc reads smug → scoff → forced-bravado → break.
- Heroes: never a dark/menace cue (expression leakage); Haritaki (S10/S15) reads **WARM, not scary**.
- S16/S17a: bottle **still, no morph**, no model-burned label text.
- S17b: stomach **lens-facing single talker**, no bottle/King in frame.
- S18: real label **pixel-sharp**.

**Ears — content (Whisper + ElevenLabs):**
- Whisper transcription per clip: every Devanagari line present, in order, correct text, correct speaker.
- ElevenLabs `speech_to_text` / `isolate_audio` to confirm dialogue + isolate voice before MOS.
- **Laugh count from ACTUAL audio:** S1 and S5 `हा हा` = exactly **2 beats**, no hallucinated laugh-track.
- **Confirm silence where required:** NO spoken "BOOM" in S15, NO spoken scream in S17a (POST-only).
- Captions/karaoke text cut from the **actual audio**, never from the script.

**Ears — quality (UTMOS):** RELATIVE MOS only (English-trained model → relative ranking + re-roll trend; isolate the voice first). Flag the lowest outliers; do NOT threshold absolutely on Hindi.

**Stays needs-human:** frame-exact lip-sync offset; calibrated-absolute Hindi MOS; final comedic-timing + good/evil polish; **S17b organ lip-sync acceptability (never auto-PASS)** and the go/no-go on the documented narrated fallback.

**Tied to this ad's known failure modes:** laugh-count (S1/S5), dash-garble (verified zero), `!` leak (fixed at S17b), lens-facing organ (S17b), label drift (deferred to S18), Saunf female-voice gender (S8/S14), two-mouth mis-assignment on the S1/S2 silhouette.

**Extra re-roll surface (vs AI-friendly):** the 4 restored King taunts + the 4 freeze-frame quips + the lens-facing S17b stomach are the new re-roll-prone surfaces. Budget extra review passes and credits accordingly.

---

## 6. FIXES APPLIED TO `prompts/v5_faithful.md`
1. **S17b Veo:** `अब लग रहा है पेट हल्का है!` → `...हल्का है।` (removed the `!` leak — R1).
2. **S1 Veo mouth-guard:** rewrote to "Only the King speaks and only the King's mouth moves; the stomach silhouette is faceless, has no visible mouth and stays silent and still; no other mouth is in frame." (removed the self-contradiction — R2).
3. **S2 Veo mouth-guard:** same rewrite as S1 (R3).

---

## 7. GATE

**APPROVE to proceed to generation** (clean pass ~804.5 cr; realistic need ~1,000–1,150 cr with re-rolls) **— REQUIRES a credit top-up first: balance 647.4 cr is insufficient even for a clean pass.** Or tell me what to revise (e.g. pick AI-friendly, or trim FAITHFUL to a hybrid per the script's trim plan to fit budget).

**Nothing generates until you approve AND the balance covers the run.**
