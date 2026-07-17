#!/usr/bin/env bash
# Build the SFX library from manifest_raw.txt (category | Title :: url).
# Dedupe by Mixkit sfx id, download (free Mixkit license), index, license note.
set -uo pipefail
cd "$(dirname "$0")"
UA="Mozilla/5.0 (Windows NT 10.0; Win64; x64)"; REF="https://mixkit.co/"
RAW="manifest_raw.txt"

# 1) dedupe by id -> keep first (category, title) seen per id
#    line: "cat | Title :: https://assets.mixkit.co/active_storage/sfx/<id>/<id>-preview.mp3"
awk -F' \\| | :: ' '
  { cat=$1; title=$2; url=$3;
    if (match(url, /sfx\/[0-9]+/)) { id=substr(url, RSTART+4, RLENGTH-4); }
    else next;
    if (!(id in seen)) { seen[id]=1; print id "\t" cat "\t" title "\t" url }
  }' "$RAW" | sort -n > index.tsv

total=$(wc -l < index.tsv)
echo "unique sounds: $total"

# 2) slugify + download
> INDEX.csv; echo "id,category,duration_s,file,title,source_url,license" >> INDEX.csv
n=0; ok=0
while IFS=$'\t' read -r id cat title url; do
  n=$((n+1))
  slug=$(echo "$title" | tr '[:upper:]' '[:lower:]' | tr -cs 'a-z0-9' '_' | sed 's/^_//;s/_$//' | cut -c1-40)
  mkdir -p "$cat"
  out="$cat/${id}_${slug}.mp3"
  if [ ! -s "$out" ]; then curl -s -L -A "$UA" -e "$REF" -o "$out" "$url"; fi
  sz=$(stat -c%s "$out" 2>/dev/null || echo 0)
  if [ "$sz" -gt 1000 ]; then
    ok=$((ok+1))
    dur=$(ffprobe -v error -show_entries format=duration -of default=nk=1:nw=1 "$out" 2>/dev/null)
    # CSV-safe title
    ct=$(echo "$title" | sed 's/"/'"'"'/g')
    echo "$id,$cat,$dur,$out,\"$ct\",$url,mixkit-free" >> INDEX.csv
  else
    rm -f "$out"
  fi
  [ $((n % 50)) -eq 0 ] && echo "  $n/$total ..."
done < index.tsv
echo "downloaded ok: $ok / $total"

# 3) license + readme
cat > LICENSE.txt <<EOF
SFX library sourced from Mixkit (https://mixkit.co) free sound effects.
License: Mixkit Free License — free for commercial & non-commercial use, no attribution required.
See https://mixkit.co/license/ . Files are the public preview MP3s from assets.mixkit.co.
Downloaded $(date +%Y-%m-%d) for the "Punjab Di Kursi" / So Sorry showcase. Index: INDEX.csv.
EOF
echo "wrote LICENSE.txt + INDEX.csv"
