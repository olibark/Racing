import os

playerCoords = [0, 200]

carTypes = {
            "red": {"turnRate": 5, "acceleration": 2, "maxSpeed": 6, "braking": 8, "maxReverse": 5},
            "blue": {"turnRate": 4, "acceleration": 3, "maxSpeed": 12},
            "green": {"turnRate": 6, "acceleration": 1, "maxSpeed": 8}
        }

friction = 0.1

running = True

clear = 'cls' if os.name == 'nt' else 'clear'

BACKGROUND = (0, 0, 0)

HEIGHT = 800
WIDTH = 1000
ROAD_HEIGHT = 400

FPS = 60

PLAYER_SCALE = 0.5

playerImage = None
backgroundImg = None 