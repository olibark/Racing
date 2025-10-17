import constants as c
import init, loop

(screen, clock, player, backgroundImg) = init.Init()

while c.running:
    clock.tick(c.FPS)
    loop.main_loop(player, screen)