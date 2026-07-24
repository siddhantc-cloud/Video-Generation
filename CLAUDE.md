# CLAUDE.md

Read and follow `AGENTS.md`; it is the shared project contract, current tool inventory, safety policy,
and source of truth for Codex/Claude parity.

## Checklist

| Requirement | Pass condition | Evidence | Owner | Status |
|---|---|---|---|---|
| Shared contract | `AGENTS.md` was read before project work | Session behavior | Claude | Required |
| Correct skill | A generic `script-video-*` skill or a Ramayana evidence skill is selected intentionally | Work log | Claude | Required |
| Shared agent | Claude agent file matches `video-production-system/agents/` | Agent parity check | Claude | Required |
| Provider safety | Current schema, quote, and approval exist before paid generation | Job packet | Claude / human | Required |
| Encoded evidence | Review and delivery claims refer to probed encoded artifacts | Review record | Claude | Required |

For any new script, read `video-production-system/PRODUCTION_SYSTEM.md` and
`.agent-harness/recipes/script-to-video-production.md`, then start with `script-video-bootstrap`.
Claude's `/learn` command uses the mirrored `script-video-learn` skill.

Generic skills are canonical under `.codex/skills/script-video-*` and mirrored into
`.claude/skills/` with `tools/sync-script-video-skills.ps1`. Shared agent definitions are canonical
under `video-production-system/agents/` and mirrored into `.claude/agents/` with
`tools/sync-script-video-agents.ps1`. Never edit a mirror as the source of truth.

For Ramayana-specific page navigation, provider IDs, established continuity records, job outcomes,
and detailed review evidence, use the `ramayana-*` skills. Do not promote campaign-specific story,
brand, or cost values as generic defaults.

Use the official HyperFrames skill bundle for HyperFrames work and follow
`.agent-harness/recipes/hyperframes-motion-graphics.md`. Create each composition inside the current
project's `edit/animations/slot_*` directory and run the pinned project checks before rendering.

The canonical editorial stack is video-use plus FFmpeg/FFprobe and the project frame manifest.
DaVinci Resolve Free is optional supervised finishing only. The external Resolve MCP requires Studio
and is not a dependency for this workflow.

For an ElevenLabs narration replacement after picture lock, follow
`.agent-harness/recipes/elevenlabs-phrase-locked-narration.md`. The verified conformer is
`Ramayana-ZebpaySIP/tools/build_elevenlabs_phrase_locked_audio.py`; keep the continuous performance,
provider timing metadata, whole-frame phrase slots, native SFX, and human listening gate separate.

Qwen3-TTS 1.7B VoiceDesign is the project-local open-source narration tool. Run it only from
`Ramayana-ZebpaySIP/.venv-qwen3-tts`, keep its package/model caches under ignored `_cache/` on `D:`,
and use PyTorch SDPA on this Windows host. Indian-accent and project-term pronunciation require a
recorded benchmark and human listening approval before a take can replace approved narration.
Follow `.agent-harness/recipes/local-qwen3-tts-narration.md`; the canonical generator, Scribe
verifier, and phrase conformer are listed in `AGENTS.md`.

Follow `.agent-harness/recipes/git-lfs-video-delivery.md` when the owner explicitly requests the
approved final in Git. Never add raw takes or review media to Git as a shortcut.
