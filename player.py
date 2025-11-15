import pygame 
import constants as c 

class Player(pygame.sprite.Sprite):
    class Stats:
        def __init__(self, car_type):
            car = c.car_stats.get(car_type, c.car_stats["red"])
            self.move_rate_x = car["move_rate_x"]
            self.move_rate_y = car["move_rate_y"]
            self.acceleration = car["acceleration"]
            self.braking = car["braking"]
            self.max_reverse = car["max_reverse"]
            self.accel_x = car["acceleration"]
            self.max_speed_x = self.move_rate_x
            
    def __init__(self, x, y, car_type):
        super().__init__()
        
        assert c.playerImage is not None, "load player image before creating Player instance"
        
        self.image: pygame.Surface = c.playerImage
        
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.stats = self.Stats(car_type)
        
        self.moveX = 0.0
        self.moveY = 0.0
        
    def move(self, keys):
        depth_ratio = (self.rect.centery - c.HORIZON_Y) / (c.HEIGHT - c.HORIZON_Y)
        depth_ratio = max(0.0, min(1.0, depth_ratio))
        speed_factor = 0.2 + 0.8 * depth_ratio

        max_speed_x = self.stats.max_speed_x * speed_factor
        accel_x = self.stats.accel_x * speed_factor

        if keys[pygame.K_d]:
            self.moveX = min(self.moveX + accel_x, max_speed_x)

        elif keys[pygame.K_a]:
            self.moveX = max(self.moveX - accel_x, -max_speed_x)

        else:
            if self.moveX > 0:
                self.moveX = max(self.moveX - c.FRICTION, 0)
            elif self.moveX < 0:
                self.moveX = min(self.moveX + c.FRICTION, 0)

        self.moveX = max(-max_speed_x, min(self.moveX, max_speed_x))
                      
        self.image = c.playerImage

        if keys[pygame.K_w] and self.moveY < self.stats.move_rate_y:
            self.moveY = min(self.moveY + self.stats.acceleration, self.stats.move_rate_y)

        elif keys[pygame.K_s]:

            self.image = c.playerBreakingImage
            
            if self.moveY > 0:
                self.moveY = max(self.moveY - self.stats.braking, 0)
            else: 
                self.moveY = max(self.moveY - self.stats.acceleration - self.stats.braking, -self.stats.max_reverse)
        
        else:
            if self.moveY > 0:
                self.moveY = max(self.moveY - c.FRICTION, 0)
            elif self.moveY < 0:
                self.moveY = min(self.moveY + c.FRICTION, 0)

        self.setCoords()        
        self.checkBounds()
        self.setScale()
        
    def checkBounds(self):
        top_lim = c.HORIZON_Y
        bottom_lim = c.HEIGHT
        left_lim = 0
        right_lim = c.WIDTH
        
        if self.rect.left < left_lim:
            self.rect.left = left_lim
        elif self.rect.right > right_lim:
            self.rect.right = right_lim
        
        if self.rect.top < top_lim:
            self.rect.top = top_lim
        elif self.rect.bottom > bottom_lim:
            self.rect.bottom = bottom_lim
            
    def setScale(self):
        base = c.playerBaseImage or c.playerImage
        
        diff = self.rect.y - c.HORIZON_Y
        ratio = diff / (c.HEIGHT - c.HORIZON_Y)
        ratio = max(0, min(1, ratio))
        
        scale = c.PLAYER_SCALE + (1 - c.PLAYER_SCALE) * (ratio * 4)
        
        new_width = int(base.get_width() * scale)
        new_height = int(base.get_height() * scale)
        
        self.image= pygame.transform.smoothscale(base, (new_width, new_height))
        self.rect = self.image.get_rect(center=self.rect.center)
        
    def draw(self, screen):
        screen.blit(self.image, self.rect)
    
    def setCoords(self):
        self.rect.x += int(self.moveX)
        self.rect.y -= int(self.moveY)
        