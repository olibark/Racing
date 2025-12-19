import os, pygame, sys, constants as c, player as pl

def playerInit() -> object:
    rect = c.playerImage.get_rect()
    c.player_start = [(c.WIDTH // 2) - (rect.width // 2), c.HEIGHT- rect.height]
    player = pl.Player(c.player_start[0], c.player_start[1], "red")
    
    return player

def load_image(target: str, folder: str):
    target_image_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "img", str(folder), str(target)
    )
    return pygame.image.load(target_image_path).convert_alpha()

def imageTransform(target: str, scaled: bool, player: bool, scale: float, folder: str):
    base_image = load_image(target, folder)

    if not scaled:
        return base_image.copy()

    if scale is None:
        scale = c.PLAYER_SCALE if player else 1

    width, height = base_image.get_size()
    new_size = (int(width * scale), int(height * scale))

    return pygame.transform.smoothscale(base_image, new_size)

def pygameInit():
    pygame.init()
    
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((c.WIDTH, c.HEIGHT))
    
    return screen, clock

def imageAlloc():
    c.playerBaseImage = imageTransform(target="red_car.png",    scaled=False, player=True,  scale=None, folder="cars")
    c.playerImage =     imageTransform(target="red_car.png",    scaled=True,  player=True,  scale=None, folder="cars")
    c.backgroundImage = imageTransform(target="background.png", scaled=False, player=False, scale=None, folder="backgrounds")
    c.cursorImage =     imageTransform(target="cursor.png",     scaled=False, player=False, scale=None, folder="cursors")

def Init():
    os.system(c.CLEAR)
    screen, clock = pygameInit()
    imageAlloc()
    player = playerInit()
    mouseInit()
    
    return screen, clock, player

def mouseInit():
    pygame.mouse.set_visible(False)
    c.cursor_rect = c.cursorImage.get_rect()