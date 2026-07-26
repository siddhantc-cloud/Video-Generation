# Frame packet: 06-enable-rebalancing

## Project inputs

- Project: D:\startup_dev\so_sorry\CryptoBalancing-Zebpay\production\edit\animations\cryptopack-rebalancing
- Design tokens: D:\startup_dev\so_sorry\CryptoBalancing-Zebpay\production\edit\animations\cryptopack-rebalancing\frame.md
- RULES_DIR: C:\Users\SE\.agents\skills\hyperframes-animation\rules

## Assigned storyboard block

## Frame 6 — Enable Rebalancing

- scene: The real Enable Rebalancing sheet expands into the hero, the CTA receives one clean confirmation pulse, and the final frame holds.
- voiceover: "Keep your CryptoPack ready for changing markets. Enable Rebalancing today."
- duration: 4.849s
- transition_in: blur-crossfade
- status: outline
- src: compositions/frames/06-enable-rebalancing.html
- type: cta
- persuasion: Direct action after mechanism and trust proof
- beat: motivation
- blueprint: cta-morph-press
- blueprint_posture: adapt
- focal_element: authentic Enable Rebalancing button on the real confirmation sheet
- element_roles: compact Pack-ready mark = presence; enable sheet = same-center CTA; tap ring = human confirmation
- sfx: short brand resolve, tactile press, soft success bloom
- motion_rules: scale-swap-transition, physics-press-reaction, cursor-click-ripple, ambient-glow-bloom
- timeline:
  - "Scene 1 (0.0-1.2s): Hold a compact 'Ready for changing markets' mark at center with rotation-only aliveness."
  - "Scene 2 (1.2-2.3s): Condense the mark at the same center as the authentic Enable Rebalancing sheet scales into place."
  - "Scene 3 (2.3-3.0s): A touch ring approaches and lands slightly off-center on the real Enable Rebalancing button."
  - "Scene 4 (3.0-4.0s): Button and touch ring compress and release together, followed by one blue confirmation bloom and a clean one-second hold."
- asset_candidates: assets/app-enable-rebalancing.png — real Enable Rebalancing CTA

narrativeRole: Resolve the story on one unambiguous action.
keyMessage: Enable Rebalancing.

## Video direction

Use a single bright ZebPay-blue visual world across all frames. The authentic screen is always the
product proof; explanatory graphics sit beside it or emerge from it without redrawing the
underlying UI. Treat the composition like a premium mobile product film: large typography, clean
asymmetry, one focal blue, softly tinted information surfaces, generous breathing room, and no
generic crypto coins flying through space.

Reveal one idea at a time and pace every reveal to the narration cue that names it. Allocation
values may animate only inside a separate module labelled **Illustrative**. Keep captions inside the
lower safe band without covering the real app CTA. Finish with at least a one-second resolved hold
on the Enable Rebalancing button.

## Selected blueprint: cta-morph-press

# cta-morph-press — CTA Morph & Press

**intent**: A resting brand mark condenses at the same screen center into a smaller, brighter CTA, then a cursor arrives from off-stage and lands a human-aimed click on it. The viewer's eye is walked from "this is who we are" to "and this is what you do." The morph and the click are the two headline beats.

**roles served**

