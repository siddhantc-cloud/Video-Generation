# Continuity

Host-neutral project conversation state. Update this file whenever meaningful work lands.

## Now
- Three SOPs are live: setup, story film (category A), product explainer (category B). 52 LFS files, including the paid inputs for both reference films, are on the remote.

## Goal
- Deliver approved ZebPay video case studies, and make both video categories reproducible by any operator from a clone.

## Done
- Initialized .agent-conversation/
- Reconstructed real project state from live evidence and re-verified the packaged ZebPay showcase
- Added `docs/SOP-00-SETUP.md`, `tools/setup-video-repo.ps1`, and a cross-host `/setup` command
- Reframed the film SOPs as category playbooks: `docs/SOP-01-STORY-FILM.md` and `docs/SOP-02-PRODUCT-EXPLAINER.md`
- Pushed the owner-approved reproduction set through Git LFS, 187 MB across 49 new objects

## Evidence
- `tools/setup-video-repo.ps1` reports 29 pass, 0 fail, with 52 LFS files present as real media.
- `git lfs push --dry-run` sends nothing. Every object is on the remote.
- Skill, agent, and Ramayana parity checks pass, including the new `script-video-setup`.
- All quoted document paths in the three SOPs resolve.
- Commits `2732515`, `a85243f`, `91f33ca`, `75f2d2b` are pushed to `codex/cryptopack-rebalancing-video`.

## Blockers
- Every open production item needs a human decision. No machine work is pending.

## Next
- Human listening pass on the exact CryptoPack v002 encode.
- Human confirmation that the registered screenshots are current product UI, and approval of the deterministic claim mask treatment.
- Human product, brand, and legal approval for the v002 cut.
- Owner instruction to promote an approved MP4 hash to `deliverables/final/`.
- Optional: test `/setup` and a full rebuild on a clean second machine, then record what the SOPs missed.

## Active host
- claude

## Last update
- 2026-08-06T10:55:20Z
- Reframed the SOPs as category playbooks and pushed the approved reproduction set via Git LFS
