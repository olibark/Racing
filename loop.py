import pygame, draw, os
import constants as c
import background as bg

def main_loop(player, screen):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            c.running = False
    
    keys = pygame.key.get_pressed()
    
    player.move(keys)
    
    if keys[pygame.K_d] or keys[pygame.K_a] or keys[pygame.K_w] or keys[pygame.K_s]:
        #os.system(c.clear)
        print(f"Player X: {player.rect.x}, Player Y: {player.rect.y}, Speed: {player.speed}")
    if keys[pygame.K_ESCAPE]:
        c.running = False

    draw.all(screen, player)
    pygame.display.flip()
    