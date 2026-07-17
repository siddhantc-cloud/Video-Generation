# Clear Gut "Ingredient Army" — PROMPTS (v5 AI-FRIENDLY variant)

Per-scene generation prompts for the **v5 AI-FRIENDLY** shot list
(`01_script_v5_AIFRIENDLY.md`, 12 shots, ~62s). 8 SOLO dialogue shots + 3 NARRATOR-VO shots +
1 ffmpeg product card. Spoken Devanagari lines are copied **verbatim** from the script.

Keyframes via `nano_banana_2` (multi-image-ref). Video via `veo3_1` (native audio), single start-image per clip.
Refs live in `bible/` (king, amla, ajwain, saunf, haritaki, stomach, bottle) and `assets/clear_gut_product.png`.

Shared keyframe style suffix `[ST]`:
`Glossy 3D Pixar/DreamWorks-caricature style, cinematic rim lighting, vibrant, vertical 9:16. ABSOLUTELY NO TEXT, no letters, no captions.`

Shared veo negatives/ambient suffix `[NEG]`:
`Ambient: faint gut room-tone, no music, no audience, no laugh track. Glossy 3D cartoon animation. no subtitles, no captions, no on-screen text.`

Rules baked in: colon dialogue · "natural lip sync" · "line begins after a half-second pause" · ONE speaker, all others off-frame/mouth-guarded · narrated shots say "no character moves their mouth, all mouths closed" with non-speakers in HARD profile · NO quotation marks around any spoken line · stylized 3D bottle, still, no morph (legible label is the S12 card only).

---

## Keyframe prompts (nano_banana_2)

### S1 — King (ref: king, stomach) · AD-fix: stomach = faceless turned-away shadow (no 2nd renderable mouth); comedic-gross not horror
`Low-angle: the comically gross CONSTIPATION KING (image 1) looms large upper-center with a goofy-evil grin and comically glowing eyes, one hand raised in a gloating gesture; in the lower foreground a small frightened stomach (image 2) appears ONLY as a dim turned-away silhouette in shadow (its face NOT visible). Dark gut-cave, thick sickly-green gas, hard top-light on the King. Comically menacing, filter-safe. [ST]`

### S2 — King (ref: king, stomach) · same frame, grinning, gesturing to his unseen gang
`Low-angle: the comically gross CONSTIPATION KING (image 1) center-frame, grinning wide and gesturing outward with both hands toward an unseen gang as if introducing his friends; the small stomach (image 2) remains a dim turned-away silhouette in shadow at the lower edge (face NOT visible). Dark gut-cave, thick sickly-green gas, hard top-light on the King. Comically menacing, filter-safe. [ST]`

### S3 — Stomach (ref: stomach) · sad bloated face NOW to camera, King fully out of frame
`Medium close-up: a small sad bloated pink STOMACH character (image 1) ALONE, centered, its worried face turned TO camera with pleading hopeful eyes, hands clasped. The Constipation King is fully OUT of frame. Sickly-green ambient light, lonely dim gut-cave, a faint hopeful glow beginning at the edge. Only this one character in frame. [ST]`

### S4 — Amla (ref: amla) · crashes in, heroic stance, to camera, warm golden rim-glow
`Medium close-up hero shot: the green gooseberry hero BHUI AMLA (image 1) ALONE, centered, just crashed in mid-landing in a confident FRIENDLY heroic stance, facing camera with a warm reassuring smile and kind brave eyes. Bright warm golden rim-glow surrounds him (a good guy bringing light). Soft glowing gut background, clean. Only this one character in frame. [ST]`

### S5 — Ajwain (ref: ajwain) · action-movie entry, energetic, to camera, bright punchy warm
`Medium close-up hero shot: the carom-seed hero AJWAIN (image 1) ALONE, centered, bursting in with an energetic action-movie entry pose, facing camera with a bright eager friendly grin and kind lively eyes. Bright punchy warm golden glow surrounds him. Soft glowing gut background, clean. Only this one character in frame. [ST]`

