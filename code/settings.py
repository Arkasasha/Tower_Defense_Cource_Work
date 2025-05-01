import pygame
import random
from pytmx.util_pygame import load_pygame
from os.path import join 
from os import walk

WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 640 
TILE_SIZE = 32

def singleton(cls):
    instances = {}

    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return get_instance