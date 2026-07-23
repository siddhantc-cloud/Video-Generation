# Production learning and cost plan

## Control checklist

| Requirement | Pass condition | Evidence | Owner | Status |
|---|---|---|---|---|
| Baseline | Actual settings, charge, output, and verdict are recorded for the first controlled run | `footage/generated/S1-a_v002.md`; account ledger | Producer/Operator | Complete: 100 credits, rejected |
| Iteration discipline | A retry changes one diagnosed variable and retains every other approved input | Per-shot packet diff | Director/Operator | Planned for S1-a v003 |
| Spend approval | Live price and maximum candidate count are approved immediately before submission | Preflight record and human approval | Human | Mandatory |
| Duplicate protection | One click produces one verified job ID before any further action | Job list plus transaction ledger | Operator | Proven on v002 |
| Keeper economics | Actual takes, credits, and reject class are tracked for every attempt | Iteration ledger below | Producer | Active |
| Scale gate | Full-shot production starts only after representative pilot classes have a keeper workflow | K01 v002 keeper; short-v004 motion review | Human/Director | Complete for the approved short-v004 pass |
| Animatic gate | The human approves a shorter frame-locked alternative before broad motion spend | v004 animatic, phrase map, and human approval | Human/Editor | Complete: 52.2-second v004 locked |
| Faithful experiment route | Use the exact `seedance_2_0` model in `std` mode at 480p, high bitrate, and Sound On; do not substitute Fast, Mini, or Seedance 1.5 as quality/consistency evidence | `production-decisions.md`; live model schema | Human/Director | Locked 2026-07-23 |
| Cheaper repeat path | Draft or deterministic alternatives are used only when they preserve the shot requirement and have a verified lower live cost | Cost preflight and review | Producer/Editor | Pending live quotes |

## Known cost baseline

The only verified Cinema Studio 3.5 price in this project is the 2026-07-22 S1-a v002 configuration:

- 9:16, 1080p, 10 seconds, Sound On, one candidate.
- Live button quote: 100 credits.
- Account ledger charge: exactly 100 credits.
- Post-run account balance: 4019.03 credits.

This is a benchmark, not a standing tariff. Higgsfield discounts, plans, models, durations, resolutions, and audio pricing can change. Every estimate below must be replaced by a live preflight before approval.

## Minimum-cost faithful experimentation baseline

Authenticated, non-generating CLI checks without uploaded media references on 2026-07-23 established:

- `480p` is the lowest resolution accepted by `seedance_2_0`; there is no 360p route.
- Keep `mode=std`. Fast, Mini, and Seedance 1.5 are cheaper but change the inference/model tier and
  therefore cannot prove final Seedance quality or consistency.
- 480p Standard costs 3 credits per generated second in the tested range: 4 s = 12 credits,
  5 s = 15, 8 s = 24, 10 s = 30, and 15 s = 45.
- The live maximum is 15 seconds. The live minimum is 4 seconds.
- At 480p Standard, `bitrate_mode=standard` and `high` both quoted 12 credits for 4 s and 24 for
  8 s. Sound On and Sound Off also quoted the same price. Keep high bitrate and Sound On so the
  same spend also tests the final control shape and diegetic SFX. Exact references can change a
  shot quote, so re-price the fully staged packet.

The cheapest price probe is a **4-second, 480p, Standard, Sound-On, one-candidate** run at a current
reference quote of **12 credits**. It is not the default scene duration. Use the shortest duration
that contains the complete visual beat and the failure window being tested. For an intended
10-second oner, a four-second pass cannot prove full-shot continuity; test the intended 10 seconds.
Use 15 seconds only when the scene genuinely needs 15 seconds and the prompt is either one coherent
action arc or an explicitly designed multi-shot sequence.

