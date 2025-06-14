from app import generate
from video_merge import download_video, merge_audio_video

# Step 1: Generate voice + script
data = generate()
script = data["script"]
audio_file = data["audio_file"]

print("🎤 Generated script:", script)

# Step 2: Download background video
video_file = download_video(query="emotional man")

# Step 3: Merge audio + video
merge_audio_video(video_file, audio_file, output_file="final_video.mp4")

print("✅ Reels ready: final_video.mp4")
