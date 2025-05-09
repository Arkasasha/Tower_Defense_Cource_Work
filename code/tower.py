from settings import *
from groups import LevelSprites
from math import atan2, degrees


class TowerRange(pygame.sprite.Sprite):
    def __init__(self, surf, mask_surf, pos, tower, groups):
        super().__init__(groups)

        self._image = surf
        width, height = self._image.get_size()
        self._image = pygame.transform.scale(self._image, (width * 2, height * 2))
        self._rect = self._image.get_frect(center = pos)

        mask_surf = pygame.transform.scale(mask_surf, (width * 2, height * 2))
        self._mask = pygame.mask.from_surface(mask_surf)

        self._tower = tower
        self.istower_range = True
        self.hasToBeShown = True

    # getters
    def get_image(self):
        return self._image

    def get_rect(self):
        return self._rect

    def get_mask(self):
        return self._mask


    def _update_pos(self):
        self._rect.center = self._tower.get_rect().center

    def update(self, dt):
        self._update_pos()

class TowerHitbox(pygame.sprite.Sprite):
    def __init__(self, surf, tower, groups):
        super().__init__(groups)
        self._tower = tower

        pos = pygame.Vector2(pygame.mouse.get_pos())
        self._image = surf
        width, height = self._image.get_size()
        self._image = pygame.transform.scale(self._image, (width * 2, height * 2))
        self._rect = self._image.get_frect(center = tower.get_rect().center)
        self.istower_hitbox = True
        self.hasToBeShown = True
    
    # getters
    def get_image(self):
        return self._image

    def get_rect(self):
        return self._rect
    

    def _update_pos(self):
        self._rect.center = self._tower.get_rect().center
    
    def update(self, dt):
        self._update_pos()

class TowerHead(pygame.sprite.Sprite):
    def __init__(self, surf, pos, tower, groups):
        super().__init__(groups)
        self._original_image = surf
        self._image = surf
        self._rect = self._image.get_frect(center = pos)

        self._tower = tower
        
        self._direction = pygame.Vector2(-1, 0)

        self.istower_head = True

    # getters
    def get_image(self):
        return self._image

    def get_rect(self):
        return self._rect

    # setters
    def set_direction(self, pos):
        new_direction = pos - pygame.Vector2(self._rect.center)
        self._direction = new_direction.normalize() if new_direction.length() != 0 else self._direction


    def _rotate(self):
        angle = degrees(atan2(self._direction.x, self._direction.y)) + 90
        if self._direction.x > 0:
            self._image = pygame.transform.rotozoom(self._original_image, -angle, 1)
            self._image = pygame.transform.flip(self._image, False, True)
        else:
            self._image = pygame.transform.rotozoom(self._original_image, angle, 1)
        self._rect = self._image.get_frect(center = self._tower.get_head_pos())

    def _update_pos(self):
        self._rect.center = self._tower.get_head_pos()

    def update(self, dt):
        if not self._tower.get_state():
            self._update_pos()
        else:
            self._rotate()

class TowerBottom(pygame.sprite.Sprite):
    def __init__(self, surf, grid, groups):
        super().__init__(groups)
        # status
        self.grid = grid
        self.placed = False
        
        # Get an image and a rect
        self._image = surf
        width, height = self._image.get_size()
        self._image = pygame.transform.scale(self._image, (width / 2, height / 2))
        self._rect = self._image.get_frect(center = pygame.Vector2(pygame.mouse.get_pos()))

        self._tower_head_offset_x = 0
        self._tower_head_offset_y = 10

        self.istower = True

    # getters
    def get_image(self):
        return self._image

    def get_rect(self):
        return self._rect

    def get_state(self):
        return self.placed

    def get_head_pos(self):
        return (self._rect.midtop[0] + self._tower_head_offset_x,
                 self._rect.midtop[1] + self._tower_head_offset_y)

    # setters
    def set_hitbox(self, hitbox):
        self._tower_hitbox = hitbox


    def _check_place(self):
        x = int(self._rect.topleft[0] / TILE_SIZE)
        y = int(self._rect.topleft[1] / TILE_SIZE)
        if not self.grid[y][x]:
            if LevelSprites().check_ground(self._tower_hitbox._rect):
                return True
        return False

    def _reserve_place(self):
        self.placed = True
        x = int(self._rect.topleft[0] / TILE_SIZE)
        y = int(self._rect.topleft[1] / TILE_SIZE)
        self.grid[y][x] = True

    def _place_tower(self):
        x_count = pygame.Vector2(pygame.mouse.get_pos()).x / TILE_SIZE
        y_count = pygame.Vector2(pygame.mouse.get_pos()).y / TILE_SIZE
        new_x = int(x_count) * TILE_SIZE - LevelSprites().get_offset()
        new_y = int(y_count) * TILE_SIZE - LevelSprites().get_offset()
        self._rect.topleft = (new_x, new_y)
        if pygame.mouse.get_just_pressed()[0]:
            if self._check_place():
                self._reserve_place()


    def update(self, dt):
        if not self.placed:
            self._place_tower()