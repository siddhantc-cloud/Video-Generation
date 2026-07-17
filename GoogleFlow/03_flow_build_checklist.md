# Google Flow build checklist — Scene 1 (work down the list in the Flow UI)

Bound to `01_flow_shooting_script.md`. Do the one-time setup once, then generate the 4 Scene-1 shots.
Flow's exact button labels drift; the *actions* below are stable — map them to whatever the current UI calls them.

**Two golden rules for this whole video:**
- **Audio:** every shot = ambient/diegetic sound ONLY. In each prompt end with *"no spoken dialogue, no
  narration, no music, no on-screen text."* The narrator (`02_narration_VO.txt`) is layered externally, later.
- **Identity:** attach only the character(s) actually in the shot — never several Ingredient sheets at once.

---

## STEP 0 — One-time project setup (do once)

| # | Action | Pass condition | Done |
|---|---|---|---|
| 0.1 | New Flow project. Set output aspect ratio to **9:16 vertical** and default clip length to **8s**. | Project is 9:16. | ☐ |
| 0.2 | Create Ingredient **RAMA** → upload `ingredients/rama_sheet.png`. | Ingredient saved, thumbnail correct. | ☐ |
| 0.3 | Create Ingredient **SQUIRREL** → `ingredients/squirrel_sheet.png`. | Saved. | ☐ |
| 0.4 | Create Ingredient **LEAD VANARA** → `ingredients/lead_vanara_sheet.png`. | Saved. | ☐ |
| 0.5 | Create Ingredient **BABY VANARA** → `ingredients/baby_vanara_sheet.png`. | Saved. | ☐ |
| 0.6 | Create Ingredient **SENA** → `ingredients/sena_sheet.png`. | Saved. | ☐ |
| 0.7 | Create Ingredient **BRIDGE-STATES** (optional) → upload the 4 files in `keyframes/bridge/`. | Saved (attach the matching state per shot). | ☐ |

---

## The per-shot method (applies to every shot below)

You have a locked **keyframe** for all 4 Scene-1 shots, so prefer **Frames-to-Video**:
1. New shot → choose **Frames to Video**.
2. **Start frame** = the shot's keyframe PNG (it already sets composition + identity). Add an **End frame**
   only where noted.
3. Attach the character **Ingredient** as reinforcement (belt-and-braces for identity through motion).
4. **Prompt = the MOTION, not the scene** (the frame already shows the scene). Describe what moves + the
   one camera move + the ambient audio + the STYLE tail. Keep it short.
5. Set **duration**, generate, then judge against the pass condition. Re-roll a shot max ~3× before using
   the script's fallback.

**STYLE tail to paste on every prompt:** *photoreal, grounded, warm golden-hour, 65mm cinematic, fine
grain; smooth slow constant-speed motion, stable framing; no on-screen text, no captions, no watermark;
no spoken dialogue, no narration, no music (ambient sound only).*

---

## SCENE 1 — THE PURPOSE (4 shots)

### ☐ S1-a — Rama at the shore  *(establishes Rama)*
| Field | Value |
|---|---|
| Mode | Frames-to-Video (start frame only) |
| Start frame | `keyframes/S1-a.png` |
| Ingredient | **RAMA** |
| Duration | **8s** |
| Motion prompt | *Hold on Rama at the shore; his hair and cloth drift in a steady sea wind; a slow, steady push-in; his gaze stays fixed on the far horizon; distant surf and wind.* + STYLE tail |
| Pass condition | Face matches the Rama sheet, no drift/warp; motion is calm (breath + wind), not floaty; no lips reading as speech; no text. |
| VO it plays under (external) | "Across this ocean waited a battle for dharma. Sita had to be brought home. Ravana had to fall." |

### ☐ S1-b — The vanara sena gathered
| Field | Value |
|---|---|
| Mode | Frames-to-Video (start frame only) |
| Start frame | `keyframes/S1-b.png` |
| Ingredient | **SENA** (keep crowd distant) |
| Duration | **7s** |
| Motion prompt | *A single slow aerial pull-back rises up and away, revealing the vast vanara army massed behind Rama; the crowd stays still and distant; low crowd murmur and wind.* + STYLE tail |
| Pass condition | ONE smooth camera move; no close warped faces; crowd reads as a mass, not morphing individuals. |
| VO | "And to get there, an army would build what had never been built before. A bridge across the sea." |

### ☐ S1-c — Boulder hurled into the sea
| Field | Value |
|---|---|
| Mode | Frames-to-Video (**start + end**) |
| Start frame | `keyframes/S1-c.png` (boulder mid-air) |
| End frame | a splash-plume frame — if you don't have one, generate start-only and let the splash happen |
| Ingredient | none (or leave empty) |
| Duration | **5s** |
| Motion prompt | *The boulder falls in an arc and strikes the sea, throwing up a huge splash plume; a slight camera tilt follows the arc; thunderous splash and surf.* + STYLE tail |
| Pass condition | Boulder stays solid and large (doesn't float/vanish); splash looks like water, not tearing; single action only. |
| VO | "Stone by stone. Boulder by boulder." |

### ☐ S1-d — Marked boulder set into the bridge
| Field | Value |
|---|---|
| Mode | Frames-to-Video (start frame only) |
| Start frame | `keyframes/S1-d_inscription.png` |
| Ingredient | **LEAD VANARA** + **BRIDGE-STATES** (first-boulders) |
| Duration | **6s** |
| Motion prompt | *A vanara settles the great boulder into the bridge line; golden backlight catches the stone; a very slow push-in; ambient stone grind and surf.* + STYLE tail |
| Pass condition | Stone stays put, no morph; hand contact looks natural. **Leave the carved राम blank/rough — do NOT try to render text.** |
| Post step (later, not in Flow) | Composite the golden Devanagari **राम** as a clean overlay on the finished clip. |
| VO | "Each one marked with Ram's name, and his faith." |

---

## After Scene 1 (review gate)
- ☐ Watch all 4 clips in order. The make-or-break check is **S1-a Rama identity** — that's your quality
  ceiling for the whole film. If Rama holds here, the rest of the Rama shots (S4, S7) will too.
- ☐ If a shot fails twice, switch to that shot's **fallback** in `01_flow_shooting_script.md`.
- ☐ Keep the 4 clips silent/ambient — do NOT add narration yet. VO + music + captions are the final
  assembly pass (external), after all scenes are shot.
- ☐ Happy with Scene 1? Repeat the same method for Scenes 2-5 and 7 (Scene 6 + the logo card stay Mode B
  graphics, not generated).

**Next:** once S1-a looks right, I can write the same checklist for Scenes 2-7 (or just the next scene).
