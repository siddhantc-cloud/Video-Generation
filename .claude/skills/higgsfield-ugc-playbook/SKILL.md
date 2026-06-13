---
name: higgsfield-ugc-playbook
description: "Opinionated playbook for producing UGC-style (user-generated-content) ad videos with Higgsfield: hook-first 15s ad anatomy, preset/surface decision tree (Marketing Studio vs UGC Factory vs UGC Builder), authenticity techniques, avatar persona-matrix batching, variant fan-out strategy, and spend discipline on this machine's wired CLI+MCP. Use whenever the user wants a UGC ad, product ad video, TikTok/Reels/Shorts ad, testimonial/unboxing/try-on video, ad variants for A/B testing, or says 'make a UGC video'. For Marketing Studio API mechanics defer to higgsfield-cinematic/skills/higgsfield-marketing-studio; for prompt fundamentals defer to higgsfield-cinematic/skills/higgsfield-prompt."
user-invocable: true
metadata:
  tags: [higgsfield, ugc, ads, marketing-studio, ugc-factory, ugc-builder, batch, avatar, playbook]
  version: 1.0.0
  updated: 2026-06-11
  verified-against: "live MCP enumeration 2026-06-11 (presets/hooks/settings) + higgsfield.ai docs/blog"
---

# Higgsfield UGC Playbook (project-scoped)

The **creative + operational layer** for UGC ad production. Mechanics live elsewhere — don't duplicate them:

| Layer | Lives in |
|---|---|
| Marketing Studio API shapes, 9 presets, avatar/media slots, picklist UUIDs | `../higgsfield-cinematic/skills/higgsfield-marketing-studio/SKILL.md` (read it before any MS generation) |
| MCSLA, iteration rule, anti-slop vocabulary, I2V rules | `../higgsfield-cinematic/skills/higgsfield-prompt/SKILL.md` |
| Product/UGC genre template | `../higgsfield-cinematic/templates/02-product-ugc-showcase.md` |
| **This skill** | UGC ad anatomy, surface decision tree, authenticity stack, persona-matrix batching, spend gates |

---

## 0. SPEND GATE (non-negotiable on this account)

Marketing Studio has **NO `get_cost` preflight** — you cannot estimate before submitting. Budget anchor: **~150 credits ≈ $9 per MS video** (high anchor; plan-dependent).

1. **Never call `generate_video` (MCP) or `higgsfield generate create` (CLI) without the user's explicit go** on a written plan: N clips × preset × duration × resolution, with the anchor cost math shown.
2. **Iterate at 720p, finalize at 1080p.** Default `resolution` is 720p — keep it there until a take is approved.
3. **Audit post-hoc:** `transactions(limit=200)` (MCP) or `higgsfield account transactions` (CLI) after every batch; report actual spend vs. the plan.
4. Non-MS models (Kling, Veo, etc.) DO support preflight — `generate cost <model>` / `get_cost: true`. Always run it first there.

---

## 1. Anatomy of a UGC ad (the 15-second skeleton)

Marketing Studio caps clips at **4–15s**. The platform-native sweet spot is **15–30s** total → one MS clip, or two stitched. Default **9:16**, casual register.

| Beat | Time | What happens | Craft rule |
|---|---|---|---|
| **Hook** | 0–2s | Scroll-stopper: trend-shaped, relatable, or a picklist hook (stunt/subtle) | Never open on the product alone; open on a person/situation |
| **Context** | 2–5s | The problem or POV, first-person ("I", "you") | Caption overlay carries it: `POV: you're a gym bro who can't cook…` |
| **Demo** | 5–11s | Product in hands, in use, in the real environment | One primary action only; product visibly held ≥ once per 5s |
| **Payoff + CTA** | 11–15s | Result + one-line verdict to camera | Conversational verdict beats slogan: *"Cue said fifteen minutes. It was fifteen minutes."* |

