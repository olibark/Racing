import os

car_stats = {
    "red": {"move_rate_x": 8, "acceleration": 0.5, "move_rate_y": 5, "braking": 0.2, "max_reverse": 5},
    "blue": {"move_rate_x": 4, "acceleration": 3, "move_rate_y": 12},
    "green": {"move_rate_x": 6, "acceleration": 1, "move_rate_y": 8}
}

FRICTION = 0.2

running = True

CLEAR = 'cls' if os.name == 'nt' else 'clear'

BACKGROUND = (0, 0, 0)

HEIGHT = int(os.getenv('HEIGHT', default=1080))
WIDTH = int(os.getenv('WIDTH', default=1920))

HORIZON_Y = int(HEIGHT * 0.5)
ROAD_COLOUR = (50, 50, 50)
CENTERLINE_COLOUR = (200, 200, 200)

FPS = 60

PLAYER_SCALE = 0.5

player_start = [HEIGHT * 0.9, WIDTH // 2]

playerImage = None