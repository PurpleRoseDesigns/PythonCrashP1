import sys
import pygame
from settings import Settings
from ship import Ship

class AlienInvasion:
    '''Class manages game behaviour and assets'''
    def __init__(self):
        '''initialises the game'''
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)

       
    def run_game(self):
        '''start the main loop for the game'''
        while True:
            self._check_events()
            self.ship.update()
            self._update_screen()
            
    def _check_events(self):
        '''Game controls (left/right key movements for ship )'''
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    self._check_key_down(event)
                elif event.type == pygame.KEYUP:
                      self._check_key_up(event)

    def _check_key_down(self, event):
        '''Responds to keypress'''
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        # elif event.key == pygame.K_UP:
        #      self.ship.moving_up = True
        # elif event.key == pygame.K_DOWN:
        #      self.ship.moving_down = True
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_key_up(self, event):
        '''Responds to key release'''
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False 
        # elif event.key == pygame.K_UP:
        #      self.ship.moving_up = False
        # elif event.key == pygame.K_DOWN:
        #      self.ship.moving_down = False
    
    def _update_screen(self):
            # makes the most recently drawn screen visible
            self.screen.fill(self.settings.bg_colour)
            self.ship.blitme()
            pygame.display.flip()

if __name__ == '__main__':
    # Makes a game instance and runs the game
    ai = AlienInvasion()
    ai.run_game()
