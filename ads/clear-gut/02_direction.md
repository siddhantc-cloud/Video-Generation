# Clear Gut, DIRECTION (shot list, blocking, camera, lighting)

Conventions: vertical 9:16. Camera moves written as their own sentence (Veo parses better). Good/evil contrast: villain dark+green-murk, heroes bright+warm-glow.

| # | Shot size | Blocking | Camera (standalone) | Lighting / grade | Keyframe refs |
|---|---|---|---|---|---|
| 1 | Medium, low angle | King looms upper-center; Stomach only a faceless turned-away shadow, lower edge (no 2nd mouth) | The camera slowly pushes in on the King. | dark, sickly-green gas, hard top-light; comically-gross grin (filter-safe) | king (solo) |
| 2 | Medium close-up | Amla alone, centered, heroic stance, to camera | Locked-off with a gentle slow push-in. | BRIGHT warm golden rim-glow around Amla, clean | amla (solo) |
| 3 | Medium close-up | Ajwain alone, centered, energetic, to camera | Quick, lively gentle push-in. | bright, warm, a touch punchy | ajwain (solo) |
| 4 | Medium close-up | Saunf alone, centered, calm graceful, to camera | Smooth, slow locked dolly-in. | bright, soft, cool-warm gentle | saunf (solo) |
| 5 | Medium close-up | Haritaki alone, centered, wise powerful kindly, to camera | Slow majestic push-in. | warm gold, gentle thunder shimmer (not menacing) | haritaki (solo) |
| 6 | Wide, low angle | 4 heroes TURNED inward (3/4 / profile) shielding the Stomach, fists up, none lens-facing (no front mouths); King tiny + dark, far back | The camera cranes up slightly to reveal the full team mid-action. | heroes bright/warm; King's corner dark/green | 4 heroes + stomach |
| 7 | Centered product | Bottle dead-center; 10+ herbs swirl in as streaks of gold light and coalesce into the bottle's glowing form | The camera holds steady as the herbs swirl into the bottle. | radiant golden, magical; **bottle still, label may be soft, legible payoff is S9** | **stylized 3D bottle** (Nano-gen from product ref) |
| 8 | Medium | Happy Stomach dancing left in profile, looking AT the bottle (mouth off-lens); glowing bottle on a locked pedestal, right | Locked-off, gentle. | bright, clean, healthy warm; **bottle still & sharp** | clear_gut_product + stomach |
| 9 | Product card (NOT Veo) | Real bottle still, centered; tagline + logo text | Slow Ken-Burns zoom on the still. | clean studio warm | clear_gut_product (still, ffmpeg) |

## Hard rules carried from the skill
- Dialogue shots (1-5): the SOLE on-camera character speaks; colon syntax + "natural lip sync" + "line begins after a half-second pause"; `no subtitles, no captions, no on-screen text`; one ambient bed, no music.
- Narrated shots (6-8): "warm Hindi NARRATOR voiceover, no character moves their mouth, no visible talking."
- Bottle shots (7-8): the Clear Gut bottle stays still and does NOT morph. **Label legibility is NOT demanded in motion (Veo warps fine text, confirmed in 3.1).** S7 ends on a *forming/glowing* bottle (label may be soft); S8 keeps it still & sharp; **the guaranteed-legible label lives in S9 only** (ffmpeg card from the real PNG).
- Assembly: normalize 1080×1920/24fps → crossfade (xfade 0.4s + acrossfade) → music bed → optional burned Devanagari captions → product card last.

## Pacing
Shots 1-5 cut briskly (hook + rapid hero intros). 6 = the swell (team). 7 = the reveal beat (hold). 8, 9 = warm CTA close. **Veo `duration` is 4 / 6 / 8 only, no 7s; dialogue shots = 8s (room for the half-second pause + line), tighter beats = 6s.**
