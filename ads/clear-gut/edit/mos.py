# -*- coding: utf-8 -*-
# Objective voice-quality MOS via UTMOS (naturalness, 1-5). Local, free, GPU/CPU.
# Run with comfy python:  C:/Users/SE/miniforge3/envs/comfy/python.exe edit/mos.py <wav> [<wav> ...]
# CAVEAT: UTMOS is English-TTS-trained -> absolute scores read LOW on Hindi/character/ambient audio.
#   Use RELATIVE ranking (flag lowest outliers) + TREND across re-rolls, not a raw threshold.
#   Isolate the voice (ElevenLabs isolate_audio) first for a fairer number.
import sys, wave, numpy as np, torch
def load_wav(p):
    w = wave.open(p, "rb"); sr = w.getframerate(); n = w.getnframes()
    raw = w.readframes(n); ch = w.getnchannels(); w.close()
    x = np.frombuffer(raw, dtype=np.int16).astype(np.float32) / 32768.0
    if ch > 1: x = x.reshape(-1, ch).mean(axis=1)
    return x, sr
wavs = sys.argv[1:] or [f"edit/verify/s{i}.wav" for i in (1,2,3,4,5)]
pred = torch.hub.load("tarepan/SpeechMOS:v1.2.0", "utmos22_strong", trust_repo=True); pred.eval()
scores = {}
for p in wavs:
    try:
        x, sr = load_wav(p)
        with torch.no_grad(): scores[p] = float(pred(torch.from_numpy(x).unsqueeze(0), sr))
        print(f"  {p}: MOS={scores[p]:.2f}")
    except Exception as e:
        print(f"  {p}: ERROR {e}")
ok = [v for v in scores.values()]
if len(ok) > 1:
    med = float(np.median(ok))
    print(f"\nmedian={med:.2f} -> flag (>=0.3 below median, listen/re-roll):")
    for p, s in sorted(scores.items(), key=lambda kv: kv[1]):
        if s <= med - 0.3: print(f"  FLAG {p}: {s:.2f}")
