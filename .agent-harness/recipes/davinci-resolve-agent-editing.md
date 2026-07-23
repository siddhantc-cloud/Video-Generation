# DaVinci Resolve Agent Editing Recipe

## Checklist

| Requirement | Pass condition | Evidence | Owner | Status |
|---|---|---|---|---|
| Source claim reviewed | The linked demonstration is transcribed and compared with current upstream documentation | `.agent-harness/evidence/davinci-mcp-setup/oXKK7l3-DVc.info.json`; `.agent-harness/evidence/davinci-mcp-setup/oXKK7l3-DVc.en.json3` | Partner agent | Complete |
| Compatible Python isolated | Python 3.12 exists without replacing the system Python default | `py -0p`; verifier output | Partner agent | Complete |
| Core MCP installed | Managed v2.63.0 Python server and virtual environment exist | `C:\Users\SE\AppData\Local\davinci-resolve-mcp`; verifier output | Partner agent | Complete |
| Advanced MCP installed | Pinned v2.63.0 npm package exposes the offline server | `C:\Users\SE\AppData\Local\davinci-resolve-mcp-advanced`; verifier output | Partner agent | Complete |
| Codex registered | `davinci-resolve` and `davinci-resolve-advanced` appear in `codex mcp list` | Verifier output | Partner agent | Complete |
| Claude registered | Both servers exist in project `.mcp.json` | Verifier output | Partner agent | Complete; first-session approval pending |
| MCP protocol works | Core discovers at least 34 tools and advanced discovers at least 18 | `tools/verify-davinci-environment.ps1 -AllowMissingResolve` | Partner agent | Complete |
| DaVinci Resolve Studio installed | Official Studio application and scripting API exist at standard Windows paths | Verifier output | Human + partner agent | Pending; application absent |
| Studio license available | DaVinci Resolve Studio launches as an activated Studio edition | Human confirmation plus launch evidence | Human | Pending |
| External scripting enabled | Preferences → General → External scripting using is set to `Local` | Screenshot plus live read-only connection | Human + partner agent | Pending |
| Live connection verified | MCP reads Resolve version, current project state, and timeline state without mutation | Read-only smoke-test record | Partner agent | Pending |
| Safe production workflow | Sources remain immutable; all generated projects, timelines, sidecars, caches, and renders stay in the Ramayana workspace | Review evidence and output paths | Human + partner agent | Required for every edit |
| No-license fallback selected | `video-use` and the existing frame-locked renderer remain the primary automated editor; Resolve Free is optional visual finishing only | `tools/verify-video-environment.ps1`; `Ramayana-ZebpaySIP/edit/AV_SYNC_SYSTEM.md` | Human + partner agent | Complete |

## Correct interpretation of the demonstration

The demonstrated system can inspect media, transcribe/analyze footage, create projects and timelines, import clips, and produce a useful first assembly. It does not replace editorial judgment. The demonstration itself required manual correction of seams and acknowledged imperfect silence/dead-space decisions. Treat the agent as an editing assistant whose work is reviewed after every bounded operation.

The live Python server requires **DaVinci Resolve Studio 18.5 or later** and a running application with external scripting set to `Local`. The free edition does not expose the external scripting interface needed by this MCP. Blackmagic currently advertises DaVinci Resolve Studio 21; this local MCP release is verified upstream against older Studio releases, so Studio 21 must receive a real-machine compatibility smoke test before production use.

This does **not** mean Resolve Free is unusable. Blackmagic's manual distinguishes external scripting, which is Studio-only, from scripts entered inside Resolve's own Console. Computer Use can also operate the visible Windows interface with screenshots, UI Automation, and keyboard input. That fallback is appropriate for bounded, supervised operations, but it does not provide the structured timeline state, deterministic readback, or reliability of the external MCP.

## No-license production decision

Use this order unless the owner changes it:

1. **Primary automated editor:** `video-use`, FFmpeg/FFprobe, the existing Ramayana EDLs, and `tools/av_sync_render.py`.
2. **Motion graphics:** HyperFrames, Remotion, PIL, or Manim only when a beat requires them.
3. **Optional visible finishing:** DaVinci Resolve Free operated through Computer Use or by the owner. Use it for visual inspection, manual trims, color polish, Fairlight adjustments, and export—not as an unattended automation engine.
4. **Structured Resolve MCP:** dormant until a valid Studio license exists.

The Ramayana workspace already has the stronger source of truth for this film: a 30 fps, 1080x1920, 24-row audio-master timeline; a frame-locked 166.633-second animatic; an inspectable EDL; narration assets; generated selects; deterministic graphics; and an audit. Do not rebuild that structure in another editor merely to obtain a graphical timeline.

### Alternatives reviewed

| Option | Finding | Decision |
|---|---|---|
| Generic FFmpeg MCPs | Expose trimming, concatenation, overlays, subtitles, and filters already available through `video-use` and direct FFmpeg | Do not install; duplicate surface with weaker project rules |
| Kdenlive | Free, MLT/XML project files, OpenTimelineIO import/export, and command-line rendering; no mature project-standard MCP found | Optional manual NLE only |
| OpenShot/libopenshot | Free and programmable through a video-editing library with Python bindings; no stronger ready-to-use MCP workflow than the current stack | Do not add now |
| Blender plus BlenderMCP | Free and deeply scriptable, but the popular MCP is designed mainly for 3D scene work and allows arbitrary Python execution | Reserve for a real Blender/VFX requirement |
| FireRed OpenStoryline | Promising MCP project, but currently requires API configuration and lists voiceover editing and additional effects as TODOs | Not production-ready for this film |

## Resolve Free computer-use procedure

