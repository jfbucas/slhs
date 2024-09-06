# 8. Dictionaries
# Example: Robot Translator

robot_speak = {
    "hello": "beep-boop", 
    "world": "blip-blop",
    "pizza": "pizzabot activated"
}

word = input("Enter a word for your robot: ")

if word in robot_speak:
    print("Robot says: " + robot_speak[word])
else:
    print("Robot doesn't understand.")
