#!/usr/bin/env bash
# Controllable timeline view: filmstrip (frames on a time axis) + audio waveform, aligned.
# Usage: bash edit/make_timeline.sh <video.mp4> [out.png]
# Regenerate after every edit so the view always matches the current cut.
set -e
V="${1:?usage: make_timeline.sh <video.mp4> [out.png]}"
OUT="${2:-edit/timeline.png}"
FF="C:/Users/SE/miniforge3/envs/mfa/Library/bin/ffmpeg.exe"
TMP="edit/_tl"; rm -rf "$TMP"; mkdir -p "$TMP"
# 1) one frame per second
"$FF" -y -i "$V" -vf fps=1 "$TMP/f%03d.png" 2>/dev/null
N=$(ls "$TMP"/f*.png | wc -l)
FW=54; W=$((N*FW))
# 2) filmstrip — single row, time = x-axis
"$FF" -y -framerate 1 -i "$TMP/f%03d.png" -frames:v 1 -vf "scale=${FW}:96,tile=${N}x1:padding=0,format=rgb24" "$TMP/strip.png" 2>/dev/null
# 3) audio waveform at the SAME width (so it aligns to the filmstrip time axis)
"$FF" -y -i "$V" -filter_complex "[0:a]aformat=channel_layouts=mono,showwavespic=s=${W}x220:colors=0x3fd0ff" -frames:v 1 "$TMP/wave.png" 2>/dev/null
# 4) stack: filmstrip on top, waveform below
"$FF" -y -i "$TMP/strip.png" -i "$TMP/wave.png" -filter_complex "[0][1]vstack=inputs=2" -frames:v 1 "$OUT" 2>/dev/null
echo "timeline -> $OUT  (${W}x316, ${N}s @1fps; each frame = 1 second; waveform aligned to the same axis)"
