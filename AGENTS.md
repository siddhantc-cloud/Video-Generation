# AGENTS.md

## Checklist

| Requirement | Pass condition | Evidence | Owner | Status |
|---|---|---|---|---|
| Active scope | Root contains the current film, reusable system, tools, and agent configuration only | Root inventory | Partner agent | Required |
| Repeatable workflow | Generic production skills and canonical documentation cover script through delivery | `.codex/skills/script-video-*` and `docs/video-production-workflow.md` | Partner agent | Required |
| Host parity | Canonical skills and agents match Claude mirrors byte-for-byte | Sync scripts with `-Check` | Partner agent | Required |
| Source safety | Raw media and working renders stay immutable and outside Git by default | Project layout and `.gitignore` | All operators | Required |
| Spend safety | Every paid generation has a current quote and explicit approval | Shot packet and job ledger | Human / operator | Required |
| Delivery integrity | Final media is promoted explicitly, QC'd, hashed, and LFS-tracked only when requested | Delivery record and LFS pointer | Editor / partner agent | Required |

## Operating contract

This repository is a script-to-video production workspace. Read
`docs/video-production-workflow.md` and `video-production-system/PRODUCTION_SYSTEM.md` before
starting from an idea. `.agent-harness/recipes/idea-to-cinematic-social-video.md` is the
machine-routing entry; `.agent-harness/recipes/script-to-video-production.md` is a compatibility
pointer. Neither duplicates the process.

- Keep original scripts, raw provider results, narration sources, and approved renders immutable.
- Use one continuous narration performance as the master clock unless the project records otherwise.
- Express all timeline boundaries as integer frames.
- Approve stills and an encoded animatic before paid motion.
- Obtain approval against the final live provider quote immediately before every paid job.
- Use deterministic post-production for exact text, claims, numbers, graphs, logos, and captions.
- Judge the actual encoded artifact. Inspect deterministic boundaries at `n-1`, `n`, and `n+1`.
- Preserve evidence in the project; promote only cross-project learning into shared recipes and skills.

## Active workspace

| Path | Purpose |
|---|---|
| `Ramayana-ZebpaySIP/` | Approved prior film: sources, assets, keyframes, footage, edit state, review, and delivery |
| `CryptoBalancing-Zebpay/` | Current film: supplied brief, canonical production workspace, deterministic HyperFrames edit, review evidence, and local review delivery |
| `docs/` | Canonical human-readable production process |
| `video-production-system/` | Canonical generic production contract, templates, shared agent definitions, and archive manifest |
| `.codex/skills/script-video-*/` | Canonical reusable production skills |
| `.claude/skills/script-video-*/` | Byte-equivalent Claude mirrors |
| `.agent-harness/recipes/` | Shared repeatable production recipes |
| `tools/` | Scaffold, sync, verification, and deterministic edit helpers |
| `_archive/legacy-workspace-2026-07-24/` | Recoverable local archive; intentionally ignored by Git |

Do not reintroduce Google Flow or unrelated campaigns into the active root. Restore an archived path
only after recording its purpose in `video-production-system/archive-manifest-2026-07-24.md`.

## Project MCP servers

The repository `.mcp.json` contains server configuration without embedded secrets.

| Server | Purpose | Availability rule |
|---|---|---|
| `ElevenLabs` | Speech, voice, and audio workflows | Key is inherited from the Windows user environment; never write it to the repo |
| `davinci-resolve` | Live Resolve Studio control | Optional; requires owner-supplied Resolve Studio and local external scripting |
| `davinci-resolve-advanced` | Offline Resolve project and deliverable operations | Optional; not the canonical editorial stack |

Workspace-provided `puppeteer` and `context7` may be used when exposed by the current host. Do not
claim they are configured in `.mcp.json`.

## Reusable production skills

Canonical packages live under `.codex/skills/` and are mirrored under `.claude/skills/`.

| Skill | Trigger | Purpose |
|---|---|---|
| `script-video-production` | Turn an idea into a complete cinematic social video | Route the full workflow through atomic skills, agents, gates, and evidence |
| `script-video-bootstrap` | Start a film from a script | Create the clean canonical project workspace |
| `script-video-plan` | Script breakdown, shots, timing, or cost | Build frame-locked production and iteration plans |
| `script-video-continuity` | Characters, locations, props, or brand sources | Control reusable element identity and continuity |
| `script-video-animatic` | Storyboard, keyframes, or timing proof | Build the audio-master free animatic |
| `script-video-cinema-navigation` | Inspect an authenticated cinema page | Navigate safely and update the provider runbook |
| `script-video-generate` | Run one approved paid shot | Preflight, quote, submit once, monitor, and preserve |
| `script-video-review` | Review a take or cut | Produce evidence-backed keeper and QC verdicts |
| `script-video-motion-graphics` | Graphs, logo, copy, or transitions | Build exact deterministic premium motion |
| `script-video-post` | Assemble, mix, caption, or master | Create frame-locked review cuts and finals |
| `script-video-learn` | `/learn` or verified new evidence | Promote learning without duplicating project facts |

After any generic skill change:

```powershell
powershell -ExecutionPolicy Bypass -File tools/sync-script-video-skills.ps1
powershell -ExecutionPolicy Bypass -File tools/sync-script-video-skills.ps1 -Check
```

## Shared production agents

Canonical agent prompts live in `video-production-system/agents/` and are mirrored into
`.claude/agents/`: `script-rewriter`, `assistant-director`, `scene-expectations`,
`prompt-reviewer`, `video-editor`, and `video-reviewer`.

