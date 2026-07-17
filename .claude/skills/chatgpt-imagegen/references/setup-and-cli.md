# chatgpt-imagegen — setup and CLI reference

Fuller reference for the [`chatgpt-imagegen`](https://github.com/leeguooooo/chatgpt-imagegen) CLI (MIT), captured 2026-07-03. Read `../SKILL.md` first for the so_sorry hard rules (save-path, ToS, quality limits) and the verified Windows invocation. Where this doc and a rule in `../SKILL.md` conflict, `../SKILL.md` wins.

## What it is

A zero-dependency, single-file, stdlib-only Python CLI that generates images through the user's ChatGPT subscription — no `OPENAI_API_KEY`, no gateway, no daemon. It exposes the same internal `backend-api/codex` image capability that the official Codex CLI uses. Because it is one pure-Python file, the "install" is just fetching the file; the AI-agent skill self-heals by curling it on first use.

## Two backends and how billing differs

OpenAI meters two separate buckets; which you spend depends on where the image is made.

- **`web` (default)** — drives the user's already-logged-in Chrome through [`chrome-use`](https://github.com/leeguooooo/chrome-use) and generates in a normal ChatGPT chat (Temporary Chat disables the image tool, so it always opens a regular chat). This runs on the ChatGPT conversation surface and does **not** consume the metered Codex-usage limit; it works on any account including free tier (subject to the daily image cap). Each run's chat is filed under a ChatGPT Project (default `imagegen`, auto-created) and deleted afterward by default. Only a real logged-in browser clears the Cloudflare edge check, the sentinel proof-of-work, and the interactive Cloudflare Turnstile token — a headless client cannot forge Turnstile, and the token is single-use, so there is no "grab token then go headless" shortcut.
- **`codex`** — headless POST to `chatgpt.com/backend-api/codex/responses` with `tools: [{"type":"image_generation"}]`, reusing the OAuth token in `~/.codex/auth.json`. Streams an SSE response and base64-decodes the `image_generation_call` result. This bills the **Codex-usage** bucket. Auto-refreshes the OAuth token on 401/403 via `auth.openai.com/oauth/token` and persists it back.

`auto` prefers `web` and falls back to `codex` only when the browser is unavailable/not-logged-in. It does NOT fall back to `codex` if `web` was reachable but generation failed after submitting (that would spend the bucket auto-mode protects) — it errors and suggests `--backend codex`.

## Prerequisites

- **Python 3.10+** on `PATH` (needed to run the one-file CLI).
- **For `web`:** `chrome-use` installed and its browser extension connected to a Chrome signed in to chatgpt.com. Do NOT install `chrome-use` for the user unprompted (see SKILL.md policy).
- **For `codex`:** run once, ever — `npm i -g @openai/codex` then `codex login` (opens a browser to sign in; writes `~/.codex/auth.json`).

No `OPENAI_API_KEY` is required for either backend, and setting one does not help — this is the subscription path.

### Opt-in `chrome-use` setup (only after the user agrees)

```bash
# 1. Install the CLI (provides `chrome-use`)
curl -fsSL https://raw.githubusercontent.com/leeguooooo/chrome-use/main/install.sh | sh
# 2. Register the native-messaging host
chrome-use extension install
# 3. Load the Chrome extension (chrome://extensions -> Developer mode -> Load unpacked / Web Store), then restart Chrome
# 4. Sign in to https://chatgpt.com in that Chrome
# 5. Verify: a quick `chatgpt-imagegen "test" --backend web` should report "using current Chrome (relay)"
```

Verify the relay with `chrome-use daemon status --json` → `"relay": true`.

## Windows / cmd host notes

This repo's host is Windows (cmd/PowerShell). The upstream examples are bash. Adaptations:

- No executable bit — run as `python "<skill-dir>\chatgpt-imagegen" ...`, not `./chatgpt-imagegen`.
- Self-heal fetch (cmd):
  ```cmd
  if not exist ".agents\skills\chatgpt-imagegen\chatgpt-imagegen" curl -fsSL https://raw.githubusercontent.com/leeguooooo/chatgpt-imagegen/main/chatgpt-imagegen -o ".agents\skills\chatgpt-imagegen\chatgpt-imagegen"
  ```
  PowerShell alternative if `curl` maps to `Invoke-WebRequest`: `curl.exe -fsSL <url> -o <path>` (force the real curl with `.exe`).
- Capture the saved path (cmd): `for /f "delims=" %p in ('python "...\chatgpt-imagegen" "prompt" --quiet') do set OUT=%p`
- Environment vars: `set CHATGPT_IMAGEGEN_BACKEND=web` (cmd) or `$env:CHATGPT_IMAGEGEN_BACKEND="web"` (PowerShell).
- `chrome-use` is a Chrome-driver; confirm it and the extension actually run on this host before relying on the `web` backend. If not, the `codex` fallback still works headlessly.

## CLI options (full)

```
chatgpt-imagegen "<prompt>" [options]
```

| Flag | Default | Notes |
| --- | --- | --- |
| `--backend` | `auto` | `auto` \| `web` \| `codex`. Also `CHATGPT_IMAGEGEN_BACKEND`. |
| `-o, --out PATH` | `assets/generated/<slug>.<ext>` | Output file; parent dirs created. |
| `--size` | `auto` | `auto` or `WIDTHxHEIGHT`. Verified: `1024x1024`, `1536x1024`, `1024x1536`. Larger (e.g. `3840x2160`) forwarded as-is; backend may reject — fall back to a verified size. |
| `--format` | `png` | `png` \| `jpeg` \| `webp`. |
| `-i, --ref PATH_OR_URL` | - | Image-to-image: edit a reference. Repeatable; max 4 attach per run (character-first). Local path or http(s) URL. |
| `--style NAME` | - | Apply a saved style/character asset (text + pinned refs). Repeatable to stack. |
| `--no-style` | off | Skip all active assets for this run. |
| `--profile` | `auto` | (web) Which Chrome profile to drive: `auto` / `relay` / a name. |
| `--session NAME` | - | (web) Reuse a named Chrome tab group across runs. |
| `--project NAME` | `imagegen` | (web) ChatGPT Project to file the chat under; created if absent. `--project ""` = plain top-level chat. |
| `--keep-conversation` | off | (web) Keep the chat (default deletes it). |
| `--keep-tab` | off | (web) Leave the tab open (implies keep-conversation). |
| `--open` | off | Open the saved image in the default viewer. |
| `--quiet` | off | stdout = only the saved path. Progress still on stderr. |
| `--no-progress` | off | Silence the stderr progress timeline (errors still print). |
| `--timeout SECONDS` | 300 | Total wall-clock budget. Large images can take 2-3 min. |
| `--stall-timeout SECONDS` | 120 | Max silence before declaring a stall (clamped to `--timeout`). |
| `-V, --version` | - | Print CLI version. |

Subcommands: `doctor` (which backend is ready + which `auto` picks), `style <verb>` (`list`/`show`/`add`/`add-ref`/`rm-ref`/`rm`/`use`/`clear`/`reset`).

Output contract: the saved path prints on **stdout**; the readable timeline (stamped with elapsed seconds) and errors go to **stderr**.

## Styles and assets

Stored in `~/.config/chatgpt-imagegen/styles.json` (honors `$XDG_CONFIG_HOME`); pinned images copied under `assets/`.

- `--kind style` (default): match an aesthetic, don't copy content.
- `--kind character`: reproduce a recurring subject faithfully (mascot/persona).

```bash
chatgpt-imagegen style add brand "flat vector, bold shapes, teal accent, white background"
chatgpt-imagegen style add pip "a round orange fox" --kind character --ref pip-a.png --ref pip-b.png
chatgpt-imagegen "Pip ordering coffee" --style pip --style brand   # same fox, brand style (stacked)
chatgpt-imagegen style add pip --from-last --kind character        # pin the image you just liked
chatgpt-imagegen "a photorealistic forest" --no-style              # skip active assets once
```

Resolution order: `--no-style` > `--style NAME...` > active default set > none. Built-in styles: `doodle` (crude MS-Paint look), `xiaohei` (Ian hand-drawn explainer), `snoopy` (Peanuts newspaper-comic look). For so_sorry, prefer project-owned character-bible refs (`--kind character --ref ...`) over external built-in styles when you need a recurring mascot/ingredient to stay on-model.

## Concurrency

`web` runs serialized (1 at a time — one shared Chrome, and the page rate-limits hard); `codex` runs up to 4 in parallel. Excess runs queue on a lock pool and `--timeout` only starts once a slot frees. Override via `CHATGPT_IMAGEGEN_WEB_CONCURRENCY` / `CHATGPT_IMAGEGEN_CODEX_CONCURRENCY` (`0` = unlimited). Shared subscription quota — do not sustain >10 images/min.

## When NOT to use (route to the official API instead)

Use the official `/v1/images/generations` API with an `OPENAI_API_KEY` when you need: true `quality=high` or native transparent backgrounds (subscription exposes neither); a public-facing service (personal subscription would violate OpenAI ToS); deterministic per-call billing; or sustained >10 images/min.

## Error / status reference

| Symptom | Cause | Fix |
| --- | --- | --- |
| `~/.codex/auth.json not found` | Codex CLI never signed in | `npm i -g @openai/codex && codex login` |
| `no ChatGPT OAuth access_token in ~/.codex/auth.json` | Only an API key present, not a subscription OAuth token | `codex login` (an API key is not a substitute) |
| `HTTP 400 requires a newer version of Codex` | Local codex CLI outdated | `npm i -g @openai/codex@latest` |
| `HTTP 401` / `403` then works | Token expired, refresh succeeded | None — auto-retried |
| `refresh_token is no longer valid` | Refresh token revoked/rotated | `codex login` again |
| `no logged-in ChatGPT browser available` | (web) relay/extension not connected or profile launch failed | `chrome-use extension install` + load extension + restart Chrome; or fully quit+reopen Chrome; or `--backend codex`. Run `doctor` for the precise reason. |
| `stalled: ... no data for ~Ns` | Backend hung/overloaded | Retry; raise `--stall-timeout` / `--timeout`. |
| `timed out: no image within Ns` | Genuinely large image | Raise `--timeout` (e.g. 420) and retry. |
| `no image returned. events seen: ...` | Model didn't call the tool | Rephrase: "Use the image_generation tool to render ...". |
| `HTTP 429` / `Too many requests` | Rate-limited | Wait a few minutes; do not loop. |
| `warning: project 'X' unavailable ...` | (web) Project API hiccup | None — image still generated in a plain chat. |

Run `chatgpt-imagegen doctor` for a read-only readiness checklist (codex token; chrome-use installed + version; relay connected; logged-in profiles; which backend `auto` would pick, and the CLI version vs latest on `main`).

## Related upstream

- `chrome-use` (web backend driver): https://github.com/leeguooooo/chrome-use
- HTTP gateway sibling (OpenAI-compatible server): https://github.com/leeguooooo/agent-cli-to-api
- How-it-works (technical): https://github.com/leeguooooo/chatgpt-imagegen/blob/main/docs/how-it-works.md

Content on this page was rephrased and condensed from the upstream README/SKILL/how-it-works for compliance with licensing restrictions.