The first fully referenced v004 packet, K01 v001, was staged in the authenticated Cinema Studio
workspace on 2026-07-23 using actual Seedance 2.0 / Standard / 9:16 / 480p / 6 seconds / one
candidate / High / Sound On / Unlimited Off. Both the CLI cost check and the final live Generate
button agreed on **18 credits**. The UI showed 36 crossed out and 18 final. This packet remains
unsubmitted pending immediate approval; see `footage/generated/K01_v001.md` and screen 034.

The current 22 generative EDL units would require about 151 billed seconds after four-second minimums
and integer-duration rounding: about **453 credits for one 480p Standard pass**. Rendering S5-e
deterministically reduces that estimate to **411 credits**. Do not run that full pass during learning;
test only the representative pilot classes.

Minimum useful representative round using each shot's intended edit duration at the no-reference quote:

| Test | Why this duration | Reference quote |
|---|---|---:|
| S1-a, 10 s | Full planned oner; includes the known 6.375 s unwanted-cut window | 30 credits |
| S4-c, 7 s | Covers the 6.267 s hand/squirrel contact beat | 21 credits |
| S2-c, 4 s | Covers the 3.5 s squirrel/pebble contact and native foley beat | 12 credits |
| **Initial three-class subtotal** | One candidate each, complete intended beats | **63 credits** |

Using 15 seconds for all three would cost 135 credits before any media-reference pricing effect and
would add unused time to S4-c and S2-c. Maximum duration is not a continuity control; it is a capacity
ceiling. This 63-credit round is cheaper and more informative than generating all 22 units once.

### Animatic-first production economics

The previous free keyframe workflow is already complete and preserved in the clean project:

- 30 keyframes;
- 24 frame-locked edit rows;
- 298 scratch-narration words;
- 166.633 seconds at 30 fps with 0.0003 seconds reported drift.

Do not regenerate these planning artifacts. Review or shorten the keyframe animatic first, then
replace its approved cells with moving selects. The production-readiness audit proposes a cautious
17-job grouping at about 133 billed seconds, or about 399 credits at the dated no-reference 480p
Standard quote. This saves only about 12 credits versus the current 411-credit deterministic-S5-e
estimate because Seedance pricing is duration-based. A shorter approved script/animatic is the
material cost lever; grouping primarily reduces submissions and editorial handling.

See `review/audits/animatic-production-readiness-audit.md` for the proposed conform map and the
keyframe repairs required before generation.

### Potential zero-marginal-credit route

Higgsfield's current Unlimited Marketplace can be website-only and model-specific. Use it for this
project only if the authenticated UI explicitly says the active bundle includes standard Seedance
2.0, not merely Fast or Mini. CLI, MCP, Canvas, and Supercomputer remain credit-charged. Account plan
status alone does not prove that an Unlimited bundle is active; verify the composer mode and displayed
price before submission. Do not purchase a bundle until its live price is compared with the approved
experiment-seconds budget.

## Iteration budget for the current S1-a pilot

| Iteration | Purpose | Variable changed | Estimated incremental cost if the same quote holds | Estimated cumulative pilot spend | Authorization | Result |
|---|---|---|---:|---:|---|---|
| v002 | Establish the Cinema 3.5 identity/look/audio baseline | Initial controlled packet | 100 actual | 100 actual | Approved | Rejected: extra cut at 6.375 s |
| v003 | Establish the locked standalone Seedance experiment baseline and test the complete S1-a oner | `seedance_2_0`; `std`; 480p; high bitrate; Sound On; 10 s; this differs from Cinema Studio v002 and is a new baseline, not a causal one-variable retry | 30-credit no-reference quote; exact staged packet must be re-priced | 130 plus any reference-price effect | Resolution/model policy approved; paid run not authorized | Pending |
| v004 contingency | Retry only after v003 identifies one structural cause | Keep the 10-second duration and change exactly one diagnosed prompt/reference/control variable | 30-credit no-reference quote | 160 plus any reference-price effect | Not authorized | Conditional |

Confidence is not a cost assumption. Cinema Studio 3.5 v002 is useful failure evidence but is not a
matched standalone Seedance baseline. Do not attribute any v003 difference to one causal variable;
v003 establishes the new experimental baseline, and systematic one-variable iteration begins after it.

