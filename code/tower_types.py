from settings import *
from tower import Tower, TowerHead, TowerRange, TowerHitbox
from groups import LevelSprites

class TowerType(pygame.sprite.Sprite):
    def update(self, dt):
        if self.tower_base.placed:
            self.tower_range.kill()
            self.tower_hitbox.kill()

class Cannon(TowerType):
    def __init__(self, grid, groups):
        super().__init__(groups[1])
        tower_base_surf = pygame.image.load(join('Game', 'Assets', 'Towers', 'Tower', 'tower.png')).convert_alpha()
        tower_head_surf = pygame.image.load(join('Game', 'Assets', 'Towers', 'Cannon', '0.png')).convert_alpha()
        tower_range_surf = pygame.image.load(join('Game', 'Assets', 'additional', 'radius', 'B.png')).convert_alpha()

        self.tower_base = Tower(tower_base_surf, grid, groups[0])
        self.tower_head = TowerHead(tower_head_surf, self.tower_base.rect.midtop, self.tower_base, groups[0])
        self.tower_range = TowerRange(tower_range_surf, self.tower_base.rect.center, self.tower_base, groups[0])
        self.tower_hitbox = TowerHitbox(self.tower_base, groups[0])

        self.tower_base.set_hitbox(self.tower_hitbox)
        # print(self.tower_base, self.tower_head)