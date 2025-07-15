import pygame
import random
import os
import sys

pygame.init()

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

COLOUR_BLACK = (0, 0, 0)
COLOUR_WHITE = (255, 255, 255)
COLOUR_RED = (255, 0, 0)
COLOUR_GREEN = (0, 255, 0)
COLOUR_BLUE = (0, 0, 255)
COLOUR_YELLOW = (255, 255, 0)
COLOUR_ORANGE=(255, 97, 18)
TABLE = (44, 252, 3)

icon = pygame.image.load(resource_path("images/icon.ico"))
field = pygame.image.load(resource_path("images/field.png"))

gay_ban = [
    pygame.mixer.Sound(resource_path("sounds/1.mp3")),
    pygame.mixer.Sound(resource_path("sounds/2.mp3")),
    pygame.mixer.Sound(resource_path("sounds/3.mp3")),
    pygame.mixer.Sound(resource_path("sounds/4.mp3")),
    pygame.mixer.Sound(resource_path("sounds/5.mp3"))
    ]

hit = pygame.mixer.Sound(resource_path("sounds/ball_hit.mp3"))




p_width = 20
p_height = 100
p_speed = 40

ball_radius = 30
ball_speed = 2

ball_dx = ball_speed
ball_dy = ball_speed
pLeft_score = 0
pRight_score = 0