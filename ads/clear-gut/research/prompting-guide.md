# Prompting research — general → Veo → this-format (synthesized 2026-06-13)

Three levels deep, plus our own hard-won project findings.

## LEVEL 1 — General AI video-gen prompting (2026 consensus)
- **Prompt like a film crew, not a writer.** A good prompt reads as a **mini-storyboard**: shot size + subject + action + context + lighting + style. Keep it **under ~150 words** — high-impact nouns/verbs, not a wall of text.
- **Specific cinematography beats adjectives.** Not "bright light" → "golden-hour key light at 45°, soft rim light." Not "moves dramatically" → name the move.
- **Consistency = reference images, NOT longer text.** Reference-image control replaced "describe harder." (Veo Ingredients = 3 refs; Seedance 2.0 = 12; Wan 2.7 = 9-grid.) Our equivalent on the CLI: bible-ID keyframes.
- **One idea per shot.** Don't cram multiple actions/subjects/sounds into one clip — it turns to mush.

## LEVEL 2 — Veo 3.1 (and Higgsfield-Veo) specifics
- **Direct it like a film crew:** shot sizes (extreme-wide → wide → medium → close-up → macro), lens/focal (18–85mm), moves (dolly-in/out, crane, gimbal glide, handheld sway, **locked-off static**, whip-pan, rack focus).
- **★ Camera move = its OWN standalone sentence.** "The camera slowly dollies in." as a separate line parses far more reliably than burying it in description.
- **Motivated lighting** stated explicitly; **edit timing** can be given as `[00:00-00:02] …` timestamp blocks for multi-beat 8s shots.
- **Dialogue/lip-sync (our verified rules):** `<Speaker> looks at camera and says in a <tone> voice, natural lip sync, line begins after a half-second pause: <DEVANAGARI line>` — colon triggers sync; Devanagari = correct Hindi; half-second pause kills cold-start; ONE short line.
- **Kill burned text:** always `no subtitles, no captions, no on-screen text` (Veo burns Devanagari otherwise).
- **Higgsfield-CLI reality:** `veo3_1` = single `--image` start frame only (no end-frame/multi-ref on CLI — those are web-UI). So: consistency via the start keyframe; motion via prompt.
- **Audio = a layer, not "with sound":** one line + one ambient bed ("faint gut room-tone, no music"); don't overload.

## LEVEL 3 — THIS format (animated mascot/ingredient ad) + our project findings
- **★ ONE speaker per shot. Multiple characters together → NARRATOR voiceover.** (Director's discipline + Veo constraint: Veo moves EVERY visible mouth, so two characters = "who's talking?" mush. The Krishna reference does exactly this — each ingredient gets its own solo shot; groups are narrated.) → **Every hero gets a SOLO talking shot; team/reveal/CTA are narrated.**
- **Good vs evil must read in <1s:** villain = dark, gross, red eyes, sickly-green murk; heroes = bright, warm, glowing, friendly confident smiles. Reserve evil faces for the villain ONLY (v2 mistake: heroes looked like villains).
- **Mascot = brand memory** (Duracell Bunny / M&M logic): consistent, expressive, likable characters.
- **Product fidelity:** Veo I2V blurs fine label text during motion → keep the bottle **still & sharp** in-prompt, reference the real product, and ALWAYS end on a **clean real-product still card** (the one frame that must be perfect).
- **Ad rhythm:** hook (problem) in first 2-3s → escalation (heroes arrive, accelerating) → reveal (product as hero) → CTA. Solo shots cut fast; narrated team beats are the "swell."

## Our locked technical method (proven this project)
bible-ID refs → speaker keyframe (one clear subject) → Veo 3.1 (`--image`, colon dialogue, half-second pause, no-subtitles, mouth-guard) → crossfade assembly + product end-card. Native Veo audio (lip-synced); ElevenLabs/Kling/local-lipsync all abandoned (see [[hinglish-tts-bakeoff]], `caricature-talking-ad` skill).

## Sources
[Google Cloud Veo 3.1 guide](https://cloud.google.com/blog/products/ai-machine-learning/ultimate-prompting-guide-for-veo-3-1) · [Veo native-audio guide](https://www.veo3ai.io/blog/veo-3-native-audio-prompt-guide-2026) · [Higgsfield: unlimited Veo 3.1](https://higgsfield.ai/blog/How-to-Generate-Unlimited-Google-Veo-3.1-Videos) · [Invideo Veo 3.1 guide](https://invideo.io/blog/google-veo-prompt-guide/) · [DreamHost Veo 3.1 guide](https://www.dreamhost.com/blog/veo-3-1-prompt-guide/) · [digen text-to-video guide](https://resource.digen.ai/text-to-video-ai-prompt-guide/) · [VidAU no-subtitles](https://www.vidau.ai/veo-3-prompt-no-subtitles/)
