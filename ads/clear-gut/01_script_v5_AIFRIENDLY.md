# Clear Gut, "Ingredient Army", SCRIPT (v5 AI-FRIENDLY) — GATE-0 OUTPUT, AWAITING HUMAN APPROVAL

> Output of the **script-rewriter** agent (Gate 0), run on the RAW HUMAN script
> `00_input_script_HUMAN.md` (frozen reference of truth) on 2026-06-14.
> This is a **full restructure**, not a light edit — the raw script has two speakers in almost
> every scene and a four-mouths-in-one-frame beat (S6), which Veo 3.1 cannot shoot cleanly.
> **NOT yet approved — do not hand downstream (assistant-director → scene-expectations → production)
> until the human approves.** Full change-log + reasoning at the bottom.
>
> Target engine: **Veo 3.1** (`veo3_1`, native audio) via Higgsfield CLI. Single start-image per clip.
> Durations **4 / 6 / 8s ONLY** (no 7s). Model voices dialogue + animates mouths natively.
> Keyframes via `nano_banana_2` (multi-image-ref).

**Format:** vertical 9:16, **12 shots**, ~62s. 3D-caricature (So Sorry / Krishna's-SHAPEFIX style).
**Story preserved:** Constipation King torments a sad bloated stomach → four herb-heroes arrive one by
one (each landing a hit on the King's confidence) → the team reveals there are 10+ of them → all power
merges into one bottle → King is blasted away, stomach is happy. Comedic, warm, clear good-vs-evil.

---

## Core discipline (the director's rules — carried + extended for THIS script)
1. **ONE speaker per dialogue shot.** Only the speaking character is on camera, talking to lens.
   Veo animates EVERY visible mouth and (per Google's own Veo 3.1 guide) mis-assigns lines when 2+
   characters are present → two-talker shots = mush. Every two-talker beat in the raw script is
   **split into solo shots** or **converted to NARRATOR VO**.
2. **Multiple / background characters in frame → NARRATOR voiceover** (no character lip-sync); all
   non-speaking characters' mouths CLOSED and turned to **HARD profile / away**, never three-quarter
   to lens. (v5 recurring failure: a "3/4" or "profile" stomach still turned to camera and opened its
   mouth under VO — so HARD profile / minimized / turned fully away, expect re-rolls.)
3. **Good vs evil reads in under 1s:** villain = dark / gross / menacing green murk; heroes =
   bright / warm / friendly golden glow; stomach = sympathetic victim. **Menacing face for the King
   ONLY** — never give a hero a fierce/dark cue (expression leakage makes heroes read as villains).
4. Dialogue verbatim in **Devanagari**; scene direction in English.
5. **No dashes / hyphens (`-` `—` `–`) anywhere in a spoken line** (Veo voices them as a garbage
   sound). Comma or full stop (`।` / `.`) only — including inside compound words
   (जड़ी बूटियों, not जड़ी-बूटियों). Ellipses from the raw script (`...`) are rewritten as a full stop
   or comma; they are NOT spoken pauses to Veo and risk being voiced/shown.
6. **Onomatopoeia / laughs / screams written as the model will actually SAY them** — short, low count.
   Veo says fewer repeats than written and hallucinates a laugh-track. Captions in post are cut from
   the ACTUAL Whisper audio, NEVER from this text.
7. **One short line per shot (~20 words / "sayable in ~8s").** Long multi-sentence speeches are split
   across shots; over-packing makes the model speak too fast and raises subtitle-leak risk.
8. **No model-burned on-screen text.** Every visible word (product label, tagline, captions) is post
   (S12 card + karaoke). Prompts keep `no subtitles, no on-screen text` + an explicit ambient bed
   `clean room tone, no audience, no laugh track, no music`. **Do not wrap spoken lines in quotation
   marks in the prompt** (possible subtitle-leak trigger; prompt-stage concern for the assistant-director).
9. **Legible product label is NOT demanded in motion** (Veo warps fine text under I2V, confirmed 3.1).
   The forming bottle (S10) may have a soft label; the still hero bottle (S11) is sharp but not relied
   on for the word-perfect label; the **guaranteed-legible brand moment is the S12 post card** (real PNG).
10. **Claims soft / Ayurvedic** — "digestion support", "helps with everyday gut issues", never a
    medical cure. (The raw line "tumhara pet kabhi properly saaf nahi hone dunga" is the VILLAIN
    boasting, so it stays as comedic menace, not a product claim.)

---

## The rewritten AI-friendly shot list

| # | Who's on camera | Speaker | Dur | Line (Devanagari, verbatim, dash-free) | Intent |
|---|---|---|---|---|---|
| **1** | **King SOLO**, looming on a sad bloated stomach that is a faceless, turned-away dark shape at the lower frame edge (no 2nd mouth) | **King** (dialogue) | 8s | हा हा। मैं हूँ कॉन्स्टिपेशन किंग। मैं तुम्हारा पेट कभी ठीक से साफ़ नहीं होने दूँगा। | HOOK: the villain + the problem, comedic menace |
| **2** | **King SOLO**, same frame, grinning, gesturing to his unseen gang | **King** (dialogue) | 8s | एसिडिटी मेरी दोस्त है। ब्लोटिंग मेरा भाई है। हम सब मिलकर तुम्हारा पूरा दिन ख़राब करेंगे। | Villain stacks the problem (acidity, bloating); raises stakes |
| **3** | **Stomach SOLO**, sad bloated face now to camera, King fully out of frame, sickly-green light | **Stomach** (dialogue) | 6s | कोई है जो मेरी मदद कर सके? | Victim's cry for help (the turn) |
| **4** | **Amla SOLO**, crashes in, heroic stance, to camera, warm golden rim-glow | **Amla** (dialogue) | 8s | रुको ज़रा। मैं हूँ भुई आँवला। मैं डाइजेशन को नैचुरली सपोर्ट करता हूँ और गट को बैलेंस रखने में मदद करता हूँ। | Hero 1 arrives, warm, reassuring |
| **5** | **Ajwain SOLO**, action-movie entry, energetic, to camera, bright punchy warm | **Ajwain** (dialogue) | 6s | अकेला नहीं। मैं हूँ अजवाइन। पेट का भारीपन और बेचैनी, मेरा काम। | Hero 2, upbeat, answers the King's taunt without a 2-shot |
| **6** | **Saunf SOLO**, slides in gracefully, calm, to camera, soft warm | **Saunf** (dialogue) | 8s | और मैं हूँ सौंफ। खाने के बाद जो ब्लोटिंग और भारीपन लगता है, उसके ख़िलाफ़ मैं भी टीम में हूँ। | Hero 3, calm, joins the team |
| **7** | **Haritaki SOLO**, lands with gentle thunder shimmer, wise-kindly, to camera, warm gold | **Haritaki** (dialogue) | 8s | गेम ओवर बोलने से पहले मुझे मत भूलो। मैं हूँ हरीतकी। आयुर्वेद की सबसे भरोसेमंद जड़ी बूटियों में से एक। | Hero 4, wise, warm-powerful (NOT menacing) |
| **8** | **King SOLO**, shrinking back, comically worried (still gross-but-funny, not sympathetic), green murk | **King** (dialogue) | 6s | ओह नो। तुम सब एक साथ? | Villain's confidence breaks (the one taunt-reaction kept, as a solo) |
| **9** | 4 heroes in **HARD PROFILE** turned inward, fists up, shielding the stomach (no lens-facing mouths, mouths CLOSED); King tiny + dark, far back corner | **NARRATOR** (VO) | 6s | ये सिर्फ़ चार की कहानी नहीं है। ये तो दस से ज़्यादा आयुर्वेदिक जड़ी बूटियों की पूरी फौज है। | Team-up swell + "there are more than 4" reveal (replaces the 4-mouth S6) |
| **10** | 10+ herbs swirl in as gold-light streaks and coalesce into the bottle's glowing form (stylized 3D bottle, still, no morph; label may be soft) | **NARRATOR** (VO) | 8s | दस से ज़्यादा आयुर्वेदिक ताक़त, अब एक ही आयुर्वेदिक क्लियर गट ड्रॉप्स में। ये सब मिलकर डाइजेशन को सपोर्ट करते हैं। | Product reveal (spectacle); the "merge into one bottle" payoff |
| **11** | Healthy happy stomach in **HARD PROFILE**, mouth CLOSED, dancing lightly, looking AT the bottle; glowing bottle still on a locked pedestal (King already gone) | **NARRATOR** (VO) | 8s | और मदद करते हैं कॉन्स्टिपेशन, एसिडिटी और ब्लोटिंग जैसी रोज़मर्रा की दिक़्क़तों से। पेट हल्का, दिन हल्का। | King defeated (implied) + happy resolution + benefit + tagline |
| **12** | CLEAN PRODUCT CARD, real bottle still (NOT Veo; ffmpeg Ken-Burns) | (post text / optional narrator tail) | — | दस से ज़्यादा आयुर्वेदिक जड़ी बूटियाँ। सिर्फ़ दस से पंद्रह बूँदें, सुबह और रात। · पेट हल्का। दिन हल्का। · BLUMELIFE Clear Gut | Pixel-perfect brand close + dose CTA |

**Total runtime:** 8+8+6+8+6+8+8+6+6+8+8 = **80s of Veo** before crossfades; with ~0.4s crossfade
overlaps (11 joins) and the S12 card (~4s), the assembled cut lands ~**62s**. If a tighter ~50s cut is
wanted, S2 and S8 are the safest trims (see "lighter-touch alternatives" in the change log).

---

## Cast & assigned voice tone (Veo native, described in the prompt — NOT quoted)
- **Constipation King** = deep, gravelly, comically-villainous; short dry chuckle, says "ha ha" (2 beats, NOT a laugh track). Menacing/gross face — the ONLY menacing face in the ad.
- **Stomach** = soft, anxious, sympathetic (S3); bright, light, relieved (S11, profile/closed-mouth — narrated, NOT speaking).
- **Amla** = warm, confident young-hero (male).
- **Ajwain** = bright, fast, energetic (male).
- **Saunf** = smooth, calm, gentle **FEMALE**.
- **Haritaki** = deep, wise, kindly-elder; warm, NOT menacing (male).
- **Narrator** = warm, trustworthy, authoritative; **same voice across S9 / S10 / S11**.
- **Ambient bed every clip:** `clean room tone, no audience, no laugh track, no music`. Music + SFX
  (the "BOOM", the blast) are added in POST, not requested from Veo (Veo mis-voices written SFX and
  hallucinates beds). The raw script's "BOOM!" / "Nahiiiiiii!" become post SFX / a visual blast, not
  spoken lines (see change log).

---

## Change log (RAW human script → v5 rewrite, with full reasoning)

| Scene / Line | Original RAW text (quoted) | Rewrite (v5) | Failure mode it prevents | Creativity cost | Severity |
|---|---|---|---|---|---|
| **S1 — two characters + 6-line speech + laugh** | `CONSTIPATION KING: Hahaha! / Main hoon Constipation! / Aur main tumhara pet kabhi properly saaf nahi hone dunga! / Acidity meri dost hai... / Bloating mera bhai hai... / Aur hum sab milkar tumhara poora din kharab karenge!` **and** `STOMACH: Koi hai jo meri help kar sakta hai?` **and** `BOOM!` | **Split into 3 solo shots:** **v5-S1** King (हा हा। मैं हूँ कॉन्स्टिपेशन किंग। मैं तुम्हारा पेट कभी ठीक से साफ़ नहीं होने दूँगा।), **v5-S2** King (एसिडिटी मेरी दोस्त है। ब्लोटिंग मेरा भाई है। हम सब मिलकर तुम्हारा पूरा दिन ख़राब करेंगे।), **v5-S3** Stomach SOLO (कोई है जो मेरी मदद कर सके?). "BOOM!" → POST SFX, not a spoken line. | **Two-mouth shot** (King + Stomach both animate); **6 lines is far over the ~20-word/8s budget** (over-packing → too-fast speech + subtitle leak); `...` and `Hahaha!` (3 syllables) and `BOOM!` get voiced as garbage. | The single brooding intro becomes a 2-beat villain build; the King's monologue is now paced across two shots instead of one breath. Menace preserved, slightly less "one menacing wall of text". | **blocker** |
| **S1 laugh count** | `Hahaha!` (King) | `हा हा।` (2 beats, full stop) | v5 BLOCKER recurrence: Veo says fewer laugh repeats than written + hallucinates a laugh-track; caption must be cut from actual audio. 2 beats matches what Veo voices. | Negligible — menace lives in voice-tone. | **blocker** |
| **S1 product-claim safety** | `tumhara pet kabhi properly saaf nahi hone dunga` | kept as VILLAIN boast: `मैं तुम्हारा पेट कभी ठीक से साफ़ नहीं होने दूँगा।` ("properly" → "ठीक से") | This is the villain threatening, not a product claim, so it stays. "properly" Anglicism dropped for a clean Devanagari read; no soft-claim issue because the speaker is the bad guy. | None. | minor |
| **S2 (raw) acidity/bloating lines** | `Acidity meri dost hai... / Bloating mera bhai hai... / Aur hum sab milkar tumhara poora din kharab karenge!` | moved to **v5-S2** (King solo): `एसिडिटी मेरी दोस्त है। ब्लोटिंग मेरा भाई है। हम सब मिलकर तुम्हारा पूरा दिन ख़राब करेंगे।` (`...` → `।`, `!` → `।`) | Ellipses voiced/shown as garbage; keeps the villain's "my friends are acidity & bloating" comedy intact but as its own ~8s beat with one mouth. | None — the gag is fully preserved, just given its own shot. | major |
| **S3 (raw) stomach line** | `STOMACH: Koi hai jo meri help kar sakta hai?` | **v5-S3** Stomach SOLO, King out of frame: `कोई है जो मेरी मदद कर सके?` ("help" → "मदद", "sakta hai" → "सके" for a cleaner read) | Removes the stomach from the King's frame so it is a clean SOLO speaker; "help" Anglicism → "मदद" reads better in Devanagari. | The stomach now gets its own sympathetic close-up (arguably an UPGRADE for the emotional turn). | major |
| **S2→S5 (raw) King taunts** | `King: Ek akela aaya hai mujhe haraane? Hahaha!` (after Amla); `Do logon se kuch nahi hoga!` (after Ajwain); `Abhi bhi main jeet raha hoon!` (after Saunf); `Oh no... Tum sab ek saath?` (after Haritaki) | **Three taunts CUT; one kept.** The per-hero King taunts are removed so each hero is a clean SOLO. The King's arc is preserved by keeping the FINAL reaction as a solo shot **v5-S8** (ओह नो। तुम सब एक साथ?). The "akela / do logon" disbelief is folded into the heroes' own lines ("रुको ज़रा" / "अकेला नहीं") and the team reveal. | Each raw hero scene is a **two-mouth shot** (hero + King taunting back). Cutting the taunts is the cleanest fix; one solo King reaction at the end keeps the villain present without ever putting two mouths in a frame. | The back-and-forth banter rhythm is reduced. Mitigation: the heroes' lines absorb the call-and-response ("रुको ज़रा", "अकेला नहीं"), and the King's deflation still lands at v5-S8. **This is the biggest creative trade in the rewrite — flagged for human review; see lighter-touch alternative below.** | **major** |
| **S2 Amla (raw)** | `Ruko zara! Main hoon bhui Amla! Main digestion ko naturally support karta hoon aur gut ko balance rakhne mein madad karta hoon!` | **v5-S4** Amla SOLO: `रुको ज़रा। मैं हूँ भुई आँवला। मैं डाइजेशन को नैचुरली सपोर्ट करता हूँ और गट को बैलेंस रखने में मदद करता हूँ।` (Latin→Devanagari; `!`→`।`) | Latin script mis-pronounced by Veo; `!` over-emphasis/leak risk. ~22 words at the 8s ceiling — kept because it is the lead hero's full pitch; fallback trim drops the second clause if lip-sync drifts. | None (verbatim intent kept; only script + punctuation). | major |
| **S3 Ajwain (raw)** | `Akela nahi! Main hoon Ajwain! Main pet ki heaviness aur discomfort se ladne aaya hoon!` | **v5-S5** Ajwain SOLO: `अकेला नहीं। मैं हूँ अजवाइन। पेट का भारीपन और बेचैनी, मेरा काम।` (Latin→Devanagari; "heaviness/discomfort" → "भारीपन/बेचैनी"; tightened) | Latin mis-pronunciation; "heaviness aur discomfort" Anglicisms read poorly; tightened to fit a brisk 6s energetic beat. | Slightly punchier than the raw "ladne aaya hoon"; energy preserved (the v5 video-reviewer flagged Ajwain as the weakest clip, so a shorter line helps lip-sync). | major |
| **S4 Saunf (raw)** | `Aur main hoon Saunf! Khane ke baad jo bloating aur fullness feel hoti hai... Uske against main bhi team mein hoon!` | **v5-S6** Saunf SOLO: `और मैं हूँ सौंफ। खाने के बाद जो ब्लोटिंग और भारीपन लगता है, उसके ख़िलाफ़ मैं भी टीम में हूँ।` (Latin→Devanagari; `...`→`,`; "fullness feel hoti hai"→"भारीपन लगता है"; "against"→"ख़िलाफ़") | Ellipsis garbage; "fullness feel"/"against" Anglicisms mis-voiced; smooth single ~8s line. | None — full meaning ("post-meal bloating & fullness, I'm on the team against it") preserved. | major |
| **S5 Haritaki (raw)** | `Game over bolne se pehle mujhe mat bhoolo. Main hoon Haritaki. Ayurveda mein digestion support ke liye sabse trusted herbs mein se ek.` | **v5-S7** Haritaki SOLO: `गेम ओवर बोलने से पहले मुझे मत भूलो। मैं हूँ हरीतकी। आयुर्वेद की सबसे भरोसेमंद जड़ी बूटियों में से एक।` (Latin→Devanagari; "trusted herbs"→"भरोसेमंद जड़ी बूटियों", NO hyphen) | Latin mis-pronunciation; "जड़ी-बूटियों" hyphen voiced as garbage (v5 #5); ~17 words OK at 8s. Haritaki staged warm/kindly, NOT menacing (expression-leakage guard — a "powerful elder" can read as a 2nd villain). | The "Ayurveda mein digestion support ke liye" qualifier is compressed to "आयुर्वेद की सबसे भरोसेमंद" — keeps the trust claim, soft/Ayurvedic. | major |
| **S6 — FOUR heroes each speak, frozen frame** | `AMLA: Ek minute... / AJWAIN: Tumhe lagta hai... / SAUNF: Bas hum chaar hi hain? / HARITAKI: Ab asli surprise dekho.` + `BOOM!` | **COLLAPSED to NARRATOR VO, v5-S9:** 4 heroes in HARD PROFILE (mouths CLOSED, no lens-facing), NARRATOR says `ये सिर्फ़ चार की कहानी नहीं है। ये तो दस से ज़्यादा आयुर्वेदिक जड़ी बूटियों की पूरी फौज है।`. "BOOM!" → POST SFX + visual energy burst. | **The worst multi-mouth case — four animated mouths + four ellipses in one frozen frame** = guaranteed mush + line mis-assignment (Google's own guide: 2+ talkers → use scene-flow narration, not dialogue). Narration carries the exact same "you think it's just 4 of us?" reveal with zero lip-sync. | The four individual hero quips are lost as on-camera dialogue. The CONTENT ("there are more than 4 of us — surprise") is fully preserved in the narrator line and is actually CLEARER. Heroes still get a hero-team hard-profile flex. | **blocker** |
| **S7 Narrator (raw, 5 sentences)** | `Ye sirf 4 herbs ki kahani nahi hai. / 10 se zyada Ayurvedic ingredients ki power... / Ab ek hi Ayurvedic Clear Gut Drop mein. / Sab ek saath milkar digestion ko support karte hain. / Aur help karte hain constipation, acidity aur bloating jaise everyday gut issues se nipatne mein.` | **Split across v5-S9, S10, S11.** "Ye sirf 4 ki kahani nahi… 10 se zyada…" → v5-S9 (team). "10 se zyada… ek hi Clear Gut Drops mein… sab milkar digestion support" → v5-S10 (reveal). "help karte hain constipation, acidity, bloating jaise everyday issues" → v5-S11 (resolution). `...`→`।`, `help`→`मदद`. | 5 sentences in one clip is ~2-3x the ~20-word/8s budget → too-fast VO + subtitle leak. Splitting across the 3 narrated shots keeps each ≤~20 words and lets each line sit on its own visual. | None — every sentence is preserved, just distributed across the shots it describes (which is what each line is ABOUT anyway). | **major** |
| **S8 — King + Stomach + Narrator, 3 speakers + scream** | `CONSTIPATION KING: Nahiiiiiii! / STOMACH: Ab lag raha hai pet halka hai! / NARRATOR: 10+ Ayurvedic herbs. Sirf 10-15 drops. Subah aur raat. Ayurvedic Clear Gut Drops. Pet halka. Din halka.` | **Restructured:** King's blast = POST (visual blast + SFX, NO spoken "Nahiiiiiii"). Stomach is happy but **does NOT speak** — staged HARD PROFILE / mouth closed under NARRATOR VO (v5 BLOCKER #4). The narrator CTA is split: benefit+tagline → v5-S11 VO; the dose/brand list → the **S12 post product card** (on-screen text, not spoken by Veo). | THREE mouths in one beat + a long-drawn scream ("Nahiiiiiii" Veo will clip/mangle) + "10-15" hyphen voiced as garbage + a 6-line list over budget + the recurring stomach-turns-to-camera-and-talks failure. | The King's death-scream as audible dialogue is cut (becomes a visual/SFX blast — arguably punchier). The stomach's happy line "Ab lag raha hai pet halka hai" becomes narrator-described joy ("पेट हल्का"); if the human wants the stomach to SPEAK it, that needs its own solo shot (see lighter-touch alt). | **blocker** |
| **S8 dose "10-15 drops"** | `Sirf 10-15 drops.` | spoken (S12 tail, optional): `सिर्फ़ दस से पंद्रह बूँदें`; on-card text: `10–15` is fine as POST graphic | Hyphen `10-15` voiced as garbage if spoken (v5 dash rule). Spelled out in Devanagari when spoken; the numeric "10–15" only ever appears as POST card text, never voiced by Veo. | None. | major |
| **"BOOM!" / "Nahiiiiiii!" interjections** | `BOOM!` (S1, S6); `Nahiiiiiii!` (S8) | All → **POST SFX / visual energy bursts**, removed from spoken lines | Veo voices written SFX literally and mangles long-drawn screams; they also pollute the single-line-per-shot budget. | None — these are sound effects, and they hit harder as designed post audio over a visual blast. | major |
| **Discipline header** | (raw script has no AI-video rules) | Added rules 1–10 (one speaker/shot, narrated groups in HARD profile, good/evil reads, Devanagari, no dashes, laugh/SFX counts, ~20-word budget, no model-burned text + no quotes in prompt, label-deferred-to-card, soft claims) | Encodes every Veo 3.1 failure mode + the v5 produced-cut failures + this round's research as standing rules for the downstream gates. | None. | major (process) |

## Lighter-touch alternatives (if the human wants more of the raw banter back)
- **Keep more King taunts:** add up to 3 extra King-SOLO reaction micro-shots (4s each) between the
  hero intros (e.g. after Amla: `एक अकेला आया है मुझे हराने?`; after Saunf: `अभी भी मैं जीत रहा हूँ।`).
  Cost: +12s runtime and 3 more clips to generate (more spend), but restores the call-and-response.
  Still one mouth per shot — safe. **I recommend at most ONE extra** (after Amla) to keep pace tight.
- **Let the stomach SPEAK its happy line:** add a Stomach-SOLO 6s shot before S11 with
  `अब लग रहा है पेट हल्का है।` (to camera, happy). Cost: +6s and one clip; restores the raw S8 stomach
  beat as real dialogue instead of narrated joy. Safe (solo).
- **Tighten to ~50s:** drop v5-S2 (fold acidity/bloating into S1) and v5-S8 (King reaction). Cost:
  less villain texture; faster, more punch-forward edit.

---

## Deliberately kept (creative intent protected)
- **The whole story + comedic good-vs-evil arc:** villain torments stomach → 4 herb-heroes arrive
  → "we are more than 4" reveal → merge into one bottle → villain blasted, stomach happy. Untouched.
- **Every hero's identity line** ("मैं हूँ …" + what they do) — kept verbatim in meaning, only
  Latin→Devanagari + dash/`!`/ellipsis cleanup + Anglicism smoothing for pronunciation.
- **The "रुको ज़रा" and "अकेला नहीं" call-outs** — kept inside the heroes' own solo lines so the
  banter energy survives without a second mouth.
- **Haritaki's "game over bolne se pehle mujhe mat bhoolo"** swagger — kept (it is the best line),
  staged warm/kindly so he does not read as a second villain.
- **The "10+ herbs into one Ayurvedic Clear Gut Drops" payoff** and **"पेट हल्का, दिन हल्का" tagline** —
  kept verbatim; the tagline + dose + brand live pixel-perfect on the S12 real-product card.
- **Hinglish loanwords** (डाइजेशन, गट, ब्लोटिंग, एसिडिटी, कॉन्स्टिपेशन, नैचुरली, बैलेंस, ड्रॉप्स,
  गेम ओवर) — on-brand and natural for the audience, preserved in Devanagari/as-pronounced.
- **Soft Ayurvedic claims** ("डाइजेशन को सपोर्ट", "मदद करते हैं … दिक़्क़तों से") — no medical-cure
  language; the only "won't let your stomach clear" line is the villain's boast, which is safe.
- **{4, 6, 8}s legal durations, S12 real-bottle card, no model-burned text** — already correct, kept.

---

## Research delta (live, 2026-06-14) — what's new / confirmed vs the catalog
- **Subtitle leakage is real and frequent on dialogue clips** (~40% of dialogue output gets gibberish
  burned subtitles even when not asked). Mitigation: `no subtitles / no text` negative prompt + keep
  dialogue under 8s. → Confirms our label-on-S12-card-only discipline + the no-model-text rule.
  [MIT Technology Review](https://www.technologyreview.com/2025/07/15/1120156/googles-generative-video-model-veo-3-has-a-subtitles-problem/)
- **Multi-character dialogue: Veo mis-assigns the line to the wrong mouth**, and Google's OWN Veo 3.1
  guide says for 2+ characters you should describe **scene flow, not dialogue snippets** — i.e. there is
  no reliable way to prompt two simultaneous talkers. → Hard confirmation that EVERY two-talker beat
  must be split into solos or narrated (the core of this rewrite).
  [Google Cloud — Ultimate prompting guide for Veo 3.1](https://cloud.google.com/blog/products/ai-machine-learning/ultimate-prompting-guide-for-veo-3-1) ·
  [Skywork — 10 most common Veo 3.1 mistakes](https://skywork.ai/blog/veo-3-1-prompting-mistakes-fixes/)
- **Quotation marks as a subtitle trigger: sources conflict** — one Veo 3.1 dialogue guide uses quotes
  as the required format; another (Google-aligned) advises NOT using quotation marks because they "can
  trigger subtitles accidentally." Net: treat quotes as a possible leak trigger and keep them OUT of
  the prompt (a prompt-stage decision for the assistant-director, not a spoken-line change).
  [GlobalGPT — Veo 3.1 dialogue guide](https://www.glbgpt.com/hub/how-to-make-characters-speak-in-veo-3-1-the-ultimate-guide-to-dialogue-audio-lip-sync/) ·
  [Medium — Veo 3 dialogue format](https://medium.com/@kvxxpb/ive-been-using-veo-3-wrong-this-whole-time-dialogue-game-changer-cc51c9f61b05)
- **8s line budget confirmed:** "keep it to something sayable in ~8s; packing too much makes the
  character speak too fast." → Confirms the ~20-word/one-line-per-shot rule (drove the S1, S7-narrator
  and S8 splits).
  [Replicate — prompting Veo 3](https://replicate.com/blog/using-and-prompting-veo-3)
- Native lip-sync is real (single-pass, <120ms latency) but cartoon lip-sync stays APPROXIMATE and
  native voices can read robotic — matches our v5 fixlist BLOCKER #1 (lip-sync stays needs-human,
  shorter lines + speaker-dominant framing help, never auto-PASS).
  [ComputerTech — Veo 3.1 review](https://computertech.co/veo-3-1-review/)

---

## APPROVAL GATE
**APPROVE to hand to the assistant-director / tell me what to revise.**
(Specifically, please decide: (a) keep the King's per-hero taunts CUT, or restore ONE/some via the
4s King-SOLO micro-shots? (b) keep the stomach's happy line narrated, or give it its own SOLO speaking
shot? (c) target ~62s as written or tighten to ~50s? Nothing proceeds downstream until you approve.)
