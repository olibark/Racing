import os, tkinter

FRICTION = 0.2

running = True

CLEAR = 'cls' if os.name == 'nt' else 'clear'

BACKGROUND = (0, 0, 0)

root = tkinter.Tk()
WIDTH = root.winfo_screenwidth()
HEIGHT = root.winfo_screenheight()
CENTRE = WIDTH / 2

HORIZON_Y = int(HEIGHT * 0.5)
ROAD_COLOUR = (50, 50, 50)
CENTRELINE_COLOUR = (200, 200, 200)

FPS = 60

PLAYER_SCALE = 0.5

player_start = None

playerBaseImage = None
playerImage = None
playerBreakingImage = None
backgroundImage = None
