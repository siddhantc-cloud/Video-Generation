# Clear Gut, "Ingredient Army" — PROMPTS (v5 FAITHFUL variant)

> Per-scene generation prompts for the **FAITHFUL** cut (`01_script_v5_FAITHFUL.md`).
> 17 Veo shots (S1–S17; S17 split into S17a + S17b) + S18 final product card (ffmpeg, NO Veo).
> Restores all 4 King taunts as King-SOLO shots, the 4-hero "एक मिनट…" exchange as 4 solo hero
> shots, and the Stomach SPEAKS its resolution line (S17b, dialogue shot).
> Spoken Devanagari lines are copied VERBATIM from the script — never reworded, never quoted.
> AUTHORED ONLY. Nothing generated here. No API/CLI/MCP calls, no spend.

Refs live in `bible/` (king, amla, ajwain, saunf, haritaki, stomach, bottle) and `assets/clear_gut_product.png`.

Shared keyframe style suffix `[ST]`:
`Glossy 3D Pixar/DreamWorks-caricature style, cinematic rim lighting, vibrant, vertical 9:16. ABSOLUTELY NO TEXT, no letters, no captions.`

Shared veo negatives/ambient suffix `[NEG]`:
`Ambient: faint gut room-tone, no music, no audience, no laugh track. Glossy 3D cartoon animation. no subtitles, no captions, no on-screen text.`

Rules baked in: colon dialogue · "natural lip sync" · "line begins after a half-second pause" · ONE speaker per dialogue shot, mouth-guard appended · narrated shots say "no character moves their mouth, all mouths closed" with background characters in HARD profile / mouths closed / turned away · Devanagari verbatim, NEVER in quotes · King taunts ride a confidence→panic arc · Haritaki WARM (kind eyes, golden light), never menacing · bottle is a STYLIZED 3D cartoon bottle (real ref = shape/color/label-colorway only), still, no morph · "BOOM!" / the King's scream are POST SFX, never in any dialogue block.

---

## Keyframe prompts (`nano_banana_2`, 9:16, 2k)

### S1 — King (ref: king, stomach)  ·  AD-fix: stomach = faceless turned-away dark shape (no 2nd renderable mouth); comedic-gross not horror
`Low-angle: the comically gross CONSTIPATION KING (image 1) looms large upper-center with a goofy-evil grin and comically glowing eyes; in the lower foreground a sad bloated stomach appears ONLY as a dim turned-away dark silhouette at the lower frame edge (its face NOT visible). Dark gut-cave, thick sickly-green gas, hard top-light on the King. Comically menacing, filter-safe. [ST]`

### S2 — King (ref: king, stomach)  ·  reuse S1 staging; King now grinning wider, gesturing to an unseen gang
`Low-angle: the comically gross CONSTIPATION KING (image 1) looms large upper-center, grinning wider and gesturing one hand outward to an unseen gang off-frame; the same sad bloated stomach is ONLY a dim turned-away dark silhouette at the lower frame edge (face NOT visible). Dark gut-cave, thick sickly-green gas, hard top-light on the King. Comically menacing, filter-safe. [ST]`

### S3 — Stomach SOLO (ref: stomach)  ·  King fully out of frame; sympathetic victim, sickly-green light
`Medium close-up: the pink STOMACH (image 1) ALONE, centered, a sad bloated worried face turned to camera with pleading eyes, slightly hunched. The Constipation King is completely OUT of frame. Sickly-green gut light, lonely and gloomy. Only this one character in frame, sympathetic and sad. [ST]`

### S4 — Amla SOLO (ref: amla)  ·  heroic arrival, bright warm — NOT menacing
`Medium close-up character hero shot: the green gooseberry hero BHUI AMLA (image 1) ALONE, centered, crashing in mid-stride into a confident FRIENDLY heroic stance, facing camera with a warm smile and kind brave eyes. Bright warm golden rim-glow surrounds the hero (a good guy bringing light). Soft glowing clean gut background. Only this one character in frame. [ST]`

