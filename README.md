# Marketing Video Generation Pipeline

A repeatable, evidence-gated system for producing short marketing videos with AI agents. It covers
two categories, carries two finished reference films with their full production records, and hands
almost all of the setup to the agent.

**You clone. The agent does the rest.**

## The two categories

| | Category A: story film | Category B: product explainer |
|---|---|---|
| What it is | A short emotional brand film. Characters, place, performance. | A short marketing video built on real product screens. |
| Picture comes from | A generative video model, plus deterministic sections | A deterministic renderer only. No generative video. |
| Exactness | A metaphor is allowed | Every number, label, and claim must be exact |
| Metered cost | Higgsfield credits | **None.** Subscriptions only. |
| Playbook | `docs/SOP-01-STORY-FILM.md` | `docs/SOP-02-PRODUCT-EXPLAINER.md` |
| Reference film | Ramayana x ZebPay SIP, 52.2 s | ZebPay CryptoPack Rebalancing, 46.6 s |

A mixed film is normal. Route each interval separately, never the whole film at once.

## What it costs

Separate **subscriptions** you already hold from **metered spend** that grows with output.

| Subscription | Used for |
|---|---|
| Claude Code, Codex, or Cursor | The agent that does the work |
| ChatGPT or Codex | Keyframes and reference stills. Category A only. |
| ElevenLabs | Narration. A free account was enough for both reference films. |

Metered spend is **Higgsfield credits for Category A only**, about 147 to 165 at 480p for a
52 second film. Category B had none at all.

The free ElevenLabs tier covers a voice you create and own in your own account. It refuses Voice
Library voices and music generation with HTTP 402. Move to a paid ElevenLabs plan or a Sarvam
subscription when you want a different or cloned voice, or real volume. Narration can also run on
free Edge TTS with no account, at a quality cost.

Credit numbers are dated evidence from 2026-07-24. Re-quote live before you spend.

---

# Getting started

## Step 1. Clone. THIS IS THE ONLY STEP YOU DO BY HAND

Install Git and Git LFS first. A clone without LFS gives you small text pointers where the videos
should be.

```powershell
winget install Git.Git
winget install GitHub.GitLFS
git lfs install

git clone https://github.com/MythyaVerse/marketing-video-generation-pipeline.git
cd marketing-video-generation-pipeline
git lfs pull
```

On macOS or Linux, use `brew install git git-lfs` or your package manager, then the same three Git
commands.

## Step 2. Open an agent in that folder and paste this

Open Claude Code, Codex, or Cursor with the repository as the working directory. Then paste the
prompt below. Nothing else is needed to begin.

```text
Set up this repository on my machine.

Read README.md and docs/SOP-00-SETUP.md first, then follow the script-video-setup skill.

1. Run tools/setup-video-repo.ps1 and show me the real output.
2. Tell me which rows a machine can fix, and fix those after I approve.
3. Tell me which rows only I can do, as a numbered list, and stop there.
4. Do not run any provider login. Do not print any credential value. Do not spend money.

Then tell me which video category I should read next.
```

If your host already has the command installed, `/setup` runs exactly this. It works in Claude Code,
Codex, and Cursor.

## Step 3. What the agent does for you

The agent works through `docs/SOP-00-SETUP.md` and reports evidence at each step. It will:

- check Git, Git LFS, Node, npm, Python, FFmpeg, FFprobe, uv, yt-dlp, and the Higgsfield CLI, and
  install the missing ones;
- confirm the LFS media downloaded as real megabyte files, not pointer text;
- install the Python packages the deterministic tools need;
- check `.mcp.json` server paths and repoint the ElevenLabs entry at your own `uvx`;
- verify that no credential is committed and that `.env` is ignored;
- check the user-level provider skills for your host;
- sync and verify the project skill and agent mirrors;
- re-run the check and show you the new summary.

The setup script is read-only by default. `-Install` performs only the safe repairs. It never logs
in, never prints a credential value, and never spends money.

