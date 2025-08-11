class Settings():
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_colour = (230, 230, 230)
        self.bg_blue = (0, 0, 255)
        # Ship settings
        self.ship_speed = 1.5
        self.ship_limit = 3
        # Bullet settings
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_colour = (60, 60, 60)
        self.bullets_allowed = 3
        # Alien settings
        self.alien_speed = 1.0
        self.fleet_drop_speed = 7
        self.fleet_direction = 1