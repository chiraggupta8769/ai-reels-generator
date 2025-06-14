import os

def create_final_video(video_path="background.mp4", audio_path="output.mp3", output_path="final_video.mp4"):
    print("🎬 Merging audio and video...")
    command = f"ffmpeg -y -i {video_path} -i {audio_path} -c:v copy -c:a aac -shortest {output_path}"
    print(f"🎬 Running command: {command}")
    os.system(command)
    print(f"✅ Final video created: {output_path}")