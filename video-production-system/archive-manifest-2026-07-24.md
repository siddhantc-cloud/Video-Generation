# Workspace archive manifest — 2026-07-24

## Checklist

| Requirement | Pass condition | Evidence | Owner | Status |
|---|---|---|---|---|
| Active production preserved | `Ramayana-ZebpaySIP/` remains at the workspace root | Post-move inventory | Codex | Pass |
| Operational surfaces preserved | `.git`, `.codex`, `.claude`, `.agent-harness`, root instructions, MCP config, and lightweight tools remain active | Post-move inventory | Codex | Pass |
| Legacy material recoverable | Every classified legacy path is under `_archive/legacy-workspace-2026-07-24/` | Post-move inventory | Codex | Pass |
| No archive committed | `_archive/` is ignored; tracked legacy files become repository deletions while remaining recoverable locally and in Git history | Git status and `.gitignore` | Codex | Pass |
| Final film retained | Approved v005 captioned film is promoted under `Ramayana-ZebpaySIP/deliverables/final/` and tracked with Git LFS | LFS pointer and hash checks | Codex | Pending until push |

## Archive root

`_archive/legacy-workspace-2026-07-24/`

This is a reversible local archive, not a deletion. The archive is intentionally excluded from the
new repository tree. Previously tracked files also remain recoverable from Git history.

## Classified legacy workspace paths

| Source | Size (bytes) | Files | Tracked files | Destination group | Reason |
|---|---:|---:|---:|---|---|
| `ads/` | 1,031,162,253 | 414 | 177 | `legacy-projects/` | Previous Clear Gut production |
| `GoogleFlow/` | 127,907,870 | 51 | 51 | `legacy-projects/` | Unrelated Google Flow work |
| `marketing/` | 12,016 | 1 | 1 | `legacy-projects/` | Legacy marketing notes |
| `productions/` | 1,490,767,462 | 1,062 | 101 | `legacy-projects/` | Previous production outputs |
| `references/` | 9,144,370 | 2 | 1 | `legacy-projects/` | Legacy campaign references |
| `simple_ads/` | 995,984,017 | 217 | 146 | `legacy-projects/` | Previous simple-ad production |
| `UGC/` | 392,019,570 | 120 | 66 | `legacy-projects/` | Previous UGC production |
| `zebpay/` | 557,452,494 | 325 | 85 | `legacy-projects/` | Pre-canonical ZebPay workspace superseded by `Ramayana-ZebpaySIP/` |
| `AI_VIDEO_WORKFLOW.md` | 24,868 | 1 | 1 | `legacy-docs/` | Superseded by the generic production system and recipes |
| `AV_SYNC_SYSTEM.md` | 5,858 | 1 | 1 | `legacy-docs/` | Project copy remains under `Ramayana-ZebpaySIP/edit/` |
| `.gstack/` | 104,632 | 4 | 0 | `runtime-state/` | Stale ignored browser runtime state |
| `.agent-harness/evidence/davinci-mcp-setup/` | 968,610 | 3 | 0 | `legacy-research-evidence/` | Source transcript and metadata are preserved locally; active Resolve recipe retains the reusable conclusions |

## Classified legacy project-local skills

The following Claude-only skill copies are archived because they were campaign-specific, duplicated
user-level provider skills, or referenced legacy workspace paths:

- `audio-first-reel`
- `caricature-talking-ad`
- `chatgpt-imagegen`
- `comfyui-wan-local`
- `cut-video`
- `higgsfield-cinematic`
- `higgsfield-ugc-playbook`
- `multi-take-video-edit`
- `seedance-satire-director`
- `storyboard-animatic`
- `video-captions-karaoke`
- `video-use`

Their combined local payload is approximately 5.87 MB. Generic replacements live canonically under
`.codex/skills/script-video-*` and are mirrored under `.claude/skills/script-video-*`.

## Classified heavy local tool payload

| Source | Size (bytes) | Destination group | Reason |
|---|---:|---|---|
| `tools/ffmpeg-libass/` | 626,277,659 | `heavy-tools/` | Bundled duplicate; verified system FFmpeg remains canonical |
| `tools/ffmpeg-gpl.zip` | 221,744,311 | `heavy-tools/` | Installer archive, not an active dependency |

## Restore rule

Restore only an exact required path, never the whole archive by default. Move the archived path back
to its recorded source, then inspect references and Git status before using it.
