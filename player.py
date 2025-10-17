import pygame
import constants as c


class Player(pygame.sprite.Sprite):
    class Stats: 
        def __init__(self, carType):
            car = c.carTypes.get(carType, c.carTypes["red"])
            self.turnRate = car["turnRate"]
            self.acceleration = car["acceleration"]
            self.maxSpeed = car["maxSpeed"]
            self.braking = car["braking"]
            self.maxReverse = car["maxReverse"]

    def __init__(self, x, y, carType):
        super().__init__()
        self.image = c.playerImage
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.stats = self.Stats(carType)
        self.speed = 0

    def move(self, keys):
        if keys[pygame.K_d]:
            self.rect.x += self.stats.turnRate
        if keys[pygame.K_a]:
            self.rect.x -= self.stats.turnRate

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

        self.rect.y -= self.speed

    def checkBounds(self):
        # clamp the player within the visible road area
        top_limit = c.HORIZON_Y
        bottom_limit = c.HEIGHT
        left_limit = 0
        right_limit = c.WIDTH

        if self.rect.left < left_limit:
            self.rect.left = left_limit
        elif self.rect.right > right_limit:
            self.rect.right = right_limit

        if self.rect.top < top_limit:
            self.rect.top = top_limit
        elif self.rect.bottom > bottom_limit:
            self.rect.bottom = bottom_limit

    def draw(self, screen):
        screen.blit(self.image, self.rect.topleft)
