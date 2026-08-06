# SOP 00: Set up the machine and the repository

This is the first document a new operator reads. It takes a person from an empty machine to a
verified workspace that can produce a video in either category this repository supports.

| Document | Purpose |
|---|---|
| `docs/SOP-00-SETUP.md` | This file. Machine setup, credentials, MCP servers, skills, verification. |
| `docs/SOP-01-STORY-FILM.md` | Produce a NEW story-driven generative brand film. Reference case: Ramayana x ZebPay SIP. |
| `docs/SOP-02-PRODUCT-EXPLAINER.md` | Produce a NEW deterministic product explainer. Reference case: CryptoPack Rebalancing. |

The complete creative process stays in `docs/video-production-workflow.md`. This SOP does not repeat
it. This SOP tells you how to make the tools work.

## The two categories

Pick the category before you pick a tool.

| | Category A: story film | Category B: product explainer |
|---|---|---|
| SOP | `docs/SOP-01-STORY-FILM.md` | `docs/SOP-02-PRODUCT-EXPLAINER.md` |
| The value is | Emotion, character, atmosphere, performance | Clarity about a real product |
| Picture comes from | A generative video model, plus deterministic sections | A deterministic renderer only |
| Exactness | A metaphor is allowed | Every number and claim must be exact |
| Marginal cost | Generation credits, per film | Effectively one small text-to-speech call |
| Rebuild | Each take is a fresh performance | Byte-reproducible |
| Reference case | `Ramayana-ZebpaySIP/` | `CryptoBalancing-Zebpay/` |

A mixed film is normal. Route each interval separately, never the whole film at once.

## What each category costs

| Item | Category A | Category B |
|---|---|---|
| Agent (Claude Code, Codex, or Cursor) | Existing subscription | Existing subscription |
| Generative motion | About 147 to 165 credits at 480p for a 52 second film | **None** |
| Keyframe stills | An image engine, per shot | **None**. Real screenshots. |
| Deterministic graphics | Free, local render | Free, local render. This is the whole picture. |
| Music and SFX | Licensing, or produce your own | Free. Seeded local synthesis. |
| Narration | ElevenLabs, small | ElevenLabs, small. The only paid item. |
| Encode, probe, QC | Free | Free |

Category B is effectively free. Its only paid item is one narration call of a few hundred
characters, and even that can be replaced with the free Edge TTS helper at a quality cost. See
`docs/SOP-02-PRODUCT-EXPLAINER.md`.

Credit numbers are dated evidence from 2026-07-24. Re-quote live before you spend.

## Checklist

| Requirement | Pass condition | Evidence | Owner | Status |
|---|---|---|---|---|
| Repository | The clone exists and LFS media is real, not pointer text | `git lfs ls-files`, file sizes | Operator | Required |
| Host tools | Git, Git LFS, Node, npm, Python, FFmpeg, FFprobe, uv resolve | `tools/setup-video-repo.ps1` | Operator | Required |
| Credentials | ElevenLabs key is in the environment; Higgsfield CLI is logged in | Setup script rows | Human only | Required |
| MCP servers | The ElevenLabs server command resolves on this machine | Setup script rows | Operator | Required |
| Agent skills | Provider skills exist for the host; project skill mirrors match | Setup script parity rows | Operator | Required |
| Spend safety | No paid job runs before a live quote and a human approval | Job packet | Human | Required |

## Who does what

| Symbol | Meaning |
|---|---|
| **HUMAN ONLY** | A person must do this. An agent must never do it. It needs a browser login, a password, a payment method, or a personal account. |
| **AGENT OK** | An agent can run this for you after you approve the command. |
| **EITHER** | A person or an agent can do it. |

## What a fresh clone gives you

The owner approved a **reproduction set** on 2026-08-06. The paid and otherwise irreplaceable inputs
for both reference films are now in Git LFS. Run `git lfs pull` and you can rebuild.

| Reference film | In the clone through Git LFS |
|---|---|
| Ramayana x ZebPay SIP | The 13 approved selects, their native SFX stems, the raw and repaired ElevenLabs narration, the phrase-locked narration and audio masters, the two selected deterministic renders, and the promoted v005 master |
| CryptoPack Rebalancing | The six narration segments, the ElevenLabs provider master, the seeded music bed, the six SFX files, and the packaged v002 review cut |

