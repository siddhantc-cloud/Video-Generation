---
name: comfyui-wan-local
description: "Operate the local ComfyUI + WanVideoWrapper (Kijai) stack on this box's RTX 5060 Ti 16GB: InfiniteTalk/MultiTalk audio-driven talking video (image+TTS→lip-synced clip), parameter settings code-verified from the wrapper source, VRAM/block-swap management, long-form windowing, and headless API driving (queue/poll/fetch). Use when generating talking-head video locally, when the user says 'run it through ComfyUI', 'local lip-sync', 'InfiniteTalk', or when debugging local generation (OOM, slow, artifacts). Composes with audio-first-reel (this is the local dialogue lane) and references/comfyui-ugc-stack.md (model research)."
metadata:
  version: 1.0.0
  updated: 2026-06-12
  verified: "parameter defaults extracted from wrapper source on disk; install paths verified; runtime settings to be validated on first generation"
---

# ComfyUI Wan Local Pipeline (this box)

## Installed stack map (all verified on disk)

| Piece | Path |
|---|---|
| ComfyUI 0.24.0 | `D:\ComfyUI` · boot: `start_comfyui.bat` or `conda run -n comfy python main.py --listen 127.0.0.1 --port 8188` |
| Env | conda `comfy` (py3.12, torch 2.11+cu128 — Blackwell needs cu128+) |
| Wrapper nodes | `custom_nodes/ComfyUI-WanVideoWrapper` (Kijai) + `custom_nodes/ComfyUI-Manager` |
| Backbone | `models/diffusion_models/wan2.1-i2v-14b-480p-Q5_K_M.gguf` |
| InfiniteTalk | `models/diffusion_models/InfiniteTalk/Wan2_1-InfiniTetalk-Single_fp16.safetensors` (note repo TYPO "InfiniTetalk") + `-Multi_fp16` |
| Speed LoRA | `models/loras/Lightx2v/lightx2v_I2V_14B_480p_cfg_step_distill_rank64_bf16.safetensors` |
| VAE / text enc / clip vision | `models/vae/Wan2_1_VAE_bf16.safetensors` · `models/text_encoders/umt5-xxl-enc-fp8_e4m3fn.safetensors` · `models/clip_vision/split_files/clip_vision/clip_vision_h.safetensors` |
| Audio encoder | `models/wav2vec2/wav2vec2-chinese-base_fp16.safetensors` (or node auto-downloads `TencentGameMate/chinese-wav2vec2-base`) |
| Reference workflow | `custom_nodes/ComfyUI-WanVideoWrapper/example_workflows/wanvideo_2_1_14B_I2V_InfiniteTalk_example_03.json` |

## Production workflow library (cloned 2026-06-12)