### S5 — King (ref: king)  ·  TAUNT #1, smug/dismissive sneer, green murk
`Medium close-up: the comically gross CONSTIPATION KING (image 1) ALONE, centered, leaning back with a smug dismissive sneer and a goofy-evil grin, one eyebrow cocked. Dark green murk around him, hard top-light. Only this one character in frame, comically menacing, filter-safe. [ST]`

### S6 — Ajwain SOLO (ref: ajwain)  ·  action-movie entry, energetic, bright punchy warm
`Medium close-up character hero shot: the carom-seed hero AJWAIN (image 1) ALONE, centered, bursting in with an energetic action-movie entry pose, facing camera with a bright confident friendly grin and kind brave eyes. Bright warm punchy golden rim-glow. Soft glowing clean gut background. Only this one character in frame. [ST]`

### S7 — King (ref: king)  ·  TAUNT #2, scoffing/waving them off, green murk
`Medium close-up: the comically gross CONSTIPATION KING (image 1) ALONE, centered, scoffing and waving one hand dismissively, goofy-evil grin. Dark green murk around him, hard top-light. Only this one character in frame, comically menacing, filter-safe. [ST]`

### S8 — Saunf SOLO (ref: saunf)  ·  slides in gracefully, calm, soft warm
`Medium close-up character hero shot: the fennel hero SAUNF (image 1) ALONE, centered, sliding in gracefully into a calm composed stance, facing camera with a gentle warm smile and kind eyes. Bright soft warm golden glow. Soft glowing clean gut background. Only this one character in frame. [ST]`

### S9 — King (ref: king)  ·  TAUNT #3, forced bravado, faintly sweating, green murk
`Medium close-up: the comically gross CONSTIPATION KING (image 1) ALONE, centered, puffing his chest in forced bravado with a strained grin and one faint sweat-bead, eyes a little less sure. Dark green murk around him, hard top-light. Only this one character in frame, comically menacing, filter-safe. [ST]`

### S10 — Haritaki SOLO (ref: haritaki)  ·  wise kindly elder, WARM gold, gentle thunder shimmer (NOT menacing)
`Medium close-up character hero shot: the wise myrobalan elder-hero HARITAKI (image 1) ALONE, centered, landing with calm gentle authority, facing camera with kind twinkling eyes and a warm grandfatherly smile, clearly a benevolent good guy. Bathed in WARM GOLDEN light with a gentle golden thunder shimmer around him (powerful but warm, NOT an angry monster, NOT menacing). Soft glowing clean gut background. Only this one character in frame. [ST]`

### S11 — King (ref: king)  ·  TAUNT #4, confidence BREAKS, eyes wide, shrinking back, green murk
`Medium close-up: the comically gross CONSTIPATION KING (image 1) ALONE, centered, eyes comically wide, shrinking back with a worried open-mouthed gulp (gross-but-funny, NOT sympathetic, still the villain). Dark green murk around him, hard top-light. Only this one character in frame, comically menacing, filter-safe. [ST]`

### S12 — Amla SOLO (ref: amla)  ·  S6-exchange beat 1, freeze-frame energy, half-turn to camera, sly grin
`Medium close-up character hero shot: the green gooseberry hero BHUI AMLA (image 1) ALONE, centered, frozen mid-action with a half-turn toward camera and a sly confident grin, kind brave eyes. Bright warm golden rim-glow, dynamic freeze-frame energy. Soft glowing clean gut background. Only this one character in frame. [ST]`

### S13 — Ajwain SOLO (ref: ajwain)  ·  S6-exchange beat 2, freeze-frame energy, to camera, eyebrow raise
`Medium close-up character hero shot: the carom-seed hero AJWAIN (image 1) ALONE, centered, frozen mid-action facing camera with a playful raised eyebrow and a bright confident grin, kind brave eyes. Bright warm punchy golden rim-glow, dynamic freeze-frame energy. Soft glowing clean gut background. Only this one character in frame. [ST]`

