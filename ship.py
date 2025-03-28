import pygame

class Ship:
    """A class to manage the ship."""
    def __init__(self, ai_game):
        """Initialize the ship and set its starting position."""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()
        # Load the ship image and get its rect.
        self.image = pygame.image.load('images/spaceship.bmp')
        self.rect = self.image.get_rect()
        # Start each new ship at the bottom center of the screen.
        point = (1200,400)
        self.rect.midbottom = self.screen_rect.midbottom
        self.rect.x = 550
        self.rect.y = 600

        # Store a decimal value for the ship's horizontal position
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)


        #Moving flag right
        self.moving_right = False

        #Moving flag left
        self.moving_left = False

        #Moving up
        self.moving_up = False

        #Moving down
        self.moving_down = False

    def update(self):
        # Update the ship's x value , not the rect
        #The self.rect.right returns the x-coordinate of the ship 
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed 

        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.ship_speed
        
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.ship_speed
        
        # Update rect object from self.x and self.y
        self.rect.x = self.x
        self.rect.y = self.y

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)
    
    