`D:\ComfyUI\workflows-library\` = [digitalinnovator/comfyui-production-workflows](https://github.com/digitalinnovator/comfyui-production-workflows) — 12 production UGC workflows + utilities, each with README + model list:
`01/02` AI-UGC video (voice-clone / prebuilt-audio) · `03/04` trend-copy via Wan-Animate · `05/06` multi-character (Qwen / regional prompting) · `07` image realism enhancer · `08` **product-placement (Qwen)** · `09` **talking-avatar InfiniteTalk** ← our lane, model list matches our stack · `10` music (ACE-Step) · `11/12` Flux.2 dataset builders · `bonus-utilities/` (video-combine, caption-generator, audio-separator, voice-design TTS).

**Node packs:** WanVideoWrapper ✓ · ComfyUI-KJNodes ✓ (installed) · audio-separation-nodes (NOT installed — bypass those nodes; our TTS is clean) · `comfy-core`.

**Production-tuned sampler settings from workflow 09** (the values the docs never state):
`steps 7 · cfg 1.0 · shift 11 · scheduler dpm++_sde · LoRA strength 1.0 · fp16_fast + sdpa · ImageToVideoMultiTalk 832×480 (FLIP to 480×832 for vertical reels), window 81, mode 'infinitetalk'`

**ElevenLabs-in-ComfyUI caveat:** `ElevenLabsTextToSpeech`/`InstantVoiceClone` nodes (seen in `UGC/Comfy Workflows/template_image_speech_to_video.json`) are **comfy-core API nodes — they bill via a ComfyUI cloud account, NOT your ElevenLabs key**. Do TTS outside ComfyUI (our REST/MCP path with our own key) and feed the WAV in via `LoadAudio`.

## InfiniteTalk parameters — code-verified defaults → 16GB recommendations

| Param (node) | Code default | Use on this box | Why |
|---|---|---|---|
| `steps` (WanVideoSampler) | — | **4–6 iterate, 8 finalize** | LightX2V distill LoRA makes low-step viable; community standard |
| `cfg` | — | **1.0** with distill LoRA | distilled models want cfg≈1; higher reintroduces cost+burn |
| `audio_scale` (MultiTalk embeds) | 1.0 | 1.0 | strength of audio conditioning on lips |
| `audio_cfg_scale` | 1.0 | 1.0; try **1.5–2** if body motion too static | >1 adds a no-audio pass: slower, more motion freedom |
| `frame_window_size` | **81** (step 4) | 81 | the temporal window the model is trained-good at |
| `motion_frame` (long-form overlap) | **25** | 25 | overlap between windows; lower (5) = faster, more seam risk |
| `blocks_to_swap` (BlockSwap) | — | **start 20; +2 when LoRA unmerged** | README: LoRA weights join blocks under swap — ~1GB LoRA across 20 swapped blocks ≈ +500MB VRAM → compensate +2 blocks |
| Resolution | — | **480×832 vertical** (Wan 480p native), upscale at assembly | backbone is the 480p model; don't fight it |
| LoRA strength (lightx2v) | — | 1.0 | per example workflow |
| Scheduler | per example | keep example's (don't invent) | read from example_03.json at runtime |

**Audio input prep:** 16kHz mono WAV; author the lead-in (0.4–0.5s silence) and tail into the TTS — this is OUR audio, the cold-start problem cannot exist here. Clean TTS needs NO vocal separation: bypass the `MelBandRoFormer`/`AudioSeparation` nodes from the example.

**Post-pass:** frame interpolation (RIFE) to double fps after generation — community-standard for smoothing micro-flicker; then conform to the reel's 24fps at assembly.

## Long-form (the InfiniteTalk superpower)

Generates beyond the 81-frame window by sliding with `motion_frame` overlap — reference: 1025 frames via 81-window/16-overlap. Practical recipe per dialogue scene: audio length × 25fps + ~12 frames; let windowing handle anything longer than ~3s. Multi-person: load `-Multi` model variant + per-speaker reference masks (see `infinitetalk.org/infinitetalk-multi-person`).

## VRAM management (RTX 5060 Ti 16GB)

1. OOM → raise `blocks_to_swap` (20 → 24 → 28); generation slows ~linearly but completes.
2. Skip `torch.compile` initially (README: wrapper is no longer reliant on it; Windows + triton has a first-run VRAM-spike cache quirk — if compiled run OOMs once, just run again).
3. Keep GGUF backbone + fp8 text encoder (already chosen for this reason).
4. Tiled VAE decode if decode-stage OOM.

## Driving headlessly (the agent path)

UI-format workflow JSON (`example_workflows/*.json`) ≠ API format. Convert once: load in UI → `Save (API Format)`, or build API JSON directly (node-id → {class_type, inputs} map). Then:

```python
import json, urllib.request, time
p = json.load(open('workflow_api.json'))
# edit inputs: p['<node_id>']['inputs']['image'] = 'keyframe.png' etc.
req = urllib.request.Request('http://127.0.0.1:8188/prompt', json.dumps({'prompt': p}).encode())
pid = json.loads(urllib.request.urlopen(req).read())['prompt_id']
while True:
    h = json.loads(urllib.request.urlopen(f'http://127.0.0.1:8188/history/{pid}').read())
    if pid in h and h[pid].get('outputs'): break
    time.sleep(5)
# outputs reference files in D:\ComfyUI\output\
```
Inputs (images/audio) go in `D:\ComfyUI\input\` first. Progress streaming: `ws://127.0.0.1:8188/ws?clientId=...`. Other endpoints: `/object_info` (node schemas), `/queue`, `/interrupt`, `/system_stats`.

## Slot in the production pipeline

This is the **local dialogue lane** of `audio-first-reel`: ElevenLabs/edge-tts Hindi audio (authored lead-in) + NB-Pro keyframe → InfiniteTalk → lip-synced clip → karaoke captions (timing from the TTS synthesis — exact by construction) → EDL assembly. Replaces the 22cr Veo step for talking shots; Higgsfield remains the keyframe/B-roll/cinematic engine. Quality gate: side-by-side vs the Veo take before adopting (visual-polish risk is the known unknown, ~50–60% prior).

## LatentSync 1.6 (lip-sync EDIT of existing video) — working recipe + hard-won Windows fixes

**Use LatentSync, NOT InfiniteTalk, when the goal is "keep an existing video, fix only the mouth"** (e.g. re-sync a Veo human clip to a clean ElevenLabs VO). InfiniteTalk *generates* from a still (discards the source animation); LatentSync *edits* the source.

**⚠️ CARTOON VERDICT (proven 2026-06-12): LatentSync FAILS on stylized cartoon characters — "Face not detected"** (insightface needs a human face). The villain ran the full pipeline then errored at face detection. So: face-detection lip-sync (LatentSync/MuseTalk/Wav2Lip) is for HUMAN faces only; cartoons need generative (InfiniteTalk) or loose-sync.

**The full chain of Windows gotchas to clear BEFORE it runs (each one cost a failed run):**
1. **Never launch ComfyUI via `conda run`** — it buffers/rewraps stdout (blinds you) AND crashes on multiline/Unicode. Launch the env python directly with the env dirs on PATH: `PATH="$E:$E/Library/bin:$E/Scripts:$E/DLLs:<ffmpeg>:$PATH" "$E/python.exe" -u main.py ...` where `$E=/c/Users/SE/miniforge3/envs/comfy`.
2. **triton-windows** — `pip install triton-windows` (LatentSync 1.6 PatchTritonVAE needs it).
3. **The node runs a HIDDEN `pip install` at first execution** (`check_and_install_dependencies`, output piped → invisible hang). Pre-install its list manually (`pytorch_lightning accelerate` were missing; rest satisfied) and write the skip-flag: `~/.latentsync16_dependencies_installed`. Guard torch — pytorch_lightning did NOT downgrade our cu128 torch.
4. **Pre-stage models** (else it silently downloads mid-hang): `hf download ByteDance/LatentSync-1.6 latentsync_unet.pt whisper/tiny.pt --local-dir ~/.latentsync16_models`.
5. **torchcodec needs FFmpeg SHARED libs** — `pip install torchcodec` then `conda install -n comfy -c conda-forge ffmpeg` (gyan.dev static build lacks the `avcodec-*.dll` shared libs torchcodec loads).
6. **Patched `nodes.py`** — its save calls `torchvision.io.write_video` (removed in our torchvision) and only catches `TypeError`; replaced with `imageio.mimsave(..., codec='libx264', macro_block_size=1)`.
7. **insightface + onnxruntime-gpu** — `pip install insightface onnxruntime-gpu` (the face analyzer; auto-downloads buffalo pack on first run).

**Run mechanics:** workflow = `custom_nodes/ComfyUI-LatentSyncWrapper/example_workflows/latentsync1.5_comfyui_basic.json` (LoadVideo→VideoLengthAdjuster→LatentSyncNode→VHS_VideoCombine). Convert with `ui2api.py`, patch via `patch_ls.py` (VIDEO + audio + filename_prefix; `silent_padding_sec ≥ 0.1`). LatentSyncNode params: `lips_expression 1.5, inference_steps 20`. Output to `D:\ComfyUI\output\`.

## Troubleshooting quick table

| Symptom | Fix |
|---|---|
| OOM at sampling | +4 `blocks_to_swap`; check LoRA-block note above |
| OOM at decode | tiled VAE decode |
| First compiled run OOM (Windows) | rerun (triton cache quirk) or drop compile |
| Lips lag audio | check audio is 16kHz mono; `audio_scale` up to 1.2 |
| Body frozen, only lips move | `audio_cfg_scale` 1.5–2.0 |
| Window seams in long clips | `motion_frame` 25 (not 5); consistent seed |
| Identity drift from keyframe | it's the I2V conditioning — regenerate keyframe closer-cropped |

## Sources
[InfiniteTalk ComfyUI guide](https://infinitetalk.org/infinitetalk-comfyui) · [setup guide](https://www.infinitetalk.net/infinitetalk-comfyui) · [speed issue #1229](https://github.com/kijai/ComfyUI-WanVideoWrapper/issues/1229) · [API guide](https://medium.com/@yushantripleseven/comfyui-using-the-api-261293aa055a) · [production API guide](https://www.viewcomfy.com/blog/building-a-production-ready-comfyui-api) · wrapper README + source (local, code-verified)
