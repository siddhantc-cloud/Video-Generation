# Video 1 — “PUNJAB DI KURSI: THE FREEBIE TRAP” · Production Playbook

> The executable plan for our first showcase clip. Single ~14s silent, text-driven Seedance shot; caricature Modi / Shah / Kejriwal; So Sorry house style. This is the **foundation** video — its 3-character bible is reused in V2–V4.
>
> Governing docs: `../../so-sorry-higgsfield-strategy.md` (how-to + Consistency Cheat-Sheet), `../../so-sorry-showcase-roadmap.md` (ladder + costing).

---

## LOCKED SCRIPT  *(approved — balanced satire, no citizens)*

**Format:** single ~14s Seedance shot · So Sorry 3D caricature · **silent + English on-screen text & comic SFX, no dialogue** · 16:9
**Cast:** **Kejriwal** (glasses, mustache, sweater + muffler) · **Modi** (white beard, glasses, kurta) · **Amit Shah** (bald, glasses, waistcoat — *the strategist*) · the **PUNJAB chair** (golden, labelled).
**Theme:** balanced jab at competitive freebie/revdi politics — both camps try to win the chair with freebies; the chair (Punjab) refuses to be bought.

| Beat | Visual | On-screen text / SFX |
|------|--------|----------------------|
| **1 — THE BAIT** (0:00–0:04) | Golden chair labelled **PUNJAB** center-stage. **Kejriwal** sneaks in from the left, unspooling a glowing electricity wire, lassoes one chair-leg. Sneaky grin, tiptoe walk. | Title flash **"OPERATION: KURSI"** · glowing wire tag **"FREE BIJLI ⚡"** · SFX *"sneak… sneak…"* |
| **2 — THE COUNTER-MOVE** (0:04–0:09) | **Modi** strides in from the right; **Amit Shah** behind as the strategist, holding a giant **"PLAN-B"** blueprint, whispering & pointing. On his cue Modi flings ration-sacks that rope the other chair-leg. **Tug-of-war** — the chair stretches and wobbles between the two camps. | **"FREE RATION!"** · **"FREE CYLINDER!"** · bug-eyed strain, sweat-drops, motion lines · SFX *"TUG!"* |
| **3 — PUNJAB DECIDES** (0:09–0:14) | The overloaded chair **sprouts tiny legs, SNAPS every wire and rope** — Kejriwal flies off one way, Modi+Shah crash in a heap — shrugs off the freebies, and trots to center stage, alone and dignified under a spotlight. The three sit dazed in the dust. | SFX **"TWANG!"**, **"DHADAAM!"** · final card **"PUNJAB ISN'T FOR SALE — IT'S EARNED"** |

---

## 0. Definition of "best quality" — the bar we're gating against

V1 PASSES only when ALL of these are true (this is the QC contract, not a vibe):
1. **Style fidelity:** placed side-by-side with a real *So Sorry* frame, it reads as the same show.
2. **Caricature recognizability:** Modi, Shah, Kejriwal each instantly identifiable.
3. **Consistency through the whole clip:** all three stay on-model across *every* extracted frame, not just the endpoints.
4. **Motion quality:** slapstick reads as intentional, no melting/jitter/limb-morph (human verdict).
5. **Readable in-style text:** the SFX text + final card render cleanly in the cartoon style.
6. **No disqualifying artifacts:** hands, faces, the chair hold up under frame-by-frame inspection.

If any fails → iterate on that specific axis. We do not ship a "good enough" first video; the whole point is best-achievable quality.

---

## 1. The stack — every skill/agent and its job

| Tool / skill / agent | Role in V1 |
|----------------------|------------|
| **`so-sorry-director`** (agent) | Orchestrates the whole run, maintains this workspace, enforces the phase gates, does still + multi-frame QC, hands off motion verdicts to you |
| **`seedance-satire-director`** (skill) | Converts the shot into the production-ready Seedance prompt JSON (engine rules, `mode: animation`, in-style text SFX, `Total:` line, no-audio) |
| **`higgsfield-cinematic`** (skill) | Refines the MCSLA prompt, camera presets, model nuance; troubleshoots failed gens |
| **`higgsfield:generate`** (skill) → CLI / `mcp__higgsfield__*` | Executes image + video generations |
| **`higgsfield:soul-id`** (skill) | *Optional / likely skip* — caricatures use reference sheets, not real-face Soul ID |
| **Higgsfield Angles** | Spins each caricature master into a turnaround; alternate-angle coverage |
| **Nano Banana Pro / Soul Cinema** | Image gen for caricature sheets, expression sheets, location plate, keyframe |
| **Kling 3.0** | Cheap previz to block timing/gag before spending Seedance credits |
| **Seedance 2.0** | The final animation engine for the hero shot |
| **`ffmpeg`** (installed, Win + WSL) | Extract frame sequences from candidate clips for multi-frame visual QC |

