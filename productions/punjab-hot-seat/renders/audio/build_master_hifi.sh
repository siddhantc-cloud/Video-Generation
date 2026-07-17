#!/usr/bin/env bash
# Rebuild full master with the hi-fi Act 3 swapped in. Pure ffmpeg, NO Higgsfield, NO credits.
# Timeline: Act1 0-10.04 | Act2 10.04-25.14 | Act3-hifi 25.14-45.34 | Act4 45.34-55.46
set -uo pipefail
cd "$(dirname "$0")"   # renders/audio
R=".."                  # renders/
A1="$R/v1_final.mp4"; A2="$R/act2/act2_final.mp4"; A3="$R/act3_hifi/act3_hifi_silent.mp4"; A4="$R/act4/act4_final.mp4"
MUSIC="music_monkeys.mp3"; S="sfx"
OUT="$R/punjab_di_kursi_master_hifi.mp4"

# 1) concat 4 acts (silent) -> master_v2_silent
ffmpeg -y -i "$A1" -i "$A2" -i "$A3" -i "$A4" -filter_complex \
"[0:v]scale=1920:1080:force_original_aspect_ratio=decrease,pad=1920:1080:-1:-1,setsar=1,fps=30[v0]; \
 [1:v]scale=1920:1080:force_original_aspect_ratio=decrease,pad=1920:1080:-1:-1,setsar=1,fps=30[v1]; \
 [2:v]scale=1920:1080:force_original_aspect_ratio=decrease,pad=1920:1080:-1:-1,setsar=1,fps=30[v2]; \
 [3:v]scale=1920:1080:force_original_aspect_ratio=decrease,pad=1920:1080:-1:-1,setsar=1,fps=30[v3]; \
 [v0][v1][v2][v3]concat=n=4:v=1:a=0[out]" -map "[out]" -c:v libx264 -pix_fmt yuv420p -crf 18 "$R/master_v2_silent.mp4" 2>/dev/null
echo "silent dur: $(ffprobe -v error -show_entries format=duration -of default=nk=1:nw=1 "$R/master_v2_silent.mp4")"

# 2) re-timed cue table (t gain dur file)
CUES=(
"0.2 -11 1.2 drum.mp3" "1.6 -14 0.8 whoosh.mp3" "5.0 -6 1.5 boing.mp3" "5.5 -9 1.2 impact.mp3" "9.0 -12 1.6 bell.mp3"
"10.4 -11 1.0 boing.mp3" "11.6 -10 0.9 whoosh_rocket.mp3" "15.3 -17 4.5 whir.mp3" "16.6 -12 1.2 coin.mp3" "18.6 -13 1.5 slot.mp3" "20.8 -12 1.3 sparkle.mp3" "23.1 -10 1.9 suspense.mp3"
"25.5 -10 1.0 whoosh_arrow.mp3" "26.0 -11 1.6 trombone.mp3" "29.5 -14 1.3 pop.mp3" "33.3 -19 4.0 birds.mp3" "37.6 -13 2.5 running.mp3" "41.6 -10 0.8 whoosh.mp3" "41.8 -11 1.0 impact.mp3"
"46.0 -10 1.0 button.mp3" "47.2 -13 1.2 bell.mp3" "49.6 -10 1.5 sadhorn.mp3" "51.6 -8 1.4 sparkle.mp3" "52.3 -10 2.5 cheer.mp3" "53.2 -9 2.0 win.mp3"
)
inputs=(-i "$R/master_v2_silent.mp4" -i "$MUSIC")
filt="[1:a]atrim=0:56,afade=t=in:st=0:d=1,afade=t=out:st=54:d=1.5,volume=-1dB[music];"
idx=2; labels=""
for c in "${CUES[@]}"; do set -- $c; t=$1; g=$2; d=$3; f=$4
  ms=$(awk "BEGIN{printf \"%d\", $t*1000}")
  inputs+=(-i "$S/$f")
  filt+="[${idx}:a]aformat=channel_layouts=stereo:sample_rates=44100,atrim=duration=${d},asetpts=PTS-STARTPTS,volume=${g}dB,adelay=${ms}|${ms}[s${idx}];"
  labels+="[s${idx}]"; idx=$((idx+1)); done
n=$((idx-2))
filt+="${labels}amix=inputs=${n}:normalize=0:dropout_transition=0,apad=whole_dur=56[sfxraw];"
filt+="[sfxraw]asplit=2[sa][sb];"
filt+="[music][sa]sidechaincompress=threshold=0.03:ratio=6:attack=5:release=250[duck];"
filt+="[duck][sb]amix=inputs=2:normalize=0:dropout_transition=0,alimiter=limit=0.97[aout]"
ffmpeg -y "${inputs[@]}" -filter_complex "$filt" -map 0:v:0 -map "[aout]" -c:v copy -c:a aac -b:a 192k -shortest "$OUT" 2>err2.log
code=$?; if [ $code -ne 0 ]; then echo "FAIL:"; tail -8 err2.log; exit $code; fi
rm -f "$R/master_v2_silent.mp4"
echo "OK -> $OUT"
ffprobe -v error -select_streams v:0 -show_entries stream=width,height -of csv=p=0 "$OUT"
ffprobe -v error -select_streams a:0 -show_entries stream=codec_name -of default=nk=1:nw=1 "$OUT"
ffprobe -v error -show_entries format=duration -of default=nk=1:nw=1 "$OUT"
