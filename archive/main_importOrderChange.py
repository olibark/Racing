from init import Init
from loop import main_loop 
from constants import running, FPS

(screen, clock, player) = Init()

while running:
    clock.tick(FPS)
    main_loop(player, screen)