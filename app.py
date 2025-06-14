import os
import requests
from flask import Flask, jsonify
from edge_voice import text_to_speech
from video_maker import create_final_video

PEXELS_API_KEY = os.getenv("PEXELS_API_KEY")

# Optional Flask for local testing
app = Flask(__name__)

def generate_script(query):
    print(f"🧠 Generating script for: {query}")
    return f"This is a story about {query.lower()} that will touch your heart."

def get_video_from_pexels(query):
    headers = {"Authorization": PEXELS_API_KEY}
    params = {"query": query, "per_page": 1}
    try:
        res = requests.get("https://api.pexels.com/videos/search", headers=headers, params=params)
        res.raise_for_status()
        videos = res.json().get("videos", [])
        if not videos:
            raise Exception("No videos found for this query.")

        url = videos[0]["video_files"][0]["link"]
        print(f"📹 Downloading background video from: {url}")
        r = requests.get(url)
        with open("background.mp4", "wb") as f:
            f.write(r.content)
    except Exception as e:
        print(f"⚠️ Pexels API failed: {e}")
        print("📂 Using fallback local video instead.")
        fallback = "fallback.mp4"
        if not os.path.exists(fallback):
            # Download or generate a default fallback video if it doesn't exist
            fallback_url = "https://github.com/marcopeg/video-samples/raw/master/video.mp4"
            r = requests.get(fallback_url)
            with open(fallback, "wb") as f:
                f.write(r.content)
        os.rename(fallback, "background.mp4")


    if not videos:
        raise Exception("❌ No videos found")

    url = videos[0]["video_files"][0]["link"]
    print(f"📹 Downloading background video from: {url}")
    r = requests.get(url)
    with open("background.mp4", "wb") as f:
        f.write(r.content)

def generate(query):
    script = generate_script(query)
    audio_path = text_to_speech(script)
    get_video_from_pexels(query)
    create_final_video("background.mp4", audio_path)
    print("✅ Final video created as final_video.mp4")
    return {"status": "done", "query": query}

@app.route("/")
def index():
    return jsonify({"status": "ready"})

@app.route("/generate", methods=["GET"])
def run_generate():
    return jsonify(generate("Emotional story"))
