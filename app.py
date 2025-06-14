from video_maker import create_final_video
import os
import requests
import asyncio
from flask import Flask
from edge_voice import text_to_speech
from script_generator import generate_script

PEXELS_API_KEY = os.getenv("PEXELS_API_KEY", "")
fallback = "background.mp4"

def get_video_from_pexels(query):
    print("🔍 Searching Pexels for video...")
    headers = {"Authorization": PEXELS_API_KEY}
    try:
        response = requests.get(
            f"https://api.pexels.com/videos/search?query={query}&per_page=1",
            headers=headers
        )
        response.raise_for_status()
        data = response.json()
        videos = data.get("videos", [])
        if not videos:
            raise Exception("❌ No videos found")
        url = videos[0]["video_files"][0]["link"]
        print("⬇️ Downloading stock video...")
        with open("background.mp4", "wb") as f:
            f.write(requests.get(url).content)
    except Exception as e:
        print(f"⚠️ Pexels API failed: {e}")
        print("📂 Using fallback local video instead.")
        if not os.path.exists(fallback):
            raise Exception("❌ No fallback video found")

def generate(query):
    print(f"🧠 Generating script for: {query}")
    script = generate_script(query)

    # Voice
    print("🎤 Generating voiceover...")
    asyncio.run(text_to_speech(script))

    # Video
    get_video_from_pexels(query)

    # Merge
    print("🎬 Merging audio and video...")
    os.system(f"ffmpeg -y -i background.mp4 -i output.mp3 -c:v copy -c:a aac -shortest final_video.mp4")
    print("✅ Final video created: final_video.mp4")

# Optional Flask endpoint if needed
app = Flask(__name__)

@app.route("/")
def index():
    return "AI Reels Generator is running!"