Everything not paid for stays in ordinary Git: scripts, keyframes, storyboards, timelines, phrase
maps, caption groups, audio metadata, review records, cost ledgers, and the complete HyperFrames
project.

Still excluded on purpose, and why:

| Excluded | Reason |
|---|---|
| Rejected and superseded takes | Large, and the review records already describe why they failed |
| Working renders and intermediate mixes | Regenerable from the timelines |
| Superseded final versions v001 to v003 | v005 is the promoted master |
| Third-party licensed demo music | Do not redistribute it. Its source is in `Ramayana-ZebpaySIP/audio/music/demo-v011/SOURCE.md`. |

Ask the owner if you need any of it. It is one command to add.

One honest limit: a generative take is never byte-identical. If you regenerate motion instead of
reusing the selects, you get a new film that follows the same plan, not the same file.

## Step 1. Clone the repository. HUMAN ONLY

Install Git and Git LFS before you clone. A clone without LFS gives you small text pointers where the
videos should be.

```powershell
winget install Git.Git
winget install GitHub.GitLFS
git lfs install
```

Then clone and fetch the media.

```powershell
git clone https://github.com/MythyaVerse/marketing-video-generation-pipeline.git
cd marketing-video-generation-pipeline
git switch codex/cryptopack-rebalancing-video
git lfs pull
```

Confirm the media is real. Each file must be megabytes, not bytes.

```powershell
git lfs ls-files
Get-ChildItem meetings\2026-07-29-zebpay-video-showcase\videos | Select-Object Name, Length
```

If a file is about 130 bytes, the LFS objects did not arrive. Run `git lfs install` and `git lfs pull`
again.

## Step 2. Install the host tools. EITHER

The verified host is Windows 11 with PowerShell. The commands below use winget.

```powershell
winget install Git.Git
winget install GitHub.GitLFS
winget install OpenJS.NodeJS.LTS
winget install Python.Python.3.12
winget install Gyan.FFmpeg
winget install astral-sh.uv
```

Then install the runtime tools.

```powershell
npm install --global @higgsfield/cli@latest
uv tool install yt-dlp
uv tool update-shell
python -m pip install requests librosa matplotlib pillow numpy
```

Close the terminal and open a new one. New PATH entries do not reach an open shell.

Versions verified on the reference machine on 2026-08-06:

| Tool | Verified version |
|---|---|
| Git | 2.54.0 |
| Git LFS | 3.7.1 |
| Node.js | 24.16.0 |
| npm | 11.13.0 |
| Python | 3.14.5 |
| FFmpeg and FFprobe | 8.1.1 |
| uv and uvx | 0.11.21 |
| Higgsfield CLI | 1.1.19 |
| yt-dlp | 2026.07.04 |

Older versions can work. Newer versions can change behavior. Record what you used.

## Step 3. Credentials. HUMAN ONLY

Never put a credential in a tracked file. Never let an agent read a key value back to you. Never
paste a key into chat.

### 3.1 ElevenLabs. Required for narration

1. Sign in at `elevenlabs.io` with the account that owns the campaign voices.
2. Create an API key.
3. Set it as a Windows user environment variable named `ELEVENLABS_API_KEY`.

```powershell
[Environment]::SetEnvironmentVariable('ELEVENLABS_API_KEY', '<paste-your-key>', 'User')
```

Open a new terminal afterwards. The name matters. The project tools read `ELEVENLABS_API_KEY` from
the process environment. The repository `.env` file also accepts `ELEVEN_LABS_API_KEY`, but only the
Ramayana Python helper reads that older name. Use `ELEVENLABS_API_KEY` for new work.

### 3.2 Higgsfield. Required only for generative motion

Run the login yourself in an interactive terminal. An agent must not do this.

```powershell
higgsfield auth login
higgsfield account status --json
```

The account needs credits before any paid job. See the dated credit model in
`docs/video-production-workflow.md`. Credits and prices change. Always re-quote live.

### 3.3 Sarvam. Optional

