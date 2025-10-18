import pygame
import constants as c

def drawBG(screen):
    screen.fill(c.BACKGROUND)
    pygame.draw.rect(screen, c.ROAD_COLOR, (0, c.HORIZON_Y, c.WIDTH, c.HEIGHT - c.HORIZON_Y))
    pygame.draw.line(screen, (255, 255, 255), (c.WIDTH // 2, c.HORIZON_Y), (c.WIDTH // 2, c.HEIGHT), 5)
    #screen.blit(c.backgroundImg, (0, 0))