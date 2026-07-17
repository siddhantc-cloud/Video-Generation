# ComfyUI local UGC stack — research (2026-06-12)

Target: RTX 5060 Ti 16GB · podcast-style + all UGC types · researched for the BLUMELIFE/so_sorry pipeline.

## The architecture insight

Local changes the audio game completely. The cloud pipeline's unsolved problems (engine TTS quality, first-word clipping, voice drift, no-lip-sync-without-a-model) all dissolve because **locally we own a lip-sync model**: the pipeline inverts to true audio-first —

```
script → ElevenLabs TTS (natural Hindi, one voice ID forever)
       → keyframe image (character + product)
       → InfiniteTalk renders the VIDEO to match the AUDIO   ← lips correct BY CONSTRUCTION
       → karaoke captions from exact TTS word boundaries
       → EDL assembly (existing toolchain)
```
No cold-start (we author the audio), no voice drift (one voice ID), no lip-sync repair (it's generative, not corrective).

## Recommended models (16GB-fit verified by research)

| Role | Model | Size | Why |
|---|---|---|---|
| **Talking podcast video (core)** | **InfiniteTalk** (MeiGen) on Wan2.1-I2V-14B-480p **GGUF** via Kijai WanVideoWrapper | ~14–18 GB stack | Top human-eval lip-sync + body-motion ranking; long-form (no 15s cap); **multi-person** (two-host podcast!); 480p runs on ≥8GB |
| Short clips, fast | MultiTalk (same family) | +2–4 GB | ≤15s champion, shares the Wan backbone — cheap add-on |
| Re-sync existing footage | LatentSync 1.6 (ByteDance) | ~5 GB | corrective lip-sync (video+audio in → synced out), 512×512 |
| **Keyframes + product edits** | **Qwen-Image-Edit-2511** GGUF | ~12–15 GB | the local Nano-Banana: edit-by-instruction, character consistency, **bilingual text rendering** (Hindi labels) |
| Premium image alt | Flux.2-dev (fp8/quant) | ~24 GB+ | top quality; tight but possible on 16GB — phase 2 |
| Cheap image volume | SDXL | ~7 GB | persona-matrix batch stills |
| B-roll video (optional) | Wan2.2 TI2V-5B | ~10 GB | fast 720p text/image-to-video |

Required stack for InfiniteTalk: Wan2.1-I2V-14B-480P GGUF (`city96/Wan2.1-I2V-14B-480P-gguf`, Q5_K_M ≈ 11GB) + InfiniteTalk/MultiTalk GGUF weights + Wan 2.1 VAE (bf16) + UMT5-XXL text encoder + Kijai `ComfyUI-WanVideoWrapper` custom nodes. Keep backbone and InfiniteTalk weights BOTH in GGUF (mixed formats break).

## Download phases (proposed)
1. **Phase 1 — talking-head core (~20 GB):** InfiniteTalk stack. Unlocks the whole podcast-UGC use case.
2. **Phase 2 — image side (~13 GB):** Qwen-Image-Edit-2511 GGUF (+SDXL if batch stills wanted).
3. **Phase 3 — optional:** LatentSync (corrective), Wan2.2 5B (B-roll), MultiTalk.

## Sources
- [Best open-source lip-sync models 2026](https://www.pixazo.ai/blog/best-open-source-lip-sync-models) · [MultiTalk vs InfiniteTalk vs WAN-S2V](https://zanno.se/lets-talk-multitalk-infinitetalk-wan-s2v/) · [InfiniteTalk benchmarks](https://www.infinitetalkai.org/lib/benchmarks) · [InfiniteTalk (MeiGen) HF](https://huggingface.co/MeiGen-AI/InfiniteTalk)
- [InfiniteTalk ComfyUI setup + GGUF requirements](https://www.infinitetalk.net/infinitetalk-comfyui) · [official Comfy InfiniteTalk template](https://comfy.org/workflows/templates-wan2_1_infinitetalk_music-1eab7aa23f6a/) · [multi-person setup](https://infinitetalk.org/infinitetalk-multi-person)
- [Qwen Image Edit vs Flux Kontext](https://www.mimicpc.com/learn/qwen-image-edit-vs-flux-kontext-which-better-for-image-editing) · [Model rundown: Z-Image/Qwen-2512/Flux.2-dev](https://medium.com/diffusion-doodles/model-rundown-z-image-turbo-qwen-image-2512-edit-2511-flux-2-dev-fc787f5e87ad) · [Fine-tuned Qwen-Edit vs Nano-Banana vs Kontext](https://ghost.oxen.ai/fine-tuned-qwen-image-edit-vs-nano-banana-and-flux-kontext-dev/)
- [LatentSync 1.6 ComfyUI wrapper](https://github.com/ShmuelRonen/ComfyUI-LatentSyncWrapper)
