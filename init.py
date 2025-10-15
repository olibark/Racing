import pygame, os
import constants as c 
import player as pl

def Init():
    os.system(c.clear)
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((c.WIDTH, c.HEIGHT))
    c.playerImage = pygame.image.load(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'img', 'cars', 'red_car.png')).convert_alpha()
    player = pl.Player(c.playerCoords[0], c.playerCoords[1], "red")
    
    return screen, clock, player