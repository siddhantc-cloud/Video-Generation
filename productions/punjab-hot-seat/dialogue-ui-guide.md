# Dialogue (V2) — Higgsfield Web-UI Guide + Prompts

> **Goal:** add lip-synced dialogue to the So Sorry caricatures using **Higgsfield Ultra's web UI** (already owned — no new subscription). These features are **web-UI only (not MCP)**, so YOU generate in the browser; the agent then composites the clips into the film with ffmpeg (free). Builds on `so-sorry-v1-framework.md` (V1 = no dialogue).
>
> **⚠️ Legal:** lip-syncing real politicians = highest-risk content. **Private capability showcase only — do not distribute without disclosure/legal review.**

## 0. Decision (why no new purchase)
Higgsfield Ultra bundles: **TTS + 3 custom voices + 40+ presets**; lip-sync: **Kling AI Avatar, Kling Lipsync, InfiniteTalk (multi-person), Speak v2, lipsync-2, Veo 3**. Test free first. Optional add-ons only if a weak link: **ElevenLabs Creator $22** (better/automatable voices) · **Hedra $30** (best 2D-cartoon lip-sync).

## 1. The per-shot pipeline
1. **Voice bible** — create & lock ONE custom voice per character (3 max on Ultra): `modi-voice`, `shah-voice`, `kejriwal-voice` (+ reuse a preset for the voter).
2. **TTS** — generate each line in that character's locked voice → audio file.
3. **Source frame** — a **front-facing, mouth-visible** caricature still (use a bible image or generate a clean close-up).
4. **Lip-sync** — **Kling AI Avatar** (single speaker) or **InfiniteTalk** (2–3 in one frame) : image + audio → talking clip.
5. **Composite** — hand the clips to the agent → ffmpeg into the film (free, no credits).

## 2. Step-by-step (Higgsfield web UI)
1. Log in → open **Higgsfield Audio** (TTS / Voice).
2. **Create a custom voice** (Voice Design from a text description, OR clone from a sample). Name it `modi-voice`. Repeat for `shah-voice`, `kejriwal-voice`. (Ultra cap = 3 custom; use a preset for the voter.)
3. **Generate speech**: paste the line (§4), pick the matching voice, generate, **download the audio** (or note its workspace ID).
4. Open **Lipsync Studio → Kling AI Avatar** (single speaker). Upload the **front-facing caricature still** + the audio. Generate. (For a 2–3 person exchange in one frame, use **InfiniteTalk** and add one audio track per face.)
5. Download the talking clip → drop into `productions/punjab-hot-seat/renders/dialogue/` → tell the agent to composite.

## 3. Voice-design prompts (paste into Higgsfield Voice Design / ElevenLabs)
- **modi-voice:** "Elderly Indian male, warm resonant baritone, slow measured oratorical delivery with theatrical pauses and rising emphasis; confident, statesmanlike; light Hindi/Gujarati accent."
- **shah-voice:** "Middle-aged Indian male, firm assertive mid-range voice, blunt clipped no-nonsense delivery, steady and controlled; Hindi accent."
- **kejriwal-voice:** "Middle-aged Indian male, earnest slightly-nasal everyman tone, mild complaining/aggrieved cadence, plain and direct; Delhi Hindi accent."
- **voter-voice (preset ok):** "Middle-aged Punjabi male, warm grounded plain-spoken voice, calm and good-humoured."

> Keep satire **balanced** and lighthearted; no fabricated claims; comedic, not defamatory.

## 4. Test script — run ONE of these first (decisive, ~free)
**Pick the source still** = a front-facing close-up caricature (e.g. `bible/refs/modi_so_sorry.png`, or generate a CU). Keep lines SHORT (lip-sync degrades on long lines).

- **Option A — Voter punchline (recommended: balanced, ties to the film's thesis):**
  - Voice: `voter-voice` (preset). Frame: a front-facing Punjabi-voter caricature.
  - Line (Hinglish): **"Kursi koi tohfa nahi — yeh naukri hai."**  *(EN: "The chair isn't a gift — it's a job.")*
- **Option B — Politician comedic beat (balanced jab):**
  - Voice: `modi-voice`. Frame: front-facing Modi caricature CU.
  - Line (Hinglish): **"Mitron… free ka matlab — sirf vote!"**  *(EN: "Friends… 'free' means just one thing — votes!")*
- **Option C — quick English smoke test** (fastest): voice `kejriwal-voice`, line: **"Everything free… except the truth."**

## 5. Acceptance criteria (what makes the test a PASS)
- **Lip-sync:** mouth shapes track the words; reads as intentional, not floaty.
- **On-model:** face/proportions stay the caricature; no melt/warp at the mouth/jaw.
- **Voice fit:** voice suits the character and is **reusable/consistent** across lines (the voice-bible test).
- **2D-friendly:** the engine handles the flat caricature (if it "realism-ifies" the face → try InfiniteTalk, or fall back to Hedra).

→ If all pass: dialogue is viable inside Higgsfield, **zero new spend**. If voice is the weak link → ElevenLabs Creator $22. If lip-sync on 2D is the weak link → Hedra $30.

## 6. Then: build a V2 dialogue scene
Once the test passes, write a short dialogue beat (2–4 lines, balanced), generate each line's voice + lip-sync clip, shoot non-talking coverage on Kling pro (bounded + camera per V1 framework), and the agent edits it together (dialogue clips + music + SFX). Keep it to a single short exchange first (lip-sync is the weakest link — minimize it).