### S14 — Saunf SOLO (ref: saunf)  ·  S6-exchange beat 3, freeze-frame energy, to camera, knowing smile
`Medium close-up character hero shot: the fennel hero SAUNF (image 1) ALONE, centered, frozen mid-action facing camera with a calm knowing smile and kind eyes. Bright soft warm golden glow, dynamic freeze-frame energy. Soft glowing clean gut background. Only this one character in frame. [ST]`

### S15 — Haritaki SOLO (ref: haritaki)  ·  S6-exchange beat 4, freeze-frame energy, to camera, confident, WARM gold (NOT menacing)
`Medium close-up character hero shot: the wise myrobalan elder-hero HARITAKI (image 1) ALONE, centered, frozen mid-action facing camera with a confident warm grandfatherly smile and kind twinkling eyes, clearly a benevolent good guy. Bathed in WARM GOLDEN light with a gentle golden shimmer (powerful but warm, NOT menacing). Dynamic freeze-frame energy, soft glowing clean gut background. Only this one character in frame. [ST]`

### S16 — product reveal / merge (ref: bottle, clear_gut_product)  ·  AD-fix: STYLIZED 3D cartoon bottle matching the world; label may be soft; legible payoff lives on S18 card
`Centered: more than ten glowing Ayurvedic herbs swirl in as streaks of golden light and coalesce into ONE radiant amber glass dropper bottle of Clear Gut, rendered as a GLOSSY 3D CARICATURE bottle that matches this cartoon world (use image 1 bottle ref and image 2 product ref for bottle SHAPE, amber color and yellow label COLORWAY only — stylize it; the label text need not be perfectly legible here), standing heroic and glowing on a clean pedestal, triumphant golden rays, magical reveal. No characters. Bottle still, no morph. [ST]`

### S17a — product benefit / King blasted (ref: bottle, clear_gut_product)  ·  AD-fix: King already GONE; just a settling gold-light blast where he was; bottle locked & sharp
`Centered: the healthy amber Clear Gut dropper bottle (image 1 bottle ref / image 2 product ref, match closely, label sharp) stands glowing on a locked pedestal; behind it, a soft settling burst of golden light marks the empty dark-green corner where the Constipation King WAS (the King is already GONE, NOT in frame). Warm clean bright gut, triumphant. No characters, bottle still and steady, no morph. [ST]`

### S17b — Stomach SOLO (ref: stomach)  ·  resolution: Stomach SPEAKS; happy/healthy, lens-facing (flagged); no other mouth in frame
`Medium close-up: the pink STOMACH (image 1) ALONE, now HAPPY, bright and healthy, bouncing lightly with a big joyful smile facing camera. Warm clean bright healthy gut light. The King is gone and no bottle or other character is in frame. Only this one character in frame, uplifting and cheerful. [ST]`

### S18 — product card (NO generation; ffmpeg)
Use `assets/clear_gut_product.png` directly with Ken-Burns + burned tagline / dose / brand. No model call — guarantees a pixel-perfect, legible label. See the ffmpeg entry under the Veo section.

---

## Veo prompts (`veo3_1 --image <keyframe> --duration <d> --aspect_ratio 9:16 --quality high`)

### S1, King (keyframe: s1)  ·  --duration 8  ·  AD-fix: stomach = faceless silhouette (no 2nd mouth); comedic-menace, filter-safe
`Medium low-angle shot. The comically gross Constipation King looms over a sad bloated stomach seen ONLY as a dim turned-away dark silhouette at the lower frame edge (its face NOT visible, NOT talking). The camera slowly pushes in on the King. The King looks at the camera and says in a deep gravelly, comically-villainous Hindi voice, natural lip sync, line begins after a half-second pause: हा हा। मैं हूँ कॉन्स्टिपेशन। और मैं तुम्हारा पेट कभी ठीक से साफ़ नहीं होने दूँगा। Only the King speaks and only the King's mouth moves; the stomach silhouette is faceless, has no visible mouth and stays silent and still; no other mouth is in frame. [NEG]`

