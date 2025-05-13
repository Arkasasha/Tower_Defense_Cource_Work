from settings import *
from math import atan2, degrees
from numpy import sign, pi
from enemy import Enemy
from groups import EnemySprites

class TowerProjectile(pygame.sprite.Sprite):
    def __init__(self, surf, pos, enemy, damage, groups):
        super().__init__(groups)

        self._image = surf
        self._original_image = self._image
        self._rect = self._image.get_frect(center = pos)
        self._mask = pygame.mask.from_surface(self._image)
        
        self._damage = damage
        self._enemy = enemy
        self.isprojectile = True

        self._speed = 150
        self._direction = None
        self._set_direction()
        self._rotate()

    def get_image(self):
        return self._image
    
    def get_rect(self):
        return self._rect

    def _set_direction(self):
        projectile_pos = pygame.Vector2(self._rect.center)
        enemy_pos = pygame.Vector2(self._enemy.get_rect().center)
        self._direction = (enemy_pos - projectile_pos).normalize()

    def _rotate(self):
        angle = degrees(atan2(self._direction.x, self._direction.y)) + 90
        if self._direction.x > 0:
            self._image = pygame.transform.rotozoom(self._original_image, -angle, 1)
            self._image = pygame.transform.flip(self._image, False, True)
        else:
            self._image = pygame.transform.rotozoom(self._original_image, angle, 1)
        self._rect = self._image.get_frect(center = self._rect.center)

    def _check_if_reached_enemy(self):
        offset = (self._enemy.get_rect().left - self._rect.left, 
                  self._enemy.get_rect().top - self._rect.top)
        if self._mask.overlap(self._enemy.get_mask(), offset):
                return True
        return False

    def _move(self, dt):
        self._rect.midright += self._direction * self._speed * dt

    def update(self, dt):
        self._set_direction()
        self._rotate()
        self._move(dt)
        if self._check_if_reached_enemy():
            self._enemy.deal_damage(40, 'normal')
            self.kill()