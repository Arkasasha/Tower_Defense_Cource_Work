from settings import *
from tower import TowerBottom, TowerHead, TowerRange, TowerHitbox
from groups import EnemySprites

class Tower(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)

        self.enemyTracked = None

    def func():
        
        
        return False

    @staticmethod
    def get_enemies_in_range(mask):
        enemie_sprites = [sprite for sprite in EnemySprites()]
        collisions = []
        for sprite in enemie_sprites:
            x, y = sprite.rect.midbottom
            if 0 <= x < mask.get_size()[0] and 0 <= y < mask.get_size()[1]:
                if mask.get_at((x, y)) == 1:
                    collisions.append(sprite)
        return collisions

    def wait_for_enemy(self):
        detected_enemies = self.get_enemies_in_range(self.tower_range.mask)
        if detected_enemies:
            furthest_enemy = detected_enemies[0]
            for enemy in detected_enemies:
                if enemy.traveled_distance == max(enemy.traveled_distance, 
                                                furthest_enemy.traveled_distance):
                    furthest_enemy = enemy
            self.enemyTracked = furthest_enemy
    
    def track_an_enemy(self):
        print(self.enemyTracked)
        # pass

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
        tower_range_surf = pygame.image.load(join('Game', 'Assets', 'additional', 'radius', 'B.png')).convert_alpha()
        tower_hitbox_surf = pygame.image.load(join('Game', 'Assets', 'additional', 'Radius3', '0.png')).convert_alpha()

        self.tower_base = TowerBottom(tower_base_surf, grid, groups[0])
        self.tower_head = TowerHead(tower_head_surf, self.tower_base.rect.midtop, self.tower_base, groups[0])
        self.tower_range = TowerRange(tower_range_surf, self.tower_base.rect.center, self.tower_base, groups[0])
        self.tower_hitbox = TowerHitbox(self.tower_base, groups[0])

        self.tower_base.set_hitbox(self.tower_hitbox)