### S2, King (keyframe: s2)  ·  --duration 8  ·  stacks the problem, "acidity is my friend, bloating is my brother" gag
`Medium low-angle shot. The same comically gross Constipation King grins wider and gestures one hand outward to an unseen gang off-frame; the sad bloated stomach stays a dim turned-away dark silhouette at the lower edge (face NOT visible, NOT talking). The camera holds with a slow push-in. The King looks at the camera and says in a deep gravelly, comically-villainous Hindi voice, natural lip sync, line begins after a half-second pause: एसिडिटी मेरी दोस्त है। ब्लोटिंग मेरा भाई है। और हम सब मिलकर तुम्हारा पूरा दिन ख़राब करेंगे। Only the King speaks and only the King's mouth moves; the stomach silhouette is faceless, has no visible mouth and stays silent and still; no other mouth is in frame. [NEG]`

### S3, Stomach (keyframe: s3)  ·  --duration 6  ·  the victim's cry — the turn; King fully out of frame
`Medium close-up shot. The sad bloated pink stomach is alone, the Constipation King completely out of frame, sickly-green gut light around it. The camera holds gently. The Stomach looks at the camera and says in a soft worried anxious Hindi voice, natural lip sync, line begins after a half-second pause: कोई है जो मेरी हेल्प कर सके? Only the Stomach's mouth moves; no other character is visible. [NEG]`

### S4, Amla (keyframe: s4)  ·  --duration 8  ·  Hero 1 arrives
`Medium close-up of the green gooseberry hero Bhui Amla alone, glowing warm, crashing into a confident friendly heroic stance, facing camera with a kind brave smile. Locked-off with a gentle slow push-in. Amla looks at the camera and says in a warm confident heroic young male Hindi voice, natural lip sync, line begins after a half-second pause: रुको ज़रा। मैं हूँ भुई आँवला। मैं डाइजेशन को नैचुरली सपोर्ट करता हूँ और गट को बैलेंस रखने में मदद करता हूँ। Only Amla's mouth moves; no other character is visible. [NEG]`

### S5, King (keyframe: s5)  ·  --duration 4  ·  TAUNT #1, smug
`Medium close-up of the comically gross Constipation King alone in dark green murk, leaning back with a smug dismissive sneer. The camera holds. The King looks at the camera and says in a deep gravelly, comically-villainous Hindi voice, natural lip sync, line begins after a half-second pause: एक अकेला आया है मुझे हराने? हा हा। Only the King's mouth moves; no other character is visible. [NEG]`

### S6, Ajwain (keyframe: s6)  ·  --duration 6  ·  Hero 2 answers the taunt
`Medium close-up of the carom-seed hero Ajwain alone, glowing warm, bursting in with an energetic action entry, facing camera with a bright friendly grin. Quick lively gentle push-in. Ajwain looks at the camera and says in a bright fast energetic male Hindi voice, natural lip sync, line begins after a half-second pause: अकेला नहीं। मैं हूँ अजवाइन। मैं पेट की हेविनेस और डिस्कम्फर्ट से लड़ने आया हूँ। Only Ajwain's mouth moves; no other character is visible. [NEG]`

### S7, King (keyframe: s7)  ·  --duration 4  ·  TAUNT #2, scoffing
`Medium close-up of the comically gross Constipation King alone in dark green murk, scoffing and waving one hand dismissively. The camera holds. The King looks at the camera and says in a deep gravelly, comically-villainous Hindi voice, natural lip sync, line begins after a half-second pause: दो लोगों से कुछ नहीं होगा। Only the King's mouth moves; no other character is visible. [NEG]`

### S8, Saunf (keyframe: s8)  ·  --duration 8  ·  Hero 3 joins; explicit FEMALE voice (Veo guesses gender)
`Medium close-up of the fennel hero Saunf alone, glowing warm, sliding in gracefully into a calm composed stance, facing camera with a gentle smile. Smooth slow dolly-in. Saunf looks at the camera and says in a smooth gentle calm FEMALE Hindi voice, natural lip sync, line begins after a half-second pause: और मैं हूँ सौंफ। खाने के बाद जो ब्लोटिंग और भारीपन लगता है, उसके ख़िलाफ़ मैं भी टीम में हूँ। Only Saunf's mouth moves; no other character is visible. [NEG]`