Only needed for Indian-English narration experiments. Put `SARVAM_API_KEY=<value>` in the ignored
`.env` file at the repository root, or set it in the process environment. Follow
`.agent-harness/recipes/sarvam-bulbul-v3-narration.md`.

### 3.4 Rotate a leaked key

If a key ever appears in a file, a log, a screenshot, or a chat, rotate it at the provider
immediately. Do not try to hide it in history.

## Step 4. MCP servers. EITHER

`.mcp.json` at the repository root configures three servers. It holds no secrets.

| Server | Purpose | Needed? |
|---|---|---|
| `ElevenLabs` | Speech, voice, and audio tools | Required for narration work |
| `davinci-resolve` | Live Resolve Studio control | Optional. Needs Resolve Studio. |
| `davinci-resolve-advanced` | Offline Resolve project operations | Optional |

The committed file contains absolute paths from the reference machine. On your machine the
ElevenLabs entry must point at your own `uvx`. Find it with `(Get-Command uvx).Source`, then edit the
`command` value in `.mcp.json`. Do not commit a machine-specific path unless the team agrees to it.

If you do not use DaVinci Resolve, leave the two Resolve entries in place and ignore them, or delete
them locally. They are not required for either film. The canonical editorial stack is video-use plus
FFmpeg and FFprobe.

Restart your agent host after you change `.mcp.json`.

## Step 5. Agent skills. EITHER

Two skill layers exist. Both matter.

### 5.1 User-level provider skills

These live in your home directory, not in the repository. They teach the agent how to drive the
providers.

| Skill | Upstream source |
|---|---|
| `higgsfield` | `OSideMedia/higgsfield-ai-prompt-skill` |
| `higgsfield-generate`, `higgsfield-soul-id` | `higgsfield-ai/skills` |
| `video-use` | `browser-use/video-use` |
| `remotion-best-practices`, `remotion-create`, `remotion-render`, `remotion-captions` | `remotion-dev/skills/skills` |

Install the same paths into both host roots so Codex and Claude behave the same way:

