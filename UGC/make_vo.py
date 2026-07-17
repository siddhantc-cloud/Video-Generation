import asyncio, json, edge_tts

async def tts(text, mp3, words_json):
    audio = b''
    words = []
    async for chunk in edge_tts.Communicate(text, "hi-IN-MadhurNeural").stream():
        if chunk["type"] == "audio":
            audio += chunk["data"]
        elif chunk["type"] == "WordBoundary":
            words.append({"word": chunk["text"], "start": chunk["offset"] / 1e7,
                          "end": (chunk["offset"] + chunk["duration"]) / 1e7})
    open(mp3, 'wb').write(audio)
    json.dump(words, open(words_json, 'w', encoding='utf-8'), ensure_ascii=False)
    print(mp3, len(words), "words,", round(words[-1]["end"], 2), "s")

S4 = "Ye koi harsh solution nahi hai. Ye das se zyada Ayurvedic herbs se bana hai, jaise Haritaki, Ajwain aur Saunf, jo digestion ko naturally support karte hain."
S5 = "Iska use bahut simple hai. Subah aur raat ko sone se pehle, bas 10 se 15 drops paani mein milaiye aur pee lijiye."
asyncio.run(tts(S4, "s4_vo.mp3", "s4_words.json"))
asyncio.run(tts(S5, "s5_vo.mp3", "s5_words.json"))
