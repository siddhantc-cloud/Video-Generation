---
name: ramayana-shot-generate
description: Stage, preflight, price, approve, submit, monitor, download, and record one Ramayana-ZebpaySIP Higgsfield shot. Use for paid Cinema Studio or Seedance execution, including duplicate-spend protection and companion generation records; never use it to authorize an unapproved retry.
---

# Ramayana shot generation

Read the relevant shot packet plus:

- `Ramayana-ZebpaySIP/project/higgsfield-manual-generation-operating-spec.md`
- `.agent-harness/recipes/ramayana-higgsfield-manual-generation.md`
- `Ramayana-ZebpaySIP/project/production-learning-and-cost-plan.md`
- `Ramayana-ZebpaySIP/project/global-visual-law.md`
- Steps 17-20 of the Cinema Studio navigation runbook.

When writing or changing a Higgsfield prompt, also use the shared Higgsfield prompt, recall, camera, Cinema, Seedance, or audio skills that match the surface.

## One-job sequence

1. Verify shot intent, exact references, conformance, and one-variable delta.
2. Inspect current model/schema where the CLI exposes it.
3. Stage the exact surface, controls, prompt, duration, resolution, aspect, candidate count, and Sound state. During learning, the default is standalone `seedance_2_0`, `mode=std`, 480p, high bitrate, Sound On, one candidate; Fast, Mini, and Seedance 1.5 are prohibited as fidelity proxies. When the approved keyframe must establish the opening story state, send it through the explicit CLI `--start-image` field; a website picker record with role `image` is only a generic reference.
4. Read and record the live cost after all controls are set.
5. Present the full approval packet and wait for immediate human approval.
6. Click Generate once.
7. Confirm a new Processing asset or CLI job ID and persist it before another submission. Never click again because the composer remains visible.
8. Monitor the verified job to completion or failure.
9. Download without overwriting a raw take; extract native audio when present.
10. Record job ID, timestamps, parameters, live quote, actual ledger charge, hashes, output paths, and review status.
11. Hand off to `$ramayana-video-review`. Do not promote or retry here.

No approval carries forward to another version, candidate, or changed price. A human may explicitly
approve a named manifest set with exact per-row quotes, one candidate each, and a total cap. That
approval covers only unchanged rows in that manifest; any new version, changed packet, or higher
price requires a new approval.

Cinema Studio is a workspace, not proof of the active engine. Before pricing, verify that the composer
label reads `Seedance 2.0`, audit for a stale start frame left by an engine switch, and confirm the
intended references by thumbnail and inline `@` tag. Keep Unlimited mode Off unless the live UI
explicitly proves that the active bundle covers standard Seedance 2.0. The final number on the live
Generate button is the approval amount even when a larger crossed-out price is also shown.

Use the duration required by the complete beat and known failure window. Four seconds is valid only
when the entire question is observable within four seconds; it cannot approve a 10-second oner's
continuity. Use 15 seconds only for a coherent oner or a deliberately timed multi-shot scene, never as
padding. A 480p pass can approve blocking, camera behavior, unwanted cuts, gross continuity, and SFX
timing, but not final fine-detail quality.

Treat `start_image` as conditioning, not a promise that frame zero will pixel-match the source.
Review the actual opening for story state, identity, geography, direction, and editability; a
similarity score is supporting evidence only. When an approved batch is active, skip every row that
already has a persisted job ID. If the service returns `rate_limit_reached`, verify that no job and
no account delta were created, wait for capacity, and submit only the still-missing rows. The
eight-job Seedance limit observed on 2026-07-23 is dated account evidence, not a universal tariff or
standing concurrency promise.
