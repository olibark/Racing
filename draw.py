import pygame as pyg
import constants as c
import background as bg

def all(screen, player):
    bg.drawBG(screen)
    screen.blit(player.image, (player.x, player.y))