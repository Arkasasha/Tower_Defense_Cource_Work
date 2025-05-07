from settings import *
from tower import TowerBottom, TowerHead, TowerRange, TowerHitbox
from groups import EnemySprites

class Tower(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)

        self.enemyTracked = None

    @staticmethod
    def check_point_in_mask(x, y, mask):
        if 0 <= x < mask.get_size()[0] and 0 <= y < mask.get_size()[1]:
                if mask.get_at((x, y)) == 1:
                    return True
        return False

    def get_enemies_in_range(self):
        mask = self.tower_range.mask
        mask_rect = self.tower_range.rect
        enemie_sprites = [sprite for sprite in EnemySprites()]
        collisions = []
        for sprite in enemie_sprites:
            x = sprite.rect.midbottom[0] - mask_rect.topleft[0]
            y = sprite.rect.midbottom[1] - mask_rect.topleft[1]
            if self.check_point_in_mask(x, y, mask):
                    collisions.append(sprite)
        return collisions

    def wait_for_enemy(self):
        detected_enemies = self.get_enemies_in_range()
        if detected_enemies:
            furthest_enemy = detected_enemies[0]
            for enemy in detected_enemies:
                if enemy.traveled_distance == max(enemy.traveled_distance, 
                                                furthest_enemy.traveled_distance):
                    furthest_enemy = enemy
            self.enemyTracked = furthest_enemy

    def check_enemy_still_in_range(self):
        mask = self.tower_range.mask
        mask_rect = self.tower_range.rect
        x = self.enemyTracked.rect.midbottom[0] - mask_rect.topleft[0]
        y = self.enemyTracked.rect.midbottom[1] - mask_rect.topleft[1]
        if self.check_point_in_mask(x, y, mask):
            return True
        self.enemyTracked = None
        return False

    def track_an_enemy(self):
        if self.check_enemy_still_in_range():
            self.tower_head.set_direction(self.enemyTracked.rect.center)

    def update(self, dt):
        if self.tower_base.placed:
            self.tower_range.hasToBeShown = False
            self.tower_hitbox.hasToBeShown = False

            if self.enemyTracked is not None:
                self.track_an_enemy()
            else:
                self.wait_for_enemy()


class Cannon(Tower):
    def __init__(self, grid, groups):
        super().__init__(groups[1])
        tower_base_surf = pygame.image.load(join('Game', 'Assets', 'Towers', 'bottom_tower', 'tower.png')).convert_alpha()
        tower_head_surf = pygame.image.load(join('Game', 'Assets', 'Towers', 'cannon', 'tower', '0.png')).convert_alpha()
        tower_range_surf = pygame.image.load(join('Game', 'Assets', 'additional', 'radius', 'B', 'surface.png')).convert_alpha()
        tower_range_mask = pygame.image.load(join('Game', 'Assets', 'additional', 'radius', 'B', 'mask.png')).convert_alpha()
        tower_hitbox_surf = pygame.image.load(join('Game', 'Assets', 'additional', 'Hitbox', '1x1', 'surface.png')).convert_alpha()

        self.tower_base = TowerBottom(tower_base_surf, grid, groups[0])
        self.tower_head = TowerHead(tower_head_surf, self.tower_base.rect.midtop, self.tower_base, groups[0])
        self.tower_range = TowerRange(tower_range_surf, tower_range_mask, self.tower_base.rect.center, self.tower_base, groups[0])
        self.tower_hitbox = TowerHitbox(tower_hitbox_surf, self.tower_base, groups[0])

        self.tower_base.set_hitbox(self.tower_hitbox)