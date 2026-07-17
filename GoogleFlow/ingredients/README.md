# Flow Ingredient sheets — cast (clean AI turnarounds)

One **clean, label-free turnaround per character** (front · three-quarter · profile · close-up), generated
with the `chatgpt-imagegen` lane (ChatGPT subscription, **zero Higgsfield credits**), each seeded
image-to-image from the locked `../../zebpay/bible/` refs so the design matches. These are label-free on
purpose — upload the file directly as that character's **Ingredient** in Google Flow.

**Rule:** attach only the character(s) actually in a shot — never several sheets at once (Flow averages
attached references and blends identities). For the Sena, keep the crowd distant in prompts.

| Sheet | Character | Panels | Notes |
|---|---|---|---|
| `rama_sheet.png` | Rama | front (bow) · 3/4 · profile · close-up | **PHOTOREAL serial-devotional style** (Ramanand Sagar Ramayan spirit, live-action photoreal): serene, tall crown, dhoti+angavastram, vanamala, graceful build; quality=high. Variants in `gen/`: `rama_turnaround.png` (cinematic muscular, also at `rama_sheet_cinematic.png`), `rama_serial_turnaround.png` (painterly/poster look, rejected) |
| `squirrel_sheet.png` | Squirrel | front · 3/4 · profile · head | three back-stripes + tail consistent across views |
| `lead_vanara_sheet.png` | Lead vanara | front · 3/4 · profile · grin close-up | boastful hero, gold ornaments |
| `baby_vanara_sheet.png` | Baby vanara | front · 3/4 · profile · close-up | young/soft version of the vanara design |
| `sena_sheet.png` | Vanara sena (army) | five distinct crowd soldiers | varied builds/ages, plain loincloths; use as crowd variety, keep distant |

Raw generations are kept in `gen/` (same pixels). These 5 supersede the earlier keyframe-crop montages.

**Quality note:** this lane caps at `medium` image quality (Rama happened to return `high`). For a sheet
that must be production-tight, regenerate that ONE via Higgsfield Nano Banana Pro (~2 cr). Reasoning-effort
settings (e.g. "xhigh") tune the text model's planning, not the image model's pixels — they don't raise
sheet fidelity on this lane.

**Regenerate any sheet:** re-run `../../` scratchpad `gen_sheets.sh`-style call:
`PYTHONUTF8=1 PYTHONPATH=".claude/skills/chatgpt-imagegen/_winshim" python ".claude/skills/chatgpt-imagegen/chatgpt-imagegen" "<turnaround prompt>" -i "zebpay/bible/<ref>.png" -o "GoogleFlow/ingredients/gen/<char>_turnaround.png" --size 1536x1024 --backend codex --quiet`
