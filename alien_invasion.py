import sys
import pygame
from settings import Settings
from ship import Ship
class AlienInvasion:
# . Overall class to manage game assets and behavior
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        
# Initialize the game, and create game resources.
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Alien Invasion")
        self.ship = Ship(self)

    def run_game(self):
# Start the main loop for the game.
        while True:
            self._check_events()
            self._update_screen()
            self.ship.update()
# Make the most recently drawn screen visible. d
            pygame.display.flip()

    def _check_events(self):
        # Watch for keyboard and mouse events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self.check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self.check_keyup_events(event)
    
    def check_keydown_events(self, event):
        #Move the ship to the rights
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        if event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        if event.key == pygame.K_UP:
            self.ship.moving_up = True
        if event.key == pygame.K_DOWN:
            self.ship.moving_down = True
        if event.key == pygame.K_q:
            sys.exit()

    def check_keyup_events(self, event):
        #Stop moving the ship 
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        if event.key == pygame.K_LEFT:
            self.ship.moving_left = False
        if event.key == pygame.K_UP:
            self.ship.moving_up = False
        if event.key == pygame.K_DOWN:
            self.ship.moving_down = False
    

    def _update_screen(self):
        # Update images on the screen, and flip to the new screen.
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        
if __name__ == '__main__':
# Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()






 