- `%USERPROFILE%\.claude\skills\`
- `%USERPROFILE%\.codex\skills\`

The pinned upstream commits and the full install method are in
`.agent-harness/recipes/video-production-environment.md`.

The HyperFrames skills install through the HyperFrames CLI:

```powershell
npx hyperframes skills update
```

Restart the agent host after any skill install. A running session does not see new skills.

### 5.2 Project skills and agents

These live in the repository and travel with the clone. You do not install them. You only keep the
mirrors in sync.

| Layer | Canonical source | Mirror |
|---|---|---|
| Generic production skills | `.codex/skills/script-video-*` | `.claude/skills/script-video-*` |
| Ramayana evidence skills | `.codex/skills/ramayana-*` | `.claude/skills/ramayana-*` |
| Shared production agents | `video-production-system/agents/` | `.claude/agents/` |

Never edit a mirror as the source of truth. After any change, sync and check:

```powershell
powershell -ExecutionPolicy Bypass -File tools/sync-script-video-skills.ps1
powershell -ExecutionPolicy Bypass -File tools/sync-script-video-skills.ps1 -Check
powershell -ExecutionPolicy Bypass -File tools/sync-script-video-agents.ps1 -Check
powershell -ExecutionPolicy Bypass -File tools/sync-ramayana-video-skills.ps1 -Check
```

Codex has no project file-agent discovery surface. It reads the canonical agent definitions
directly. That is an intentional host mapping, not a missing feature.

## Step 6. Verify. AGENT OK

Run the setup checker from the repository root.

```powershell
powershell -ExecutionPolicy Bypass -File tools/setup-video-repo.ps1
```

It prints one row per requirement, then a list of the actions only a human can do. It never prints a
credential value, never logs in, and never spends money.

Run the safe automated repairs with:

```powershell
powershell -ExecutionPolicy Bypass -File tools/setup-video-repo.ps1 -Install
```

`-Install` runs `git lfs install`, `git lfs pull`, the npm and uv tool installs, the Python packages,
and the skill and agent syncs. It still refuses to log in for you.

Exit codes: `0` ready, `1` a machine fix is required, `2` a human action is required.

The deeper environment verifier still exists and checks user-level skill parity and hashes:

```powershell
powershell -ExecutionPolicy Bypass -File tools/verify-video-environment.ps1
```

That verifier uses absolute paths from the reference machine. On a different machine, treat its
skill-path failures as informational and trust `tools/setup-video-repo.ps1`.

## Step 7. Use `/setup` inside your agent. EITHER

The same instructions are available as a command in all three hosts.

| Host | How to start it |
|---|---|
| Claude Code | Type `/setup` |
| Cursor | Type `/setup` |
| Codex | Type `/setup`, or invoke the skill as `$script-video-setup` |

The command reads this SOP, runs `tools/setup-video-repo.ps1`, explains each failing row, fixes what
a machine may fix, and then stops and hands you the list of human actions. It never runs a login and
never spends credits.

Codex reads custom prompts from `%USERPROFILE%\.codex\prompts`. To get `/setup` there, copy the file
once:

```powershell
New-Item -ItemType Directory -Force -Path "$env:USERPROFILE\.codex\prompts" | Out-Null
Copy-Item .codex\prompts\setup.md "$env:USERPROFILE\.codex\prompts\setup.md" -Force
```

Codex can always use the project skill without that copy.

## Human-only actions, collected

| # | Action | Why an agent must not do it |
|---|---|---|
| 1 | Clone the repository and run `git lfs pull` | It needs your Git credentials and repository access |
| 2 | Create the ElevenLabs API key and set `ELEVENLABS_API_KEY` | It needs a provider account login |
| 3 | Run `higgsfield auth login` | It opens a browser login and binds a paid account |
| 4 | Buy or top up Higgsfield credits | It spends money |
| 5 | Approve every paid generation against a live quote | Spend safety. See `AGENTS.md`. |
| 6 | Listen to the encoded film and judge voice, tone, and pronunciation | A machine transcript is not a taste verdict |
| 7 | Give brand, product, legal, and regulatory approval | Only a person carries that responsibility |
| 8 | Promote a review cut to a final | Delivery is an explicit human decision |
| 9 | Rotate any leaked credential | It needs the provider account |

## Safety rules that never change

- Never commit `.env`, a key value, a provider token, or customer data.
- Never add raw takes, working renders, or review media to Git. Track a final only when the owner
  asks, and follow `.agent-harness/recipes/git-lfs-video-delivery.md`.
- Never run a paid job without a current schema, a live quote, and a recorded human approval.
- Never treat a technical pass as a creative approval.
- Never force-push for media delivery.
- Do not reinstall Qwen3-TTS. The owner removed it on 2026-07-25. It needs explicit owner approval
  and about 15 GiB.

## Troubleshooting

| Symptom | Cause | Fix |
|---|---|---|
| A video file is about 130 bytes | The LFS object did not download | `git lfs install`, then `git lfs pull` |
| `ELEVENLABS_API_KEY is not available` | The variable is set but the shell is old | Open a new terminal. Check the spelling. It has no underscore between Eleven and Labs. |
| `higgsfield: command not found` | The npm global bin is not on PATH | Reopen the terminal. Check `npm bin -g`. |
| The ElevenLabs MCP server fails to start | `.mcp.json` points at another machine's `uvx` | Set the `command` value to your own `(Get-Command uvx).Source` |
| A skill parity check fails | Somebody edited a mirror | Edit the canonical copy, then rerun the sync script without `-Check` |
| `npm run render` fails in the HyperFrames project | Chromium or the pinned CLI is missing | Run `npm run check` first and read the error. See `docs/SOP-02-PRODUCT-EXPLAINER.md`. |
| The agent cannot see a new skill | The session started before the install | Restart the agent host |

## Next

- To make a story-driven brand film, read `docs/SOP-01-STORY-FILM.md`.
- To make a product explainer, read `docs/SOP-02-PRODUCT-EXPLAINER.md`.
- For the complete creative theory behind both, read `docs/video-production-workflow.md` and enter
  through the `script-video-production` skill.
- To work on the two reference films specifically, open `Ramayana-ZebpaySIP/WORKFLOW.md` or
  `CryptoBalancing-Zebpay/production/WORKFLOW.md` for their live status and open gates.
