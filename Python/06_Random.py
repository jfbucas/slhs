# 7. Random Module
# Example: Magic 8-Ball Predictions


import random

responses = [
    "Yes, definitely!", 
    "Ask again later.", 
    "No chance!",
    "Outlook not so good."
]

print("Magic 8-Ball says: " + random.choice(responses))
