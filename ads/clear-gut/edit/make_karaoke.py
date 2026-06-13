# -*- coding: utf-8 -*-
import json, io, sys

KNOWN = {
 's1': "हा हा हा! मैं हूँ कॉन्स्टिपेशन किंग! तुम्हारा पेट मैं कभी साफ़ नहीं होने दूँगा!",
 's2': "मैं हूँ भुई आँवला! मैं डाइजेशन को नैचुरली सपोर्ट करता हूँ!",
 's3': "मैं हूँ अजवाइन! पेट का भारीपन और गैस, मेरा काम!",
 's4': "मैं हूँ सौंफ! खाने के बाद की ब्लोटिंग को शांत करती हूँ!",
 's5': "मैं हूँ हरीतकी! आयुर्वेद की सबसे भरोसेमंद जड़ी बूटियों में से एक!",
 's6': "ये चार ही नहीं, दस से ज़्यादा आयुर्वेदिक जड़ी बूटियों की पूरी फौज!",
 's7': "सबकी ताक़त, अब एक ही, आयुर्वेदिक क्लियर गट ड्रॉप्स में!",
 's8': "रोज़ सुबह और शाम, सिर्फ़ दस से पंद्रह बूँदें। पेट हल्का, दिन हल्का!",
}
OFF = {'s1':0.0,'s2':7.6,'s3':15.2,'s4':22.8,'s5':30.4,'s6':38.0,'s7':45.6,'s8':53.2}
ORDER = ['s1','s2','s3','s4','s5','s6','s7','s8']

def span(s):
    d = json.load(open(f'edit/verify/{s}.json', encoding='utf-8'))
    words = [w for seg in d.get('segments',[]) for w in seg.get('words',[])]
    if words:
        t0 = max(0.0, float(words[0]['start']))
        t1 = float(words[-1]['end'])
    else:
        seg = d['segments']; t0 = float(seg[0]['start']); t1 = float(seg[-1]['end'])
    t0 = max(t0, 0.4)   # clips have a scripted ~half-second pause; whisper reports 0.0
    t1 = min(t1, 7.9)
    if t1 - t0 < 1.0: t1 = t0 + 1.0
    return t0, t1

def fmt(t):
    h=int(t//3600); m=int((t%3600)//60); sec=t%60
    return f"{h:d}:{m:02d}:{sec:05.2f}"

def kf_line(text, span_cs):
    words = text.split()
    weights = [max(1,len(w)) for w in words]
    tot = sum(weights)
    out=[]; acc=0
    for i,(w,wt) in enumerate(zip(words,weights)):
        if i < len(words)-1:
            cs = max(8, round(wt/tot*span_cs)); acc+=cs
        else:
            cs = max(8, span_cs-acc)   # remainder to last word
        out.append(f"{{\\kf{cs}}}{w} ")
    return "".join(out).rstrip()

header = """[Script Info]
ScriptType: v4.00+
PlayResX: 1080
PlayResY: 1920
WrapStyle: 0
ScaledBorderAndShadow: yes

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: K,Nirmala UI,58,&H0000D7FF,&H00FFFFFF,&H00202020,&H64000000,-1,0,0,0,100,100,0,0,1,4,2,2,90,90,235,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""

events=[]
for s in ORDER:
    t0,t1 = span(s)
    span_cs = int(round((t1-t0)*100))
    start = OFF[s] + t0
    end   = OFF[s] + t1 + 0.5
    txt = kf_line(KNOWN[s], span_cs)
    events.append(f"Dialogue: 0,{fmt(start)},{fmt(end)},K,,0,0,0,,{txt}")
    print(f"{s}: off={OFF[s]} t0={t0:.2f} t1={t1:.2f} -> [{fmt(start)} - {fmt(end)}]")

with io.open('edit/captions.ass','w',encoding='utf-8') as f:
    f.write(header + "\n".join(events) + "\n")
print("WROTE edit/captions.ass with", len(events), "events")
