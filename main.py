import random
from app import generate
from video_merge import download_video, merge_audio_video

queries = ["emotional man", "crying woman", "sad street", "lonely person", "dark sky"]
query = random.choice(queries)

data = generate()
script = data["script"]
audio_file = data["audio_file"]

video_file = download_video(query=query)
merge_audio_video(video_file, audio_file)
