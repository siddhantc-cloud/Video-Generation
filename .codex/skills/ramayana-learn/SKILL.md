---
name: ramayana-learn
description: Promote verified Ramayana-ZebpaySIP production evidence into the navigation runbook, cost plan, recipes, and project skills. Use when the user says /learn, asks to remember current production context, finishes inspecting a Cinema Studio page, or confirms a generation/review outcome.
---

# Learn from the Ramayana production

This is a documentation and skill-maintenance workflow. It never generates media, spends credits, deletes assets, changes sharing, or promotes a select.

## Evidence order

1. Current media and technical evidence.
2. Higgsfield job/account records and page screenshots.
3. Human keeper/reject or approval decisions.
4. Per-shot generation/review records.
5. Navigation runbook, cost plan, production decisions, and tracker.
6. Chat context only when anchored to one of the above.

## Learn workflow

1. Build a checklist of candidate learnings and their evidence.
2. Separate facts, inferences, hypotheses, and unverified UI behavior.
3. Update the detailed Cinema Studio runbook for every newly inspected page/state.
4. Update the production cost plan after every paid job with quote, actual charge, version, verdict, and next-variable decision.
5. Update the per-shot record, review note, tracker, and production decisions when their current status changes.
6. Update a focused skill only when the finding is reusable. Keep incident detail in project records and add only the operational law to SKILL.md.
7. Edit canonical skills under `.codex/skills/ramayana-*` with `apply_patch`.
8. Run `tools/sync-ramayana-video-skills.ps1` to mirror canonical skills to `.claude/skills/`.
9. Run the skill validator on all canonical and mirrored packages, then run the parity script with `-Check`.
10. If a rule is genuinely cross-project, promote it through `script-video-learn` into
    `video-production-system/` or a generic `script-video-*` skill. Keep Ramayana story, brand,
    provider IDs, dated costs, and final hashes project-specific.
11. Report evidence, changed files, unresolved hypotheses, and the next safe action.

## Truth rules

- Do not mark a proposed fix as confirmed until a later generation passes the failed criterion.
- Do not turn a dated price into a standing quote.
- Record resolution savings separately from model/mode substitutions. A cheaper model or Fast tier is not evidence for locked Standard-mode behavior.
- Record duration as a story/risk decision, not a minimum-or-maximum default. Maximum duration reduces files only when the grouped scene remains coherent; it does not guarantee fewer visible cuts.
- Do not store secrets, auth tokens, account email, unrelated screenshots, or raw private data.
- Do not compress away rejected attempts; they are required for cost and keeper-rate learning.
- When an older production folder is rediscovered, compare hashes and timelines before copying or
  rebuilding. Promote the clean canonical location and record exact identity instead of duplicating
  byte-identical media.
- A keyframe that works in an animatic is not automatically safe for image-to-video. Record aspect,
  identity, endpoint geometry, and reachable-motion failures before paid generation.
- If the shared Higgsfield ledger lacks the actual model ID, keep the accurate project-local record rather than logging a false model.
