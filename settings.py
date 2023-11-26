class Settings:
    def __init__(self):
        #SCreen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0, 0, 139)
        #ship settings
        self.ship_speed = 5
        self.ship_limit = 3
        #bullet settings
        self.bullet_speed = 8.0
        self.bullet_width = 10
        self.bullet_height = 15
        self.bullet_color = (253, 255, 0)
        #alien settings
        self.alien_speed = 10
        self.fleet_drop_speed = 10
        self.fleet_direction = 1
        # How quickly the game speeds up
        self.speedup_scale = 1.2
        # How quickly point values increase
        self.score_scale = 1.5
        self.initialize_dynamic_settings()
        #scoring settings
        self.alien_points = 10
    
    def initialize_dynamic_settings(self):
        #Initialize settings that change throughout the game.
        self.ship_speed = 5
        self.bullet_speed = 7
        self.alien_speed = 3
        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1

    def increase_speed(self):
        #Increase speed settings
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
        if self.fleet_direction == 1:
            self.fleet_direction = - 1
        else:
            self.fleet_direction = 1