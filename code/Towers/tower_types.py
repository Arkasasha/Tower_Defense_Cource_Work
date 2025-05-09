from settings import *
from Towers.tower import Tower

class Cannon(Tower):
    def __init__(self, grid, groups):
        tower_base_surf = pygame.image.load(join('Game', 'Assets', 'Towers', 'bottom_tower', 'tower.png')).convert_alpha()
        tower_head_surf = pygame.image.load(join('Game', 'Assets', 'Towers', 'cannon', 'tower', '0.png')).convert_alpha()
        tower_range_surf = pygame.image.load(join('Game', 'Assets', 'additional', 'radius', 'B', 'surface.png')).convert_alpha()
        tower_range_mask = pygame.image.load(join('Game', 'Assets', 'additional', 'radius', 'B', 'mask.png')).convert_alpha()
        tower_hitbox_surf = pygame.image.load(join('Game', 'Assets', 'additional', 'Hitbox', '1x1', 'surface.png')).convert_alpha()
        super().__init__(groups, grid, tower_base_surf, tower_head_surf, tower_range_surf, tower_range_mask, tower_hitbox_surf)

        # Stats
        self._cooldown_time = 300
    
    def get_projectile_pos(self):
        x = self._tower_head.get_rect().centerx
        y = self._tower_head.get_rect().centery
        if self._tower_head.get_direction().x >= 0:
            return (x + 4, y - 7.5)
        if self._tower_head.get_direction().x < 0:
            return (x - 4, y - 7.5)