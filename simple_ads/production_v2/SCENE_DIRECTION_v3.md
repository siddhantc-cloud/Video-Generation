# Clear Gut ad — DIRECTION v3 (logic + tone fix). DRAFT for approval — no generation yet.

## The core logic problem in v2, and the fix
v2 made the herb heroes look like villains (fierce/angry faces, same dark gut, snarling). They're the GOOD guys. Three character roles must be visually unmistakable:

| Role | Who | Look & expression | Lighting/grade |
|---|---|---|---|
| **VILLAIN** (only one) | Constipation King (+ unseen "friends" Acidity/Bloating) | gross, menacing, evil grin, glowing red eyes, looming, smug | dark, murky, sickly-green gas |
| **VICTIM** (sympathetic) | the Stomach | soft, cute, suffering→hopeful→joyful; reacts to each hero with RELIEF & gratitude | soft, caught between dark & light |
| **HEROES** (good guys) | Bhui Amla, Ajwain, Saunf, Haritaki | **warm, friendly, confident, brave — like friendly Pixar superheroes.** Kind eyes, reassuring smiles. Determined toward the King, WARM toward the stomach. NOT snarling/angry. | **bright, clean, warm golden/green glow — they bring LIGHT into the dark gut** |
| **PRODUCT** | Clear Gut bottle | the payoff; label must be perfect | radiant, clean, golden |

### The two rules that make good-vs-evil read instantly
1. **Expression rule:** heroes smile warm + confident (a hero can be brave/strong without looking evil). Reserve evil faces (red eyes, jagged grin, scowl) for the King ONLY. Each hero gives the stomach a reassuring look/thumbs-up — that single beat tells the audience "this one's on your side."
2. **Light rule:** every time a hero arrives, the gut gets BRIGHTER and warmer (hope arriving); the King's zone stays dark/green. Heroes glow; villain lurks.

## Product-fidelity rule (fixes the blank label)
- Pass the real `bible/bottle.png` (= clear_gut.png) as a reference into EVERY keyframe where the bottle appears (S7, S8) — done in keyframe, but Veo's motion blurred the label.
- In the Veo prompt for bottle scenes: *"the Clear Gut bottle stays perfectly still and sharp, exact BLUMELIFE 'Clear Gut' label fully legible, bottle does NOT morph or change."* Minimal bottle motion = label survives.
- **Guaranteed safety net:** end on a 1.5–2s clean PRODUCT CARD built from the real `clear_gut.png` still (Ken-Burns) — so the key brand moment is pixel-perfect regardless of what Veo does. (Optionally drop the real bottle as a composited overlay in S7/S8 if Veo still degrades it.)

## Revised scene-by-scene (blocking + tone + single speaker)
| # | Beat | Speaker | Tone/expression direction | Line (Devanagari) |
|---|---|---|---|---|
| 1 | Villain torments stomach | **King** | King menacing/evil; stomach scared, pleading | हाहाहा! मैं हूँ कॉन्स्टिपेशन किंग! तुम्हारा पेट मैं कभी साफ़ नहीं होने दूँगा! |
| 1b (optional tag) | stomach cries for help | Stomach | sympathetic, desperate | कोई है जो मेरी मदद कर सकता है? |
| 2 | **Amla** answers the call | **Amla** | warm BRAVE hero smile, glowing, reassuring nod to the stomach, confident point at King (not angry) | रुको ज़रा! मैं हूँ भुई आँवला! मैं डाइजेशन को नैचुरली सपोर्ट करता हूँ! |
| 3 | **Ajwain** joins | **Ajwain** | upbeat energetic friendly, playful confidence, gives stomach a wink/thumbs-up | अकेला नहीं! मैं हूँ अजवाइन! पेट की हेविनेस से लड़ने आया हूँ! |
| 4 | **Saunf** joins | **Saunf** | calm cool kind, gentle reassuring smile | और मैं हूँ सौंफ! ब्लोटिंग के ख़िलाफ़ मैं भी टीम में हूँ! |
| 5 | **Haritaki** arrives | **Haritaki** | wise warm GRANDFATHER-hero (powerful but kind, twinkling eyes — NOT angry monster), golden glow | मैं हूँ हरीतकी! आयुर्वेद की सबसे भरोसेमंद जड़ी-बूटियों में से एक! |
| 6 | Team reassures + turns on King | **Haritaki (leads)** | all four warm/heroic, smiling confidently, standing protectively in front of the stomach; King shrinks | घबराओ मत! अब हम तुम्हारे साथ हैं! |
| 7 | Herbs unite → bottle | **Narrator (VO)** | bright, magical, uplifting; bottle PERFECT & still | दस से ज़्यादा आयुर्वेदिक जड़ी-बूटियों की ताक़त, अब एक ही क्लियर गट ड्रॉप में। |
| 8 | Healthy stomach + product | **Narrator (VO)** | joyful, bright; PRODUCT CARD with perfect label | सिर्फ़ दस-पंद्रह ड्रॉप्स, सुबह और रात। पेट हल्का, दिन हल्का! |
| 9 | Clean product card (still) | — | real `clear_gut.png`, Ken-Burns, optional logo/CTA text | (silent or hold narrator tail) |

### Notes
- Hindi tweaks: "help" → "मदद" (S1b), "trusted herbs" → "भरोसेमंद जड़ी-बूटियों", "power" → "ताक़त" (cleaner spoken Hindi than English loanwords where natural).
- What gets regenerated: the 4 hero keyframes + Haritaki/team (S2–S6) with the WARM-HERO expression + bright glow; S1 (villain) is already right; S7/S8 re-done with the bottle-lock prompt + add the product end-card (S9).
- Everything else (speaker-focus framing, colon dialogue, half-second pause, no-subtitles, crossfade assembly) stays — it works.