### S6 — Saunf (ref: saunf) · slides in gracefully, calm, to camera, soft warm
`Medium close-up hero shot: the fennel hero SAUNF (image 1) ALONE, centered, mid graceful slide-in, calm and poised, facing camera with a gentle warm smile and kind soft eyes. Soft warm golden glow surrounds her. Soft glowing gut background, clean. Only this one character in frame. [ST]`

### S7 — Haritaki (ref: haritaki) · lands with gentle thunder shimmer, wise-kindly, to camera, warm gold
`Medium close-up hero shot: the wise myrobalan elder-hero HARITAKI (image 1) ALONE, centered, just landed amid a gentle golden thunder shimmer, facing camera, bathed in WARM GOLDEN light with kind twinkling eyes and a warm benevolent smile, a wise kindly grandfather-hero (powerful but warm, clearly a GOOD guy, NOT an angry monster, NOT menacing). Soft glowing gut background, clean. Only this one character in frame. [ST]`

### S8 — King (ref: king) · shrinking back, comically worried (still gross-but-funny, not sympathetic), green murk
`Medium close-up: the comically gross CONSTIPATION KING (image 1) ALONE, centered, shrinking back and cowering with a comically worried wide-eyed expression, sweating, hands up defensively (still goofy-gross and funny, NOT sympathetic). Dark sickly-green murk closing in around him, hard top-light. Filter-safe comedic menace. Only this one character in frame. [ST]`

### S9 — team (refs: amla, ajwain, saunf, haritaki, stomach) · AD-fix: heroes TURNED inward in HARD profile, none lens-facing → no front mouths to animate
`Wide low-angle: the FOUR herb heroes (Amla img1, Ajwain img2, Saunf img3, Haritaki img4) seen in HARD profile / turned fully inward toward the small hopeful STOMACH (img5) they protect — fists raised in a heroic protective SHIELDING action pose, NONE facing the camera, NO face to lens (hard profile, not three-quarter), all mouths CLOSED. The Constipation King is TINY, dark and cowering in the far background corner. Heroes glow bright and warm; the King's corner is dark and green. Epic friendly team-up, mid-action. [ST]`

### S10 — product reveal (ref: bottle, clear_gut_product) · AD-fix: STYLIZED 3D bottle matching the cartoon world (label may be soft); legible payoff lives in S12
`Centered: more than ten glowing Ayurvedic herbs swirl as streaks of golden light and coalesce into ONE radiant amber glass dropper bottle of Clear Gut, rendered as a GLOSSY 3D CARICATURE bottle that matches this cartoon world (use the product reference images for bottle shape, amber color and label COLORWAY only — stylize it; the label text need NOT be legible here), standing heroic and glowing on-axis, triumphant golden rays, magical reveal. Bottle still, no morph. No characters. [ST]`

### S11 — resolution (refs: clear_gut_product, stomach) · AD-fix: stomach in HARD profile looking AT the bottle (mouth off-lens); bottle on a locked pedestal, King already gone
`The pink STOMACH (image 2) is now HAPPY, bright and healthy, dancing lightly on the left in HARD profile, looking ADMIRINGLY toward the bottle (face turned fully away from camera, mouth CLOSED); the amber Clear Gut dropper bottle (image 1, match reference closely, label sharp) stands glowing on the right on a still locked pedestal in a warm clean bright gut. The King is GONE. Uplifting victory, warm golden light. [ST]`

### S12 — product card (NO generation; ffmpeg)
Use `assets/clear_gut_product.png` directly with Ken-Burns + burned tagline + dose + brand. No model call — guarantees a pixel-perfect, word-perfect label. (See product-card entry below.)

---

## Veo prompts (`veo3_1 --image <keyframe> --duration <d> --aspect_ratio 9:16 --quality high`)

### S1, King (keyframe: s1) · duration 8
`Medium low-angle shot. The comically gross Constipation King looms over a small frightened stomach seen ONLY as a dim turned-away silhouette in shadow at the lower frame edge (its face NOT visible). The camera slowly pushes in on the King. The King looks at camera and says in a deep gravelly, comically-villainous Hindi voice, natural lip sync, line begins after a half-second pause: हा हा। मैं हूँ कॉन्स्टिपेशन किंग। मैं तुम्हारा पेट कभी ठीक से साफ़ नहीं होने दूँगा। ONLY the King speaks and ONLY the King's mouth moves; the stomach silhouette has NO visible face and its mouth never moves; no other character speaks. [NEG]`

