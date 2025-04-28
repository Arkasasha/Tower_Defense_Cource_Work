from settings import *

class TowerHitbox(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        self.image = 0

class Tower(pygame.sprite.Sprite):
    def __init__(self, surf, grid, groups):
        super().__init__(groups)
        self.grid = grid
        
        # Get an image and a rect
        self.image = surf
        self.rect = self.image.get_frect(center = pygame.Vector2(pygame.mouse.get_pos()))

        self.placed = False

    def check_place(self):
        x = int(self.rect.centerx / TILE_SIZE)
        y = int(self.rect.centery / TILE_SIZE)
        tiles = [self.grid[y][x], self.grid[y][x-1], self.grid[y-1][x], self.grid[y-1][x-1]]
        if all(not tile for tile in tiles):
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
        if not self.placed:
            x_count = pygame.Vector2(pygame.mouse.get_pos()).x / TILE_SIZE
            y_count = pygame.Vector2(pygame.mouse.get_pos()).y / TILE_SIZE
            new_x = int(x_count) * TILE_SIZE if x_count % 1 <= 0.5 else (int(x_count) + 1) * TILE_SIZE
            new_y = int(y_count) * TILE_SIZE if y_count % 1 <= 0.5 else (int(y_count) + 1) * TILE_SIZE
            self.rect.center = (new_x, new_y)
            if pygame.mouse.get_just_pressed()[0]:
                if self.check_place():
                    self.reserve_place()
                    
    def update(self, dt):
        self.place_tower()