---

## 2. Step-by-step — every step has a measurable success criterion

Legend: **Tool** = what runs it · **✅ Pass** = the checkable success criterion · **❌ Fail →** = what to do if it misses. Phases end in a **GATE** that must pass before the next phase starts.

**Gate order (why it's this sequence):** Script is a thin *spec-lock* that defines the asset manifest → **the first visual/production gate is the Character + Expression sheets (GATE 2)** → the Storyboard (beat keyframes) comes *next* because it references the locked characters → then animation. Sheets must precede the storyboard; the storyboard can't be in the same gate as the sheets it depends on.

### Phase 1 — Script  *(PASSED)*
| Step | Action | Tool | ✅ Pass criterion |
|------|--------|------|-------------------|
| 1.1 | Lock the Freebie Trap beat sheet (silent, English text, single ~14s shot) | — | ✅ Approved (see LOCKED SCRIPT above); one shot, no dialogue, balanced, 3 beats |
**GATE 1:** ✅ user-approved script. *(met)*

### Phase 2 — Style lock + asset bible  *(make-or-break; no animation until GATE 2 passes)*
| Step | Action | Tool | ✅ Pass criterion · ❌ Fail → |
|------|--------|------|------------------------------|
| 2.1 | Ingest real So Sorry frames | user provides → `bible/refs/` | **≥8 clean, varied frames** (full-body, face CU, 2-char, wide). ❌ <8 or low-res → request more |
| 2.2 | Derive + calibrate the house-style text block | Read frames + write block | Block names render-finish, head:body ratio, palette, lighting; a 1 test image from it **sits convincingly beside a real frame** (your eye + my Read). ❌ off → adjust wording, re-test |
| 2.3 | Face gen — per figure (Modi/Shah/Kejriwal) | `generate_image` soul_2/nano_banana_pro | Figure **instantly recognizable** in So Sorry style; bone structure **stable across 3 regenerations**. ❌ unstable → fix base prompt, re-run |
| 2.4 | Outfit gen — per figure | `generate_image` | Signature attire correct; **every accessory written explicitly** (Modi kurta, Shah waistcoat, Kejriwal sweater+muffler). ❌ missing detail → add, re-run |
| 2.5 | Master sheet (fuse face+outfit) — per figure | `nano_banana_pro` | Full-body, white bg, on-style, recognizable; **passes side-by-side vs a real frame**. ❌ → edit-in-place (not regenerate) |
| 2.6 | Expression set — per figure (neutral/sneaky/shock/sprawled) | `generate_image` (edit from master) | **Same face structure across all 4 expressions** — no morphing. ❌ morph → re-derive from master |
| 2.7 | Turnaround — per figure | **Higgsfield Angles** (spin master) | front/L/R/back **clearly the same character**. ❌ drift → re-spin or Nano Banana fallback |
| 2.8 | Location plate (stage + PUNJAB chair, multi-view) | `generate_image` + Angles | On-style; chair prominent; **"PUNJAB" label legible**. ❌ → regenerate |
| 2.9 | Register `@tags` + write a Character Anchor Block per figure | Write to `bible/` | Every asset tagged; anchor block exists per character |
**GATE 2 (strict):** ✅ all 3 caricatures (master + expressions + turnaround) **and** the plate are on-style and recognizable, **each passing a side-by-side vs a real So Sorry frame.** ❌ any fail → do not advance.

### Phase 3 — Storyboard (beat keyframes) + shot prompt
*The single-shot "storyboard" = 2–3 still keyframes, one per beat, built FROM the locked sheets. These double as the Seedance `start_image` / `end_image` bookends.*
| Step | Action | Tool | ✅ Pass criterion · ❌ Fail → |
|------|--------|------|------------------------------|
| 3.1 | Build the shot prompt | **`seedance-satire-director`** | Valid single-scene JSON: `mode: animation`, three-layer Dynamic, in-style text SFX (PHEEE!/DHADAAM!/OYE!) + final card, **no audio**, closing `Total:` line, **turnarounds tagged at each name** |
| 3.2 | **Beat-board keyframe A — "the bait/tug-of-war"** (start frame): PUNJAB chair center; Kejriwal at left with the FREE BIJLI wire, Modi+Shah at right with ration-sack ropes, all roping the chair | `generate_image` (from sheets) | **All 3 recognizable + on-model in ONE frame**; chair labeled; freebie tags legible; reads as the setup. ❌ a figure off → 3.4 |
| 3.3 | **Beat-board keyframe B — "Punjab walks off"** (end frame): chair on tiny legs, snapped ropes dangling, alone center under spotlight; Kejriwal sprawled one side, Modi+Shah heaped the other | `generate_image` (from sheets) | All 3 on-model; matches the punchline; **visually consistent with frame A** (same style/lighting) |
| 3.4 | Repair any off-model figure | `nano_banana_pro` **edit-in-place** | Corrected **without losing composition/lighting**. ❌ twice → re-board |
**GATE 3 (Storyboard):** ✅ a 2-frame beat-board (start + end), all three on-model + on-style in both, consistent with each other — ready to bracket the Seedance shot.

### Phase 4 — Previz  *(cheap — protect Seedance credits)*
| Step | Action | Tool | ✅ Pass criterion · ❌ Fail → |
|------|--------|------|------------------------------|
| 4.1 | Block the gag motion | **`kling3_0`** ~10–15 passes (~6 cr ea) from keyframe | **≥1 pass shows the 3 beats** (bait → tug-of-war → chair snaps free & walks off) at acceptable timing. ❌ none → adjust keyframe/prompt before spending Seedance |
**GATE 4:** ✅ a chosen motion/timing direction.

### Phase 5 — Finalize (Seedance 2.0)
| Step | Action | Tool | ✅ Pass criterion · ❌ Fail → |
|------|--------|------|------------------------------|
| 5.1 | Generate hero shot | **`seedance_2_0`** (genre comedy; **beat-board A as `start_image`, beat-board B as `end_image`**; sheets tagged) | Clip at 12s / 16:9 produced, landing on the approved end frame |
| 5.2 | Multi-frame visual QC per candidate | **ffmpeg** (evenly-spaced + 1 per beat) → Read | Across **all** extracted frames: 3 figures on-model, **no artifacts** (hands/faces/chair), all beats present, text legible. ❌ → discard, adjust |
| 5.3 | Motion verdict (what stills can't show) | **user** | Slapstick reads as intentional; **no melt/jitter/limb-morph**; chair-run reads as a gag. ❌ → iterate |
| 5.4 | Iterate to best | keep-best; **two-strikes → change approach**, log `FAILURE.md` | A candidate passes **5.2 + 5.3** |
**GATE 5:** ✅ a clip passing multi-frame QC **and** your motion verdict.

### Phase 6 — Text & polish
| Step | Action | Tool | ✅ Pass criterion · ❌ Fail → |
|------|--------|------|------------------------------|
| 6.1 | Decide per text element: in-shot (Seedance) vs added in edit | director call | SFX text in-style in-shot; **final card cleanest in edit** if in-shot text garbles |
| 6.2 | Verify legibility | Read frames | **Every text element readable** and on-style. ❌ garbled → move to edit |
**GATE 6:** ✅ all text readable + on-style.

### Phase 7 — Fidelity QC + deliver
| Step | Action | Tool | ✅ Pass criterion · ❌ Fail → |
|------|--------|------|------------------------------|
| 7.1 | Side-by-side vs a real So Sorry frame | user + Read | **Reads as a So Sorry episode** (your call). ❌ → loop to weakest phase |
| 7.2 | Consistency spot-check across non-adjacent frames | ffmpeg + Read | Same 3 figures, on-model throughout |
| 7.3 | Optional: virality signal | `virality_predictor` | Secondary only — not a gate |
| 7.4 | Export + archive | ffmpeg/NLE | 16:9 (+9:16 if wanted) in folder; **3-char bible saved for reuse**; learnings logged for V2 |
**GATE 7 (DONE):** ✅ the §0 quality bar fully met **and** a final export exists.

---

## 3. How we ensure best quality — the QC mechanisms (fires at every step)

| Mechanism | What it catches | When |
|-----------|-----------------|------|
| **Real-frame style anchor** | "Looks AI, not So Sorry" | Phase 2a, re-checked at keyframe + final |
| **Strict asset gate** | Bad characters poisoning every downstream shot | End of Phase 2 |
| **Read-image QC on every still** | Off-model faces, wrong proportions, artifacts | Phases 2, 3 |
| **Edit-don't-regenerate** | Losing a good composition while fixing one detail | Phases 2, 3, 5 |
| **Turnaround tagged at name** | Limb/proportion morphing across the clip | Phase 5 (every gen) |
| **Cheap previz on Kling** | Wasting Seedance credits on bad timing | Phase 4 |
| **Multi-frame ffmpeg QC** | Mid-clip drift/artifacts (not just endpoints) | Phase 5 (every candidate) |
| **Human motion verdict** | Jitter, melting, comedic timing, anything stills miss | Phases 5–6 |
| **Two-strikes → change approach** | Burning credits looping a failing prompt | Throughout |
| **Side-by-side benchmark** | Final fidelity vs the real show | Phase 7 |
| **Cost guardrail** | Runaway iteration | Throughout (Kling previz, capped Seedance) |

---

## 4. Draft prompts (starting points — recalibrate against the real frames)

**House-style block (placeholder until frames arrive):**
> *3D-rendered politoon caricature, So Sorry house style: heavily exaggerated oversized head on a smaller body, smooth stylized 3D surfacing, clean bright even lighting, bold saturated colors, crisp readable silhouettes, expressive cartoon acting.*

**Caricature master sheet (repeat per figure — feature-based, recognizable):**
> *`<<<style_frame>>>` is the STYLE reference ONLY — match its render finish, proportions, lighting. Create a caricatured 3D politoon of [Modi: round glasses, full white beard, side-parted white hair / Shah: bald crown, glasses, clean-shaven, stocky / Kejriwal: black mustache, glasses, simple sweater + muffler], oversized head, full-body, neutral pose, white studio background.*

**Expression sheet:** *grid — neutral, sneaky/scheming, wide-eyed shock, comically sprawled — same character, consistent design.*

**Location plate:** *empty show-stage, a single grand golden throne-chair labelled "PUNJAB" center, spotlights, So Sorry style, wide establishing.*

**Hero shot (seedance-satire-director will formalize):**
> *Style & Mood: So Sorry 3D politoon caricature, bright stage lighting, bold saturated colors. Dynamic Description: a golden chair labelled PUNJAB sits center-stage; @kejriwal [turnaround] tiptoes in from the left unspooling a glowing "FREE BIJLI" electricity wire and lassoes a chair-leg (sneaky grin); @modi [turnaround] strides in from the right with @shah [turnaround] behind him holding a "PLAN-B" blueprint, whispering & pointing — Modi flings ration-sack ropes onto the other chair-leg; a frantic tug-of-war, the chair stretching and wobbling, bug-eyed strain, sweat-drops [VFX: motion lines, comic strain marks]; the chair suddenly sprouts tiny legs, SNAPS every wire and rope [VFX: TWANG snap, dust puff] — Kejriwal flies off left, Modi+Shah crash in a heap right — and the chair trots to center, alone under a spotlight. On-screen text in-style: "OPERATION: KURSI", "FREE BIJLI ⚡", "FREE RATION!", "TWANG!", final card "PUNJAB ISN'T FOR SALE — IT'S EARNED". Static Description: show-stage, golden PUNJAB chair, spotlights, dark backdrop. NO MUSIC / NO SFX (silent + text). Total: 14s / 3 beats / 16:9.*

---

## 5. V1-specific risks & mitigations

| Risk | Why it's the hard part | Mitigation |
|------|------------------------|------------|
| **3 caricatures in ONE shot drifting** | Multi-character consistency is the hardest single-shot ask | Lock all 3 sheets first; tag turnarounds at names; multi-frame QC; re-keyframe if one figure breaks |
| Style reads generic, not So Sorry | Text prompts alone can't clone a look | Real frames as style refs — non-negotiable |
| The "chair runs away" gag rendering wrong | Surreal motion can confuse the engine | Previz on Kling first; describe as simple intent ("chair sprouts legs, scoots away"), don't over-choreograph |
| In-shot text garbled | Engines can mangle long text | Keep text short; consider adding the final card in edit instead |
| Iteration cost runaway | 3-char slapstick may need many gens | Kling previz, cap Seedance attempts per approach, two-strikes rule |

---

## 6. Definition of done & next
- **Done when:** the §0 bar is met and a final 16:9 export exists in this folder, with the 3-character bible saved for reuse.
- **Act 1 status:** ✅ DONE → `renders/v1_final.mp4`.

---

# ACT 2 — "THE VAADA FACTORY"  *(the first appended act of the growing film)*

> **Capability proven:** multi-scene + frame-chaining + B-roll (continuity across cuts). **Story:** the trio refuse to quit — they chase the runaway chair, build a promise-factory, lay a bait-trail; cliffhanger = the chair eyes the bait. Continues directly from Act 1's final frame.
> **Engine policy (locked, see `../../so-sorry-model-policy.md`):** images `nano_banana_pro` (2cr) · previz `kling3_0` **std** (20/10s) · finalize `kling3_0` **pro** (25/10s) · Seedance only if Kling can't sell a shot. **Style = 2D caricature, matching `renders/v1_final.mp4`** (NOT 3D).

## Act 2 LOCKED SCRIPT
**Format:** 3 chained scenes + 2 B-roll cutaways · silent + ambient SFX + on-screen text · 16:9 · ~12–14s total.
**Cast/Elements:** `<<<modi>>>` `<<<amit-shah>>>` `<<<kejriwal>>>` + the runaway **PUNJAB chair** (now a sentient character on tiny legs).

| Scene | Visual | On-screen text / SFX |
|-------|--------|----------------------|
| **S1 — THE CHASE TRIGGER** (~4s) *(seam: opens on Act 1's EXACT final composition)* | Chair center, **Kejriwal sprawled far left**, **Modi+Shah heaped right**, snapped ropes dangling, spotlit stage. They blink awake, spring up, shoot each other a competitive glare, and bolt off-frame chasing the (escaped) chair. Whip-pan exit. | **"BUT THE NETA NEVER QUITS…"** · SFX *boing, whoosh* |
| **S2 — THE VAADA FACTORY** (~5s) | Interior of a surreal promise-factory: a big conveyor-machine churns out balloons & crates stamped **NAUKRI / FREE BIJLI / KISAN KARZ MAAF / LAPTOP**. The trio crank it into overdrive — gears, smoke, freebies piling sky-high. | Title **"THE VAADA FACTORY"** · **"NAUKRI!" "BIJLI!" "KARZ MAAF!"** · SFX *clank, ka-ching* |
| **S3 — THE BAIT-TRAIL** (~4s) *(cliffhanger)* | They lay a glittering trail of freebies leading into a big net/snare; duck behind a crate, grinning, peeking. The runaway **PUNJAB chair** peeks in from the frame edge on its tiny legs, eyeing the bait — freeze on temptation. | **"THE TRAP IS SET…"** · SFX *sparkle, suspense sting* |
| **B-roll B1** (insert at S1→S2 seam) | Extreme CU: a **NAUKRI** balloon inflating bigger and bigger, label stretching. | — |
| **B-roll B2** (insert at S2→S3 seam) | CU: a rubber-stamp slams **"VAADA"** onto a crate, dust puff. | — |

**Continuity contract (the Act-2 capability):**
- **Invisible seam to Act 1:** S1's `start_image` = `bible/refs/act2/act1_final_frame.png` (same poses/positions/lighting). The cut from Act 1 must be unnoticeable.
- **Frame-chaining within Act 2:** each scene animated `start_image → end_image`; the end keyframe of a scene seeds the next where the location is continuous; hard location cut (stage→factory) is absorbed by a B-roll cutaway.
- **Character lock:** all three via Elements every gen; multi-frame QC across each seam, not just endpoints.
- **Look lock:** same 2D palette/lighting as Act 1; re-grade in the master concat.

## Act 2 keyframes (nano_banana_pro, 2cr each)
| KF | Role | Content |
|----|------|---------|
| KF1 | S1 start | = `act1_final_frame.png` (already have) |
| KF2 | S1 end | trio sprung to their feet mid-glare, chair-shaped gap center, motion lines, about to bolt |
| KF3 | S2 start | wide of the Vaada Factory interior; trio arriving at the machine |
| KF4 | S2 end | factory in overdrive, freebies (NAUKRI/BIJLI/KARZ MAAF/LAPTOP) piling up, trio cranking |
| KF5 | S3 end | bait-trail laid into a net; trio hiding behind a crate; PUNJAB chair peeking in at frame edge |
| B1 | B-roll | extreme CU NAUKRI balloon inflating |
| B2 | B-roll | CU rubber-stamp "VAADA" hitting a crate |

## Act 2 gates
- **GATE 2A (keyframes):** KF1–KF5 + B-roll on-model (all 3 via Elements), 2D-style-consistent with Act 1, factory reads clearly, freebie labels legible. ❌ → edit-in-place.
- **GATE 2B (previz):** Kling std passes per scene show acceptable motion/timing; the S1 seam from Act 1 reads as continuous. ❌ → adjust keyframe/prompt before pro.
- **GATE 2C (finalize):** Kling pro finals per scene pass multi-frame QC (no drift/artifacts across seams) + your motion verdict.
- **GATE 2D (assembly):** scenes + B-roll concatenated → `renders/act2/act2_final.mp4`; then concatenated with Act 1 → `renders/punjab_di_kursi_master.mp4`, re-graded as one piece.

## Act 2 budget (est., live costs)
~7 keyframes ×2 = ~14 · previz ~3–4 scenes ×~10 (5s std) ×2 iters ≈ ~70 · finalize ~4 scenes ×25 ×~2 iters ≈ ~200 → **~280–350 cr** for a clean first pass (more if motion needs heavy re-rolls). Check `balance` after. *(ACTUAL: ~59 cr.)*

---

# ACT 3 — "THE ELECTION MONTAGE"  *(audio enters the film)*

> **Capability proven:** audio pipeline + **beat-synced** montage. **Story:** the bait springs but the chair DODGES → a full election spectacle erupts; the trio dance/chase the chair across Punjab while ordinary Punjabis calmly work, unimpressed; ends at a polling booth (→ Act 4). Continues from Act 2's S3 cliffhanger.
> **Audio decision (locked):** **music-only, NO VO.** MCP has no standalone TTS/music generator (audio is bundled in video models only). So: generate visuals silent on Kling → source a **royalty-free dhol track** → add SFX + on-screen **Hinglish** text in edit → cut montage to the beat. VO deferred to Act 4.
> **Engine:** images `nano_banana_pro`(→nano_banana_2, 1.5cr) · previz Kling std · finalize Kling pro. Style = 2D caricature matching Acts 1–2.

## Act 3 montage shot list (~15s, 5 shots ×~3s, beat-cut)
| Shot | Visual | On-screen Hinglish text |
|------|--------|------------------------|
| **M1 — THE DODGE** *(chains from S3)* | Trap net snaps up EMPTY — the cute PUNJAB chair leaps aside out a big factory door into daylight; freebies burst everywhere; the trio faceplant. | **"PUNJAB BACH GAYA!"** (Punjab escaped!) |
| **M2 — FREEBIE RAIN** | Wide Punjab mustard field, blue sky; balloons & crates (NAUKRI/BIJLI) rain from the sky; the chair scampers across, dodging. | **"VAADON KI BARSAAT"** (a downpour of promises) |
| **M3 — UNIMPRESSED PUNJAB** | A Sikh farmer plowing, a student reading, a woman at her shop — calm, working, ignoring the freebies falling around them. *(new generic villagers, not the trio)* | **"...par Punjab kaam mein busy"** (but Punjab's busy working) |
| **M4 — THE GREAT CHASE** | Stylized Golden-Temple silhouette at golden hour; the chair dashes across the foreground, the trio scrambling after it. | **"KURSI KE PEECHE BHAAG!"** (running after the chair!) |
| **M5 — THE BOOTH** *(cliffhanger → Act 4)* | The chair stops dead at a polling booth (EVM, "MATDAAN / VOTE" sign); the trio skid to a halt behind it. | **"FAISLA Punjab ka."** (Punjab decides.) |

**Audio plan:** dhol-tumbi loop bed (sourced) under the whole montage; comic SFX (whoosh, boing, sparkle) on cuts; cut each shot on the dhol beat in edit. **No character lip-sync / no VO.**

## Act 3 gates
- **3A keyframes:** M1–M5 on-model (trio via Elements; villagers generic), 2D-style-consistent, vistas read.
- **3B previz:** Kling std motion per shot acceptable; M1 chains from S3.
- **3C finalize:** Kling pro + multi-frame QC + motion verdict.
- **3D audio+assembly:** dhol bed + SFX + Hinglish text, cut to beat → `renders/act3/act3_final.mp4` → fold into master.

## Blocking inputs before we start Phase 2
1. **Real So Sorry reference frames (8–15)** — the single highest-leverage input.
2. **Generation access** — complete the Higgsfield **MCP OAuth** (in progress) or confirm the Higgsfield **CLI** is installed/authed, so we can actually generate.
