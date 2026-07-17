# Deconstruction — Video-509.mp4

## What it is
A **Krishna's SHAPEFIX Juice** ad — an Ayurvedic weight-management / fat-cutting herbal juice, sold by Krishna's Herbal & Ayurveda. Style = **3D-caricature "politoon" animation** (the *So Sorry* aesthetic exactly), where each herb ingredient is personified as an exaggerated character that fights "Fat." Closes on a live-action product shot.

## Technical specs
| | |
|---|---|
| Container | 720×1280 vertical (9:16 reel), H.264 + AAC stereo 48kHz |
| Duration | 54.95s · 30 fps · ~2.16 Mbps · 14.8 MB |
| Audio | single Hindi voice track (character lines, no on-screen captions burned) |

## Structure — character-per-line "ingredient army" format
Each ingredient introduces itself in first person; the villain is Fat. Hindi VO (verbatim):

| t (s) | Character (visual) | Line (Hindi) | Gist |
|---|---|---|---|
| 0–5 | **Fat** — bloated golden blob villain on a body-tissue landscape | मैं हूँ फैट, और तुम कितनी भी कोशिश करो, मैं जाने वाला नहीं | "I'm Fat — try all you want, I'm not leaving" |
| 6–8 | **Green Tea** — green leaf warrior, lightning | मैं हूँ ग्रीन टी, मेटाबॉलिज़म का इंजन | metabolism engine |
| 11–13 | (Green Tea) | अब सुस्ती का नामो-निशान नहीं | no more sluggishness |
| 14–18 | **Gudmar** — green Hulk-like muscular warrior | मैं हूँ गुडमार, मीठे की लत तोड़ता हूँ | breaks sugar cravings |
| 19–21 | (Gudmar) | आज से चर्बी बढ़ेगी नहीं | no more fat gain |
| 22–24 | **Apple Cider Vinegar** — liquid/water-droplet character | मैं हूँ एप्पल साइडर विनेगर | — |
| 25–27 | (ACV) | चर्बी काटना मेरा काम है | cutting fat is my job |
| 28–31 | **Amla (आँवला)** — glowing golden orb warrior | मैं हूँ आँवला, सदियों पुराना योद्धा | ancient warrior |
| 32–34 | (Amla) | अंदर की गंदगी मेरे सामने टिकती नहीं | detoxifies |
| 35–40 | the squad / golden warrior in cave | हम चार नहीं, उन्नीस हैं — आयुर्वेद की पूरी फौज | "not 4 — we're 19, a full army of Ayurveda" |
| 41–47 | **The Product** — anthropomorphized green Krishna's bottle (face + arms) | मैं हूँ शेपफिक्स जूस, उन्नीस आयुर्वेदिक जड़ी-बूटियों की फौज … तुम्हारी सेहत मेरी ज़िम्मेदारी है | "I am ShapeFix Juice, an army of 19 Ayurvedic herbs; your health is my responsibility" |
| 48–55 | **Live-action** — woman in bed, real bottle on nightstand | रोज़ सुबह और शाम, सिर्फ़ 30ml — बस इतना काफी है | dosage CTA: 30ml AM/PM |

## Craft notes (why it works / how to replicate)
- **Hook = the villain, not the product.** Fat speaks first and taunts — classic So Sorry antagonist intro. Product doesn't appear until ~41s (75% in).
- **Mascot-monster framing**: each ingredient = a "warrior" with a power and a one-line boast. Repetitive "मैं हूँ ___" cadence makes it chantable and easy to extend (more herbs = more characters).
- **Stylized lip-sync is forgiving.** Mouths move loosely in caricature style — NOT realistic talking-head sync. This is the key insight for us: this style sidesteps the entire Veo/lip-sync problem that plagued the BLUMELIFE podcast reel.
- **One narrator, many characters.** A single voice actor (or one TTS voice) can perform all characters with pitch/tone shifts — no multi-speaker coordination needed.
- **Body-horror-lite environment**: characters stand on stylized "inside the body" tissue/pore terrain → visualizes "works inside you."
- **Hard cut to live-action** at the end grounds the fantasy in a real product + real person (trust signal + dosage).

## How this maps to our stack
- This is **seedance-satire-director / politoon territory**, not the realistic podcast lane. The caricature style is exactly what `seedance-satire-director` + Kling/Higgsfield were built for.
- Audio: single-voice character VO → ElevenLabs/edge-tts, one voice with per-character delivery. No lip-sync model strictly required (cartoon mouths are loose).
- Pipeline fit: character keyframes (Nano Banana / Qwen) → animate per character (Kling/Veo/Wan) → single VO track → caption-free or light captions → EDL assembly (our existing toolchain).
- Frames extracted at `deconstruct/frame_*.png`; montage at `deconstruct/montage.png`; audio at `deconstruct/audio.mp3`.
