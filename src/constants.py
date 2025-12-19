import os, tkinter

CLEAR = 'cls' if os.name == 'nt' else 'clear'

FRICTION = 0.15

running = True

root = tkinter.Tk()
WIDTH = root.winfo_screenwidth()
HEIGHT = root.winfo_screenheight()
CENTRE = WIDTH / 2

HORIZON_Y = int(HEIGHT * 0.5)

BACKGROUND = (20, 50, 100)
OUTER_ROAD_COLOUR = (10, 30, 10)
ROAD_COLOUR = (50, 50, 50)
CENTRELINE_COLOUR = (140, 140, 140)

FPS = 60

PLAYER_SCALE = 0.55

player_start = None

playerBaseImage = None
playerImage = None
playerBreakingImage = None
backgroundImage = None
cursorImage = None

cursor_rect = None