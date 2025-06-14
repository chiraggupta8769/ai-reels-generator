import random
from app import generate

queries = [
    "Power of believing in yourself",
    "From failure to success",
    "Never give up on your dreams",
    "Small steps make big changes",
    "Your time will come"
]

# Pick a random topic
query = random.choice(queries)
print(f"🎯 Selected query: {query}")

# Generate the reel with that topic
generate(query)
