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
            else:
                self.turnRate = c.carTypes["red"]["turnRate"]
                self.acceleration = c.carTypes["red"]["acceleration"]
                self.maxSpeed = c.carTypes["red"]["maxSpeed"]
        
    def __init__(self, x, y, carType):
        pygame.sprite.Sprite.__init__(self)
        self.carType = carType
        self.image = c.playerImage
        self.x = x
        self.y = y
        self.speed = 0
        self.stats = self.Stats(self)
    def move(self):
        pass