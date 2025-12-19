import os #, tkinter

CLEAR = 'cls' if os.name == 'nt' else 'clear'

FRICTION = 0.15

running = True

#root = tkinter.Tk()
#WIDTH = root.winfo_screenwidth()
#HEIGHT = root.winfo_screenheight()

WIDTH = 1920
HEIGHT = 1080

CENTRE = WIDTH / 2

HORIZON_Y = int(HEIGHT * 0.5)

BACKGROUND = (20, 50, 100)
OUTER_ROAD_COLOUR = (94, 140, 27)
ROAD_COLOUR = (75, 75, 75)
CENTRELINE_COLOUR = (140, 140, 140)
SUN_COLOUR_BACK = (255, 29, 0)
SUN_COLOUR_MIDDLE = (255, 85, 0)
SUN_COLOUR_FRONT = (255, 144, 0)


FPS = 60

PLAYER_SCALE = 0.55

player_start = None

playerBaseImage = None
playerImage = None
playerBreakingImage = None
backgroundImage = None
cursorImage = None

cursor_rect = None