### S9, King (keyframe: s9)  ·  --duration 4  ·  TAUNT #3, forced bravado (false confidence)
`Medium close-up of the comically gross Constipation King alone in dark green murk, puffing his chest in forced bravado with a strained grin and a faint sweat-bead. The camera holds. The King looks at the camera and says in a deep gravelly, comically-villainous, slightly strained Hindi voice, natural lip sync, line begins after a half-second pause: अभी भी मैं जीत रहा हूँ। Only the King's mouth moves; no other character is visible. [NEG]`

### S10, Haritaki (keyframe: s10)  ·  --duration 8  ·  Hero 4, wise swagger; WARM not menacing
`Medium close-up of the wise myrobalan elder-hero Haritaki alone, bathed in WARM GOLDEN light with a gentle golden thunder shimmer, kind twinkling eyes and a warm grandfatherly smile, clearly a benevolent good guy, NOT menacing. Slow majestic push-in. Haritaki looks at the camera and says in a deep wise kindly elder male Hindi voice, natural lip sync, line begins after a half-second pause: गेम ओवर बोलने से पहले मुझे मत भूलो। मैं हूँ हरीतकी। आयुर्वेद की सबसे भरोसेमंद जड़ी बूटियों में से एक। Only Haritaki's mouth moves; no other character is visible. [NEG]`

### S11, King (keyframe: s11)  ·  --duration 4  ·  TAUNT #4, confidence BREAKS, rattled
`Medium close-up of the comically gross Constipation King alone in dark green murk, eyes comically wide, shrinking back, rattled. The camera holds. The King looks at the camera and says in a deep gravelly, comically-villainous, panicked Hindi voice, natural lip sync, line begins after a half-second pause: ओह नो। तुम सब एक साथ? Only the King's mouth moves; no other character is visible. [NEG]`

### S12, Amla (keyframe: s12)  ·  --duration 4  ·  S6 four-hero exchange beat 1
`Medium close-up of the green gooseberry hero Bhui Amla alone, glowing warm, frozen mid-action with a sly confident grin facing camera. Freeze-frame energy, a tiny camera snap. Amla looks at the camera and says in a warm confident young male Hindi voice, natural lip sync, line begins after a half-second pause: एक मिनट। Only Amla's mouth moves; no other character is visible. [NEG]`

### S13, Ajwain (keyframe: s13)  ·  --duration 4  ·  S6 exchange beat 2
`Medium close-up of the carom-seed hero Ajwain alone, glowing warm, frozen mid-action with a playful raised eyebrow facing camera. Freeze-frame energy, a tiny camera snap. Ajwain looks at the camera and says in a bright fast energetic male Hindi voice, natural lip sync, line begins after a half-second pause: तुम्हें लगता है? Only Ajwain's mouth moves; no other character is visible. [NEG]`

### S14, Saunf (keyframe: s14)  ·  --duration 4  ·  S6 exchange beat 3 — the setup line; FEMALE voice
`Medium close-up of the fennel hero Saunf alone, glowing warm, frozen mid-action with a calm knowing smile facing camera. Freeze-frame energy, a tiny camera snap. Saunf looks at the camera and says in a smooth gentle calm FEMALE Hindi voice, natural lip sync, line begins after a half-second pause: बस हम चार ही हैं? Only Saunf's mouth moves; no other character is visible. [NEG]`

### S15, Haritaki (keyframe: s15)  ·  --duration 4  ·  S6 exchange beat 4 — the trigger; "BOOM!" = POST SFX into S16, NOT spoken; WARM
`Medium close-up of the wise myrobalan elder-hero Haritaki alone, bathed in WARM GOLDEN light, kind twinkling eyes and a confident warm smile, clearly a benevolent good guy, NOT menacing. Freeze-frame energy, a tiny camera snap. Haritaki looks at the camera and says in a deep wise kindly elder male Hindi voice, natural lip sync, line begins after a half-second pause: अब असली सरप्राइज़ देखो। Only Haritaki's mouth moves; no other character is visible. [NEG]`

