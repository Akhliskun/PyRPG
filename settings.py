# Game options / settings

# Define basic colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
DARKGREY = (40, 40, 40)
LIGHTGREY = (100, 100, 100)
YELLOW = (255, 255, 0)
LIGHTBLUE = (0, 155, 155)

# Basic window config
WIDTH = 600
HEIGHT = 768
FPS = 60
TITLE = "My Game"
BGCOLOR = LIGHTBLUE
FONT_NAME = 'arial'
HS_FILE = "highscore.txt"
SPRITESHEET = "spritesheet_jumper.png"

TILESIZE = 32
GRIDWIDTH = WIDTH / TILESIZE
GRIDHEIGHT = HEIGHT / TILESIZE

# Player proprieties
PLAYER_ACC = 0.5
PLAYER_FRICTION = -0.12
PLAYER_GRAVITY = 0.8
PLAYER_JUMPPOWER = 22

# Game proprieties
BOOST_POWER = 60
POWER_SPAWN_RATE = 7
MOB_FRAQ = 5000
PLAYER_LAYER = 2
MOB_LAYER = 2
PLATFORM_LAYER = 1
POWER_LAYER = 1
CLOUD_LAYER = 0

# Starting Platforms
PLATFORM_LIST = [(0, HEIGHT - 60),
                 (WIDTH / 2 - 150, HEIGHT * 3 / 4),
                 (125, HEIGHT - 250),
                 (350, 300),
                 (175, 200),
                 (375, 50)]
