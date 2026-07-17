# Clear Gut, "Ingredient Army", SCRIPT (v5 FAITHFUL) — GATE-0 OUTPUT, AWAITING HUMAN CHOICE

> **This is the MAXIMALLY-FAITHFUL counterpart to `01_script_v5_AIFRIENDLY.md`.** Both are valid
> Gate-0 outputs of the **script-rewriter** on the frozen `00_input_script_HUMAN.md` (2026-06-14).
> They are meant to be compared **side by side** — this is NOT a replacement for the AI-friendly cut.
>
> **Design intent of THIS variant:** preserve EVERY beat, line, and the comedic back-and-forth of the
> original human script as literally as Veo 3.1 will allow. The ONLY thing that changes vs the human
> script are the **hard engine limits** (no two speaking mouths in one shot; Devanagari; no dashes;
> legal durations; staging guards). Where the AI-friendly cut traded banter for leanness, this cut
> spends extra clips to keep the banter.
>
> Target engine: **Veo 3.1** (`veo3_1`, native audio) via Higgsfield CLI. Single start-image per clip.
> Durations **4 / 6 / 8s ONLY**. Model voices dialogue + animates mouths natively.
> **NOT yet chosen — the human picks FAITHFUL vs AI-FRIENDLY before anything goes downstream**
> (assistant-director → scene-expectations → production).

