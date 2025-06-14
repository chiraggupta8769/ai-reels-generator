import asyncio
import edge_tts

async def generate_tts(text, filename):
    communicate = edge_tts.Communicate(text, voice="hi-IN-MadhurNeural")
    await communicate.save(filename)

def text_to_speech(text, filename):
    asyncio.run(generate_tts(text, filename))
    return filename