1. Work only in a duplicate project and versioned timeline.
2. Start each action from a fresh screenshot or UI Automation snapshot; never send blind clicks.
3. Prefer keyboard shortcuts and internal Console scripts for bounded repeatable operations.
4. Verify the visible timeline after every change.
5. Save a copy before destructive trims, ripple operations, relinks, or grade changes.
6. Render a review cut and verify it outside Resolve with FFprobe and the project review workflow.
7. Do not describe this path as MCP control; it is supervised GUI/Console automation.

## Installed topology

| Component | Installed location | Role |
|---|---|---|
| Python 3.12.10 | `C:\Users\SE\AppData\Local\Programs\Python\Python312` | Stable interpreter for this MCP only |
| Core MCP v2.63.0 | `C:\Users\SE\AppData\Local\davinci-resolve-mcp` | Live Resolve control through 34 compound tools |
| Advanced MCP v2.63.0 | `C:\Users\SE\AppData\Local\davinci-resolve-mcp-advanced\node_modules\davinci-resolve-mcp` | 18 offline DRP/DRT/DRX, conform, grade-planning, database, audio-planning, and QC tools |
| Claude configuration | `.mcp.json` | Project-scoped registration |
| Codex configuration | `C:\Users\SE\.codex\config.toml` | User-level registration |

No credential is stored in either MCP entry.

## Installation or refresh

Pin the Python runtime:

```powershell
winget install --id Python.Python.3.12 --exact --scope user --silent --accept-package-agreements --accept-source-agreements --disable-interactivity
```

Install or refresh the managed core server. `PYTHONUTF8=1` avoids a Windows cp1252 console failure in the v2.63.0 installer. Supplying `DAVINCI_RESOLVE_MCP_PYTHON` chooses Python 3.12 for environment creation; do not pass `--python`, because that option changes the generated MCP command away from the managed virtual environment.

```powershell
$python312 = (& py -3.12 -c 'import sys; print(sys.executable)').Trim()
$env:DAVINCI_RESOLVE_MCP_PYTHON = $python312
$env:PYTHONUTF8 = '1'
npx --yes davinci-resolve-mcp@2.63.0 setup --clients manual --update-policy notify
```

The v2.63.0 managed-copy path omits `resolve-advanced` even though the published npm tarball contains it. Keep the core managed install, and install the official npm package at a separate stable prefix for the advanced server:

```powershell
npm install --prefix "C:\Users\SE\AppData\Local\davinci-resolve-mcp-advanced" --omit=dev --save-exact davinci-resolve-mcp@2.63.0
```

After an upstream update, repeat the MCP handshakes before changing the pinned version. Do not silently float production to `latest`.

## Resolve Studio installation boundary

1. Obtain DaVinci Resolve Studio only from Blackmagic Design or an authorized reseller.
2. Do not install the free edition as an MCP substitute; it will not make the live MCP work. It may still be installed separately as the optional supervised finishing interface described above.
3. A human must supply or purchase the Studio activation. Never record the activation key in the repository, MCP config, logs, screenshots, or memory.
4. Install to the standard Windows location unless there is a documented reason not to.
5. Launch Resolve Studio and set **Preferences → General → External scripting using → Local**.
6. Restart Resolve after changing scripting preferences.
7. Run the full verifier without `-AllowMissingResolve`.
8. Perform the live read-only test before creating or changing any project.

## Claude and Codex activation

- Codex registrations are added with `codex mcp add` and are visible in `codex mcp list`.
- Claude reads the project-scoped `.mcp.json`. On the first interactive Claude Code session in this repository, approve only the exact servers `davinci-resolve` and `davinci-resolve-advanced`.
- Restart the agent host after adding or updating MCP servers so its tool inventory is refreshed.
- The core server may be available while Resolve is closed, but live commands will fail until Studio is running and reachable.

## Per-edit operating procedure

1. Confirm the edit strategy, intended deliverable, aspect ratio, frame rate, and approval boundary.
2. Inventory sources with read-only probes. Do not move, rename, overwrite, transcode, or delete camera originals.
3. Create a new Resolve project or a clearly named duplicate. Never experiment in the only copy of a project.
4. Create a versioned timeline for each material revision.
5. Ask the agent for one bounded operation at a time: ingest, organize, transcribe, rough assembly, trim pass, audio pass, grade plan, graphics, captions, or render.
6. Review the timeline after every operation. Do not allow a later task to certify the task that created the change.
7. Keep automated analysis outputs, transcripts, proxies, and caches inside project-specific working directories.
8. Use the advanced server read-only first. Any DRP/DRT/DRX or database mutation requires a backup plus a named output destination.
9. Render review cuts before finals. Verify seams, timing, continuity, dialogue intelligibility, music/SFX balance, captions, color, framing, and brand/legal requirements.
10. Export masters only after human approval.

## Optional transcription

The current MCP detects transcription backends but does not install one. DaVinci Resolve Studio has built-in transcription/caption capabilities; the linked demonstration used WhisperX separately. Do not install a multi-gigabyte Whisper/PyTorch stack by default. Choose a backend only after checking the machine GPU, the language/diarization need, expected footage hours, and whether Resolve's built-in transcript is sufficient.

## Verification

MCP-only preflight, valid before Resolve Studio is installed:

```powershell
powershell -ExecutionPolicy Bypass -File tools/verify-davinci-environment.ps1 -AllowMissingResolve
```

Full environment check after Studio installation:

```powershell
powershell -ExecutionPolicy Bypass -File tools/verify-davinci-environment.ps1
```

Passing the file/API checks is not the live acceptance test. The final gate is a running Studio instance, a read-only MCP connection, and one reversible test project in the real production host.
