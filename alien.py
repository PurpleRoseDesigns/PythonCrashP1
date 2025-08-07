import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        # self.settings = ai_game.settings
        # self.screen_rect = ai_game.screen.get_rect()
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)
        
        # start each new ship bottom-center of screen
        # self.rect.top = self.screen_rect.top

        # Below code sets the image in the center of screen
        # self.rect.midbottom = self.screen_rect.center

        # Store decimal value for ship horizontal position
        # self.x = float(self.rect.x)
        # self.y = float(self.rect.y)

        # Movement Flags
        # self.moving_right = False
        # self.moving_left = False

        # Movement Flags for up and down, not used in current game
        # self.moving_up = False
        # self.moving_down = False

            
    # def update(self):
    #     '''Update Ship position using movement flags'''
    #     if self.moving_right and self.rect.right < self.screen_rect.right:
    #         self.x += self.settings.alien_speed
    #     if self.moving_left and self.rect.left > 0:
    #         self.x -= self.settings.alien_speed

        # Up and Down positioning using movement flags, not used in current game
        # if self.moving_up and self.rect.top > 0:
        #     self.y -= self.settings.ship_speed
        # if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
        #     self.y += self.settings.ship_speed

        # update rect object from self.x
        # self.rect.x = self.x

        # update rect object for y axis, not used in current game
        # self.rect.y = self.y

    # def blitme(self):
    #     self.screen.blit(self.image, self.rect)
