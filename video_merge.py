import requests
import os
import subprocess

PEXELS_API_KEY = "gvTSCPuh5r47OyWrUHMZLHCsXu766LX96WcxtyZ3Ij244HlBusjToYVa"  # replace this

import random

def download_video(query="emotional man", filename="background.mp4"):
    headers = {"Authorization": PEXELS_API_KEY}
    params = {"query": query, "orientation": "portrait", "per_page": 10}
    res = requests.get("https://api.pexels.com/videos/search", headers=headers, params=params)
    res_json = res.json()

    # Randomly choose one of the top 10 videos
    video_files = res_json["videos"]
    chosen_video = random.choice(video_files)
    video_url = chosen_video["video_files"][0]["link"]

    r = requests.get(video_url)
    with open(filename, "wb") as f:
        f.write(r.content)
    return filename

def merge_audio_video(video_file, audio_file, output_file="final_video.mp4"):
    command = [
        "ffmpeg",
        "-i", video_file,
        "-i", audio_file,
        "-c:v", "copy",
        "-c:a", "aac",
        "-shortest",
        output_file
    ]
    subprocess.run(command)

def create_reel():
    video = download_video()
    merge_audio_video(video, "output.mp3")
    print("✅ final_video.mp4 created!")

# Run it
if __name__ == "__main__":
    create_reel()
