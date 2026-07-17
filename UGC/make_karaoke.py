"""Build a karaoke .ass from whisper word-timestamps + the known Latin script line.
Usage: python make_karaoke.py <whisper.json> "<latin script text>" <out.ass> [chunk_size]
Style locked per audio-first-reel skill: Impact 58, gold \\kf fill over white, MarginV 450 @720x1280.
"""
import json, sys

wj, script_text, out = sys.argv[1], sys.argv[2], sys.argv[3]
SIZE = int(sys.argv[4]) if len(sys.argv) > 4 else 4
MARGINV = int(sys.argv[5]) if len(sys.argv) > 5 else 450  # @PlayResY 1280; lower value = lower on screen

d = json.load(open(wj, encoding='utf-8'))
W = [w for s in d['segments'] for w in s.get('words', [])]
script = script_text.split()
n, m = len(W), len(script)
times = []
for i in range(m):
    a = W[min(int(i / m * n), n - 1)]['start']
    b = W[min(max(int((i + 1) / m * n) - 1, int(i / m * n)), n - 1)]['end']
    times.append((a, max(b, a + 0.12)))

def ts(t):
    h, r = divmod(max(t, 0), 3600); mn, s = divmod(r, 60)
    return f"{int(h)}:{int(mn):02d}:{s:05.2f}"

lines = []
for i in range(0, m, SIZE):
    idx = list(range(i, min(i + SIZE, m)))
    start, end = times[idx[0]][0], times[idx[-1]][1] + 0.08
    parts = []
    for j in idx:
        nxt = times[j + 1][0] if j + 1 in idx else times[idx[-1]][1]
        parts.append(r"{\kf%d}%s " % (max(int(round((nxt - times[j][0]) * 100)), 12), script[j]))
    lines.append(f"Dialogue: 0,{ts(start)},{ts(end)},Cap,,0,0,0,,{''.join(parts).rstrip()}")

HDR = """[Script Info]
ScriptType: v4.00+
PlayResX: 720
PlayResY: 1280

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Cap,Impact,58,&H0000D7FF,&H00FFFFFF,&H00000000,&H00000000,-1,0,0,0,100,100,0,0,1,3,0,2,30,30,{MARGINV},1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""
open(out, 'w', encoding='utf-8').write(HDR.replace('{MARGINV}', str(MARGINV)) + '\n'.join(lines) + '\n')
print(f"{out}: {len(lines)} caption lines, {m} words over {times[0][0]:.2f}-{times[-1][1]:.2f}s")
