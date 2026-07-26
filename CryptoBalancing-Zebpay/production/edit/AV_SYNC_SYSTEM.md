# Audio-master integer-frame timing

## Rules

1. Use one narration performance and its exact timing metadata.
2. Convert every visual boundary to an integer frame: `frame = round(seconds × fps)`.
3. Store half-open frame ranges: `[start_frame, end_frame_exclusive)`.
4. Render every segment to its exact frame count before concatenation.
5. Make the phrase’s visual appear while that phrase is spoken; do not trail it into unrelated silence.
6. Add captions after picture overlays and deterministic graphics.
7. Verify video/audio duration drift is under one frame.
8. Inspect encoded frames `n-1` and `n` at every boundary.

Use `tools/av_sync_render.py` for simple still/video animatics and a versioned timeline manifest for
final assembly.
