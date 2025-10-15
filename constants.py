import os

playerCoords = [0, 0]

carTypes = {
            "red": {"turnRate": 5, "acceleration": 2, "maxSpeed": 10},
            "blue": {"turnRate": 4, "acceleration": 3, "maxSpeed": 12},
            "green": {"turnRate": 6, "acceleration": 1, "maxSpeed": 8}
        }

running = True

clear = 'cls' if os.name == 'nt' else 'clear'

BACKGROUND = (0, 0, 0)

HEIGHT = 800
WIDTH = 800

FPS = 60

playerImage = None