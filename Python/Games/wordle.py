import random

# List of 5-letter words for the game
words = ["apple", "table", "crate", "point", "gripe", "slope", "trice", "flame", "glide", "proud"]

# Choose a random word from the list
solution = random.choice(words).lower()

# Number of attempts allowed
attempts = 6

print("Welcome to Wordle!")
print("Guess the 5-letter word. You have 6 attempts.")
print("Feedback: uppercase letters are correct and in the correct place, lowercase letters are correct but in the wrong place, '_' means incorrect letter.\n")

# Start the game
for attempt in range(1, attempts + 1):
    # Get user guess
    guess = input(f"Attempt {attempt}/{attempts}: ").lower()
    
    # Ensure the guess is a valid 5-letter word
    if len(guess) != 5 or not guess.isalpha():
        print("Please enter a valid 5-letter word.")
        continue

    # Provide feedback on the guess
    feedback = ""
    for i in range(5):
        if guess[i] == solution[i]:
            feedback += guess[i].upper()  # Correct letter and position
        elif guess[i] in solution:
            feedback += guess[i].lower()  # Correct letter but wrong position
        else:
            feedback += "_"             # Incorrect letter
    
    print("Feedback:", feedback)
    
    # Check if the guess is correct
    if guess == solution:
        print("Congratulations! You've guessed the word correctly.")
        break
else:
    print(f"Sorry, you've used all your attempts. The correct word was '{solution}'.")
