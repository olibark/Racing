import os
from functools import lru_cache

import pygame

import constants as c
import player as pl


@lru_cache(maxsize=None)
def _load_image(target: str) -> pygame.Surface:
    target_image_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "img", "cars", str(target)
    )
    return pygame.image.load(target_image_path).convert_alpha()


def imageInit(target, scaled, player, scale):
    """Load an image, optionally scaling it while keeping the aspect ratio."""

    base_image = _load_image(target)

    if not scaled:
        return base_image.copy()

    if scale is None:
        scale = c.PLAYER_SCALE if player else 1

    width, height = base_image.get_size()
    new_size = (int(width * scale), int(height * scale))

    return pygame.transform.smoothscale(base_image, new_size)

def Init():
    os.system(c.CLEAR)
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((c.WIDTH, c.HEIGHT))
    
    c.playerBaseImage = imageInit("red_car.png", False, True, None)
    c.playerImage = imageInit("red_car.png", True, True, None)
    c.playerBreakingImage = imageInit("red_car.breaking.png", True, True, None)
    rect = c.playerImage.get_rect()
    c.player_start = [(c.WIDTH // 2) - (rect.width // 2), c.HEIGHT- rect.height]
    
    player = pl.Player(c.player_start[0], c.player_start[1], "red")
    
    background_img_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'img', 'backgrounds', 'roadMoantains.png')
    temp_backgroundImg = pygame.image.load(background_img_path).convert()
    
    backgroundImg = pygame.transform.smoothscale(temp_backgroundImg, (c.WIDTH, c.HEIGHT))
    
    return screen, clock, player, backgroundImg    