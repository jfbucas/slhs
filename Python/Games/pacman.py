import random
import os

# Define the game board dimensions
WIDTH = 20
HEIGHT = 10

# Define the characters for Pac-Man, pellets, and ghosts
PACMAN = "P"
PELLET = "."
GHOST = "G"
EMPTY = " "

# Initialize the game board with pellets
board = [[PELLET for _ in range(WIDTH)] for _ in range(HEIGHT)]

# Place Pac-Man at a starting position
pacman_x, pacman_y = 1, 1
board[pacman_y][pacman_x] = PACMAN

# Place ghosts at random positions on the board
ghosts = []
for _ in range(3):  # Change the number here for more or fewer ghosts
    while True:
        ghost_x = random.randint(0, WIDTH - 1)
        ghost_y = random.randint(0, HEIGHT - 1)
        if board[ghost_y][ghost_x] == PELLET:
            board[ghost_y][ghost_x] = GHOST
            ghosts.append((ghost_x, ghost_y))
            break

# Function to display the game board
def display_board():
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear the console
    for row in board:
        print(" ".join(row))
    print("Use WASD to move. Eat all the pellets without hitting a ghost!")

# Function to move Pac-Man
def move_pacman(dx, dy):
    global pacman_x, pacman_y
    new_x = pacman_x + dx
    new_y = pacman_y + dy
    
    # Check boundaries
    if 0 <= new_x < WIDTH and 0 <= new_y < HEIGHT:
        # Check if next cell is a ghost
        if board[new_y][new_x] == GHOST:
            print("Game Over! You were caught by a ghost!")
            return False
        
        # Move Pac-Man
        board[pacman_y][pacman_x] = EMPTY
        pacman_x, pacman_y = new_x, new_y
        board[pacman_y][pacman_x] = PACMAN
    return True

# Function to check if the player has won
def check_win():
    for row in board:
        if PELLET in row:
            return False
    return True

# Main game loop
while True:
    display_board()
    
    # Check for win condition
    if check_win():
        print("Congratulations! You've eaten all the pellets!")
        break

    # Get player input for movement
    move = input("Move (WASD): ").lower()
    if move == "w":
        if not move_pacman(0, -1): break
    elif move == "a":
        if not move_pacman(-1, 0): break
    elif move == "s":
        if not move_pacman(0, 1): break
    elif move == "d":
        if not move_pacman(1, 0): break

print("Thanks for playing!")