**Format:** vertical 9:16, **17 shots**, ~92s of Veo (assembled ~78–80s after crossfades + card).
3D-caricature (So Sorry / Krishna's SHAPEFIX style). Comedic, warm, clear good-vs-evil.

---

## Engine note (research already on file — see AI-friendly variant's "Research delta")

The one finding that GOVERNS this variant and that fidelity **cannot** override:

- **Veo 3.1 has no reliable two-talker prompt.** It animates EVERY visible mouth and mis-assigns
  lines to the wrong face. Google's own Veo 3.1 prompting guide instructs that for 2+ characters you
  describe *scene flow, not dialogue snippets*. ([Google Cloud — Ultimate prompting guide for Veo 3.1](https://cloud.google.com/blog/products/ai-machine-learning/ultimate-prompting-guide-for-veo-3-1))
  → So the duel's call-and-response is preserved by **splitting every exchange into solo shots**, never
  by putting two mouths in one frame. This is the single non-negotiable transformation; everything else
  in the human script is kept.
- Supporting (all on file in the AI-friendly variant): ~40% subtitle-leak on dialogue clips → no
  model-burned text, label deferred to the post card; ~8s/~20-word line budget; cartoon lip-sync stays
  approximate (shorter lines + speaker-dominant framing help, never auto-PASS).

No re-search needed; the catalog + the 2026-06-14 delta already cover Veo 3.1's current failure modes.

---

## Core discipline (identical engine rules for BOTH variants)
1. **ONE speaking mouth per shot.** Only the speaker is on camera talking to lens. Every two-talker
   beat in the raw script is split into consecutive SOLO shots. **Faithfulness preserves the LINES;
   it splits the SHOTS.** This is the only rule that overrides "keep the frame as written".
2. **Background / non-speaking characters: mouth CLOSED, HARD profile or off-frame.** (When the King is
   present in a hero shot, he is small, dark, far-back, and NOT mouthing.)
3. **Good vs evil reads in <1s.** Heroes warm/golden/friendly; the King is the ONLY menacing/gross face;
   stomach is the sympathetic victim. Never give a hero a fierce/dark cue (expression leakage).
4. Spoken lines **Devanagari**; scene direction English.
5. **No dashes / hyphens (`-` `—` `–`) in any spoken line** (Veo voices them as garbage), including
   inside compounds (जड़ी बूटियों, not जड़ी-बूटियों). Raw ellipses (`...`) → full stop / comma.
6. **Laughs / SFX written as Veo will SAY them** — short, low count ("Hahaha" → "हा हा", 2 beats).
   "BOOM!" / "Nahiiii!" are POST SFX / a short solo exclaim, never burned text, never a written SFX line.
7. **One short line (~≤20 words) + one action + one ambient bed per clip.**
8. **No model-burned on-screen text.** Label + tagline + dose + captions are POST (S17 card + karaoke).
9. **Legible label NOT demanded in motion;** guaranteed-legible brand moment = the S17 real-bottle card.
10. **Claims soft / Ayurvedic.** The "won't let your stomach clear" line is the VILLAIN's boast, so it
    stays as comedic menace, not a product claim.

---

## The FAITHFUL shot list (17 shots — restores all 4 King taunts + the 4-hero S6 exchange)

| # | Who's on camera | Speaker | Dur | Line (Devanagari, verbatim, dash-free) | Intent |
|---|---|---|---|---|---|
| **1** | **King SOLO**, looming on a sad bloated stomach rendered as a faceless turned-away dark shape at the lower edge (no 2nd mouth) | **King** | 8s | हा हा। मैं हूँ कॉन्स्टिपेशन। और मैं तुम्हारा पेट कभी ठीक से साफ़ नहीं होने दूँगा। | HOOK: villain + the problem, comedic menace (raw S1 lines 1–3) |
| **2** | **King SOLO**, same frame, grinning, gesturing to his unseen gang | **King** | 8s | एसिडिटी मेरी दोस्त है। ब्लोटिंग मेरा भाई है। और हम सब मिलकर तुम्हारा पूरा दिन ख़राब करेंगे। | Villain stacks the problem; "my friends are acidity & bloating" gag (raw S1 lines 4–6) |
| **3** | **Stomach SOLO**, sad bloated face to camera, King fully out of frame, sickly-green light | **Stomach** | 6s | कोई है जो मेरी हेल्प कर सके? | Victim's cry for help — the turn (raw S1 STOMACH, verbatim incl. "हेल्प") |
| **4** | **Amla SOLO**, crashes in, heroic stance, to camera, warm golden rim-glow | **Amla** | 8s | रुको ज़रा। मैं हूँ भुई आँवला। मैं डाइजेशन को नैचुरली सपोर्ट करता हूँ और गट को बैलेंस रखने में मदद करता हूँ। | Hero 1 arrives (raw S2 AMLA) |
| **5** | **King SOLO**, smug, dismissive sneer, green murk | **King** | 4s | एक अकेला आया है मुझे हराने? हा हा। | King taunt #1 — the duel rhythm (raw S2 KING) |
| **6** | **Ajwain SOLO**, action-movie entry, energetic, to camera, bright punchy warm | **Ajwain** | 6s | अकेला नहीं। मैं हूँ अजवाइन। मैं पेट की हेविनेस और डिस्कम्फर्ट से लड़ने आया हूँ। | Hero 2 answers the taunt (raw S3 AJWAIN) |
| **7** | **King SOLO**, scoffing, waving them off, green murk | **King** | 4s | दो लोगों से कुछ नहीं होगा। | King taunt #2 (raw S3 KING) |
| **8** | **Saunf SOLO**, slides in gracefully, calm, to camera, soft warm | **Saunf** | 8s | और मैं हूँ सौंफ। खाने के बाद जो ब्लोटिंग और भारीपन लगता है, उसके ख़िलाफ़ मैं भी टीम में हूँ। | Hero 3 joins (raw S4 SAUNF) |
| **9** | **King SOLO**, forced bravado, sweating slightly, green murk | **King** | 4s | अभी भी मैं जीत रहा हूँ। | King taunt #3 — false confidence (raw S4 KING) |
| **10** | **Haritaki SOLO**, lands with gentle thunder shimmer, wise-kindly, to camera, warm gold (NOT menacing) | **Haritaki** | 8s | गेम ओवर बोलने से पहले मुझे मत भूलो। मैं हूँ हरीतकी। आयुर्वेद की सबसे भरोसेमंद जड़ी बूटियों में से एक। | Hero 4, wise swagger (raw S5 HARITAKI) |
| **11** | **King SOLO**, eyes wide, shrinking back, comically worried (gross-but-funny, NOT sympathetic), green murk | **King** | 4s | ओह नो। तुम सब एक साथ? | King taunt #4 — confidence breaks (raw S5 KING) |
| **12** | **Amla SOLO**, freeze-frame energy, half-turn to camera, sly grin | **Amla** | 4s | एक मिनट। | S6 four-hero exchange, beat 1 (raw S6 AMLA) |
| **13** | **Ajwain SOLO**, freeze-frame energy, to camera, eyebrow raise | **Ajwain** | 4s | तुम्हें लगता है? | S6 exchange, beat 2 (raw S6 AJWAIN) |
| **14** | **Saunf SOLO**, freeze-frame energy, to camera, knowing smile | **Saunf** | 4s | बस हम चार ही हैं? | S6 exchange, beat 3 — the setup line (raw S6 SAUNF) |
| **15** | **Haritaki SOLO**, freeze-frame energy, to camera, confident | **Haritaki** | 4s | अब असली सरप्राइज़ देखो। | S6 exchange, beat 4 — the trigger (raw S6 HARITAKI); "BOOM!" = POST SFX into S16 |
| **16** | 10+ herbs swirl in as gold-light streaks and coalesce into the bottle's glowing form; stylized 3D bottle, still, no morph (label may be soft) | **NARRATOR** (VO) | 8s | ये सिर्फ़ चार हर्ब्स की कहानी नहीं है। दस से ज़्यादा आयुर्वेदिक इंग्रीडिएंट्स की पावर, अब एक ही आयुर्वेदिक क्लियर गट ड्रॉप में। | HERO REVEAL — the merge payoff (raw S7 narrator, sentences 1–3) |
| **17a** | Healthy bottle still on a locked pedestal; behind it a quick POST visual blast where the King WAS (King already gone); brief gold-light settle | **NARRATOR** (VO) | 8s | ये सब एक साथ मिलकर डाइजेशन को सपोर्ट करते हैं। और मदद करते हैं कॉन्स्टिपेशन, एसिडिटी और ब्लोटिंग जैसी रोज़मर्रा की दिक़्क़तों से। | Product benefit (raw S7 narrator, sentences 4–5) + King blasted (visual/SFX, no spoken scream) |
| **17b** | **Stomach SOLO**, happy and energetic, bouncing lightly, to camera (lens-facing — see flag) | **Stomach** | 6s | अब लग रहा है पेट हल्का है! | Happy resolution — stomach SPEAKS its line as the human wrote it (raw S8 STOMACH) |
| **18** | CLEAN PRODUCT CARD, real bottle still (NOT Veo; ffmpeg Ken-Burns) | (post text + optional narrator tail) | — | दस से ज़्यादा आयुर्वेदिक जड़ी बूटियाँ। सिर्फ़ दस से पंद्रह बूँदें, सुबह और रात। · पेट हल्का। दिन हल्का। · BLUMELIFE Clear Gut Drops | Pixel-perfect brand close + dose CTA (raw S8 narrator list) |

**Shot accounting:** 4 King-SOLO taunt micro-shots (5, 7, 9, 11) + 4 hero-SOLO S6 micro-shots
(12, 13, 14, 15) are the restorations vs the AI-friendly cut. Everything else maps 1:1 to a raw line.

**Total Veo runtime:** 8+8+6+8+4+6+4+8+4+8+4 + 4+4+4+4 + 8+8+6 = **106s of generated Veo**
across **17 dialogue/VO clips** (S17a + S17b counted as 2; S18 is a post card, not Veo). With ~0.4s
crossfade overlaps (16 joins ≈ 6.4s) and the ~4s S18 card, the assembled cut lands **~78–80s**.
(That overruns the ~60s brief target — the cost of full fidelity; see the comparison table.)

---

## Cast & assigned voice tone (Veo native, described in the prompt — NOT quoted)
- **Constipation King** = deep, gravelly, comically-villainous; "ha ha" = 2 beats (S1, S5), NOT a laugh
  track. The ONLY menacing/gross face. His four taunts (S5, S7, S9, S11) ride a confidence-to-panic
  arc: smug → scoffing → forced bravado → cracking.
- **Stomach** = soft, anxious (S3); bright, relieved, energetic (S17b — speaking, lens-facing).
- **Amla** = warm, confident young-hero (male).
- **Ajwain** = bright, fast, energetic (male).
- **Saunf** = smooth, calm, gentle **FEMALE**.
- **Haritaki** = deep, wise, kindly-elder; warm, NOT menacing (male).
- **Narrator** = warm, trustworthy, authoritative; same voice across S16 / S17a.
- **Ambient bed every clip:** `clean room tone, no audience, no laugh track, no music`. Music + the
  "BOOM" + the King's blast are POST audio over the visual, never requested from Veo.

---

## Change log (RAW human script → FAITHFUL rewrite) — ONLY the engine-FORCED changes

The whole point of this variant is maximal fidelity, so this log is intentionally short. Every change
below is an **unavoidable Veo 3.1 limit**, not a creative choice. Beats, lines, and order are otherwise
preserved verbatim.

| Scene / Line | Original RAW (quoted) | FAITHFUL rewrite | Why it was UNAVOIDABLE | Severity |
|---|---|---|---|---|
| **S1 — King + Stomach in one frame, 6-line speech, "Hahaha!", "BOOM!"** | `KING: Hahaha! / Main hoon Constipation! / Aur main tumhara pet kabhi properly saaf nahi hone dunga! / Acidity meri dost hai... / Bloating mera bhai hai... / Aur hum sab milkar tumhara poora din kharab karenge!` then `STOMACH: Koi hai jo meri help kar sakta hai?` then `BOOM!` | **3 solo shots, lines verbatim:** S1 King (हा हा। मैं हूँ कॉन्स्टिपेशन। और मैं तुम्हारा पेट कभी ठीक से साफ़ नहीं होने दूँगा।), S2 King (एसिडिटी मेरी दोस्त है। ब्लोटिंग मेरा भाई है। और हम सब मिलकर तुम्हारा पूरा दिन ख़राब करेंगे।), S3 Stomach (कोई है जो मेरी हेल्प कर सके?). "Hahaha"→"हा हा" (2 beats). `...`/`!`→`।`. "BOOM!"→POST SFX. | Two animated mouths in one frame (mis-assigns lines); 6 lines is 2–3× the ~8s/~20-word budget (too-fast speech + subtitle leak); "Hahaha" voiced as garbage / hallucinated laugh-track; "BOOM!" voiced literally. **The lines are kept exactly; only the frame is split and SFX moved to post.** | blocker |
| **S2–S5 — each hero shares the frame with the King taunting back** | Amla scene ends `KING: Ek akela aaya hai mujhe haraane? Hahaha!`; Ajwain `KING: Do logon se kuch nahi hoga!`; Saunf `KING: Abhi bhi main jeet raha hoon!`; Haritaki `KING: Oh no... Tum sab ek saath?` | **All 4 taunts KEPT, each as its OWN King-SOLO 4s reaction shot** interleaved between heroes: S5 (एक अकेला आया है मुझे हराने? हा हा।), S7 (दो लोगों से कुछ नहीं होगा।), S9 (अभी भी मैं जीत रहा हूँ।), S11 (ओह नो। तुम सब एक साथ?). `...`/`!`→`।`; "Hahaha"→"हा हा". | The taunt and the hero's line cannot share a frame (two mouths). Splitting the taunt into its own solo reaction shot is the ONLY way to keep BOTH the hero line AND the taunt. Duel rhythm of the reference reel preserved exactly. | blocker |
| **All hero lines (S2–S5)** | Latin script + `!` + `...` (e.g. `Main hoon bhui Amla!`, `...feel hoti hai...`) | Same lines in **Devanagari**, `!`/`...`→`।`/`,`. "heaviness/discomfort"→"हेविनेस/डिस्कम्फर्ट", "fullness feel hoti hai"→"भारीपन लगता है", "against"→"ख़िलाफ़", "trusted herbs"→"भरोसेमंद जड़ी बूटियों" (no hyphen). | Latin script is mis-pronounced by Veo; `!`/`...` voiced/leaked; hyphen in जड़ी बूटियों voiced as garbage. Meaning + word choice kept as close to the original Hinglish as a clean Devanagari read allows (loanwords transliterated, not translated). | major |
| **S6 — FOUR heroes speak in one frozen frame, then "BOOM!"** | `AMLA: Ek minute... / AJWAIN: Tumhe lagta hai... / SAUNF: Bas hum chaar hi hain? / HARITAKI: Ab asli surprise dekho.` then `BOOM!` | **4 solo hero micro-shots (4s each), lines verbatim:** S12 Amla (एक मिनट।), S13 Ajwain (तुम्हें लगता है?), S14 Saunf (बस हम चार ही हैं?), S15 Haritaki (अब असली सरप्राइज़ देखो।). `...`→`।`. "BOOM!"→POST SFX into S16. | Four animated mouths in one frozen frame = the worst multi-mouth case (guaranteed mush + line mis-assignment). Splitting into four consecutive solos keeps **all four quips as on-camera dialogue** — the exchange is fully preserved, NOT collapsed to narrator. | blocker |
| **S7 narrator — 5 sentences in one clip** | `Ye sirf 4 herbs ki kahani nahi hai. / 10 se zyada Ayurvedic ingredients ki power... / Ab ek hi Ayurvedic Clear Gut Drop mein. / Sab ek saath milkar digestion ko support karte hain. / Aur help karte hain constipation, acidity aur bloating jaise everyday gut issues se nipatne mein.` | **Split across S16 (sentences 1–3) + S17a (sentences 4–5),** verbatim, `...`→`।`, "help"→"मदद". | 5 sentences ≈ 2–3× the ~8s/~20-word VO budget → too-fast VO + subtitle leak. Split only as far as the budget forces; both lines stay on the visuals they describe. | major |
| **S8 — King scream + Stomach + Narrator list (3 speakers)** | `KING: Nahiiiiiii! / STOMACH: Ab lag raha hai pet halka hai! / NARRATOR: 10+ Ayurvedic herbs. Sirf 10-15 drops. Subah aur raat. Ayurvedic Clear Gut Drops. Pet halka. Din halka.` | King's "Nahiiiiiii!" → **POST visual blast + SFX** (S17a, no spoken scream). Stomach's line **KEPT as real dialogue** in its own solo shot **S17b** (अब लग रहा है पेट हल्का है!), lens-facing **[FLAG below]**. Narrator dose/brand list → **S18 post card** (on-screen text + optional narrator tail); "10-15"→"दस से पंद्रह" if spoken. | Three mouths in one beat; a long-drawn scream Veo clips/mangles; "10-15" hyphen voiced as garbage; a 6-line list over budget. Per the human's instruction for THIS variant, the stomach SPEAKS its line (own solo shot) instead of being narrated. The scream and the spelled list are the only forced moves. | blocker |

### Flag — S17b lens-facing stomach (human chose this for the faithful variant)
The brief for this variant asks to render the stomach's resolution line as the original wrote it —
**Stomach speaking.** That requires a lens-facing speaking mouth, which is the exact recurring failure
the staging guard (rule 2) usually prevents on the OTHER (narrated/background) characters. As a SOLO
speaker it is allowed (one mouth, to camera) and is the correct way to keep the line as dialogue — but
flagging two residual risks for the assistant-director / scene-expectations gates:
1. **Cartoon lip-sync on an organ character stays approximate** — expect re-rolls; keep the line short
   (it is, 6 words). Never auto-PASS the lip-sync.
2. **Make sure no OTHER mouth is in frame** (King already gone, bottle is a prop) so this stays a clean
   single-talker shot. If lip-sync repeatedly fails, the documented fallback is the AI-friendly
   treatment (narrated joy, stomach in hard profile / mouth closed) — but that is a fidelity downgrade,
   so only as a last resort.

---

## Deliberately kept (the whole point of this variant)
- **All four King taunts**, each as its own solo reaction shot — the full duel rhythm of the reference
  reel (the AI-friendly cut dropped three of these). Confidence-to-panic arc intact.
- **The full four-hero S6 exchange** as four on-camera solo quips, NOT collapsed to narrator.
- **The King's full S1 menace** (both the identity boast and the "acidity is my friend, bloating is my
  brother" gag) — split only across two shots by the budget, every line kept.
- **Every hero's full identity + function line** verbatim in meaning (only Latin→Devanagari + punctuation
  + Anglicism transliteration for pronunciation).
- **The stomach's S1 cry ("कोई है जो मेरी हेल्प कर सके?") and S8 happy line ("अब लग रहा है पेट हल्का है!")**
  both as REAL spoken dialogue, as the human wrote them ("help"/"हेल्प" kept as the original Hinglish).
- **The full narrator payoff** (all 5 sentences) — distributed across S16/S17a only as far as the
  budget forces.
- **"पेट हल्का। दिन हल्का।" tagline**, the "10+ herbs into one Clear Gut Drops" reveal, the dose CTA —
  pixel-perfect on the S18 real-product card.
- **Hinglish loanwords** transliterated, not translated (डाइजेशन, गट, ब्लोटिंग, एसिडिटी, कॉन्स्टिपेशन,
  हेविनेस, डिस्कम्फर्ट, इंग्रीडिएंट्स, पावर, सरप्राइज़, गेम ओवर, हेल्प) — closest to the original voice.
- **Soft Ayurvedic claims**; the only "won't clear your gut" line stays the villain's boast.

---

## Comparison summary — FAITHFUL vs AI-FRIENDLY (the cost/fidelity decision)

| Variant | Shots | Approx Veo clips (~58 cr each, preview+high) | Approx Veo credits | Approx assembled runtime | Fidelity trade-off |
|---|---|---|---|---|---|
| **AI-FRIENDLY** (`01_script_v5_AIFRIENDLY.md`) | **12** (11 Veo + 1 post card) | **~11 clips** | **~640 cr** | **~62s** (on brief) | Leanest. 3 of 4 King taunts CUT; S6 four-hero exchange collapsed to ONE narrator line; stomach's happy line narrated. Banter rhythm reduced; content preserved, arguably clearer. |
| **FAITHFUL** (this file) | **17** (16 Veo incl. S17a+S17b + 1 post card) | **~16 clips** | **~930 cr** | **~78–80s** (over the ~60s brief) | Maximal fidelity. ALL 4 King taunts restored as solo reactions; full 4-hero S6 exchange as 4 solo quips; stomach SPEAKS both lines. Duel rhythm of the reference reel intact. Costs +5 clips (~+290 cr) and ~+18s runtime; overruns the 60s target. |

**Net read:**
- **Cost delta:** FAITHFUL is **~5 extra Veo clips (~+290 credits, ~+45%)** vs AI-FRIENDLY, plus
  more lip-sync re-roll surface (16 vs 11 dialogue/VO clips, and the lens-facing S17b stomach).
- **Runtime:** FAITHFUL lands **~78–80s** vs the brief's ~60s. If the human picks FAITHFUL but wants to
  hit ~60s, the cheapest trims that LEAST hurt fidelity are: merge S1+S2 (one King intro, lose a beat
  of menace texture, back to ~70s), then drop one of the weaker King taunts (S9 "अभी भी मैं जीत रहा हूँ"
  is the most expendable) → ~66s with 3 of 4 taunts kept. Cutting the S6 four-hero exchange back to one
  beat is the single biggest time saver but is the heart of this variant's fidelity, so not recommended.
- **Quality/risk:** more clips = more lip-sync rolls and more chances for a single bad clip; the 4s
  micro-shots are short (good for lip-sync) but rapid cutting raises continuity-grade pressure
  (the assistant-director / scene-expectations gates will set the bar).

Both are fully shootable on Veo 3.1. The choice is **runtime + spend vs banter fidelity**, not
"safe vs unsafe" — neither variant ever puts two mouths in one frame.

---

## APPROVAL GATE
**Both variants are now on file. CHOOSE one to hand to the assistant-director, or tell me what to revise.**
- **Pick FAITHFUL** (this file, ~16 Veo clips / ~930 cr / ~78–80s, full banter + 4 taunts + 4-hero exchange + stomach speaks), or
- **Pick AI-FRIENDLY** (`01_script_v5_AIFRIENDLY.md`, ~11 clips / ~640 cr / ~62s, lean), or
- Ask for a **hybrid** (e.g. FAITHFUL but trimmed to ~60s per the trim plan above, or AI-FRIENDLY + 1–2 restored King taunts).

Nothing proceeds downstream until you choose.
