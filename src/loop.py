import pygame, draw, constants as c

def main_loop(player, screen):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            c.running = False
            
    keys = pygame.key.get_pressed()
    
    player.move(keys)
    
    if keys[pygame.K_w] or keys[pygame.K_a] or keys[pygame.K_s] or keys[pygame.K_d]:
       
        rectX = round(player.rect.x, 2)
        rectY = round(player.rect.y, 2)
        moveX = round(player.moveX, 2)
        moveY = round(player.moveY, 2)
           
        print(f"X: {rectX}   Y: {rectY}   moveX: {moveX}   moveY: {moveY}")
        
    if keys[pygame.K_ESCAPE]:
        c.running = False
        
    draw.all(screen, player)
    pygame.display.flip()