- CTA (from `cta-morph-press`): when the close moves from brand identity to a single user action, two elements share the same center sequentially (a morph, not a cut), and the payoff is a simulated click with physical feedback. Reach for it for a focused "click here" sign-off — no spatial set, no multi-step UI (that's `cursor-ui-demo`).
- Hook (ROLE-WIDENED, from `widget-morph-on-blank-field`): the same
  machinery run as an OPENER — a lone `[widget]` (pill / chip lockup) on a flat field transforms
  in place, performs its payload, then vanishes to a plain frame that a typed `[title]` resolves.
  The click, when present, ignites the morph rather than closing it; there may be no cursor at
  all. Reach for it when the product hook IS one widget doing one thing — still no spatial set,
  no multi-step UI (that's `cursor-ui-demo`). Mint-reconsideration trigger: if future mining
  brings 2+ more widget-morph openers with the vanish → typed-title resolve, promote this variant
  to its own blueprint (the beat order is fully inverted by then).

**duration**: 4–6s (Hook widget-morph opener 5–7.5s)

**shot structure** (a `[bg]` canvas; hero and CTA are flex-centered siblings sharing one `transform-origin`)

- **Scene 1 (0.0–~1.4s) — presence.** The `[hero mark / brand lockup]` holds dead-center, alive but resting — only a faint rotational breath on the mark; any title text under it stays rock-stable. Camera static.
- **Scene 2 (~1.4–2.4s) — the morph (signature move).** The hero CONDENSES at the same screen center into a smaller, brighter `[CTA]` (button / card): the outgoing mark shrink-fades exactly as the CTA scales up in its place. Because they share one `transform-origin`, the eye reads it as one element transforming, not a swap.
- **Scene 3 (~2.4–3.4s) — approach.** A `[cursor]` arrives from off-stage on a **decelerating** path (it "arrives," it does not pass through) and lands a few px **off** the CTA's geometric center, so the aim reads human, not scripted.
- **Scene 4 (~3.4–end) — press.** The cursor lands a physical CLICK — cursor and CTA compress together in lockstep, then release with feedback (an optional ripple / glow bloom). Holds on the clicked state.
- **Variant — Hook (widget-morph opener)** (from `widget-morph-on-blank-field`;
  reorders the beats — press first, morph second, title last). **(1) presence**: a lone
  `[pill / chip lockup]` sits centered on a flat `[field]`; optionally the `[cursor]` glides in, a
  hover pill-background appears behind the chip, and the click lands with the same lockstep press.
  **(2) the morph**: the widget transforms IN PLACE — expands downward anchored at its top edge
  into a `[menu]`, or spring-morphs outward into a `[prompt card]` with a small overshoot settle —
  new content fades/slides into place. **(3) payload**: the transformed state performs —
  `[placeholder]` types with a blinking caret, `[user text]` types while a control flips from
  muted to its vibrant active color, or the menu snap-collapses back to the pill carrying the
  `[new value]` + a checkmark pop; the background may snap to a new color under the persistent
  foreground card. **(4) resolve**: the widget VANISHES; a plain frame closes the beat — a
  `[closing title]` types on center, or a hold on the flipped solid.

**motion vocabulary**: faint rotation-only resting breath (logo scope only); same-center morph-swap (shrink-fade ↔ scale-up sharing `transform-origin`); cursor decel-arrival from off-stage; off-center human aim; lockstep press compression; release feedback ripple / glow. Hook opener: anchored downward expand of a pill into a menu and springy snap-collapse back;
chip-to-card spring morph with overshoot settle; placeholder / user-text typewriter with blinking
caret (may cut mid-word); control color-state flip muted → vibrant; background color snap under a
persistent foreground card; checkmark pop; widget vanish to blank frame; typed closing title.

**rule mapping**

- hero → CTA condense at one center → `scale-swap-transition` (shared `transform-origin: 50% 50%` is what sells the morph; CTA `position: absolute` so it doesn't shove the hero during the brief overlap)
- resting-hero aliveness (rotation only, scoped to the mark so the Phase-2 scale doesn't fight it) → `sine-wave-loop` (low-amplitude rotation register — subtle jitter, not a scale breath)
- cursor press + release in lockstep (single-target-array so both compress together) → `physics-press-reaction` (PRESS_DOWN + RELEASE portion)
- cursor approach (decel from off-stage, off-center landing, hard-cut opacity in) → `gsap-effects` (translate on `power2.out`)
- click ripple / release glow → `cursor-click-ripple` (attack-decay ring) and/or `ambient-glow-bloom` (release bloom)
- (Hook) chip → prompt-card spring morph at one center → `scale-swap-transition` (the base morph
  contract, run in the expand direction) + `card-morph-anchor` (corner-radius / surface ride-along)
- (Hook) anchored-edge expand / snap-collapse (pill ↔ menu, top edge pinned) →
  `anchored-layout-expand` (edge-anchored directional container growth — origin-pinned expansion
  with counter-scaled children; `card-morph-anchor` stays for uniform-scale morphs only)
- (Hook) placeholder + user typing, blinking caret, mid-word cut → `gsap-effects` (typewriter) +
  `context-sensitive-cursor` (blink) + `discrete-text-sequence` (mid-word cut states)
- (Hook) control color flip muted → vibrant → `press-release-spring` (color-transition variation)
- (Hook) checkmark pop / card-arrival overshoot → `spring-pop-entrance`
- (Hook) hover pill-background + igniting click → the base's `physics-press-reaction` +
  `cursor-click-ripple` mappings apply unchanged

**camera modifier**: camera-static — the morph and click happen in element space; a camera move would compete with the click as the climax. The Hook opener keeps the same contract — even the background color flip is an element-level
snap, not a camera event.

## Selected motion rule: ambient-glow-bloom

---
name: ambient-glow-bloom
description: Un-triggered soft radial glow that blooms in behind a hero element and holds with a bounded idle breathe, or a single-pass traveling sweep across a surface. No click, no word-sync — it just blooms. Finite, deterministic, seek-safe.
metadata:
  tags: glow, bloom, ambient, radial, sweep, hero, presence, finite, un-triggered
---

# Ambient Glow Bloom

A soft radial glow that **blooms in behind a hero element** (card, logo, metric) and holds, giving it presence. Unlike `press-release-spring`'s click-triggered burst or `asr-keyword-glow`'s word-timed envelope, this glow is **un-triggered** — it blooms on the hero's settle and stays lit. Two forms: a **hero bloom** that swells behind a settling element then breathes, and a **traveling sweep** that translates a soft highlight across a surface exactly once.

## How It Works

A radial-gradient layer sits **behind** the hero (glow `z-index: 1`, hero `z-index: 2` — a glow in front occludes it), starting at `opacity: 0`. Over the bloom-in window it ramps `opacity: 0 → peak` with a gentle `scale` swell, timed so `BLOOM_START + BLOOM_DUR` lands on the hero's settle — glow and hero resolve as ONE beat ("powering on"), never glow-then-card. After bloom-in:

1. **Hero bloom** — a **bounded idle breathe** during the hold: a finite `ease: "none"` tween advances a `phase` proxy and `onUpdate` nudges opacity + scale a hair around peak (never a `yoyo` loop). `sin(0) = 0` → the breathe starts exactly at the bloom's resting state.
2. **Traveling sweep** — a narrow highlight band at one edge translates **once** across to the other (`x` off-surface to off-surface), clipped to the surface (`overflow: hidden`). One pass, no return — a repeating sweep reads as a loading shimmer, not a reveal accent (the shimmer-sweep variation below is the sanctioned exception).

Peak opacity stays restrained (**≤ 0.45 hard ceiling**) so the glow gives presence without washing the frame; the glow color is **darker + more saturated** than the element it backs (a same-hue, same-lightness glow disappears into the surface).

## Recipe

```html
<!-- inside a standard scene clip -->
<div class="bloom-stage">
  <div class="bloom-glow" id="bloom-glow"></div>
  <!-- z-index: 1; inset: GLOW_INSET (negative); background: {glowGradient} -->
  <div class="hero-card" id="hero-card">{HeroLabel}</div>
  <!-- z-index: 2 -->
</div>
<!-- sweep form: <div class="sweep" id="sweep"> inside the overflow:hidden surface -->
```

```js
// ── Form A: HERO BLOOM ── bloom in soft, landing on the hero's settle.
tl.fromTo(
  "#bloom-glow",
  { opacity: 0, scale: GLOW_START_SCALE },
  { opacity: GLOW_PEAK_OPACITY, scale: 1, duration: BLOOM_DUR, ease: "power2.out" },
  BLOOM_START,
);
// Bounded breathe during the hold — finite phase tween, NOT a yoyo loop.
const glow = document.getElementById("bloom-glow");
const phase = { p: 0 };
tl.to(
  phase,
  {
    p: Math.PI * 2 * BREATHE_CYCLES,
    duration: BREATHE_DUR,
    ease: "none",
    onUpdate: () => {
      const s = Math.sin(phase.p);
      glow.style.opacity = String(GLOW_PEAK_OPACITY + s * OPACITY_AMP);
      glow.style.transform = `scale(${1 + s * SCALE_AMP})`;
    },
  },
  BLOOM_START + BLOOM_DUR,
);

// ── Form B: TRAVELING SWEEP ── one finite pass, constant glide.
tl.fromTo(
  "#sweep",
  { x: SWEEP_START_X, opacity: 0 },
  { x: SWEEP_END_X, opacity: SWEEP_PEAK_OPACITY, duration: SWEEP_DUR, ease: "none" },
  SWEEP_START,
);
tl.to("#sweep", { opacity: 0, duration: SWEEP_FADE_DUR, ease: "power1.in" }, SWEEP_FADE_START);
```

## Variations

- **Bloom-and-hold** — for scenes <3s or a hero with its own idle, skip the breathe: the single `fromTo` is the whole recipe.
- **Pulse-on-arrival** — bloom slightly PAST peak (`GLOW_OVERSHOOT_OPACITY`, `scale: 1.06`), then a second adjacent tween eases down to a steady hold — one breath punctuating the landing, no ongoing loop.
- **Multi-hero relay** — stagger per-glow `BLOOM_START` by ~0.15–0.3s across a row; shrink `OPACITY_AMP` / `SCALE_AMP` per the `/√N` rule below.
- **Diagonal raked sweep** — angle `{sweepGradient}` (~105°) across a wordmark: the classic one-pass logo sheen. Narrower `SWEEP_WIDTH`, higher `SWEEP_PEAK_OPACITY`.

### Shimmer sweep (text-clipped status-phrase working-state)

The sweep re-aimed **inside type**: a soft highlight gradient clipped into a status phrase ("Thinking…", "Analyzing dataset…") via `background-clip: text` travels left→right through the letterforms — the grey-on-grey shimmer that says _still working_. Unlike every other form here it legitimately **repeats while the status is live**: the repetition is diegetic working-state, not idle wobble (same defense as a blinking caret — the motion performs status). Two things keep it honest: it is **bounded** (one finite tween whose pass count is computed from the status window, never `repeat: -1`), and it is **killed at resolve** — the moment the status completes, the shimmer stops dead; a shimmer surviving into the answer beat turns a working indicator into decoration.

```js
// Status shimmer — N passes as ONE bounded tween. Killed at resolve.
const status = document.getElementById("status-phrase");
// CSS on #status-phrase: background: {shimmerGradient}; background-size: 300% 100%;
// -webkit-background-clip: text; background-clip: text; color: transparent;
const shimmer = { p: 0 };
const PASSES = Math.round(STATUS_DUR / PASS_PERIOD); // whole passes, computed up front
tl.to(
  shimmer,
  {
    p: PASSES,
    duration: STATUS_DUR,
    ease: "none",
    onUpdate: () => {
      const t = shimmer.p % 1; // 0→1 within each pass; percent axis inverted → left→right travel
      status.style.backgroundPosition = `${(1 - t) * 100}% 50%`;
    },
  },
  STATUS_START,
);
tl.set(status, { backgroundPosition: "100% 50%" }, STATUS_START + STATUS_DUR); // resolve: dead.
```

Keep it a whisper: `{shimmerGradient}` is the status text's own grey with one slightly-lighter band (highlight stop a step above the base, nothing near white); `background-size` ~300% keeps the band narrow in the glyphs; `PASS_PERIOD` 1.2–1.8s — slower reads as a sheen accent, faster as a spinner. Whole-number `PASSES` lands the band at its start position exactly at the kill frame, so the `tl.set` is visually a no-op. This is the working-state cousin of `gradient-text-sweep`: reach **here** when the sweep _means_ "in progress," **there** when the gradient is the typographic treatment itself.

## Values

| token                   | range / default                                        | notes                                                                      |
| ----------------------- | ------------------------------------------------------ | -------------------------------------------------------------------------- |
| GLOW_PEAK_OPACITY       | 0.15 (subtle) → 0.30 (default) → **0.45 hard ceiling** | higher washes the frame; a glow you consciously notice is too strong       |
| GLOW_INSET              | −200 to −450px (1920×1080)                             | negative so the halo extends past the hero; too small reads as a tight rim |
| GLOW_START_SCALE        | 0.80–1.0                                               | ≤1.0 — grow into place, never shrink                                       |
| BLOOM_DUR / BLOOM_START | 0.6–1.4s                                               | `BLOOM_START + BLOOM_DUR` ≈ the hero's settle frame                        |
| OPACITY_AMP / SCALE_AMP | 0.02–0.05 / 0.01–0.03 default                          | `PEAK + OPACITY_AMP ≤ 0.45`; push only when the glow is the sole motion    |
| BREATHE_CYCLES          | period 2.5–4s per breath                               | glow breathes slower than element breathing                                |
| SWEEP_WIDTH             | 15–35% of surface (grid) / 8–15% (wordmark)            |                                                                            |
| SWEEP_DUR               | 0.8–1.6s                                               | one deliberate pass — slow enough to read as light                         |
| SWEEP_PEAK_OPACITY      | 0.10 → 0.25 (default) → 0.40                           | same ≤ ~0.45 wash limit; tight sweeps tolerate the high end                |
| SWEEP_START_X / END_X   | fully off-surface both ends                            | no visible spawn/despawn mid-surface; fade reaches 0 as the band clears    |
| PASS_PERIOD (shimmer)   | 1.2–1.8s                                               | with whole-number PASSES                                                   |

## Critical Constraints

- **Glow peak opacity ≤ 0.45** — including breathe amplitude; default to the LOW end (0.15–0.30).
- **Glow behind, hero in front**; glow color darker + more saturated than the hero surface.
- **Land glow and hero as one beat** — before or after reads as two separate events.
- **Breathe is bounded, sweep is one pass** — the only sanctioned repetition is the shimmer sweep, bounded and killed at resolve.
- **Concurrent halos compound** — per-glow amps ≤ default `/√N`, stagger breathe periods (2.6s / 2.9s / 3.3s) so they don't pulse in lockstep.
- **Don't combine a `boxShadow` glow on the hero with this halo layer** — they compete and read muddy; the glow lives on the dedicated layer.

## See also

`sine-wave-loop` (hero breathes on scale/y while the glow breathes on opacity, out of phase) · `press-release-spring` (the click-triggered sibling — never both behind one element) · `counting-dynamic-scale` / `stat-bars-and-fills` (bloom behind a landing stat) · `center-outward-expansion` (sweep across the assembled grid) · `gradient-text-sweep` (the design-beat gradient counterpart).

## Selected motion rule: cursor-click-ripple

---
name: cursor-click-ripple
description: Animated mouse cursor moves to target, clicks with scale depression and expanding ripple rings.
metadata:
  tags: cursor, click, ripple, interaction, mouse, button
---

# Cursor Click Ripple

An animated cursor moves to a target element, performs a click with visual depression, and emits expanding ripple rings from the click point. Three sequential phases on one timeline: **move** (eased translation to the target's center) → **click** (scale depression on cursor + target together, yoyo back) → **ripple** (1–3 staggered rings expand and fade from the click point). This is a _point event at one location_ — a sustained hold across space is [cursor-drag.md](cursor-drag.md).

## Recipe

```html
<button class="target-button">{ctaLabel}</button>
<div class="cursor"><!-- arrow SVG, positioned at the entry corner --></div>
<!-- Rings live in DOM from t=0 at the click-target CENTER, scale 0 + opacity 0 -->
<div class="ripple ripple-1"></div>
<div class="ripple ripple-2"></div>
<div class="ripple ripple-3"></div>
```

```css
.ripple {
  position: absolute;
  left: 50%;
  top: 50%; /* click-target center */
  width: 100px;
  height: 100px;
  border-radius: 50%;
  border: 2px solid {rippleColor};
  transform: translate(-50%, -50%) scale(0);
  opacity: 0;
  pointer-events: none;
}
```

```js
// Phase 1 — Move: eased, not linear
tl.to(".cursor", { x: TARGET_X, y: TARGET_Y, duration: MOVE_DUR, ease: MOVE_EASE }, 0);

// Phase 2 — Click: cursor + target depress together, then return
tl.to(
  ".cursor",
  { scale: CURSOR_PRESS_SCALE, duration: PRESS_DUR, ease: "power2.in", yoyo: true, repeat: 1 },
  CLICK_AT,
);
tl.to(
  ".target-button",
  { scale: TARGET_PRESS_SCALE, duration: PRESS_DUR, ease: "power2.in", yoyo: true, repeat: 1 },
  CLICK_AT,
);

// Phase 3 — Ripple burst, N rings staggered from the click point
tl.set([".ripple-1", ".ripple-2", ".ripple-3"], { opacity: 1 }, RIPPLE_AT);
tl.to(
  [".ripple-1", ".ripple-2", ".ripple-3"],
  {
    scale: RIPPLE_SCALE,
    opacity: 0,
    duration: RIPPLE_DUR,
    ease: RIPPLE_EASE,
    stagger: RIPPLE_STAGGER,
    immediateRender: false, // holds scale 0 / opacity 0 until the click moment
  },
  RIPPLE_AT,
);
```

## Variations

- **Single ring** — one `.ripple`, no stagger; more elegant when the rest of the scene is busy.
- **Keyframed attack-decay** — a `keyframes` block ramps opacity 0 → peak → 0 across the duration; a clearer "energy radiates and dissipates" envelope.
- **Multi-ring expanding pulse** — 3 rings at 0.08 s stagger when the click is the scene's climactic moment.

## Values

| token                       | range                       | notes                                                                                                                                  |
| --------------------------- | --------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| MOVE_DUR                    | 0.4–1.0 s                   | short darts; long reads as a "considered click." Must end before CLICK_AT or it reads as a misclick                                    |
| MOVE_EASE                   | discrete choice             | `power2.inOut` calm · `power3.out` decisive · `back.out(1.2–1.4)` settles onto the button with a tiny recoil (higher reads cartoonish) |
| CLICK_AT                    | `MOVE_DUR + 0–0.3 s`        | zero pause reads as autopilot; >0.3 s reads as hesitation                                                                              |
| PRESS_DUR                   | 0.06–0.12 s (half; yoyo ×2) | short crisp, long mushy; must finish before the next phase needs normal scale                                                          |
| CURSOR / TARGET_PRESS_SCALE | 0.80–0.90 / 0.92–0.97       | cursor compresses MORE than the target — the cursor is the actor, the target the recipient                                             |
| RIPPLE_AT                   | `CLICK_AT + 0–0.08 s`       | simultaneous feels causal; slight delay feels acoustic                                                                                 |
| RIPPLE_DUR                  | 0.5–1.0 s                   | sharp ping vs soft sonar; must complete before anything that needs the ring gone                                                       |
| RIPPLE_SCALE                | 3–6                         | 3 stays near the click site; if the ring would exit the frame before fading, lower it                                                  |
| RIPPLE_STAGGER              | 0.06–0.12 s (or 0)          | below ~0.06 s reads as one thick ring; above ~0.12 s as separate events                                                                |
| RIPPLE_EASE                 | discrete choice             | `power2.out` standard ping · `power3.out` sharper attack · `expo.out` strong distant pulse                                             |
| TARGET_X / TARGET_Y         | layout-derived              | must match the target's visual centroid — a 4 px miss reads as missing the button                                                      |

Reference values: `../../examples/cta-orbit-collapse.html` — 0.5 s move on `back.out(1.3)`, click +0.2 s, press 0.08 s at 0.85/0.95, single ring to 5× over 0.7 s `power2.out`.

## Critical Constraints

- **Move before click** — trigger the click only after the move tween settles; clicking mid-motion reads as unintentional.
- **Rings live in DOM from t=0** at the click-target center with `scale: 0` + `opacity: 0` — never conditionally rendered; `immediateRender: false` on the expand so they hold invisible until the trigger.
- **Ripple from the click point** — the button's visual center, not any element's bounding-box origin.
- **Synchronized depression** — cursor + target depress at the same position with the same duration, and both yoyo back.
- **Cursor above all content** (high z-index) for the whole sequence; `pointer-events: none` on cursor + ripples.

## See also

`orbit-3d-entry` (click as the pivot that collapses orbiters) · `center-outward-expansion` (click triggers an outward burst) · `press-release-spring` (stronger physical feel on the target) · `scale-swap-transition` (the button's post-click state change).

## Selected motion rule: physics-press-reaction

---
name: physics-press-reaction
description: Cursor + element synchronized press via subtractive spring forces — cursor lands on element, both compress together, then release. Distinct from press-release-spring (which has no cursor).
metadata:
  tags: spring, click, physics, cursor, subtractive, interaction, synchronized
---

# Physics Press Reaction (Cursor + Element Synced)

Models a real click: a cursor approaches a button, lands, and both compress IN SYNC, then release together. Distinct from [press-release-spring.md](press-release-spring.md) (no cursor — just a press happening); this rule is the COMBINED cursor + element behavior. A single `PRESS_INTENSITY` drives both: press down compresses both to `1 - PRESS_INTENSITY` via **one targets array**, release springs both back to 1.0 with overshoot. The cursor translates to the button's center BEFORE the press starts; after release it may move on or hold.

## Recipe

```html
<button class="btn" id="btn">{ctaCopy}</button>
<!-- Cursor at scene-root level so it translates freely; arrow TIP is the click
     point, so transform-origin: 0 0 — scaling around the tip keeps it stable. -->
<svg class="cursor" id="cursor" style="pointer-events: none; transform-origin: 0 0">…</svg>
```

```js
gsap.set("#cursor", { x: CURSOR_START_X, y: CURSOR_START_Y }); // off-screen / far corner

// Phase 1 — approach
tl.to(
  "#cursor",
  { x: BUTTON_CENTER_X, y: BUTTON_CENTER_Y, duration: APPROACH_DUR, ease: "power2.inOut" },
  APPROACH_START,
);

// Phase 2 — coordinated press down: ONE targets array, same scale
tl.to(
  ["#btn", "#cursor"],
  { scale: 1 - PRESS_INTENSITY, duration: PRESS_DOWN_DUR, ease: "power1.in" },
  PRESS_DOWN_AT,
);

// Phase 3 — release: both spring back together
tl.to(
  ["#btn", "#cursor"],
  { scale: 1, duration: RELEASE_DUR, ease: `back.out(${BOUNCE_FACTOR})` },
  RELEASE_AT,
);

// Phase 4 — inner glow during press, resting shadow on release (contact confirmation)
tl.to(
  "#btn",
  { boxShadow: "{btnPressedShadow}", duration: PRESS_DOWN_DUR, ease: "power1.in" },
  PRESS_DOWN_AT,
);
tl.to(
  "#btn",
  { boxShadow: "{btnRestingShadow}", duration: RELEASE_DUR, ease: "power2.out" },
  RELEASE_AT,
);

// Cursor optionally exits after the press settles
tl.to(
  "#cursor",
  { x: CURSOR_EXIT_X, y: CURSOR_EXIT_Y, duration: CURSOR_EXIT_DUR, ease: "power2.out" },
  CURSOR_EXIT_AT,
);
```

## Variations

- **Multiple-element chain press** — press button A → A triggers a swap → cursor moves to button B → presses again; each press is one full down-release sub-routine.
- **Hold press (continuous pressure)** — insert a `HOLD_DUR` window between press-down and release: both scales stay at `1 - PRESS_INTENSITY`, inner glow stays on. Suggests "thinking" or "loading."
- **Synchronized inner-glow pulse** — during the hold, pulse the inset glow with a sine driver: a `{ p: 0 }` proxy tweened to `Math.PI * GLOW_PULSE_CYCLES * 2` on `ease: "none"`, `onUpdate` writing `boxShadow` with `alpha = GLOW_BASE_ALPHA + sin(p) * GLOW_PULSE_AMP`. Suggests "processing."

## Values

| token               | range / rule                             | notes                                                                                  |
| ------------------- | ---------------------------------------- | -------------------------------------------------------------------------------------- |
| APPROACH_START      | 0–0.3 s                                  | long delays read as a dead frame                                                       |
| APPROACH_DUR        | 0.7–1.3 s                                | faster = urgent, slower = deliberate                                                   |
| PRESS_DOWN_AT       | `= APPROACH_START + APPROACH_DUR`        | cursor arrives exactly as the press begins — avoids "tapping on air"                   |
| PRESS_DOWN_DUR      | 0.1–0.25 s                               |                                                                                        |
| RELEASE_AT          | > `PRESS_DOWN_AT + PRESS_DOWN_DUR`       | optional 0.05–0.4 s hold (or `HOLD_DUR` 0.3–0.8 s) for "thinking" interactions         |
| RELEASE_DUR         | 0.4–0.7 s                                | long enough for the overshoot to settle                                                |
| PRESS_INTENSITY     | 0.05 subtle · 0.10 standard · 0.15 heavy | applied to both cursor and button via the single targets array                         |
| BOUNCE_FACTOR       | 1.6 soft · 2.0 firm · 2.4 cartoony       |                                                                                        |
| CURSOR_START / EXIT | off-screen or far corner                 | the approach must read as motion-in, not a teleport; exit ≥ `RELEASE_AT + RELEASE_DUR` |
| BUTTON_CENTER       | measured                                 | for `place-items: center` at 1920×1080: `(960, 540)`                                   |
| BRAND_REVEAL_AT     | < `PRESS_DOWN_AT`                        | context precedes interaction                                                           |
| glow pulse          | 1–4 cycles; base α 0.15–0.3; amp 0.1–0.2 | `GLOW_BASE_ALPHA − GLOW_PULSE_AMP ≥ 0`                                                 |
| CURSOR_SIZE         | 48–96 px at 1080p                        |                                                                                        |

## Critical Constraints

- **Same press scale on cursor AND button** (one targets array) — only the button scaling makes the cursor "tap on air"; only the cursor scaling makes the button feel disconnected.
- **Cursor arrives BEFORE the press starts** — a clear "cursor over target" moment, or the press is unattributed.
- **`back.out(BOUNCE_FACTOR)` on the release, for both together** — a linear release loses the tactile feel; release MUST come after press.
- **Inner glow appears DURING press, fades on release** — outer shadow shrinks (pushed in), inner glow appears (energy concentrated).
- **Cursor `transform-origin: 0 0`** — the arrow's tip is the click point; scale around the tip keeps it stable. `pointer-events: none` on the cursor.
- **Climax dwell ≥ 1 s** — after release the composition must continue ≥ 1 s; the press is a beat, the viewer needs time to see the result.
- **No real `mouseenter` / `click` events** — HF is a render context; everything runs via the timeline.

## See also

`press-release-spring` (the BUTTON-only press; this rule layers the cursor on top) · `cursor-click-ripple` (adds a ripple at the click point) · `scale-swap-transition` (the press TRIGGERS the swap).

## Selected motion rule: scale-swap-transition

---
name: scale-swap-transition
description: Coordinated shrink-out + spring pop-in morph-like transition between two elements — no SVG path interpolation needed.
metadata:
  tags: transition, morph, scale, swap, spring, pop
---

# Scale-Swap Transition

Simulates a "morph" between two DOM elements by overlapping exit and entrance scale animations. Lighter weight than [card-morph-anchor.md](card-morph-anchor.md) (which morphs container dimensions — use that for SHAPE changes; this rule is for SAME-shape state swaps) and easier than SVG path interpolation.

At a single trigger, two coordinated tweens fire:

1. **Outgoing**: scale `1.0 → EXIT_SCALE` + opacity `1 → 0`, fast `power2.in` (rushing away).
2. **Incoming**: scale `EXIT_SCALE → 1.0` + opacity `0 → 1`, `back.out(BOUNCE_FACTOR)` (arriving with weight).

A small `OVERLAP` window during which both are mid-tween creates the morph illusion; the incoming sits on top via z-index so the outgoing's fade-tail doesn't bleed through.

## Recipe

```html
<!-- Both cards position: absolute; inset: 0 in one fixed-size wrapper — same
     footprint, same transform-origin: 50% 50%. Incoming starts opacity: 0,
     transform: scale(EXIT_SCALE), z-index above the outgoing. -->
<div class="swap-wrap">
  <div class="card outgoing" id="outgoing">{outgoingIcon} {outgoingLabel}</div>
  <div class="card incoming" id="incoming">
    {incomingIcon} {incomingLabel}
    <div class="sub" id="sub">{incomingSubline}</div>
  </div>
</div>
```

```js
// Outgoing: shrink + fade fast
tl.to(
  "#outgoing",
  { scale: EXIT_SCALE, opacity: 0, duration: EXIT_DUR, ease: "power2.in" },
  TRIGGER,
);

// Incoming: pops in with overshoot, starting OVERLAP before the exit finishes
tl.to(
  "#incoming",
  { scale: 1.0, opacity: 1, duration: ENTER_DUR, ease: `back.out(${BOUNCE_FACTOR})` },
  TRIGGER + EXIT_DUR - OVERLAP,
);

// Inner content reveals AFTER the incoming settles
tl.fromTo(
  "#sub",
  { opacity: 0, y: SUB_REVEAL_Y_PX },
  { opacity: 1, y: 0, duration: SUB_REVEAL_DUR, ease: "power3.out" },
  TRIGGER + EXIT_DUR + SUB_REVEAL_DELAY,
);
```

## Variations

- **Delayed inner content reveal** — the classic pattern above: morph the container, then reveal inner text once it settles; the 0.2–0.4 s gap lets the eye land on the new shape before reading.
- **Triple swap (3-state cycle)** — chain A→B→C with triggers `TRIGGER_AB` / `TRIGGER_BC`; each transition is its own tween pair, the previous incoming becoming the next outgoing. State-evolution narratives (early → mid → final labels).
- **Color-shift transition (no scale)** — for a flat morph between same-shape states, drop the scale and keep opacity + a brief background hue tween; less dramatic, more product-UI tone.

## Values

| token            | range                                 | notes                                                                                                  |
| ---------------- | ------------------------------------- | ------------------------------------------------------------------------------------------------------ |
| TRIGGER          | ≥ outgoing settled + a presence-dwell | the outgoing must "land" before transforming                                                           |
| EXIT_DUR         | 0.3–0.5 s                             |                                                                                                        |
| ENTER_DUR        | 0.45–0.7 s                            | longer than `EXIT_DUR` so the overshoot can settle                                                     |
| OVERLAP          | 0.1–0.2 s                             | >0.3 s both are clearly visible together (no morph); <0.05 s leaves a visible empty gap                |
| EXIT_SCALE       | 0.6–0.8                               | smaller exits feel dramatic but risk reading as "vanish" instead of "morph"                            |
| BOUNCE_FACTOR    | 1.4 soft · 1.8 firm · 2.2 cartoony    |                                                                                                        |
| SUB_REVEAL_DELAY | 0.2–0.4 s                             | reveals during the morph compete with the swap for attention                                           |
| BRAND_REVEAL_AT  | < TRIGGER                             | context (brand, eyebrow) sets the stage early; revealed AT the swap it competes with the headline beat |

## Critical Constraints

- **Incoming z-index ABOVE outgoing** — otherwise the outgoing's fade-tail (opacity 0.3–0.5) bleeds through and double-exposes the frame.
- **Both elements share `transform-origin: 50% 50%`** — different origins make the morph read as one thing teleporting elsewhere.
- **Bouncy ease ONLY on the incoming** — outgoing `power2.in`, incoming `back.out`; reversed, the swap feels mechanical.
- **Both cards `position: absolute; inset: 0`** in the same fixed-size wrapper (sized to fit both states; the wrap never resizes).
- **Don't `display: none` the outgoing** after the fade — leave it at `opacity: 0` so layout doesn't reflow.
- **Inner content reveals after the container settles**; **climax dwell ≥ 1 s** after the final state + subline land.

## See also

`press-release-spring` (a button press TRIGGERS the swap — cause and effect) · `card-morph-anchor` (shape-changing alternative) · `reactive-displacement` (when the replacement should read as a causal collision) · `sine-wave-loop` (idle breathing on the final state).
