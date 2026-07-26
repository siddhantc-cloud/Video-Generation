# Production cost plan

## Checklist

| Requirement | Pass condition | Evidence | Owner | Status |
|---|---|---|---|---|
| Free work first | Documents, assets, storyboard, and visual build precede paid calls | Project artifacts | Producer | Complete |
| Live provider unit quote | Exact request character count is checked; account allowance is queried | Script counter plus ElevenLabs API response | Producer | Complete with provider-permission limitation |
| Approval cap | Only one primary narration request is authorized | Owner instruction | Owner | Approved |
| Actual spend | Characters consumed and output hash are recorded | Narration metadata | Producer | Complete |
| Retry control | No second voice request without owner feedback | This plan | Producer | Locked |

| Item/version | Provider/mode | Current unit quote | Authorized cap | Actual | Status |
|---|---|---:|---:|---:|---|
| Primary narration v001 | ElevenLabs TTS | 741 UTF-8 text characters submitted; account allowance unavailable because this API key lacks `user_read` | One synthesis request | 741 submitted characters; one request | Complete |
| Product motion | HyperFrames local render | Local compute | Review renders needed to resolve encoded QC | Two high-quality renders and two local delivery transcodes | Complete through v002 |
| Music v001 | Deterministic local synthesis | Local compute | One original bed | One 46.486 s WAV | Complete |
| Generative motion | None | 0 | 0 | 0 | Not used |
| Image generation/restoration | Deferred option | Not quoted | 0 | 0 | Not authorized |

No additional paid voice, image, video, or music generation may run without a new current quote and
owner authorization.

The v002 claims and caption-timing revision used only local HyperFrames, FFmpeg, and ASR work. It
made no additional provider request and consumed no additional ElevenLabs characters.

The configured key permits voice discovery and synthesis but not subscription reads. The live
allowance could therefore not be verified without expanding credential scope. The bounded quote is
the exact request size (741 characters), and the owner's existing authorization is limited to this
single synthesis request.

The provider returned the approved take under history item `dK4KJXBOLIah09TtGV3W`. The immutable
provider master and six frame WAV hashes are recorded in
`edit/animations/cryptopack-rebalancing/assets/audio/voice/narration-v001-metadata.json`. No second
synthesis was submitted.