**Dialogue budget: ~25–30 spoken words per 15s.** More gets rushed or cut. Write the script first, then trim to the line where the verdict lands.

**Hook strategy:** trend-driven, relatable openings outperform polished ones. The 9 picklist hooks are *visual scene templates* (not copy) in two families — `stunt` (Product Hit, Random Object Mic, Blizzard, Product Dodge) and `subtle` (Spicy, Interview, Product Crash, Camera Bump, Epic Fail). Subtle for beauty/lifestyle; stunt for attention-economy products. Skipping the hook (omit `hook_id`) is correct for testimonial-register ads.

---

## 2. Surface decision tree — three UGC surfaces exist now

Research current as of 2026-06-11. The cinematic skill (v3.7.16) predates the last two.

```
Need a UGC ad?
├─ Product/app ad, ≤15s, preset structure wanted        → Marketing Studio `ugc` preset (MCP-drivable from here)
├─ Heavy spoken script, per-scene direction, lip-sync   → UGC Builder (web UI; Veo-3-backed lip-sync+audio)
├─ Product keyframes / multi-angle consistency / 70+ language localization → UGC Factory (web UI; Nano-Banana-powered, 4 keyframes per gen, auto re-lip-sync per language)
├─ Dialogue-led but free-form (no ad framing)           → Veo 3.1 / Kling 3.0 direct (preflight cost first)
└─ ASMR variant                                         → MS `ugc` preset + `generate_audio: true` + intimate setting (Bedroom/Bathroom) + NO hook
```

- **UGC Builder and UGC Factory are web-UI surfaces** — not exposed as MCP models on this connector (verified: `models_explore`/MS presets show no builder/factory model IDs). Treat them as manual steps in a plan, not automatable calls.
- **`product` vs `webproduct` matters:** advertising a physical item → `product`; advertising an app/site/service as a whole → `webproduct` (App Store / Play Store URLs ⇒ always `webproduct`).
- Within Marketing Studio, the UGC-family presets and when to pick each: `ugc` (selfie testimonial) · `product_review` (measured talking-head + B-roll) · `tutorial` (step-by-step, cuts allowed) · `ugc_unboxing` (first-touch reveal) · `ugc_virtual_try_on` (casual try-on) — full register rules in the marketing-studio sub-skill §3.

---

## 3. The authenticity stack (what makes it read as UGC, not as an ad)

Ranked by impact. The whole genre's premise: **lo-fi beats polish** on TikTok/Reels/Shorts.

