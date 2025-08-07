import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien

class AlienInvasion:
    '''Class manages game behaviour and assets'''
    def __init__(self):
        '''initialises the game'''
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

       
    def run_game(self):
        '''start the main loop for the game'''
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
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
        elif event.key == pygame.K_SPACE:
             self._fire_bullet()

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

    def _fire_bullet(self):
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        self.bullets.update()

            # Get rid of old bullets
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        # print(len(self.bullets))

    def _create_fleet(self):
        alien = Alien(self)
        alien_width = alien.rect.width
        avaliable_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = avaliable_space_x // (2 * alien_width)

        for alien_number in range(number_aliens_x):
            alien = Alien(self)
            alien.x = alien_width + 2 * alien_width * alien_number
            alien.rect.x = alien.x
            self.aliens.add(alien)
    
    def _update_screen(self):
        # makes the most recently drawn screen visible
        self.screen.fill(self.settings.bg_colour)
        self.ship.blitme()
        
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)
        pygame.display.flip()

if __name__ == '__main__':
    # Makes a game instance and runs the game
    ai = AlienInvasion()
    ai.run_game()
