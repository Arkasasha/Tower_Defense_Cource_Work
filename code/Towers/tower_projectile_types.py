from settings import *
from Towers.tower_projectile import TowerProjectile

class CannonProjectile(TowerProjectile):
    def __init__(self, pos, enemy, groups):
        surface = pygame.image.load(join('Game', 'Assets', 'Towers', 'cannon', 'projectiles', 'cannonball', '0.png')).convert_alpha()
        # surface = pygame.image.load(join('Game', 'Assets', 'Towers', 'Xbow', 'projectiles', 'bolt', '0.png')).convert_alpha()
        super().__init__(surface, pos, enemy, groups, (0.65, 0.65))
        
        # Stats
        self._speed = 400
