import random

BLUE = (255, 0, 0)
GREEN = (0, 255, 0)
RED = (0, 0, 255)

GRASS_LOWER = (27, 50, 0)
GRASS_UPPER = (70, 255, 255)

def randomColor():
    r = random.randrange(0, 256)
    g = random.randrange(0, 256)
    b = random.randrange(0, 256)
    color = (r, g, b)
    return color
