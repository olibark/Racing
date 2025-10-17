import os


carTypes = {
            "red": {"turnRate": 5, "acceleration": 1, "maxSpeed": 5, "braking": 8, "maxReverse": 5},
            "blue": {"turnRate": 4, "acceleration": 3, "maxSpeed": 12},
            "green": {"turnRate": 6, "acceleration": 1, "maxSpeed": 8}
        }

friction = 0.26

running = True

clear = 'cls' if os.name == 'nt' else 'clear'

BACKGROUND = (0, 0, 0)

HEIGHT = 1080
WIDTH = 1920
ROAD_HEIGHT = -300

FPS = 60

PLAYER_SCALE = 0.5

playerCoords = [WIDTH // 2, -HEIGHT]

playerImage = None
backgroundImg = None 