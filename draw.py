import pygame
import constants as c

def all(screen, player):
    drawBG(screen)
    centreLine(screen)
    player.draw(screen)
    
def drawBG(screen):
    screen.fill(c.BACKGROUND)
    pygame.draw.rect(screen, c.ROAD_COLOUR, (0, c.HORIZON_Y, c.WIDTH, c.HEIGHT - c.HORIZON_Y))
    
def centreLine(screen):
    centre = c.WIDTH // 2
    
    pygame.draw.line(screen, c.CENTERLINE_COLOUR, (centre, c.HORIZON_Y), (centre, c.HEIGHT), 8)