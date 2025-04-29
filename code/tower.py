from settings import *
from groups import LevelSprites

class TowerRange(pygame.sprite.Sprite):
    def __init__(self, surf, pos, groups):
        super().__init__(groups)
        self.image = surf
        width, height = self.image.get_size()
        self.image = pygame.transform.scale(self.image, (width * 2, height * 2))
        self.rect = self.image.get_frect(center = pos)
        self.isrange = True

class TowerHitbox(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        self.hitbox = True

        pos = pygame.Vector2(pygame.mouse.get_pos())
        self.rect = pygame.Rect(pos.x - TILE_SIZE, pos.y - TILE_SIZE, TILE_SIZE * 2, TILE_SIZE * 2)
        self.color = (240, 240, 240)
        self.image = pygame.Surface((self.rect.width, self.rect.height))
        self.image.fill(self.color)
        self.image.set_alpha(140)

    
    def update_pos(self, pos):
        self.rect.center = pos

    def draw(self):
        pygame.draw.rect(self.surface, self.color, self.rect)

class Tower(pygame.sprite.Sprite):
    def __init__(self, grid, groups):
        super().__init__(groups)
        # status
        self.grid = grid
        self.placed = False
        
        # Get an image and a rect
        self.image = pygame.image.load(join('Game', 'Assets', 'Towers', 'Tower', 'tower.png')).convert_alpha()
        # width, height = self.image.get_size()
        # self.image = pygame.transform.scale(self.image, (width / 2, height / 2))
        self.rect = self.image.get_frect(center = pygame.Vector2(pygame.mouse.get_pos()))

        # hitbox
        self.tower_hitbox = TowerHitbox(groups[0])
        self.tower = True

        range_surf = pygame.image.load(join('Game', 'Assets', 'additional', 'radius', f'A.png')).convert_alpha()
        self.range = TowerRange(range_surf, self.rect.center, groups)
        

    def check_place(self):
        x = int(self.rect.centerx / TILE_SIZE)
        y = int(self.rect.centery / TILE_SIZE)
        tiles = [self.grid[y][x], self.grid[y][x-1], self.grid[y-1][x], self.grid[y-1][x-1]]
        if all(not tile for tile in tiles):
            if LevelSprites().check_ground(self.tower_hitbox.rect):
                return True
        return False

    def reserve_place(self):
        self.placed = True
        x = int(self.rect.centerx / TILE_SIZE)
        y = int(self.rect.centery / TILE_SIZE)
        self.grid[y][x] = True
        self.grid[y-1][x] = True
        self.grid[y][x-1] = True
        self.grid[y-1][x-1] = True

    def place_tower(self):
        x_count = pygame.Vector2(pygame.mouse.get_pos()).x / TILE_SIZE
        y_count = pygame.Vector2(pygame.mouse.get_pos()).y / TILE_SIZE
        new_x = int(x_count) * TILE_SIZE if x_count % 1 <= 0.5 else (int(x_count) + 1) * TILE_SIZE
        new_y = int(y_count) * TILE_SIZE if y_count % 1 <= 0.5 else (int(y_count) + 1) * TILE_SIZE
        self.rect.center = (new_x, new_y)
        self.tower_hitbox.update_pos((self.rect.centerx, self.rect.centery))
        self.range.rect.center = self.rect.center
        if pygame.mouse.get_just_pressed()[0]:
            if self.check_place():
                self.reserve_place()
                self.tower_hitbox.kill()
                self.range.kill()
                    
    def update(self, dt):
        if not self.placed:
            self.place_tower()