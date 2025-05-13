import pygame
import random
from pytmx.util_pygame import load_pygame
from os.path import join 
from os import walk
import math

pygame.init()
info = pygame.display.Info()
SCREEN_WIDTH, SCREEN_HEIGHT = info.current_w, info.current_h
LEVEL_SCREEN_WIDTH, LEVEL_SCREEN_HEIGHT = 1280, 640
WINDOW_WIDTH, WINDOW_HEIGHT = 1650, 800
SCREEN_WINDOW_SCALE = (SCREEN_WIDTH / WINDOW_WIDTH, SCREEN_HEIGHT / WINDOW_HEIGHT)
# SCREEN_LEVEL_SCALE = (SCREEN_WIDTH / LEVEL_SCREEN_WIDTH, SCREEN_HEIGHT / LEVEL_SCREEN_HEIGHT)

# WINDOW_WIDTH, WINDOW_HEIGHT = 0, 0

TILE_SIZE = 32

def singleton(cls):
    instances = {}

    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return get_instance

def get_fixed_mouse_pos():
    mouse_pos = pygame.mouse.get_pos()
    fixed_mouse_pos = [mouse_pos[0] / SCREEN_WINDOW_SCALE[0], mouse_pos[1] / SCREEN_WINDOW_SCALE[1]]
    if fixed_mouse_pos[0] > LEVEL_SCREEN_WIDTH - 1:
        fixed_mouse_pos[0] = LEVEL_SCREEN_WIDTH - 1
    if fixed_mouse_pos[1] > LEVEL_SCREEN_HEIGHT - 1:
        fixed_mouse_pos[1] = LEVEL_SCREEN_HEIGHT - 1
    return fixed_mouse_pos