1. **Phone-native framing** — selfie or handheld eye-level, single continuous take. Never dolly/crane/orbit language in a `ugc` preset prompt (that's TV Spot register).
2. **Real environment over studio** — pick a `realistic` setting (Bedroom, Bathroom, Kitchen, Office, In Car, Street, Gym, Nature). The `unrealistic` six (Airplane Wing, Roofing, Volcano Rim, Tiny Reviewer, Car Roof, Train Surf) are deliberate absurdist attention plays — use for stunt-hook ads only.
3. **Imperfection cues** — "natural speech, brief pauses", ambient noise, uneven lighting. Positive phrasing only (engine prefers it): say `handheld phone camera, available light` not "no studio lighting".
4. **First-person script register** — contractions, filler-lite, verdict sentences. No brand-speak ("revolutionary", "game-changing" = instant ad-smell).
5. **Caption overlay as the hook carrier** — `POV: …` overlays outperform spoken hooks for sound-off feeds.
6. **App/UI demos: freeze the interface** — when the product is an app, append: **"Do not animate any app interface"** — UI screens display statically on the phone (animated fake UI reads as AI slop). Generate the UI screens first with GPT Image (renders text accurately), pass as reference media.
7. **Avatar fidelity lock** — when identity must hold: *"use her exact face, hair, and body throughout the entire video without any changes."*

---

## 4. Avatar strategy → the persona matrix

One avatar per generation, always pass one explicitly (empty `avatars: []` = random face per render, kills consistency). Three types: preset (~40 in library), uploaded, text-generated (e.g. *"elegant 60-year-old woman"*).

**The persona matrix is the core UGC growth tactic:** the same product gets different *emotional entry points* per audience —

| Persona | Hook angle | Setting | Avatar |
|---|---|---|---|
| Exhausted home cook | "staring at scattered ingredients" | Kitchen | 30s casual |
| Gym bro | "POV: you can't cook but track macros" | Gym → Kitchen | athletic 20s |
| Busy professional | "squeezed between meetings" | Office | 30–40s business-casual |

Write ONE locked prompt; vary only avatar + setting + hook per variant. Localization (different markets) is UGC Factory's job — 70+ languages with auto re-lip-sync — not a prompt rewrite.

---

## 5. Batch workflow: lock → fan out

**Phase 1 — LOCK (single-variable iteration, 720p):**
1. Draft script (≤30 words) + prompt; spend-gate approval.
2. Generate one baseline. Wrong? Change exactly ONE variable per retake (iteration rule). 2–3 takes typical.
3. User approves the take → prompt is locked.

**Phase 2 — FAN OUT (batch, this is where UGC wins):**
4. Re-enumerate picklists live (UUIDs drift): `show_marketing_studio(action='list', type='hook'|'setting'|'avatar', size=100)`.
5. Matrix = locked prompt × {avatars} × {hooks/settings}. Practitioners run 50+ variants per product launch; start with 6–9 (3 personas × 2–3 hooks) and let platform A/B data choose before scaling.
6. Name outputs `<product>_<preset>_<persona>_<hook>_<n>` in the plan so spend audit maps 1:1 to variants.
7. Post-batch: `transactions` audit (spend gate §0.3) + record which variant won in this project's memory.

**Iteration etiquette when a take misses:** bring the prompt back, edit only the failing part (don't regenerate from a rewritten prompt — you lose the cause-effect signal).

---

## 6. Prompt patterns (UGC register)

**Vanilla UGC — prompt optional.** Preset + product + avatar + hook/setting picks generate fine with NO prompt. Add a short flowing paragraph (<50 words) only for tone/persona:

```
She's mid-morning-routine, hair up, talking to her front camera like a friend.
Casual, a little rushed. She holds the serum up once, taps the dropper,
keeps talking. Handheld phone framing, available window light.
```

**App-demo UGC — the static-UI pattern:**

```
A woman stares at scattered ingredients on her counter, overwhelmed. She opens
the CUE app, scans the ingredients with her phone, a recipe appears. She cooks
with sudden purpose, quick cuts, plates the dish. Do not animate any app
interface — UI screens display statically on the phone. Caption overlay:
"POV: dinner in 15 minutes". Handheld selfie register, kitchen daylight. 9:16.
```

**Multi-beat (only when beats genuinely differ):** time-coded sections `0–3s / 4–7s / …` per the marketing-studio sub-skill §8. Don't section a single-take testimonial.

**Verdict line pattern for the CTA beat:** product promise, restated as lived experience, deadpan: *"It said fifteen minutes. It was fifteen minutes."*

---

## 7. Live snapshot (2026-06-11) — names only, enumerate for UUIDs

Verified via live MCP enumeration; identical names to the 2026-05-18 snapshot in the cinematic skill, UUIDs current then but **always re-enumerate before a batch**:

- **Presets (9):** ugc, tutorial, ugc_unboxing, hyper_motion, product_review, tv_spot, wild_card, ugc_virtual_try_on, virtual_try_on *(slug for Pro VTO is `virtual_try_on` — non-obvious)*
- **Hooks (9):** stunt — Product Hit, Random Object Mic, Blizzard, Product Dodge · subtle — Spicy, Interview, Product Crash, Camera Bump, Epic Fail
- **Settings (14):** realistic — Bedroom, Bathroom, Kitchen, Office, In Car, Street, Gym, Nature · unrealistic — Airplane Wing, Roofing, Volcano Rim, Tiny Reviewer, Car Roof, Train Surf

---

## 8. The Foundry pipeline — our model-flexible alternative to UGC Factory

When preset routing isn't wanted (or MS pricing isn't), run the custom chain. **All costs live-preflighted 2026-06-11** (9:16; CLI `generate cost`, no jobs submitted):

| Stage | Tool | Model ID | Cost |
|---|---|---|---|
| 1. Keyframes (product + avatar in scene, 2–4 angles) | image gen, up to 14 refs | `nano_banana_2` (Nano Banana Pro) | 2 cr/image |
| 2a. Animate — silent demo / text-overlay UGC | I2V from keyframe | `kling3_0` | 16 cr/8s · 30 cr/15s |
| 2b. Animate — spoken testimonial (lip-sync) | native audio | `seedance1_5` (best lip-sync, multilingual) | 9.6 cr/8s |
| 2c. Animate — budget volume runs | T2V/I2V | `veo3_1_lite` | 8 cr/8s |
| 2d. Animate — premium ref-consistency | up to 3 refs, first/last frame | `veo3_1` | 22 cr/8s |
| 3. Variant fan-out | edit keyframe face/setting via NB Pro, re-animate | `nano_banana_2` + 2a/b/c | ~2 + animate cost |
| 4. Finalize | upscale approved take | MCP `upscale_video` | varies |

**Cost reality vs Marketing Studio:** locked 15s ad on Kling ≈ **~34 cr** (keyframes + animate) vs MS ~150 cr anchor — **~4× cheaper per variant**, *with* preflight cost certainty MS can't give. Wholly MCP/CLI-drivable → scriptable persona-matrix batches.

**Model router rule (the flexibility UGC Factory doesn't give):** silent/caption-led → `kling3_0` · spoken script → `seedance1_5` or `kling3_0` native audio · volume A/B sweeps → `veo3_1_lite` · product-fidelity hero → `veo3_1` with product refs. Always `generate cost` preflight first — these numbers drift.

**Where UGC Factory still wins (don't rebuild these):** turnkey 70+ language auto-translate + re-lip-sync localization; zero-setup speed for one-off ads. Use the web UI for those; use the Foundry for everything where cost, model choice, or batch control matters.

**Caveats:** Recast/Lipsync Studio are web-UI apps (not MCP) — avatar swap on existing motion is a manual step. Seedance-family blocks real-person face inputs — synthetic avatars only there (use Kling for real likenesses). Head-to-head output quality vs UGC Factory is **unverified** until we run one paired eval (same product, one Factory output vs one Foundry output).

---

## 9. Sources

- [Higgsfield Marketing Studio intro](https://higgsfield.ai/marketing-studio-intro) — presets, 4-step workflow, avatar library
- [Higgsfield blog: full marketing-stack prompts](https://higgsfield.ai/blog/marketing-studio-video-2) — the CUE app worked examples (§6 patterns derive from these)
- [Higgsfield UGC Factory](https://higgsfield.ai/ugc-factory) + [UGC Factory explained](https://higgsfield.ai/blog/Higgsfield-UGC-Factory-Explained) — keyframes, localization
- [Higgsfield UGC Builder](https://higgsfield.ai/blog/Higgsfield-UGC-Builder-Gives-You-the-Director-Every-Scene) — per-scene direction, Veo-3 lip-sync
- [VO3: 5 steps to viral UGC ads with Higgsfield](https://www.vo3ai.com/blog/5-steps-launch-viral-ugc-ads-with-higgsfield-studio-no-camera-needed-2026-04-23) — 15–30s sweet spot, 50+ variants/launch, trend-driven hooks
- Internal: `higgsfield-cinematic` v3.7.16 marketing-studio sub-skill (Phase-0-probed API ground truth) + live MCP enumeration 2026-06-11