Claude discovers the mirrored files natively. Codex has no identical project file-agent discovery
surface; it reads and executes the canonical definitions directly. This is an intentional host
mapping, not missing parity.

After any agent-definition change:

```powershell
powershell -ExecutionPolicy Bypass -File tools/sync-script-video-agents.ps1
powershell -ExecutionPolicy Bypass -File tools/sync-script-video-agents.ps1 -Check
```

## Ramayana evidence skills

The existing `.codex/skills/ramayana-*` packages and `.claude` mirrors preserve detailed
project-specific navigation, generation, cost, review, post, and learning evidence. Use them for
Ramayana work; use `script-video-*` for new films. Sync with:

```powershell
powershell -ExecutionPolicy Bypass -File tools/sync-ramayana-video-skills.ps1
powershell -ExecutionPolicy Bypass -File tools/sync-ramayana-video-skills.ps1 -Check
```

## Provider and media skills

User-level host skills supply provider-specific execution:

- `higgsfield`, `higgsfield-generate`, and `higgsfield-soul-id`;
- `video-use`;
- `hyperframes`, `hyperframes-core`, `hyperframes-animation`, `hyperframes-creative`,
  `hyperframes-cli`, `hyperframes-keyframes`, `hyperframes-registry`, and `media-use`;
- `remotion-best-practices`, `remotion-create`, `remotion-render`, and `remotion-captions`.

Generic project skills decide when these tools are appropriate. Current provider schema, model
support, and price override remembered defaults.

The reusable prompt packets and four-lane production model live only in
`docs/video-production-workflow.md`; recipes, skills, agent prompts, system references, and project
status files link there rather than duplicating it. Its credit table is dated evidence, never a
standing tariff.

## Native tools

| Tool | Purpose |
|---|---|
| Higgsfield CLI | Account inspection and authenticated generation |
| FFmpeg / FFprobe | Canonical assembly, compositing, audio, probing, and delivery |
| video-use dependencies | Timeline and editorial helpers |
| Qwen3-TTS 1.7B VoiceDesign | Historical v008 evidence only; the local runtime and model/package caches were removed on 2026-07-25 and must not be reinstalled without explicit owner approval |
| Sarvam Bulbul v3 REST API | Hosted Indian-language and Indian-English narration with production voices, pace/temperature controls, and pronunciation dictionaries |
| HyperFrames CLI | Deterministic HTML/CSS/SVG/GSAP motion design and rendering |
| Node.js / npm | HyperFrames, Remotion, and provider CLI tooling |
| Python | Validation and deterministic helpers |
| `Ramayana-ZebpaySIP/tools/generate_qwen3_tts.py` | Historical/reinstall helper retained for reproducibility; not runnable on the current host without an explicitly approved Qwen environment restoration |
| `Ramayana-ZebpaySIP/tools/generate_sarvam_tts.py` | Create Sarvam pronunciation dictionaries and reproducible Bulbul v3 WAVs without persisting credentials |
| `Ramayana-ZebpaySIP/tools/transcribe_elevenlabs_scribe.py` | Create versioned Scribe timing evidence without persisting the API key |
| `Ramayana-ZebpaySIP/tools/build_elevenlabs_phrase_locked_audio.py` | Conform timestamped ElevenLabs alignment or Scribe word timing to whole-frame phrase slots without pitch shift |
| `yt-dlp` | Fetch only explicitly authorized online media |
| Git LFS | Store explicitly promoted final videos |
| DaVinci Resolve Free | Optional supervised finishing; not an MCP dependency |

The canonical editorial stack is video-use plus FFmpeg/FFprobe. Resolve is optional after picture
lock; do not purchase Studio or introduce a different NLE without a verified limitation and human
approval.

For an ElevenLabs narration replacement after picture lock, follow
`.agent-harness/recipes/elevenlabs-phrase-locked-narration.md`. The project helper named above is
the verified implementation; its project path is intentionally Ramayana-specific while the recipe
is reusable.

Qwen3-TTS is not installed on the current host. On 2026-07-25 the owner removed the project virtual
environment, dedicated Hugging Face/UV caches, rejected v008 WAVs, and encoded v008 reviews to save
space after human rejection. Compact metadata, QC, source code, and the
`.agent-harness/recipes/local-qwen3-tts-narration.md` recipe remain as historical evidence only.
Do not recreate the environment or download the model without explicit owner approval.

For Indian-English hosted narration, follow
`.agent-harness/recipes/sarvam-bulbul-v3-narration.md`. The Sarvam helper reads
`SARVAM_API_KEY` from the process environment or the ignored repository `.env`; never copy the key
into metadata, recipes, commands, or tracked files. Bulbul v3 supports speaker, pace, temperature,
sample rate, and pronunciation dictionaries; apply gain, EQ, and dynamics in post because v3 does
not expose pitch or loudness controls.

## Git and media policy

- Raw footage, generated takes, review cuts, audio stems, caches, and local archives remain ignored.
- Track a final video only when the owner explicitly asks, following
  `.agent-harness/recipes/git-lfs-video-delivery.md`.
- Use a narrow `.gitattributes` rule and verify the staged blob is an LFS pointer before committing.
- Never commit `.env`, credential values, provider tokens, or raw customer data.
- Never force-push for media delivery.

## Tool logistics update rule

Update this file and `CLAUDE.md` whenever adding or removing a project MCP, skill family, agent
surface, native production tool, or host-specific workflow. Preserve cross-host parity or record an
intentional N/A.
