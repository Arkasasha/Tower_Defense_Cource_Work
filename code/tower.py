from settings import *
from groups import LevelSprites

class TowerRange(pygame.sprite.Sprite):
    def __init__(self, surf, pos, groups):
        super().__init__(groups)
        self.image = surf
        width, height = self.image.get_size()
        self.image = pygame.transform.scale(self.image, (width * 2, height * 2))
        self.rect = self.image.get_frect(center = pos)
        self.istower_range = True

class TowerHitbox(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        self.istower_hitbox = True

        pos = pygame.Vector2(pygame.mouse.get_pos())
        self.rect = pygame.Rect(pos.x - TILE_SIZE, pos.y - TILE_SIZE, TILE_SIZE, TILE_SIZE)
        self.color = (240, 240, 240)
        self.image = pygame.Surface((self.rect.width, self.rect.height))
        self.image.fill(self.color)
        self.image.set_alpha(140)

    
    def update_pos(self, pos):
        self.rect.center = pos

    def draw(self):
        pygame.draw.rect(self.surface, self.color, self.rect)

class TowerHead(pygame.sprite.Sprite):
    def __init__(self, surf, pos, groups):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_frect(center = pos)
        self.istower_head = True

class Tower(pygame.sprite.Sprite):
    def __init__(self, grid, groups):
        super().__init__(groups)
        # status
        self.grid = grid
        self.placed = False
        
        # Get an image and a rect
        self.image = pygame.image.load(join('Game', 'Assets', 'Towers', 'Tower', 'tower.png')).convert_alpha()
        width, height = self.image.get_size()
        self.image = pygame.transform.scale(self.image, (width / 2, height / 2))
        self.rect = self.image.get_frect(center = pygame.Vector2(pygame.mouse.get_pos()))

        # hitbox
        self.tower_hitbox = TowerHitbox(groups[0])
        self.istower = True

        range_surf = pygame.image.load(join('Game', 'Assets', 'additional', 'radius', 'B.png')).convert_alpha()
        self.range = TowerRange(range_surf, self.rect.center, groups)
        tower_head = pygame.image.load(join('Game', 'Assets', 'Towers', 'cannon', '0.png'))
        self.tower_head = TowerHead(tower_head, self.rect.midtop, LevelSprites())
        self.tower_head_offset_x = 0
        self.tower_head_offset_y = 10
        
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

    def update_parts(self):
        self.tower_hitbox.update_pos((self.rect.centerx, self.rect.centery))
        self.range.rect.center = self.rect.center
        self.tower_head.rect.center = (self.rect.midtop[0] + self.tower_head_offset_x,
                                        self.rect.midtop[1] + self.tower_head_offset_y)

    def place_tower(self):
        x_count = pygame.Vector2(pygame.mouse.get_pos()).x / TILE_SIZE
        y_count = pygame.Vector2(pygame.mouse.get_pos()).y / TILE_SIZE
        new_x = int(x_count) * TILE_SIZE - LevelSprites().offset
        new_y = int(y_count) * TILE_SIZE - LevelSprites().offset
        self.rect.topleft = (new_x, new_y)
        self.update_parts()
        if pygame.mouse.get_just_pressed()[0]:
            if self.check_place():
                self.reserve_place()
                self.tower_hitbox.kill()
                self.range.kill()
                    
    def update(self, dt):
        if not self.placed:
            self.place_tower()