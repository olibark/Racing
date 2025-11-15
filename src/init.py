import os, pygame
import constants as c
import player as pl

def playerInit():
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
    c.playerBaseImage = imageTransform("red_car.png", False, True, None, "cars")
    c.playerImage = imageTransform("red_car.png", True, True, None, "cars")
    c.playerBreakingImage = imageTransform("red_car.breaking.png", True, True, None, "cars")
    c.backgroundImage = imageTransform("background.png", False, False, None, "backgrounds")
    
def Init():
    os.system(c.CLEAR)
    screen, clock = pygameInit()
    imageAlloc()
    player = playerInit()
    
    return screen, clock, player