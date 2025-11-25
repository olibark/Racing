import os, tkinter

FRICTION = 0.15

running = True

CLEAR = 'cls' if os.name == 'nt' else 'clear'

BACKGROUND = (29, 69, 133)

root = tkinter.Tk()
WIDTH = root.winfo_screenwidth()
HEIGHT = root.winfo_screenheight()
CENTRE = WIDTH / 2

HEIGHT = 1000
WIDTH = 1000

HORIZON_Y = int(HEIGHT * 0.5)

OUTER_ROAD_COLOUR = (30, 80, 30)
ROAD_COLOUR = (50, 50, 50)
CENTRELINE_COLOUR = (200, 200, 200)

FPS = 60

PLAYER_SCALE = 0.55

player_start = None

playerBaseImage = None
playerImage = None
playerBreakingImage = None
backgroundImage = None
cursorImage = None

cursor_rect = None
