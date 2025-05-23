from settings import *
from Towers.tower_parts import TowerBottom, TowerHead, TowerRange, TowerHitbox
from groups import LevelSprites, EnemySprites
from Towers.tower_projectile_types import CannonProjectile

class Tower(pygame.sprite.Sprite):
    def __init__(self, groups, grid, tower_base_surf, tower_head_surf, tower_range_surf, tower_range_mask, tower_hitbox_surf, type2x2 = False):
        super().__init__(groups[1])    # passes TowerSprites group
        self._setup(groups, grid, tower_base_surf, tower_head_surf, tower_range_surf, tower_range_mask, tower_hitbox_surf, type2x2)
        self._enemyTracked = None

        self._can_shoot = True
        self._projectile_shoot_time = 0
        self._projectiles = []

        self._proj_id = 0

    def _set_stats(self, stats_path):
        with open(stats_path, "r") as file:
            for line in file:
                parts = line.strip().split(":")
                if len(parts) == 2:
                    if parts[0] == 'radius':
                        self._range = parts[1].lstrip()
                    elif parts[0] == 'damage':
                        if parts[1].lstrip()[-1] == '%':
                            self._damage = parts[1].lstrip()
                        else:
                            self._damage = int(parts[1].lstrip())
                    elif parts[0] == 'abilities':
                        if parts[1] == None:
                            self._abilities = None
                        else:
                            self._abilities = parts[1].lstrip()
                    elif parts[0] == 'splash':
                        self._splash = parts[1].lstrip()
                    elif parts[0] == 'speed':
                        self._cooldown_time = int(parts[1].lstrip())
                    elif parts[0] == 'hitbox':
                        self._hitbox_size = parts[1].lstrip()
                    elif parts[0] == 'projectile_speed':
                        self._projectile_speed = int(parts[1].lstrip())
                    

    def _setup(self, groups, grid, tower_base_surf, tower_head_surf, tower_range_surf, tower_range_mask, tower_hitbox_surf, type2x2):
        self._tower_base = TowerBottom(tower_base_surf, grid, groups[0])
        self._tower_head = TowerHead(tower_head_surf, self._tower_base.get_rect().midtop, self._tower_base, groups[0])
        self._tower_range = TowerRange(tower_range_surf, tower_range_mask, self._tower_base.get_rect().center, self._tower_base, groups[0])
        self._tower_hitbox = TowerHitbox(tower_hitbox_surf, self._tower_base, groups[0], type2x2)

        self._tower_base.set_hitbox(self._tower_hitbox)
    
    # deleter
    def delete_tower(self):
        self._tower_base.delete_object()
        self._tower_head.delete_object()
        self._tower_range.delete_object()
        self._tower_hitbox.delete_object()
        self.kill()
        del self

    # getters
    def get_placement_state(self):
        return self._tower_base.get_state()

    @staticmethod
    def check_point_in_mask(x, y, mask):
        if 0 <= x < mask.get_size()[0] and 0 <= y < mask.get_size()[1]:
                if mask.get_at((x, y)) == 1:
                    return True
        return False

    def get_projectile_pos(self):
        pos = self._tower_head.get_rect().center
        if self._tower_head.get_direction().x >= 0:
            angle_1 = self._tower_head.get_direction().angle_to(pygame.math.Vector2(0, 1))
            upd_offset_dir = pygame.math.Vector2((self._projectile_offset_direction.x * -1, self._projectile_offset_direction.y))
            angle_2 = upd_offset_dir.angle_to(pygame.math.Vector2(0, 1))
            rotation_angle = 360 - (angle_1 - angle_2)
            rotation_angle = 360 - rotation_angle if rotation_angle < 0 else rotation_angle
            project_direct = pygame.math.Vector2(1, 0).rotate(rotation_angle)
            pos += self._projectile_offset_distance * project_direct
            return pos
        else:
            angle_1 = self._tower_head.get_direction().angle_to(pygame.math.Vector2(0, 1))
            angle_2 = self._projectile_offset_direction.angle_to(pygame.math.Vector2(-1, 0))
            angle_1 = -(360 - angle_1) if angle_1 > 0 else angle_1
            angle_2 = -angle_2 if angle_2 > 0 else angle_2
            rotation_angle = -(angle_1 + angle_2)
            project_direct = pygame.math.Vector2(0, 1).rotate(rotation_angle)
            pos += self._projectile_offset_distance * project_direct
            return pos

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
        if not self._enemyTracked.is_died():
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
            self._create_projectile()
            self._can_shoot = False
            self._projectile_shoot_time = pygame.time.get_ticks()

    def _track_an_enemy(self):
        self._tower_head.set_direction(self._enemyTracked.get_rect().center)

    def update(self, dt):
        if self._tower_base.get_state():
            self._tower_range.hasToBeShown = False
            self._tower_hitbox.hasToBeShown = False

            if self._enemyTracked is not None:
                if self._check_enemy_still_in_range():
                    self._track_an_enemy()
                    self._shoot_an_enemy()
            else:
                self._wait_for_enemy()
            
            self._shooting_timer()

