#!/usr/bin/env bash
# Bake SFX (over music, with sidechain ducking) onto the master video. Pure ffmpeg, no re-gen.
set -uo pipefail
cd "$(dirname "$0")"
V="../punjab_di_kursi_master.mp4"
MUSIC="music_monkeys.mp3"
SFX="sfx"
OUT="../punjab_di_kursi_master_sfx.mp4"

# cue: t_seconds gain_dB dur_s file
CUES=(
"0.2  -11 1.2 drum.mp3"
"1.6  -14 0.8 whoosh.mp3"
"5.0  -6  1.5 boing.mp3"
"5.5  -9  1.2 impact.mp3"
"9.0  -12 1.6 bell.mp3"
"10.4 -11 1.0 boing.mp3"
"11.6 -10 0.9 whoosh_rocket.mp3"
"15.3 -17 4.5 whir.mp3"
"16.6 -12 1.2 coin.mp3"
"18.6 -13 1.5 slot.mp3"
"20.8 -12 1.3 sparkle.mp3"
"23.1 -10 1.9 suspense.mp3"
"25.4 -10 0.7 whoosh_arrow.mp3"
"25.9 -11 1.6 trombone.mp3"
"28.5 -14 1.3 pop.mp3"
"28.5 -19 8.5 birds.mp3"
"34.3 -13 2.5 running.mp3"
"37.5 -10 0.8 whoosh.mp3"
"37.6 -11 1.0 impact.mp3"
"41.0 -10 1.0 button.mp3"
"42.2 -13 1.2 bell.mp3"
"44.6 -10 1.5 sadhorn.mp3"
"46.6 -8  1.4 sparkle.mp3"
"47.3 -10 2.5 cheer.mp3"
"48.2 -9  2.0 win.mp3"
)

inputs=(-i "$V" -i "$MUSIC")
filt="[1:a]afade=t=in:st=0:d=1,afade=t=out:st=48.5:d=2,volume=-1dB[music];"
idx=2
labels=""
for c in "${CUES[@]}"; do
  set -- $c; t=$1; g=$2; d=$3; f=$4
  ms=$(awk "BEGIN{printf \"%d\", $t*1000}")
  inputs+=(-i "$SFX/$f")
  filt+="[${idx}:a]aformat=channel_layouts=stereo:sample_rates=44100,atrim=duration=${d},asetpts=PTS-STARTPTS,volume=${g}dB,adelay=${ms}|${ms}[s${idx}];"
  labels+="[s${idx}]"
  idx=$((idx+1))
done
n=$((idx-2))
filt+="${labels}amix=inputs=${n}:normalize=0:dropout_transition=0[sfxraw];"
filt+="[sfxraw]asplit=2[sfxA][sfxB];"
filt+="[music][sfxA]sidechaincompress=threshold=0.03:ratio=6:attack=5:release=250[duck];"
filt+="[duck][sfxB]amix=inputs=2:normalize=0:dropout_transition=0,alimiter=limit=0.97[aout]"

echo "cues: $n"
ffmpeg -y "${inputs[@]}" -filter_complex "$filt" -map 0:v:0 -map "[aout]" \
  -c:v copy -c:a aac -b:a 192k -shortest "$OUT" 2>err.log
code=$?
if [ $code -ne 0 ]; then echo "FFMPEG FAILED ($code):"; tail -8 err.log; exit $code; fi
echo "OK -> $OUT"
ffprobe -v error -select_streams v:0 -show_entries stream=width,height,codec_name -of csv=p=0 "$OUT"
ffprobe -v error -select_streams a:0 -show_entries stream=codec_name -of default=nk=1:nw=1 "$OUT"
ffprobe -v error -show_entries format=duration -of default=nk=1:nw=1 "$OUT"
