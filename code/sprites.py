from settings import *

class Terrain(pygame.sprite.Sprite):
    def __init__(self, surf, pos, ground, groups):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_frect(topleft = pos)
        self.ground = ground