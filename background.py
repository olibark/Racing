import pygame
import constants as c

def drawBG(screen):
    screen.fill(c.BACKGROUND)
    screen.blit(c.backgroundImg, (0, 0))