import pygame
import constants as c 

class Player(pygame.sprite.Sprite):
    class Stats: 
        def __init__(self, carType):
            self.carType = carType
            
            if self.carType in c.carTypes:
                self.turnRate = c.carTypes[carType]["turnRate"]
                self.acceleration = c.carTypes[carType]["acceleration"]
                self.maxSpeed = c.carTypes[carType]["maxSpeed"]
                self.braking = c.carTypes[carType]["braking"]
                self.maxReverse = c.carTypes[carType]["maxReverse"]
            else:
                self.turnRate = c.carTypes["red"]["turnRate"]
                self.acceleration = c.carTypes["red"]["acceleration"]
                self.maxSpeed = c.carTypes["red"]["maxSpeed"]
                self.braking = c.carTypes["red"]["braking"]
                self.maxReverse = c.carTypes["red"]["maxReverse"]
        
    def __init__(self, x, y, carType):
        pygame.sprite.Sprite.__init__(self)
        self.carType = carType
        self.image = c.playerImage
        self.x = x
        self.y = y
        self.speed = 0
        self.stats = self.Stats(carType)
    
    def move(self, keys):
        if keys[pygame.K_d]:
            self.x += self.stats.turnRate
        if keys[pygame.K_a]:
            self.x -= self.stats.turnRate
            
        if keys[pygame.K_w] and self.speed < self.stats.maxSpeed:
            self.speed = min(self.speed + self.stats.acceleration, self.stats.maxSpeed)
        elif keys[pygame.K_s]:
            if self.speed > 0:
                self.speed = max(self.speed - self.stats.braking, 0)
            else: 
                self.speed = max(self.speed - self.stats.acceleration - self.stats.braking, -self.stats.maxReverse)
        else:
            if self.speed > 0:
                self.speed = max(self.speed - c.friction, 0)
            elif self.speed < 0:
                self.speed = min(self.speed + c.friction, 0)
                
        self.y -= self.speed
    
    def checkBounds(self):
        if self.x < 0:
            self.x = 0
        elif self.x + self.image.get_width() > c.WIDTH:
            self.x = c.WIDTH - self.image.get_width()
        if self.y < c.ROAD_HEIGHT - self.image.get_height():
            self.y = 0
        elif self.y + self.image.get_height() > c.HEIGHT:
            self.y = c.HEIGHT - self.image.get_height()
    
    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))