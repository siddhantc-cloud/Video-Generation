---
name: ramayana-video-plan
description: Plan Ramayana-ZebpaySIP shots, iteration strategy, approval packets, cost caps, and production forecasts. Use before any paid generation, when selecting the next pilot, estimating credits, defining one-variable retries, or deciding how the learned workflow can be repeated more cheaply.
---

# Ramayana video planning

Read these current sources before planning:

- `Ramayana-ZebpaySIP/project/production-learning-and-cost-plan.md`
- `Ramayana-ZebpaySIP/project/brief.md`
- `Ramayana-ZebpaySIP/scripts/shooting-script.md`
- `Ramayana-ZebpaySIP/scripts/shot-tracker.md`
- `Ramayana-ZebpaySIP/review/criteria/expectations.md`

## Produce a checklist-first shot plan

For each planned generation, specify:

1. shot/version and narrative purpose;
2. target edit duration and delivery format;
3. exact references and their roles;
4. action, camera, look, continuity, and audio locks;
5. delta from the previous version;
6. live per-job quote, maximum jobs, and total approval cap;
7. keeper criteria and stop condition;
8. output, review, and tracker destinations.

## Animatic-first rules

- Inventory and hash-check recovered storyboard/keyframe/animatic assets before recreating anything.
- The frame-locked animatic is the editorial source of truth, but existence is not human approval.
  Do not scale paid generation until the human approves its runtime or a shorter alternative.
- Every paid job names the exact animatic row(s) it will replace and preserves the approved
  narration interval at conform.
- A multi-image animatic row is editorial coverage, not automatically a valid Seedance start/end
  pair. Check identity, scale, hand/prop geometry, camera, and reachable spatial motion first.
- Conform every generation input to exact 9:16 without overwriting the original, then visually
  review the crop. Never rely on an unobserved composer crop.

## Cost rules

- Treat 100 credits for S1-a v002 at 1080x1920, 10 seconds, Sound On, and one candidate as a dated benchmark only.
- Replace every estimate with the current live quote before approval.
- During learning, preserve the exact production engine: `seedance_2_0`, `mode=std`, 480p, high bitrate, Sound On, one candidate. Do not use Fast, Mini, or Seedance 1.5 as quality/consistency evidence.
- 480p is the live minimum. As checked on 2026-07-23, 480p Standard quoted 3 credits per second: 4 s = 12 credits, 8 s = 24, 10 s = 30, and 15 s = 45. Treat these as dated reference quotes.
- Choose duration from the complete visual beat and known failure window. Four seconds is only a narrow mechanics probe; use the intended edit duration to evaluate continuity or unwanted cuts. Fifteen seconds is a capacity ceiling, not a default.
- Sound Off and lower bitrate did not reduce the tested no-reference quote. Keep Sound On so the same run tests diegetic SFX.
- A website Unlimited route is eligible only when the authenticated composer explicitly includes standard Seedance 2.0. Fast-only Unlimited is the wrong model proxy; CLI, MCP, Canvas, and Supercomputer still charge credits.
- Track actual spend and rejected takes; never report keeper economics without the denominator.
- Change one variable after a structural failure. Do not blind-reroll.
- Batch only after evidence says variance is stochastic and the human approves the full batch cap.
- Prefer deterministic editing for still pushes, text, captions, graphics, and logo work.
- Stop a shot class after two consecutive structural failures and redesign the surface or shot.

## Duration and grouping rules

- A longer generation can reduce exported files and editorial joins, but it does not guarantee fewer visible cuts; Seedance can create internal cuts.
- Use one continuous 10–15 second clip only for one coherent action arc, one location, and a stable character/reference set.
- Use an intentional multi-shot prompt only when 1–3 cuts genuinely help the scene; name and time every cut.
- Do not pad a short action to 15 seconds. Extra time costs linearly and increases the failure surface.
- Group storyboard rows only when character set, location, time, emotional unit, and reference packet all match. Split dense action, high-risk contact, location changes, and major entrances/exits.

The current EDL contains 22 generative units. Their integer/minimum durations total about 151 billed seconds: a dated 480p Standard one-pass estimate of 453 credits, or 411 when S5-e is deterministic. Do not run a whole-film pass during learning; test representative shot classes first.

The recovered animatic audit proposes a cautious 17-job grouping at about 133 billed seconds, or
399 credits at the same dated no-reference quote. The small 12-credit difference proves that
grouping mainly reduces submissions; shortening the approved animatic is the significant
duration-priced cost lever.
