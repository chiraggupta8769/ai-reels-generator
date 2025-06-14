from flask import Flask, jsonify
from edge_voice import text_to_speech
import random

app = Flask(__name__)

# 📝 Pre-written emotional scripts (Babloo Vlogger style)
templates = [
    "Ek ladka tha jise sab log neecha dikhate the, par usne sabit kiya ki sapne bhi sach hote hain.",
    "Uski maa rotiyan bechti thi, aaj beta BMW mein maa ko leke ghoomta hai.",
    "Woh ladka school drop-out tha, par aaj uske naam ka college khula hai.",
    "Zindagi mein haar tab hoti hai, jab tum khud haar maante ho.",
    "Ek waqt tha jab log usse pehchante nahi the, aaj log usse milne ka intezaar karte hain."
]
def generate():
    script = random.choice(templates)
    filename = "output.mp3"
    text_to_speech(script, filename)
    return {
        "script": script,
        "audio_file": filename
    }

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7860)
