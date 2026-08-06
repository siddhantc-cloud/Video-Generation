# Continuity

Host-neutral project conversation state. Update this file whenever meaningful work lands.

## Now
- Three SOP documents, tools/setup-video-repo.ps1, and the script-video-setup skill are committed and pushed. The setup checker passes 29 of 29 on this machine.

## Goal
- Deliver approved ZebPay video case studies and make the repository reproducible by any operator

## Done
- Initialized .agent-conversation/
- Reconstructed real project state from live evidence and re-verified the packaged ZebPay showcase
- Added operator SOPs (setup, Ramayana, CryptoPack) and a cross-host /setup command

## Evidence
- `tools/setup-video-repo.ps1` reports 29 pass, 0 fail in check mode and in `-Install` mode on the reference machine.
- Skill, agent, and Ramayana parity checks pass after adding `script-video-setup`.
- CryptoPack v002 MP4 SHA-256 `3B90B00BC81BF90F0EEC6F19696E8FF7A3175C5F9591F3F66CCCE8389190FA76`. The review record, the production cut, and the packaged meeting copy are byte-identical.
- All LFS objects are on the remote. `git lfs fsck` is OK.
- Commits `a85243f` (SOPs and /setup) and `2732515` (bridge) are pushed.

## Blockers
- Every open production item needs a human decision. No machine work is pending.

## Next
- Human listening pass on the exact CryptoPack v002 encode.
- Human confirmation that the registered screenshots are current product UI, and approval of the deterministic claim mask treatment.
- Human product, brand, and legal approval for the v002 cut.
- Owner instruction to promote an approved MP4 hash to `deliverables/final/`.
- Optional: test `/setup` on a clean second machine and record what the SOP missed.

## Active host
- claude

## Last update
- 2026-08-06T10:35:39.3013589Z
- Added operator SOPs (setup, Ramayana, CryptoPack) and a cross-host /setup command