## Scale forecast

The current shot plan contains approximately 24 generated moving units; S6, S7-b, and suitable locked-still moves remain deterministic post-production work.

| Average paid takes per moving unit | Benchmark takes | Benchmark credits at 100 each | Interpretation |
|---:|---:|---:|---|
| 1.0 | 24 | 2400 | Unrealistic best case: every first take is a keeper |
| 1.5 | 36 | 3600 | Strong pipeline with limited controlled retries |
| 2.0 | 48 | 4800 | Exceeds the current 4019.03 balance at this benchmark |
| 3.0 | 72 | 7200 | Poor economics; requires redesign, cheaper pilots, or more credits |

At the current benchmark, the present balance covers about 40 full-price takes. That is about 1.67 takes per planned moving unit, before allowing for price variation. Do not start broad production until the pilot workflow shows a credible keeper rate.

## Learning phase before scale

Lock one representative shot from each high-risk class:

1. **Camera plus identity:** S1-a, continuous move with Rama and one bow.
2. **Contact physics:** S4-c, squirrel and hand without fusion.
3. **Water/animal physics:** S5-b, squirrel maintaining contact through rough surf.
4. **Deterministic graphics:** S6/S7-b in post, proving the zero-Higgsfield-credit lane.

Do not batch the remaining shots until these classes reveal which controls are dependable.

## How repetition becomes cheaper

1. Reuse the approved Character and Location Elements; do not rebuild identity for every shot.
2. Reuse the locked Manual Style and optical settings; alter only the shot action and camera requirement.
3. Diagnose each rejection as structural or stochastic. Structural failures get one-variable prompt/control changes; blind rerolls are prohibited.
4. Use 480p Standard for learning. Use the duration required by the complete beat and known failure window; four seconds is only for questions fully observable within four seconds. Never use Fast, Mini, or an older model as evidence for the locked engine.
5. Promote proven prompt/control packets by shot class. Once a class is stable, duplicate the packet and change only shot-specific fields.
6. Use deterministic editing for still pushes, text, captions, the SIP graphic section, logo card, and any transition that does not require generative motion.
7. Batch candidates only after evidence shows the failure is stochastic and the human approves the total batch cap.
8. Stop a class after two consecutive structural failures and redesign the surface: shorter shot, stronger start/end anchoring, camera-reference video, standalone Seedance, or deterministic edit.

## Per-iteration ledger

