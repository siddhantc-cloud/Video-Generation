# Clear Gut, "Ingredient Army", SCRIPT (v4, script-doctored) — PROPOSAL, AWAITING HUMAN APPROVAL

> Output of the **script-rewriter** agent (Gate 0) run on `01_script.md` (v3) on 2026-06-13.
> NOT yet approved — do not hand downstream until the human approves. Full change-log + reasoning at the bottom.

**Format:** vertical 9:16, ~9 shots, ~60s. 3D-caricature (So Sorry / Krishna's-SHAPEFIX style).

**Core discipline (the director's rules):**
1. **One speaker per shot.** Dialogue shots are SOLO — only the speaking character on camera, talking to lens. (Veo moves every visible mouth, so two talkers = mush.)
2. **Multiple characters in frame → NARRATOR voiceover** (no character lip-sync); all non-speaking characters' mouths CLOSED and turned to **hard profile / away**, never three-quarter to lens.
3. **Good vs evil reads in under 1s:** villain = dark/gross/menacing; heroes = bright/warm/friendly; stomach = sympathetic victim. Menacing/evil face for the King ONLY.
4. Dialogue verbatim in **Devanagari**; direction in English.
5. **No dashes/hyphens anywhere in a spoken line** (Veo voices them as garbage). Comma or full stop (। / .) only — including inside compound words (जड़ी बूटियों, not जड़ी-बूटियों).
6. **Laughs are written as the model will actually SAY them** — short, low count; captions in post must be cut from the ACTUAL Whisper audio, never from this text.
7. **No quotation marks around spoken lines in the prompt, no model-burned on-screen text** — every visible word (label, tagline, captions) is post (S9 card + karaoke). Prompt keeps `no subtitles, no on-screen text` and an explicit ambient bed (`no audience, no laugh track, no music`).

| # | Shot (who's on camera) | Speaker | Dur | Line (Devanagari, verbatim) | Intent |
|---|---|---|---|---|---|
| **1** | King looming; Stomach = faceless turned-away shadow at lower frame edge (no 2nd mouth) | **King** (dialogue) | 8s | हा हा! मैं हूँ कॉन्स्टिपेशन किंग। तुम्हारा पेट मैं कभी साफ़ नहीं होने दूँगा। | HOOK: the problem, comedic menace |
| **2** | **Amla SOLO**, to camera | **Amla** (dialogue) | 8s | मैं हूँ भुई आँवला। मैं डाइजेशन को नैचुरली सपोर्ट करता हूँ। | Hero 1, warm, reassuring |
| **3** | **Ajwain SOLO**, to camera | **Ajwain** (dialogue) | 8s | मैं हूँ अजवाइन। पेट का भारीपन और गैस, मेरा काम। | Hero 2, upbeat, energetic |
| **4** | **Saunf SOLO**, to camera | **Saunf** (dialogue) | 8s | मैं हूँ सौंफ। खाने के बाद की ब्लोटिंग को शांत करती हूँ। | Hero 3, calm, gentle |
| **5** | **Haritaki SOLO**, to camera | **Haritaki** (dialogue) | 8s | मैं हूँ हरीतकी। आयुर्वेद की सबसे भरोसेमंद जड़ी बूटियों में से एक। | Hero 4, wise, warm-powerful |
| **6** | 4 heroes in HARD PROFILE turned inward shielding the Stomach (no lens-facing mouths, mouths closed); King shrinks back, tiny + dark | **NARRATOR** (VO) | 6s | ये चार ही नहीं, दस से ज़्यादा आयुर्वेदिक जड़ी बूटियों की पूरी फौज। | Team-up swell |
| **7** | 10+ herbs swirl as gold-light streaks and coalesce into the bottle's glowing form (stylized 3D bottle, still, no morph) | **NARRATOR** (VO) | 6s | सबकी ताक़त, अब एक ही आयुर्वेदिक क्लियर गट ड्रॉप्स में। | Product reveal (spectacle; legible label deferred to S9) |
| **8** | Healthy Stomach in HARD PROFILE, mouth CLOSED, looking AT the bottle; glowing bottle still on a locked pedestal | **NARRATOR** (VO) | 8s | रोज़ सुबह और शाम, सिर्फ़ दस से पंद्रह बूँदें। पेट हल्का, दिन हल्का। | Resolution + CTA |
| **9** | CLEAN PRODUCT CARD, real bottle still (NOT Veo) | (post text / narrator tail) | — | पेट हल्का। दिन हल्का। · BLUMELIFE Clear Gut | Pixel-perfect brand close |

## Cast & assigned voice tone (Veo native, described in prompt — NOT quoted)
King = deep, gravelly, comically-villainous, short dry chuckle (says "ha ha", 2 beats, NOT a laugh track) · Amla = warm confident young-hero (male) · Ajwain = bright, fast, energetic (male) · Saunf = smooth, calm, gentle **FEMALE** · Haritaki = deep, wise, kindly-elder, warm not menacing (male) · Narrator = warm, trustworthy, authoritative, **same voice across 6/7/8**. Ambient bed every clip: `clean room tone, no audience, no laugh track, no music`.

---

## Change log (what changed vs v3 and why)

| Scene / Line | Original (v3) | Rewrite (v4) | Failure mode it prevents | Creativity cost | Severity |
|---|---|---|---|---|---|
| **S1 laugh** | `हा हा हा! … साफ़ नहीं होने दूँगा!` | `हा हा। … साफ़ नहीं होने दूँगा।` (3 "हा" → 2; `!` → `।`) | Exact v5 BLOCKER: caption showed 3× "हा हा हा" but audio said "ha ha" (2×) + stray "!!". Veo says fewer laugh repeats than written and hallucinates a laugh-track; 2 beats matches what it actually voices and what the post caption must be cut to. | Negligible — menace lives in voice-tone, not a third "हा". | **blocker** |
| **S2** | `… सपोर्ट करता हूँ!` | `… सपोर्ट करता हूँ।` | `!` is a stray on-screen-text/over-emphasis risk; `।` keeps the warm read. | None. | minor |
| **S3** | `… गैस, मेरा काम!` (v5 audio/caption carried `गैस — मेरा काम`) | `… गैस, मेरा काम।` | v5 S3 clip voiced an em-dash as garbage + caption showed the dash. v3 text already used a comma (confirmed correct); `!` → `।`. **Real fix = regenerate the clip from this dash-free text.** | None. | **major** (regen) |
| **S4** | `… शांत करती हूँ!` | `… शांत करती हूँ।` | `!` → `।` normalization. | None. | minor |
| **S5** | `… भरोसेमंद जड़ी-बूटियों में से एक!` | `… भरोसेमंद जड़ी बूटियों में से एक।` (hyphen removed; `!` → `।`) | Hyphen in जड़ी-बूटियों gets voiced/shown (v5 #5). Longest line (~13 words) — at the upper 8s edge; kept, but if lip-sync drifts on regen, fallback trims to `… भरोसेमंद जड़ी बूटियों में।`. | None for dash; fallback trim loses the "one of the most trusted" nuance. | **major** |
| **S6** | line `… फौज!` + blocking "3/4 / profile" | `… फौज।`; blocking hardened to **HARD profile, mouths closed** | Narrated (no lip-sync), but v5 #4/#1 proved 3/4 staging isn't enough — Veo re-poses & opens mouths under VO. | None. | **major** (staging) |
| **S7** | `… एक ही, आयुर्वेदिक … में!` (v5 audio `एक ही — आयुर्वेदिक`) | `… अब एक ही आयुर्वेदिक … में।` | v5 #3/#5 em-dash artifact at that join; removed even the comma so the phrase flows. **Regenerate.** | Smoother phrasing; intent intact. | **major** (regen) |
| **S8** | `… दिन हल्का!` + blocking "profile, mouth off-lens" | `… दिन हल्का।`; blocking hardened to **HARD profile, mouth CLOSED** | v5's standout BLOCKER (#4): Stomach turned to camera + opened mouth under VO despite a profile/closed keyframe. | None. | **blocker** (staging) |
| **Discipline header** | rules 1–4 | added rules 5 (no dashes incl. compounds), 6 (laugh count = actual audio), 7 (no quotes in prompt + `no subtitles` + explicit no-laugh-track ambient bed) | Encodes the v5 failures + the new research finding (quotes → subtitle leakage; Veo audience-laugh hallucination) as standing rules. | None. | major (process) |

## Deliberately kept (creative intent protected)
- All four hero lines + King's threat kept **verbatim** except `!`→`।` and the S5 hyphen.
- Wording / the "पेट हल्का, दिन हल्का" rhyme / "मैं हूँ …" intros / Hinglish loanwords (डाइजेशन, ब्लोटिंग, ड्रॉप्स) — all on-brand, preserved.
- One-speaker dialogue shots, narrated groups, Devanagari, good/evil reads, S9 real-bottle card, all {4,6,8} durations, soft Ayurvedic claims — all already correct in v3, kept (only staging hardened).

## New research finding to enforce at the PROMPT stage (not a spoken-line change)
- **Quotation marks around a line are themselves a subtitle-leak trigger** on Veo 3.1, and Veo hallucinates audience/laugh-track beds. Prompts for S1/S6/S7/S8 must (a) NOT wrap Devanagari lines in quotes, (b) keep `no subtitles, no on-screen text`, (c) carry an explicit ambient bed `clean room tone, no audience, no laugh track, no music`. Belongs to the assistant-director / prompt pass.
