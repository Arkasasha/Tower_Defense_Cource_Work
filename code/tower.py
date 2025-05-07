from settings import *
from groups import LevelSprites
from math import atan2, degrees


class TowerRange(pygame.sprite.Sprite):
    def __init__(self, surf, pos, tower, groups):
        super().__init__(groups)
        self.image = surf
        width, height = self.image.get_size()
        self.image = pygame.transform.scale(self.image, (width * 2, height * 2))
        self.rect = self.image.get_frect(center = pos)
        self.mask = pygame.mask.from_surface(self.image)
        # self.image = self.mask.to_surface()
        self.tower = tower
        self.istower_range = True
        self.hasToBeShown = True
    
    def update_pos(self):
        self.rect.center = self.tower.get_pos().center

    def update(self, dt):
        self.update_pos()

class TowerHitbox(pygame.sprite.Sprite):
    def __init__(self, tower, groups):
        super().__init__(groups)
        self.istower_hitbox = True
        self.tower = tower

        pos = pygame.Vector2(pygame.mouse.get_pos())
        self.rect = pygame.Rect(pos.x - TILE_SIZE, pos.y - TILE_SIZE, TILE_SIZE, TILE_SIZE)
        self.color = (240, 240, 240)
        self.image = pygame.Surface((self.rect.width, self.rect.height))
        self.image.fill(self.color)
        self.image.set_alpha(140)
        self.hasToBeShown = True

    
    def update_pos(self):
        self.rect.center = self.tower.get_pos().center

    def draw(self):
        pygame.draw.rect(self.surface, self.color, self.rect)
    
    def update(self, dt):
        self.update_pos()

class TowerHead(pygame.sprite.Sprite):
    def __init__(self, surf, pos, tower, groups):
        super().__init__(groups)
        self.original_image = surf
        self.image = surf
        self.rect = self.image.get_frect(center = pos)

        self.tower = tower
        self.istower_head = True
        
        self.direction = pygame.Vector2()

    def get_direction(self):
        mouse_pos = pygame.Vector2(pygame.mouse.get_pos())
        new_direction = mouse_pos - pygame.Vector2(self.rect.center)
        self.direction = new_direction.normalize() if new_direction.length() != 0 else self.direction

    def rotate(self):
        angle = degrees(atan2(self.direction.x, self.direction.y)) + 90
        if self.direction.x > 0:
            self.image = pygame.transform.rotozoom(self.original_image, -angle, 1)
            self.image = pygame.transform.flip(self.image, False, True)
        else:
            self.image = pygame.transform.rotozoom(self.original_image, angle, 1)
        self.rect = self.image.get_frect(center = self.tower.get_head_pos())

    def update_pos(self):
        self.rect.center = self.tower.get_head_pos()

    def update(self, dt):
        self.get_direction()
        if self.tower.get_state():
            self.rotate()
        else:
            self.update_pos()

class TowerBottom(pygame.sprite.Sprite):
    def __init__(self, surf, grid, groups):
        super().__init__(groups)
        # status
        self.grid = grid
        self.placed = False
        
        # Get an image and a rect
        self.image = surf
        width, height = self.image.get_size()
        self.image = pygame.transform.scale(self.image, (width / 2, height / 2))
        self.rect = self.image.get_frect(center = pygame.Vector2(pygame.mouse.get_pos()))

        self.istower = True

        self.tower_head_offset_x = 0
        self.tower_head_offset_y = 10

    def set_hitbox(self, hitbox):
        self.tower_hitbox = hitbox

    def get_state(self):
        return self.placed

    def get_head_pos(self):
        return (self.rect.midtop[0] + self.tower_head_offset_x,
                 self.rect.midtop[1] + self.tower_head_offset_y)
    
    def get_pos(self):
        return self.rect

    def check_place(self):
        x = int(self.rect.topleft[0] / TILE_SIZE)
        y = int(self.rect.topleft[1] / TILE_SIZE)
        if not self.grid[y][x]:
            if LevelSprites().check_ground(self.tower_hitbox.rect):
                return True
        return False

    def reserve_place(self):
        self.placed = True
        x = int(self.rect.topleft[0] / TILE_SIZE)
        y = int(self.rect.topleft[1] / TILE_SIZE)
        self.grid[y][x] = True

    def place_tower(self):
        x_count = pygame.Vector2(pygame.mouse.get_pos()).x / TILE_SIZE
        y_count = pygame.Vector2(pygame.mouse.get_pos()).y / TILE_SIZE
        new_x = int(x_count) * TILE_SIZE - LevelSprites().offset
        new_y = int(y_count) * TILE_SIZE - LevelSprites().offset
        self.rect.topleft = (new_x, new_y)
        if pygame.mouse.get_just_pressed()[0]:
            if self.check_place():
                self.reserve_place()
                    
    def update(self, dt):
        if not self.placed:
            self.place_tower()