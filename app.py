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
import random
from edge_voice import text_to_speech

scripts = [
    "Life gives you 100 reasons to cry, show life you have 1000 reasons to smile.",
    "You were born to be real, not to be perfect.",
    "In the middle of difficulty lies opportunity.",
    "Sometimes the smallest step in the right direction ends up being the biggest step of your life.",
    "The comeback is always stronger than the setback."
]

def generate():
    script = random.choice(scripts)
    output_file = "output.mp3"
    text_to_speech(script, output_file)
    return {"script": script, "audio_file": output_file}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7860)
