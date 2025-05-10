from settings import *
from Towers.tower_projectile import TowerProjectile

class CannonProjectile(TowerProjectile):
    def __init__(self, pos, enemy, damage, groups):
        surface = pygame.image.load(join('Game', 'Assets', 'Towers', 'cannon', 'projectiles', 'cannonball', '0.png')).convert_alpha()
        width, height = surface.get_size()
        surface = pygame.transform.smoothscale(surface, (width * 0.65, height * 0.65))
        # surface = pygame.image.load(join('Game', 'Assets', 'Towers', 'Xbow', 'projectiles', 'bolt', '0.png')).convert_alpha()
        super().__init__(surface, pos, enemy, damage, groups)
        
        self._stats_setup()

    def _stats_setup(self):
        # Stats
        self._speed = 400
        self._splash = None