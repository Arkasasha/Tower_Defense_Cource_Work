from settings import *

class TowerHitbox(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        self.image = 0

class Tower(pygame.sprite.Sprite):
    def __init__(self, surf, groups):
        super().__init__(groups)
        # Get an image and a rect
        self.image = surf
        self.rect = self.image.get_frect(center = pygame.Vector2(pygame.mouse.get_pos()))
        self.placed = False

    def place_tower(self):
        if not self.placed:
            x_count = pygame.Vector2(pygame.mouse.get_pos()).x / TILE_SIZE
            y_count = pygame.Vector2(pygame.mouse.get_pos()).y / TILE_SIZE
            new_x = int(x_count) * TILE_SIZE if x_count % 1 <= 0.5 else (int(x_count) + 1) * TILE_SIZE
            new_y = int(y_count) * TILE_SIZE if y_count % 1 <= 0.5 else (int(y_count) + 1) * TILE_SIZE
            self.rect.center = (new_x, new_y)

    def update(self, dt):
        self.place_tower()


class Cannon(Tower):
    pass