## Step 4. What only you can do

The agent will stop and hand you this list. These need a browser login, a password, a payment method,
a personal account, or human judgement.

| # | Action |
|---|---|
| 1 | Clone the repository and run `git lfs pull`. Step 1 above. |
| 2 | Create an ElevenLabs API key and set `ELEVENLABS_API_KEY` in your user environment |
| 3 | Run `higgsfield auth login` yourself, only if you want Category A |
| 4 | Buy or top up Higgsfield credits |
| 5 | Approve every paid generation against a live quote |
| 6 | Listen to the encoded film and judge voice, tone, and pronunciation |
| 7 | Give brand, product, legal, and regulatory approval |
| 8 | Promote a review cut to a final |
| 9 | Rotate any leaked credential |

Items 5 through 8 are production gates, not setup. They exist because a machine transcript is not a
taste verdict, and a passing technical check is not a release.

## Step 5. Make a video

| You want to | Read |
|---|---|
| A story-driven brand film | `docs/SOP-01-STORY-FILM.md` |
| A product explainer | `docs/SOP-02-PRODUCT-EXPLAINER.md` |
| The creative theory behind both | `docs/video-production-workflow.md` |

Or just tell the agent what you want to make. It routes through the `script-video-production` skill.

---

## How the repository is organised

| Path | Contents |
|---|---|
| `docs/` | The three SOPs and the canonical production workflow |
| `video-production-system/` | The project folder contract, templates, and shared agent prompts |
| `.codex/skills/`, `.claude/skills/` | The reusable `script-video-*` skills, canonical and mirrored |
| `.claude/commands/`, `.cursor/commands/`, `.codex/prompts/` | The `/setup` command in every host |
| `.agent-harness/recipes/` | Repeatable recipes: HyperFrames, narration, LFS delivery, environment |
| `tools/` | Setup checker, project scaffold, skill and agent sync, deterministic edit helpers |
| `Ramayana-ZebpaySIP/` | Category A reference film, with its full production record |
| `CryptoBalancing-Zebpay/` | Category B reference film, with its full production record |
| `meetings/` | A packaged showcase of both films |

## Principles the whole system runs on

1. **Audio is the clock.** One continuous narration defines every frame boundary. Every boundary is
   an integer frame, so drift is impossible by construction.
2. **Prove it for free before you pay.** The complete keyframe animatic is the first cut of the film.
   A human approves it before any credit is spent.
3. **Exact things are rendered, not generated.** Text, numbers, charts, claims, captions, and logos
   never go to a probabilistic model.
4. **Judge the encoded artifact.** Not the timeline, not the preview. Probe the real file and inspect
   boundaries at `n-1`, `n`, and `n+1`.
5. **No role certifies its own output.** An independent reviewer returns the verdict.
6. **A technical pass is not an approval.** Three technically perfect narrations were rejected by ear
   in the reference film. Human listening is a required gate.

## Safety rules

- Never commit `.env`, a key value, a provider token, or customer data.
- Never run a paid job without a current schema, a live quote, and a recorded human approval.
- Never add raw takes or review media to Git. Track a final only when the owner asks, following
  `.agent-harness/recipes/git-lfs-video-delivery.md`.
- Never force-push for media delivery.

## Status of the reference films

Both are review cuts with open human gates. Neither is a released campaign.

| Film | Encoded review | Open gates |
|---|---|---|
| Ramayana x ZebPay SIP | v005 promoted master; v011 creative playback passed | Music rights, commercial voice entitlement, brand, legal, regulatory |
| CryptoPack Rebalancing | v002 keeper at the encoded-artifact gate | Human listening, screenshot currency, product, brand, legal, regulatory |

Live status lives in `Ramayana-ZebpaySIP/WORKFLOW.md` and
`CryptoBalancing-Zebpay/production/WORKFLOW.md`.

The ZebPay campaign material in this repository is client work shown as a worked example. Final
product, legal, regulatory, and brand approval for those campaigns belongs to ZebPay.
