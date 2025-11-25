import pygame, constants as c

def background(screen):
    screen.fill(c.BACKGROUND)
    
def road(screen):
    points = [(c.WIDTH * 40/100, c.HORIZON_Y), #top-left
              (c.WIDTH * 60/100, c.HORIZON_Y), #top-right
              (c.WIDTH * 80/100, c.HEIGHT), #bottom-right
              (c.WIDTH * 20/100, c.HEIGHT) #bottom-left
              ]
    
    pygame.draw.rect(screen, c.OUTER_ROAD_COLOUR, (0, c.HORIZON_Y, c.WIDTH, c.HEIGHT - c.HORIZON_Y))
    pygame.draw.polygon(screen, c.ROAD_COLOUR, points)
    centreLine(screen)
    
def centreLine(screen):
    points = [(c.WIDTH * 49.95/100, c.HORIZON_Y),
              (c.WIDTH * 50.05/100, c.HORIZON_Y),
              (c.WIDTH * 50.55/100, c.HEIGHT),
              (c.WIDTH * 49.45/100, c.HEIGHT)
              ]
    
    pygame.draw.polygon(screen, c.CENTRELINE_COLOUR, points)
    
def cursor(screen):
    screen.blit(c.cursorImage, c.cursor_rect)
    
def all(screen, player):
    background(screen)
    road(screen)
    player.draw(screen)
    cursor(screen)