### S2, King (keyframe: s2) · duration 8
`Medium low-angle shot. The Constipation King grins and gestures outward toward an unseen gang; the small stomach stays a dim turned-away silhouette at the lower frame edge (face NOT visible). The camera holds with a slow drift. The King looks at camera and says in a deep gravelly, comically-villainous Hindi voice, natural lip sync, line begins after a half-second pause: एसिडिटी मेरी दोस्त है। ब्लोटिंग मेरा भाई है। हम सब मिलकर तुम्हारा पूरा दिन ख़राब करेंगे। ONLY the King speaks and ONLY the King's mouth moves; the stomach silhouette has NO visible face and its mouth never moves; no other character speaks. [NEG]`

### S3, Stomach (keyframe: s3) · duration 6
`Medium close-up. The small sad bloated pink stomach is alone, the King fully out of frame, in lonely sickly-green light. A gentle slow push-in. The stomach looks at camera and says in a soft anxious sympathetic Hindi voice, natural lip sync, line begins after a half-second pause: कोई है जो मेरी मदद कर सके? Only the stomach's mouth moves; no other character is visible. [NEG]`

### S4, Amla (keyframe: s4) · duration 8
`Medium close-up of the green gooseberry hero Bhui Amla alone, glowing warm, facing camera with a confident friendly smile. Locked-off with a gentle slow push-in. Amla looks at camera and says in a warm confident young-hero Hindi voice, natural lip sync, line begins after a half-second pause: रुको ज़रा। मैं हूँ भुई आँवला। मैं डाइजेशन को नैचुरली सपोर्ट करता हूँ और गट को बैलेंस रखने में मदद करता हूँ। Only Amla's mouth moves; no other character is visible. [NEG]`

### S5, Ajwain (keyframe: s5) · duration 6
`Medium close-up of the carom-seed hero Ajwain alone, glowing warm, facing camera, energetic and friendly. Quick lively gentle push-in. Ajwain looks at camera and says in a bright fast energetic Hindi voice, natural lip sync, line begins after a half-second pause: अकेला नहीं। मैं हूँ अजवाइन। पेट का भारीपन और बेचैनी, मेरा काम। Only Ajwain's mouth moves; no other character is visible. [NEG]`

### S6, Saunf (keyframe: s6) · duration 8 · AD-fix: explicit FEMALE voice (Veo guesses gender)
`Medium close-up of the fennel hero Saunf alone, glowing warm, facing camera, calm and graceful. Smooth slow dolly-in. Saunf looks at camera and says in a smooth gentle calm FEMALE Hindi voice, natural lip sync, line begins after a half-second pause: और मैं हूँ सौंफ। खाने के बाद जो ब्लोटिंग और भारीपन लगता है, उसके ख़िलाफ़ मैं भी टीम में हूँ। Only Saunf's mouth moves; no other character is visible. [NEG]`

### S7, Haritaki (keyframe: s7) · duration 8 · AD-fix: warm golden light + kind eyes (kill villain-leakage)
`Medium close-up of the wise myrobalan elder-hero Haritaki alone, bathed in WARM GOLDEN light with a gentle golden shimmer, kind twinkling eyes and a warm smile, clearly a benevolent good guy, NOT menacing. Slow majestic push-in. Haritaki looks at camera and says in a deep wise kindly Hindi elder voice (warm, reassuring, NOT menacing), natural lip sync, line begins after a half-second pause: गेम ओवर बोलने से पहले मुझे मत भूलो। मैं हूँ हरीतकी। आयुर्वेद की सबसे भरोसेमंद जड़ी बूटियों में से एक। Only Haritaki's mouth moves; no other character is visible. [NEG]`

