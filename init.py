import pygame, os
import constants as c 
import player as pl

def Init():
    os.system(c.clear)
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((c.WIDTH, c.HEIGHT))
    
    P_img_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'img', 'cars', 'red_car.png')
    P_img = pygame.image.load(P_img_path).convert_alpha()
    B_img_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'img', 'backgrounds', 'roadMoantains.png')
    backgroundImg = pygame.image.load(B_img_path).convert()
    c.backgroundImg = pygame.transform.smoothscale(backgroundImg, (c.WIDTH, c.HEIGHT))
    
    height = int(P_img.get_width() * c.PLAYER_SCALE)
    width = int(P_img.get_height() * c.PLAYER_SCALE)
    
    c.playerImage = pygame.transform.smoothscale(P_img, (height, width))

    player = pl.Player(c.playerCoords[0], c.playerCoords[1], "red")
    
    return screen, clock, player, backgroundImg