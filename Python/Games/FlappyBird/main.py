# Import the pygame library and initialise the game engine
import pygame
from bird import Bird

pygame.init()
# Define some colors
BLUE = (50,150,235)

# Open a new window
size = (700, 500)

screen = pygame.display.set_mode(size)
pygame.display.set_caption("flappyBird")

#Instatiate a Bird object and set its initial position at (x=220, y=120)
flappyBird = Bird(220,120) 

#This will be a list that will contain all the sprites we intend to use in our game
all_sprites_list = pygame.sprite.Group()

# Add our flappyBird object to the list of sprites
all_sprites_list.add(flappyBird)

# The loop will carry on until the user exits the game (e.g. clicks the close button).
carryOn = True
 
# The clock will be used to control how fast the screen updates
clock = pygame.time.Clock()
 
# -------- Main Program Loop -----------
while carryOn:
    # --- Main event loop
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
              carryOn = False # Flag that we are done so we exit this loop
        elif event.type==pygame.KEYDOWN:
                if event.key==pygame.K_x: #Pressing the x Key will quit the game
                     carryOn=False  
 
    # --- Game logic should go here
    all_sprites_list.update()
 
 
    # --- Drawing code should go here
    # First, clear the screen to blue (sky). 
    screen.fill(BLUE)
    
    #Now let's draw all the sprites in one go. (For now we only have 1 sprite!)
    all_sprites_list.draw(screen) 
 
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
     
    # --- Limit to 60 frames per second
    clock.tick(60)
 
#Once we have exited the main program loop we can stop the game engine:
pygame.quit()
