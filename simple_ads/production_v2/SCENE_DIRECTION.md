# Clear Gut ad v2 — precise direction (from-scratch rebuild)

## Method (fixes v1's flaws)
- **Character IDs = locked reference images** (`bible/<char>.png`), passed as references into EVERY keyframe → identical characters across all scenes.
- **Per scene: START frame + END frame** (END = edited START), animated between with **Kling 3.0** (`--start-image` / `--end-image`, sound on). Controls motion, kills morphing.
- **Frame-chaining:** Scene N END ≈ Scene N+1 START (same character positions) → continuous flow, heroes visibly accumulate.
- **ONE speaker per scene** (the rest react silently) → no muddy multi-voice. Dialogue in Devanagari.

## Cast (locked IDs)
| Tag | Character | Look |
|---|---|---|
| @King | Constipation King (villain) | crowned brown sludge-monster, red eyes, jagged grin |
| @Stomach | the stomach (victim→hero's-ward) | soft pink anthropomorphic stomach, big eyes |
| @Amla | Bhui Amla | muscular green gooseberry, leaf sprout |
| @Ajwain | Ajwain | small feisty tan-green carom seed, spiky |
| @Saunf | Saunf | slender pale-green fennel with frond hair |
| @Haritaki | Haritaki | amber-brown myrobalan elder, golden thunder |
| @Bottle | Clear Gut product | = clear_gut.png (real bottle) |

Setting (constant): murky body-cave, pink tissue floor, green gas. Vertical 9:16.

## Scene blocking + single speaker + dialogue
| # | Who's in frame & WHERE | Speaker | Action (START → END) | Line (Devanagari) |
|---|---|---|---|---|
| 1 | @King atop @Stomach, center | **@King** | crossed-arm grin → leans in laughing; @Stomach cries | हाहाहा! मैं हूँ कॉन्स्टिपेशन किंग! तुम्हारा पेट मैं कभी साफ़ नहीं होने दूँगा! |
| 2 | @King top-right, @Stomach low-right, **@Amla enters LEFT** | **@Amla** | Amla leaps in → lands heroic flex; King scowls | रुको ज़रा! मैं हूँ भुई आँवला! मैं डाइजेशन को नैचुरली सपोर्ट करता हूँ! |
| 3 | @Amla LEFT (held), **@Ajwain enters CENTER**, @King top | **@Ajwain** | Ajwain bursts in → fists up beside Amla | अकेला नहीं! मैं हूँ अजवाइन! पेट की हेविनेस से लड़ने आया हूँ! |
| 4 | @Amla L, @Ajwain C (held), **@Saunf enters RIGHT** | **@Saunf** | Saunf slides in → cool pose; 3 heroes line up | और मैं हूँ सौंफ! ब्लोटिंग के ख़िलाफ़ मैं भी टीम में हूँ! |
| 5 | 3 heroes in row, **@Haritaki descends TOP-center w/ thunder**, @King recoils back | **@Haritaki** | Haritaki lands → thunder clap, 4 assembled | मैं हूँ हरीतकी! आयुर्वेद की सबसे ट्रस्टेड हर्ब्स में से एक! |
| 6 | 4 heroes in a row foreground, @King tiny & scared back | **@Haritaki** (leader) | heroes step forward together, glow up | हम सिर्फ़ चार नहीं — अब असली ताक़त देखो! |
| 7 | 10+ herbs swirl → **@Bottle** forms center | **Narrator (VO)** | golden swirl → radiant bottle locks in | दस से ज़्यादा आयुर्वेदिक हर्ब्स की पावर, अब एक ही क्लियर गट ड्रॉप में। |
| 8 | @Bottle center, **@Stomach HAPPY** beside it, @King dissolving smoke | **Narrator (VO)** | bottle shines, stomach dances | सिर्फ़ दस-पंद्रह ड्रॉप्स, सुबह और रात। पेट हल्का, दिन हल्का। |

Pacing: trim each line to land in ~5–6s; Kling 8s clips; tighten in edit. Add light music bed + Devanagari captions in post.
