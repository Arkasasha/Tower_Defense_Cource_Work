from settings import *
from tower import TowerBottom, TowerHead, TowerRange, TowerHitbox
from groups import LevelSprites

class Tower(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)

        self.enemyTracked = None

    def track_an_enemy(self):
        pass

    def check_enemy_in_range(self):
        pass

    def update(self, dt):
        if self.tower_base.placed:
            self.tower_range.hasToBeShown = False
            self.tower_hitbox.hasToBeShown = False

        if self.enemyTracked is not None:
            self.track_an_enemy()
        else:
            self.check_enemy_in_range()


class Cannon(Tower):
    def __init__(self, grid, groups):
        super().__init__(groups[1])
        tower_base_surf = pygame.image.load(join('Game', 'Assets', 'Towers', 'bottom_tower', 'tower.png')).convert_alpha()
        tower_head_surf = pygame.image.load(join('Game', 'Assets', 'Towers', 'cannon', 'tower', '0.png')).convert_alpha()
        tower_range_surf = pygame.image.load(join('Game', 'Assets', 'additional', 'radius', 'B.png')).convert_alpha()

        self.tower_base = TowerBottom(tower_base_surf, grid, groups[0])
        self.tower_head = TowerHead(tower_head_surf, self.tower_base.rect.midtop, self.tower_base, groups[0])
        self.tower_range = TowerRange(tower_range_surf, self.tower_base.rect.center, self.tower_base, groups[0])
        self.tower_hitbox = TowerHitbox(self.tower_base, groups[0])

        self.tower_base.set_hitbox(self.tower_hitbox)
        # print(self.tower_base, self.tower_head)