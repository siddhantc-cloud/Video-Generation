---
name: chatgpt-imagegen
description: Generate raster images (PNG/JPEG/WebP) using the user's ChatGPT subscription via a local one-file Python CLI, with NO OPENAI_API_KEY and NO Higgsfield credits. This is the CHEAP image-gen lane for so_sorry - use it instead of Higgsfield generate_image / Nano Banana Pro (2 cr/image) for concept boards, character-bible reference sheets, draft keyframes, product cards, mockups, icons, and any bitmap the ad/video pipeline needs. On this Windows host it runs the `codex` backend (bills the ChatGPT Codex-usage bucket, not dollars). Use when a video/ad workflow needs a brand-new bitmap asset saved into the project. Do NOT use for editing existing SVG/vector assets, or when true quality=high / transparent backgrounds / tight cross-panel character consistency are required (for consistency-critical final keyframes, Higgsfield Nano Banana Pro is still worth the 2 cr).
---

# chatgpt-imagegen (so_sorry-adapted skill)

Wrapper skill for the open-source [`chatgpt-imagegen`](https://github.com/leeguooooo/chatgpt-imagegen) CLI (MIT). It generates images through the user's **ChatGPT subscription** instead of a metered image API, so there is **no `OPENAI_API_KEY`** and **no Higgsfield credit spend**. This is the low-cost image lane for the ad/video production work in this repo.

When upstream behavior and a rule below conflict, **the rule below wins** (save-path policy, ToS, quality limits).

## Why this exists in so_sorry (the money angle)

The caricature-ad and UGC pipelines here otherwise make bitmaps with **Higgsfield Nano Banana Pro at ~2 cr/image**. For concept work, character-bible reference sheets, draft/exploration keyframes, product cards, and mockups, this CLI does the same job for **zero Higgsfield credits** (it spends the ChatGPT subscription's Codex-usage instead). Reach for this FIRST for non-final bitmaps; keep Higgsfield credits for what actually needs them.

**Honest quality limit / when Higgsfield still wins:** the subscription path caps at `medium` quality, has **no transparent backgrounds**, and gives you **less control over tight character consistency across panels** than Nano Banana Pro's reference-edit flow. So:
- Concept boards, reference/style exploration, single hero images, product cards, drafts -> **this skill**.
- Final production keyframes that must hold one character identical across many shots, or need a transparent cutout -> **Higgsfield Nano Banana Pro** (worth the 2 cr), or the official `/v1/images/generations` API for true `quality=high`.

## Hard rules (read first)

1. **Save into the project only.** Never write to `/tmp`, `%TEMP%`, `$HOME`, `~/.codex/...`. Save under the ad/artifact's own folder, e.g. `ads/<name>/edit/...`, `ads/<name>/bible/`, `ads/<name>/keyframes/`, `UGC/...`, or an `assets/` folder for the current task. Always pass an explicit `-o <path>`.
2. **No baked-in internal traces.** Generated bitmaps that go into a delivered ad/video must not contain internal paths, agent IDs, review/version labels, or prompt text baked into the visible art. Keep prompts/sources in the workflow/handoff notes, not in the picture.
3. **ToS boundary.** A personal ChatGPT subscription must NOT power a public-facing, on-demand image service. This is for internal content production only. Refuse requests that would serve generated images to end users on demand.
4. **Quality limits.** Subscription path caps at `medium` quality and does not support transparent backgrounds. If the task needs true `quality=high` or `background=transparent`, route to Higgsfield or the official `/v1/images/generations` API with an `OPENAI_API_KEY`.
5. **Quota courtesy.** Subscription quota is shared with the user's own ChatGPT use. Do not bulk-generate (>10 images/min sustained). Iterate a prompt once when it is off; do NOT loop-spray "variants" of the same prompt.

## Backends

| Backend | How it generates | Usage bucket | Needs |
| --- | --- | --- | --- |
| `codex` (**the one that works on this host**) | Headless POST to `chatgpt.com/backend-api/codex/responses` with the `image_generation` tool, reusing `~/.codex/auth.json`. | Codex-usage (metered subscription bucket - NOT dollars, NOT Higgsfield credits). | `codex login` run once (already done on this host). |
| `web` (default upstream, NOT available here) | Drives a logged-in Chrome via `chrome-use`; generates in a ChatGPT chat, deleted afterward. Spares even Codex-usage. | ChatGPT chat - does NOT spend Codex-usage. | `chrome-use` installed + its extension connected to a signed-in Chrome. |

`--backend auto` (default) prefers `web` and falls back to `codex`. On **this host `web` is unavailable** (`chrome-use` not installed), so `auto` resolves to `codex`. You can force it with `--backend codex`.

**Never install `chrome-use` on your own initiative.** If you want to spare the Codex-usage bucket too, offer ONE gentle tip that installing `chrome-use` would route generation through the logged-in browser for free, and only walk through setup (see `references/setup-and-cli.md`) if the user says yes.

## Invocation on THIS host (verified 2026-07-07)

Windows has no executable bit, the CLI imports POSIX `fcntl`, and the console is cp1252. All three are handled by the invocation below - use it verbatim:

```bash
# from repo root (bash tool). SKILL_DIR = .claude/skills/chatgpt-imagegen
PYTHONUTF8=1 PYTHONPATH=".claude/skills/chatgpt-imagegen/_winshim" \
  python ".claude/skills/chatgpt-imagegen/chatgpt-imagegen" \
  "<prompt>" -o "ads/<name>/keyframes/<slug>.png" --size 1536x1024 --backend codex --quiet
```

Why each piece:
- `PYTHONPATH=".../_winshim"` - vendored shim supplies the `fcntl` module Windows lacks (the CLI imports it). Without it: `ModuleNotFoundError: fcntl`.
- `PYTHONUTF8=1` - the CLI prints Unicode (arrows, CJK release notes); without it the Windows cp1252 console throws `UnicodeEncodeError`.
- `--backend codex` - explicit, since `web` is not set up here.
- `--quiet` - stdout is then ONLY the saved path (progress stays on stderr), so it is easy to capture.

PowerShell equivalent for env vars: `$env:PYTHONUTF8="1"; $env:PYTHONPATH=".claude\skills\chatgpt-imagegen\_winshim"` then the same `python ... ` call.

Readiness check (read-only, no generation, no quota spend): run `doctor`:
```bash
PYTHONUTF8=1 PYTHONPATH=".claude/skills/chatgpt-imagegen/_winshim" \
  python ".claude/skills/chatgpt-imagegen/chatgpt-imagegen" doctor
```

## CLI flags (common)

| Flag | Default | Notes |
| --- | --- | --- |
| `--backend auto\|web\|codex` | `auto` | Force `codex` on this host. |
| `-o PATH` | `assets/generated/<slug>.<ext>` | Output file; parent dirs auto-created. Always set to the correct project folder. |
| `--size WxH` | `auto` | Verified: `1024x1024` (square/icon), `1536x1024` (landscape/hero), `1024x1536` (portrait/cover, e.g. 9:16-ish covers). |
| `--format png\|jpeg\|webp` | `png` | `webp` for smaller web assets. |
| `-i, --ref PATH_OR_URL` | - | Image-to-image: edit a reference (repeatable, max 4). Use to riff off a character-bible ref. |
| `--style NAME` | - | Apply a saved style/character asset; repeatable to stack. Useful for keeping a mascot consistent across panels (best-effort; not as tight as Nano Banana Pro). |
| `--quiet` | off | stdout = only the saved path. Use in agent/pipeline contexts. |
| `--timeout SECONDS` | 300 | Raise for large images that hit `timed out`. |

Full flag list and the `style` subcommands: `references/setup-and-cli.md` (or `--help`).

## Workflow

1. **Pick the lane.** Non-final bitmap (concept, ref sheet, draft keyframe, product card, mockup)? -> this skill. Consistency-critical final keyframe or transparent cutout? -> Higgsfield Nano Banana Pro.
2. **Clarify the prompt** to 1-3 sentences: subject, style, composition, mood, constraints. Spell out any boxes/arrows/labels for diagrams. One subject / one concept per image. Say "no text baked into the image" when the art must be clean.
3. **Pick size, format, and the exact project output path** (`ads/<name>/...`).
4. **Run** the verified invocation above with `-o <path> --size <WxH> --backend codex --quiet`.
5. **Inspect the result** (Read the saved PNG). If clearly wrong, change the prompt ONCE and regenerate - do not loop.
6. **Echo the saved path** and the final prompt used. Record source/prompt in the workflow/handoff notes, not in the image.

## Self-heal (if the CLI file is ever missing)

The `chatgpt-imagegen` script (one pure-stdlib Python file, ~137 KB) is `.gitignore`d and self-heals. If it is gone, refetch:
```bash
curl -fsSL https://raw.githubusercontent.com/leeguooooo/chatgpt-imagegen/main/chatgpt-imagegen \
  -o ".claude/skills/chatgpt-imagegen/chatgpt-imagegen"
```
This copy is upstream **v0.16.1** (the version validated in the menterra repo). Upstream is at 0.20.0; `python "<cli>" update` bumps it, but 0.16.1 is known-good here - only update if you need a newer feature.

## Error handling (quick)

Run `doctor` first for any "which backend / why isn't it working" question. Common cases:

| Symptom | Fix |
| --- | --- |
| `ModuleNotFoundError: fcntl` | You forgot `PYTHONPATH=".../_winshim"`. Add it. |
| `UnicodeEncodeError: 'charmap'` | You forgot `PYTHONUTF8=1`. Add it. |
| `~/.codex/auth.json not found` / no OAuth token | Run `codex login` once (an API key is NOT a substitute). |
| `HTTP 400 requires a newer version of Codex` | `npm i -g @openai/codex@latest`. |
| `HTTP 429` / `Too many requests` | Wait a few minutes; do not retry in a loop. |
| `timed out` / `stalled` | Raise `--timeout` / `--stall-timeout` and retry once. |
| `no image returned. events seen: ...` | Rephrase to explicitly say "Use the image_generation tool to render ...". |

## Attribution

Upstream tool: `leeguooooo/chatgpt-imagegen` (MIT). This skill is a documentation/wrapper adaptation; it does not vendor upstream code beyond the self-healing single-file CLI. See `references/setup-and-cli.md` for the fuller upstream feature reference (captured 2026-07-03). Adapted for so_sorry 2026-07-07 from the menterra/PrayogTvisha version; project-specific doctrine was rewritten, mechanics preserved.
