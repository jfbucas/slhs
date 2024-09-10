import pygame
WHITE = (255,255,255)

class Bird(pygame.sprite.Sprite):
  #This class represents a bird. It derives from the "Sprite" class in Pygame.
    
  def __init__(self, x, y):
    # Call the parent class (Sprite) constructor
    super().__init__()
    
    # Load all the images for our animation and store these in a list    
    self.images = []
    self.images.append(pygame.image.load('images/flappy-bird-1.png'))
    self.images.append(pygame.image.load('images/flappy-bird-2.png'))
    self.images.append(pygame.image.load('images/flappy-bird-3.png'))
    self.images.append(pygame.image.load('images/flappy-bird-4.png'))
    self.images.append(pygame.image.load('images/flappy-bird-5.png'))
    self.images.append(pygame.image.load('images/flappy-bird-6.png'))
    self.images.append(pygame.image.load('images/flappy-bird-7.png'))
    self.images.append(pygame.image.load('images/flappy-bird-6.png'))
    self.images.append(pygame.image.load('images/flappy-bird-5.png'))
    self.images.append(pygame.image.load('images/flappy-bird-4.png'))
    self.images.append(pygame.image.load('images/flappy-bird-3.png'))
    self.images.append(pygame.image.load('images/flappy-bird-2.png'))
    
    # Use the first image for our sprite    
    self.index = 0
    self.image = self.images[self.index]
        
    # Fetch the rectangle object that has the dimensions of the image.
    self.rect = self.image.get_rect()
    
    # Position the sprite on the screen at the given coordinates
    self.rect.x = x
    self.rect.y = y
  
  def update(self):
    # Increment the inex by 1 everytimne the update method is called
    self.index += 1
 
    # Check if the index is larger than the total number of images 
    if self.index >= len(self.images):
      # Reset the index to 0
      self.index = 0
        
    # Update the image that will be displayed
    self.image = self.images[self.index] 
