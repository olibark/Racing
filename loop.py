import pygame, draw, os
import constants as c 

def main_loop(player, screen):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            c.running = False
            
    keys = pygame.key.get_pressed()
    
    player.move(keys)
    
    if keys[pygame.K_w] or keys[pygame.K_a] or keys[pygame.K_s] or keys[pygame.K_d]:
        #player.move(keys)
        print(f"X: {player.rect.x}   Y: {player.rect.y}   moveX: {player.moveX}   moveY: {player.moveY}")
    if keys[pygame.K_ESCAPE]:
        c.running = False
        
    draw.all(screen, player)
    pygame.display.flip()