### S16, NARRATOR (keyframe: s16 = stylized 3D bottle)  ·  --duration 8  ·  HERO REVEAL / merge; no legible-label demand here
`Centered shot. More than ten glowing herbs swirl in as streaks of golden light and coalesce into the GLOWING form of the Clear Gut dropper bottle (stylized 3D cartoon bottle matching the world). The camera holds steady. The bottle stays still and does NOT morph; the label may stay soft/glowing, legibility is NOT required here. A warm trustworthy male Hindi NARRATOR speaks in voiceover; NO character moves their mouth, no visible talking, all mouths closed, line begins after a half-second pause: ये सिर्फ़ चार हर्ब्स की कहानी नहीं है। दस से ज़्यादा आयुर्वेदिक इंग्रीडिएंट्स की पावर, अब एक ही आयुर्वेदिक क्लियर गट ड्रॉप में। Magical golden shimmer. [NEG]`

### S17a, NARRATOR (keyframe: s17a, bottle locked, King gone)  ·  --duration 8  ·  product benefit; King blasted = POST visual/SFX, no spoken scream
`Centered shot. The healthy Clear Gut dropper bottle stands on a locked pedestal, glowing and steady; behind it a soft settling burst of golden light marks the empty dark-green corner where the Constipation King WAS (the King is already gone, NOT in frame). The camera holds, locked-off and gentle, the bottle stays still and does NOT morph, keep it sharp. A warm trustworthy male Hindi NARRATOR speaks in voiceover; NO character moves their mouth, no visible talking, all mouths closed, line begins after a half-second pause: ये सब एक साथ मिलकर डाइजेशन को सपोर्ट करते हैं। और मदद करते हैं कॉन्स्टिपेशन, एसिडिटी और ब्लोटिंग जैसी रोज़मर्रा की दिक़्क़तों से। Bright uplifting. [NEG]`

### S17b, Stomach (keyframe: s17b)  ·  --duration 6  ·  RESOLUTION — Stomach SPEAKS (dialogue shot, SOLO, lens-facing; see flag)
`Medium close-up of the happy healthy pink stomach alone, bright and energetic, bouncing lightly, facing camera with a big joyful smile. The King is gone; no bottle and no other character is in frame. Locked-off, gentle. The Stomach looks at the camera and says in a bright relieved happy Hindi voice, natural lip sync, line begins after a half-second pause: अब लग रहा है पेट हल्का है। Only the Stomach's mouth moves; no other character is visible. [NEG]`

### S18, product card (NO Veo)
ffmpeg Ken-Burns zoom on `assets/clear_gut_product.png` (~3–4s), real bottle still centered, clean studio-warm grade, + burned Devanagari text and brand (guarantees a pixel-perfect, legible label — never demanded from Veo):
- दस से ज़्यादा आयुर्वेदिक जड़ी बूटियाँ। सिर्फ़ दस से पंद्रह बूँदें, सुबह और रात।
- पेट हल्का। दिन हल्का।
- BLUMELIFE Clear Gut Drops
Optional warm-narrator tail over the card may read the first line; brand + tagline stay as on-screen text. No model call, no Veo, no spend.

---

## Flag for the prompt-reviewer (focus here)
- **S17b — lens-facing speaking Stomach.** This is the known re-roll-prone shot: a cartoon organ
  character speaking to lens. It is authored cleanly as a SOLO dialogue shot (one mouth, to camera,
  line short at 6 words, no other mouth in frame) per the human's choice for THIS variant. Two residual
  risks per the script flag: (1) cartoon lip-sync on an organ stays approximate — never auto-PASS,
  expect re-rolls; (2) confirm no other mouth leaks into frame (King gone, no bottle). Documented
  fallback if it repeatedly fails = the AI-friendly treatment (narrated joy, stomach in hard profile /
  mouth closed), but that is a fidelity downgrade, last resort only.
