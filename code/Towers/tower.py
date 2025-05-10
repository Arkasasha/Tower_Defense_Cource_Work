from settings import *
from Towers.tower_parts import TowerBottom, TowerHead, TowerRange, TowerHitbox
from groups import LevelSprites, EnemySprites
from Towers.tower_projectile_types import CannonProjectile
from enemy import Enemy

class Tower(pygame.sprite.Sprite):
    def __init__(self, groups, grid, tower_base_surf, tower_head_surf, tower_range_surf, tower_range_mask, tower_hitbox_surf):
        super().__init__(groups[1])    # passes TowerSprites group
        self._setup(groups, grid, tower_base_surf, tower_head_surf, tower_range_surf, tower_range_mask, tower_hitbox_surf)
        self._enemyTracked = None

        self._can_shoot = True
        self._projectile_shoot_time = 0
        self._cooldown_time = 300
        self._projectiles = []

        self._proj_id = 0

    def _setup(self, groups, grid, tower_base_surf, tower_head_surf, tower_range_surf, tower_range_mask, tower_hitbox_surf):
        self._tower_base = TowerBottom(tower_base_surf, grid, groups[0])
        self._tower_head = TowerHead(tower_head_surf, self._tower_base.get_rect().midtop, self._tower_base, groups[0])
        self._tower_range = TowerRange(tower_range_surf, tower_range_mask, self._tower_base.get_rect().center, self._tower_base, groups[0])
        self._tower_hitbox = TowerHitbox(tower_hitbox_surf, self._tower_base, groups[0])

        self._tower_base.set_hitbox(self._tower_hitbox)


    @staticmethod
    def check_point_in_mask(x, y, mask):
        if 0 <= x < mask.get_size()[0] and 0 <= y < mask.get_size()[1]:
                if mask.get_at((x, y)) == 1:
                    return True
        return False


    def _get_enemies_in_range(self):
        mask = self._tower_range.get_mask()
        mask_rect = self._tower_range.get_rect()
        enemie_sprites = [sprite for sprite in EnemySprites()]
        collisions = []
        for sprite in enemie_sprites:
            x = sprite.get_rect().midbottom[0] - mask_rect.topleft[0]
            y = sprite.get_rect().midbottom[1] - mask_rect.topleft[1]
            if self.check_point_in_mask(x, y, mask):
                    collisions.append(sprite)
        return collisions

    def _wait_for_enemy(self):
        detected_enemies = self._get_enemies_in_range()
        if detected_enemies:
            furthest_enemy = detected_enemies[0]
            for enemy in detected_enemies:
                if enemy.get_traveled_distance() == max(enemy.get_traveled_distance(), 
                                                furthest_enemy.get_traveled_distance()):
                    furthest_enemy = enemy
            self._enemyTracked = furthest_enemy

    def _check_enemy_still_in_range(self):
        mask = self._tower_range.get_mask()
        mask_rect = self._tower_range.get_rect()
        x = self._enemyTracked.get_rect().midbottom[0] - mask_rect.topleft[0]
        y = self._enemyTracked.get_rect().midbottom[1] - mask_rect.topleft[1]
        if self.check_point_in_mask(x, y, mask):
            return True
        self._enemyTracked = None
        return False

    def _shooting_timer(self):
        if not self._can_shoot:
            current_time = pygame.time.get_ticks()
            if current_time - self._projectile_shoot_time >= self._cooldown_time:
                self._can_shoot = True

    def _shoot_an_enemy(self):
        if self._can_shoot:
            CannonProjectile(self.get_projectile_pos(), self._enemyTracked, LevelSprites())
            self._can_shoot = False
            self._projectile_shoot_time = pygame.time.get_ticks()

    def _track_an_enemy(self):
        if self._check_enemy_still_in_range():
            self._tower_head.set_direction(self._enemyTracked.get_rect().center)

    def update(self, dt):
        if self._tower_base.placed:
            self._tower_range.hasToBeShown = False
            self._tower_hitbox.hasToBeShown = False

            if self._enemyTracked is not None and self._enemyTracked.is_died() == False:
                self._track_an_enemy()
                self._shoot_an_enemy()
            else:
                self._wait_for_enemy()
            
            self._shooting_timer()