### S8, King (keyframe: s8) · duration 6
`Medium close-up of the Constipation King alone, shrinking back and cowering, comically worried and sweating in dark sickly-green murk (still goofy-gross, filter-safe, NOT sympathetic). The camera pushes in slightly. The King looks at camera and says in a deep gravelly, comically-villainous, now-panicked Hindi voice, natural lip sync, line begins after a half-second pause: ओह नो। तुम सब एक साथ? Only the King's mouth moves; no other character is visible. [NEG]`

### S9, team (NARRATOR VO) (keyframe: s9) · duration 6 · AD-fix: heroes in HARD profile / mouths closed → no lens-facing mouths
`Wide low-angle shot. The four glowing herb heroes are seen in HARD profile, turned fully inward toward the small hopeful stomach they shield, fists raised in a protective action pose, NONE facing the lens, all mouths CLOSED; the Constipation King is tiny and dark, cowering in the far background corner. The camera cranes up slightly to reveal the team mid-action. A warm trustworthy male Hindi NARRATOR speaks in voiceover; NO character moves their mouth, no visible talking, all mouths closed, line begins after a half-second pause: ये सिर्फ़ चार की कहानी नहीं है। ये तो दस से ज़्यादा आयुर्वेदिक जड़ी बूटियों की पूरी फौज है। (Mood is heroic and uplifting; the music swell is added in POST, do NOT generate any music.) [NEG]`

### S10, reveal (NARRATOR VO, bottle FORMING) (keyframe: s10 = stylized 3D bottle) · duration 8 · AD-fix: don't resolve on legible label, spectacle only; S12 carries the legible payoff
`Centered shot. Ten-plus glowing herbs swirl as streaks of golden light and coalesce into the radiant glowing form of the Clear Gut dropper bottle (stylized 3D cartoon bottle, matching the world). The camera holds steady. The bottle stays still and does NOT morph; the label may stay soft/glowing, legibility is NOT required here. No characters in frame. A warm trustworthy male Hindi NARRATOR speaks in voiceover; NO character moves their mouth, no visible talking, all mouths closed, line begins after a half-second pause: दस से ज़्यादा आयुर्वेदिक ताक़त, अब एक ही आयुर्वेदिक क्लियर गट ड्रॉप्स में। ये सब मिलकर डाइजेशन को सपोर्ट करते हैं। (Visual: magical golden shimmer only; any chime or music is POST, do NOT generate any music.) [NEG]`

### S11, resolution + benefit + tagline (NARRATOR VO, bottle locked) (keyframe: s11) · duration 8 · AD-fix: stomach in HARD profile looking AT bottle (mouth off-lens, closed); bottle on locked pedestal; King already gone
`Medium shot. The happy healthy stomach dances lightly on the left in HARD profile, looking ADMIRINGLY toward the bottle (its face turned fully away from the lens, mouth CLOSED, not talking); the glowing Clear Gut bottle stands on the right on a still locked pedestal, steady, not morphing, label kept sharp; the King is gone. Locked-off camera, gentle warm light. A warm trustworthy authoritative male Hindi NARRATOR speaks in voiceover; NO character moves their mouth, no visible talking, all mouths closed, line begins after a half-second pause: और मदद करते हैं कॉन्स्टिपेशन, एसिडिटी और ब्लोटिंग जैसी रोज़मर्रा की दिक़्क़तों से। पेट हल्का, दिन हल्का। (Visual is bright and uplifting; the soft chime is added in POST, do NOT generate any music or chime.) [NEG]`

### S12, product card (NO Veo)
ffmpeg Ken-Burns zoom on `assets/clear_gut_product.png` (~4s), with burned-in post text — the guaranteed-legible brand close, NOT generated by Veo:
- `दस से ज़्यादा आयुर्वेदिक जड़ी बूटियाँ। सिर्फ़ दस से पंद्रह बूँदें, सुबह और रात।`
- `पेट हल्का। दिन हल्का।`
- `BLUMELIFE Clear Gut`

The numeric `10–15` is fine as a POST graphic here (never voiced by Veo). Optional narrator tail (post, OFF-card audio) may speak `सिर्फ़ दस से पंद्रह बूँदें, सुबह और रात।` if a voiced dose CTA is wanted; the on-card text is the source of truth for the label/dose/brand.
