import pygame, draw
import constants as c
import background as bg

def main_loop(player, screen, backgroundImg):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            c.running = False
    
    keys = pygame.key.get_pressed()
    
    player.move(keys)
    
    if keys[pygame.K_d] or keys[pygame.K_a] or keys[pygame.K_w] or keys[pygame.K_s]:
        print(f"Player X: {player.x}, Player Y: {player.y}, Speed: {player.speed}")
    
    draw.all(screen, player)
    #player.checkBounds()
    pygame.display.flip()
    