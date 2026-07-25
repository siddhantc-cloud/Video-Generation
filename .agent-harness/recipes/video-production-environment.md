# Video Production Environment Recipe

## Checklist

| Requirement | Pass condition | Evidence | Owner | Status |
|---|---|---|---|---|
| Cinematic planning | `higgsfield/SKILL.md` exists on Codex and Claude | Verifier output | Partner agent | Complete |
| Higgsfield execution | Official CLI and `higgsfield-generate` exist | `higgsfield --version`; verifier output | Partner agent | Complete |
| Identity workflow | `higgsfield-soul-id` exists on both hosts | Verifier output | Partner agent | Complete |
| Editorial workflow | `video-use` and its Python imports work | Real timeline render | Partner agent | Complete |
| Motion graphics workflow | Four selected Remotion skills exist on both hosts | Verifier output | Partner agent | Complete |
| Core binaries | FFmpeg, FFprobe, Python, Node, npm, and yt-dlp resolve | Verifier output | Partner agent | Complete |
| Local narration footprint | Qwen environment and dedicated model/package caches remain absent unless the owner approves reinstallation | Filesystem check and v008 historical evidence | Partner agent | Removed 2026-07-25 |
| Credential hygiene | `.mcp.json` has no embedded credential; ElevenLabs user environment variable exists | Verifier output | Partner agent | Complete |
| Cross-host parity | Every selected skill tree matches across Codex and Claude | Verifier output | Partner agent | Complete |
| Higgsfield account | Read-only account status succeeds | `higgsfield account status --json` | Human + partner agent | Complete; authenticated and sole workspace selected |
| Paid generation | Model schema and estimated cost are reviewed before submission | Per-shot generation record | Human + partner agent | Pending production |

## Scope

This recipe provisions the reusable environment for `Ramayana-ZebpaySIP`: Higgsfield generation,
FFmpeg/video-use editing, and Remotion-based motion graphics. Qwen3-TTS, Manim, Blender, ComfyUI
models, and a global Remotion project are not installed. Heavyweight dependencies should be
introduced only when the owner explicitly approves the requirement and storage cost.

## Sources pinned on 2026-07-21

| Package | Upstream | Inspected main commit |
|---|---|---|
| Higgsfield cinematic prompting | `OSideMedia/higgsfield-ai-prompt-skill` | `69a4ab662a53a0702370c6e86951ddb73e8c74d6` |
| video-use | `browser-use/video-use` | `92c2b34e44c205cbc2acae7f6ca7c1c219d5dd66` |
| Official Higgsfield skills | `higgsfield-ai/skills` | `9ab6483d45ebead2c0cf7597ae96ab3eb605fa34` |
| Official Remotion skills | `remotion-dev/skills` | `8ea5e44b60c73a45aa77219ad3045fb47783e38b` |

Review upstream changes before refreshing a pin. A newer commit is not automatically safer or more suitable.

## Install or refresh

1. Read the installer skill at `C:\Users\SE\.codex\skills\.system\skill-installer\SKILL.md`.
2. Remove or archive an old destination only after reviewing local changes. The installer does not overwrite existing skills.
3. Install the same upstream paths into both host roots:

   - `higgsfield` from the root of `OSideMedia/higgsfield-ai-prompt-skill`.
   - `video-use` from the root of `browser-use/video-use`.
   - `higgsfield-generate` and `higgsfield-soul-id` from `higgsfield-ai/skills`.
   - `remotion-best-practices`, `remotion-create`, `remotion-render`, and `remotion-captions` from `remotion-dev/skills/skills`.

4. Install runtime tools:

   ```powershell
   npm install --global @higgsfield/cli@latest
   uv tool install yt-dlp
   uv tool update-shell
   python -m pip install requests librosa matplotlib pillow numpy
   ```

5. Restart Codex and Claude so both hosts rediscover the new user-level skills.
6. Run the verifier from the repository root.
7. Do not reinstall Qwen3-TTS by default. Its historical recipe remains at
   `.agent-harness/recipes/local-qwen3-tts-narration.md`; using it again requires explicit owner
   approval after disclosing the approximately 15 GiB reference environment/cache footprint.

## Authentication and cost boundary

- Run `higgsfield auth login` in an interactive terminal. Do not automate credentials or copy browser tokens into files.
- Use `higgsfield account status --json` as the read-only readiness check.
- Before a generation, inspect the chosen model, fetch its current schema, validate all arguments, and show the estimated cost. Submit only after the intended shot and cost are accepted.
- Soul training requires suitable face photographs and a paid Higgsfield plan. It is optional for the Ramayana campaign unless a real person's identity must be preserved.
- ElevenLabs credentials live only in the Windows user environment. Rotate a credential immediately if it is ever printed or committed.
- Historical Qwen3-TTS evidence remains in the repository, but its runtime and caches are absent.
  Reinstallation is a new storage and compute decision, not a default environment repair.

## Editing rules

- Follow video-use's editorial order: decide strategy, edit segments, assemble the timeline, mix/fade audio, add overlays, and add captions last.
- Keep source footage immutable. Write intermediates and outputs to the film workspace's established `edit/`, `review/`, and `deliverables/` locations.
- Cache transcripts and align captions against the final output timeline.
- Use yt-dlp only for media the user owns or is authorized to reuse.
- Remotion is installed as guidance, not as a global application. Scaffold it inside a specific production folder when needed.
- Review Remotion's current license before commercial use; licensing depends on organization and use case.

## Verification

Run:

```powershell
powershell -ExecutionPolicy Bypass -File tools/verify-video-environment.ps1
```

The retained reference smoke-test evidence is
`.agent-harness/evidence/video-environment/video-use-timeline.png`. Its original pilots reel was
removed during the 2026-07-25 storage cleanup. A future rerun should use the first four seconds of
the retained v011 review or promoted v005 master and must not spend generation credits.

The local-TTS reference is historical v008 evidence: Qwen3-TTS 0.1.1 and PyTorch 2.11.0+cu128
generated on the RTX 5060 Ti with 4.640 GiB peak allocated VRAM. Technical checks passed, but the
owner rejected the accent and SIP delivery. The runtime, caches, raw WAVs, and encoded reviews were
removed on 2026-07-25; compact metadata and QC records remain.
