import pygame, draw
import constants as c
import background as bg

def main_loop(player, screen):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            c.running = False
    
    for key in pygame.key.get_pressed():
        if key == pygame.K_d:
            player.x += player.Stats.turnRate
            print(player.Stats.turnRate)
        if key == pygame.K_a:
            player.x -= player.Stats.turnRate 
            print(player.Stats.turnRate)
    draw.all(screen, player)
    
    pygame.display.flip()
    