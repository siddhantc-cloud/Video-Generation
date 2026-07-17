import asyncio, json, sys, edge_tts

async def tts(text, voice, rate, pitch, mp3, words_json):
    audio, words = b'', []
    kw = {"rate": rate, "pitch": pitch, "boundary": "WordBoundary"}
    async for c in edge_tts.Communicate(text, voice, **kw).stream():
        if c["type"] == "audio":
            audio += c["data"]
        elif c["type"] == "WordBoundary":
            words.append({"word": c["text"], "start": c["offset"]/1e7, "end": (c["offset"]+c["duration"])/1e7})
    open(mp3, 'wb').write(audio)
    json.dump({"segments": [{"words": words}]}, open(words_json, 'w', encoding='utf-8'), ensure_ascii=False)
    print(f"{mp3}: {len(words)} words, {round(words[-1]['end'],2) if words else 0}s")

# Scene 1 villain — Constipation King, menacing (trimmed to fit 8s Veo clip)
LINE = "Hahaha! Main hoon Constipation King! Tumhara pet kabhi saaf nahi hone dunga!"
asyncio.run(tts(LINE, "hi-IN-MadhurNeural", "+0%", "-20Hz", "s1_villain.mp3", "s1_villain_words.json"))
