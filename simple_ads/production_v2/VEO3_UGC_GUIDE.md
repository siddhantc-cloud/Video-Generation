# Veo 3 UGC / talking-character — best practices (researched 2026-06-12)

## Why Veo for talking: it generates speech + matching mouth TOGETHER (true lip-sync). Kling can't, and overlaying audio is never synced. Trade-off: Higgsfield CLI `veo3_1` takes only a single `input_image` (no end-frame) — accept it; drive motion via prompt + scene direction.

## Prompt formula
`[Cinematography/shot] + [Subject] + [Action] + [Context/lighting] + [Style] + [Dialogue block] + [Audio layer] + [negatives]`

## Dialogue syntax — the load-bearing rules (this is what we did wrong/right)
1. **Colon trigger:** `[Character] says: [line]` — the COLON is the lip-sync trigger. Quotes also work but plain colon form reduces burned subtitles.
2. **ONE short line per clip.** Long lines wreck lip-sync. (Our trimmed Devanagari lines are already short — good.)
3. **Specify delivery:** identity + tone + pace + the words "natural lip sync". e.g. *"the villain says in a deep menacing Hindi voice, natural lip sync"*.
4. **"line begins after a half-second pause"** — bakes in lead-in → FIXES the cold-start clipping we hit on Veo.
5. **Devanagari** for the spoken line → correct Hindi pronunciation (proven on our liked villain clip).
6. **Kill subtitles (critical for Hindi):** always append **`no subtitles, no captions, no on-screen text`** — Veo otherwise burns Devanagari text on screen.

## Audio layering (don't overload an 8s clip)
- Dialogue (one line) + ONE ambient bed ("faint eerie gut ambience, no music") + at most one SFX tied to a visible action. The guide: a short clip "cannot hold dialogue, music, crowd noise… without becoming chaotic."

## Character consistency on Higgsfield CLI
- Veo's official "Ingredients to Video" (multi-ref) isn't on our CLI. Our equivalent: **compose the scene's start keyframe from the character-bible IDs** (Nano Banana refs) → pass as `--image` (input_image) to `veo3_1`. Consistency comes from the keyframe.

## Worked template for our ad (per scene)
```
higgsfield generate create veo3_1 --image ./scenes/sN_start.png --duration 8 --aspect_ratio 9:16 --quality high --prompt "
[shot] of the gut-cave scene. [BLOCKING: who is where, what they do].
<Character> looks toward camera and speaks in a [tone] Hindi voice, natural lip sync, line begins after a half-second pause: देवनागरी लाइन.
Ambient: faint eerie gut room-tone, no music. Exaggerated 3D cartoon animation.
no subtitles, no captions, no on-screen text."
```

## What changes vs our failed v1
- v1 used independent text keyframes (→ morphing) + vague dialogue (→ subtitles risk, weak sync). 
- v2-Veo: bible-ID keyframes (consistency) + colon dialogue syntax + half-second-pause + no-subtitles + delivery spec → cleaner lip-sync, no burned text, consistent characters.

## Sources
- [Google Cloud — Ultimate Veo 3.1 prompting guide](https://cloud.google.com/blog/products/ai-machine-learning/ultimate-prompting-guide-for-veo-3-1)
- [Veo 3 native-audio prompt guide (dialogue/SFX/lip-sync)](https://www.veo3ai.io/blog/veo-3-native-audio-prompt-guide-2026)
- [Skywork — prompting lip-synced dialogue in Veo 3](https://skywork.ai/blog/how-to-prompt-lip-synced-dialogue-google-veo-3/)
- [VidAU — Veo 3 no-subtitles (colon, negative prompts)](https://www.vidau.ai/veo-3-prompt-no-subtitles/) · [removing Veo captions](https://www.vidau.ai/how-to-remove-the-veo-ai-caption-from-veo-3-videos/)
- [snubroot/Veo-3-Prompting-Guide (GitHub)](https://github.com/snubroot/Veo-3-Prompting-Guide)