| Date | Shot/version | Surface/settings | Live quote | Actual charge | Job ID | Verdict | Reject class | Change for next attempt |
|---|---|---|---:|---:|---|---|---|---|
| 2026-07-22 | S1-a v002 | Cinema Studio 3.5; 9:16; 1080p; 10 s; Sound On; one candidate | 100 | 100 | `75e86d55-60de-4415-9a52-1b973498dcd9` | Reject | `extra-cuts` | Explicit labelled Camera block and full-duration single-take lock only |
| 2026-07-23 | K01 v001 | Cinema workspace, Seedance 2.0 Standard; generic image role; 9:16; 480p; 6 s; High; Sound On; one candidate | 18 | 18 | `fe298728-3bd0-4369-a167-bf22b3379f0e` | Reject | `wrong-start-role` | Change only the approved keyframe from generic `image` to explicit `start_image` |
| 2026-07-23 | K01 v002 | CLI, Seedance 2.0 Standard; explicit `start_image`; 9:16; 480p; 6 s; High; Sound On; one candidate | 18 | 18 | `b503b2d0-c3c6-478f-88ba-ef4cd4b1e3bd` | Keeper | None; generative first-frame recomposition noted | Reuse explicit `start_image`; judge story/identity/direction continuity rather than assuming pixel lock |
| 2026-07-23 | K02 v001 | CLI Seedance 2.0 Standard; explicit start; 480p; 4 s; High; Sound On | 12 | 12 | `f1c0b203-0d66-4efd-bc63-258929d0f430` | Keeper | None | Reuse packet class |
| 2026-07-23 | K03 v001 | CLI Seedance 2.0 Standard; explicit start; 480p; 4 s; High; Sound On | 12 | 12 | `4553146c-7329-4871-9e16-0f50603f604d` | Partial keeper | `disappearing-object` after 1.50 s | Use valid range plus deterministic hold; no blind reroll |
| 2026-07-23 | K04 v001 | CLI Seedance 2.0 Standard; explicit start; 480p; 4 s; High; Sound On | 12 | 12 | `1f9880fb-36c3-4893-ae50-f0279a1e54af` | Keeper | None | Reuse packet class |
| 2026-07-23 | K05 v001 | CLI Seedance 2.0 Standard; explicit start; 480p; 4 s; High; Sound On | 12 | 12 | `6415571c-d083-46ad-8f17-0ae2cd7494b8` | Keeper | None | Reuse packet class |
| 2026-07-23 | K06 v001 | CLI Seedance 2.0 Standard; explicit start; 480p; 4 s; High; Sound On | 12 | 12 | `7f604ce9-c4a9-4427-92e2-1dbd451f9bad` | Keeper | Native ambience very quiet | Retain visual; supplement shot-local ambience in post when needed |
| 2026-07-23 | K07 v001 | CLI Seedance 2.0 Standard; explicit start; 480p; 4 s; High; Sound On | 12 | 12 | `187e9197-a17f-4423-984c-b9eaa5ce9b50` | Keeper | None | Reuse packet class |
| 2026-07-23 | K08 v001 | CLI Seedance 2.0 Standard; explicit start; 480p; 4 s; High; Sound On | 12 | 12 | `29fe5358-0ddb-4daa-ab43-bec0f7bb89c4` | Keeper | None | Reuse storm-motion class |
| 2026-07-23 | K09 v001 | CLI Seedance 2.0 Standard; explicit start; 480p; 5 s; High; Sound On | 15 | 15 | `cff1a816-6403-4a57-ac8b-71256ad740d8` | Keeper | None | Reuse macro seam class |
| 2026-07-23 | K10 v001 | CLI Seedance 2.0 Standard; explicit start; 480p; 4 s; High; Sound On | 12 | 12 | `070ebadc-f706-40d3-8a25-372cbacc7679` | Keeper | None | Reuse completed-bridge glide class |
| 2026-07-23 | K14 v001 | CLI Seedance 2.0 Standard; explicit start; 480p; 6 s; High; Sound On | 18 | 18 | `23c8706e-a3d4-4360-a85c-fde110452187` | Keeper | Native ambience very quiet | Retain visual; supplement shot-local ambience in post when needed |

Add one row immediately after every job. Never erase rejected attempts: they are the denominator used to decide whether the production is learning or merely spending.

## Current paid-action queue

| Shot/version | Purpose | Exact staged controls | Live quote | Maximum jobs | Total cap | Status |
|---|---|---|---:|---:|---:|---|
| K01 v002 | Correct the structural media-role failure while preserving every creative control | Seedance 2.0 Standard; explicit start image; 9:16; 480p; 6 s; one candidate; High; Sound On; approved K01 frame + Early Bridge + Rama | 18 | 1 | 18 | Complete: keeper; actual charge 18 credits |
| K02-K10/K14 first pass | Replace all remaining approved short-v004 motion cells | Seedance 2.0 Standard; explicit start images; 9:16; 480p; 4-6 s; one candidate each; High; Sound On | 12-18 | 10 | 129 | Complete: nine full keepers, one K03 partial keeper; actual charge 129 credits |

## Approval packet for every paid run

- Shot/version and purpose.
- Exact references and their roles.
- Exact prompt/control delta from the previous attempt.
- Model/surface, aspect, resolution, duration, sound, and candidate count.
- Live per-job cost, maximum jobs authorized, and total credit cap.
- Stop condition and keeper criteria.
- Human approval captured immediately before submission.
