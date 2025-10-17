import pygame as pyg
import constants as c
import background as bg

def all(screen, player):
    bg.drawBG(screen)
    player.draw(screen)