import init, loop, constants

(screen, clock, player) = init.Init()

while constants.running:
    clock.tick(constants.FPS)
    loop.main_loop(player, screen)