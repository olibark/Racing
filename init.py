import pygame, os 
import constants as c
import player as pl 

def Init():
    os.system(c.CLEAR)
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((c.WIDTH, c.HEIGHT))
    
    player_img_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'img', 'cars', 'red_car.png')
    temp_playerImg = pygame.image.load(player_img_path).convert_alpha()
    
    height = int(temp_playerImg.get_width() * c.PLAYER_SCALE)
    width = int(temp_playerImg.get_height() * c.PLAYER_SCALE)
    
    c.playerImage = pygame.transform.smoothscale(temp_playerImg, (height, width))
    
    player = pl.Player(c.player_start[0], c.player_start[1], "red")
    
    background_img_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'img', 'backgrounds', 'roadMoantains.png')
    temp_backgroundImg = pygame.image.load(background_img_path).convert()
    
    backgroundImg = pygame.transform.smoothscale(temp_backgroundImg, (c.WIDTH, c.HEIGHT))
    
    return screen, clock, player, backgroundImg    