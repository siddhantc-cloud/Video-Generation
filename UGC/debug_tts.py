import asyncio, edge_tts, json
async def probe():
    types = {}
    words = []
    async for chunk in edge_tts.Communicate("Iska use bahut simple hai. Subah aur raat.", "hi-IN-MadhurNeural").stream():
        t = chunk.get("type")
        types[t] = types.get(t, 0) + 1
        if t and "Boundary" in str(t):
            words.append({k: chunk.get(k) for k in ("text", "offset", "duration")})
    print("chunk types:", types)
    print("first boundaries:", json.dumps(words[:4], ensure_ascii=False))
print("edge-tts version:", edge_tts.__version__ if hasattr(edge_tts, "__version__") else "unknown")
asyncio.run(probe())
