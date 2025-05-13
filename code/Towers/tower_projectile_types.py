from settings import *
from Towers.tower_projectile import TowerProjectile

class CannonProjectile(TowerProjectile):
    def __init__(self, pos, enemy, damage, speed, splash, groups):
        surface = pygame.image.load(join('Game', 'Assets', 'Towers', 'cannon', 'projectiles', 'cannonball', '0.png')).convert_alpha()
        width, height = surface.get_size()
        surface = pygame.transform.smoothscale(surface, (width * 0.65, height * 0.65))
        super().__init__(surface, pos, enemy, damage, speed, splash, groups)

class MegaCannonProjectile(TowerProjectile):
    def __init__(self, pos, enemy, damage, speed, splash, groups):
        surface = pygame.image.load(join('Game', 'Assets', 'Towers', 'mega_cannon', 'projectiles', 'mega_cannonball', '0.png')).convert_alpha()
        width, height = surface.get_size()
        surface = pygame.transform.smoothscale(surface, (width, height))
        super().__init__(surface, pos, enemy, damage, speed, splash, groups)

class ReactiveCannonProjectile(TowerProjectile):
    def __init__(self, pos, enemy, damage, speed, splash, groups):
        surface = pygame.image.load(join('Game', 'Assets', 'Towers', 'reactive_cannon', 'projectiles', 'reactivecannonball', '0.png')).convert_alpha()
        width, height = surface.get_size()
        surface = pygame.transform.smoothscale(surface, (width, height))
        super().__init__(surface, pos, enemy, damage, speed, splash, groups)

class XBowProjectile(TowerProjectile):
    def __init__(self, pos, enemy, damage, speed, splash, groups):
        surface = pygame.image.load(join('Game', 'Assets', 'Towers', 'Xbow', 'projectiles', 'bolt', '0.png')).convert_alpha()
        width, height = surface.get_size()
        surface = pygame.transform.smoothscale(surface, (width, height))
        super().__init__(surface, pos, enemy, damage, speed, splash, groups)

class TeslaProjectile(TowerProjectile):
    pass

class ArtaProjectile(TowerProjectile):
    pass

class ArtaSonProjectile(TowerProjectile):
    pass

class WizardTowerProjectile(TowerProjectile):
    def __init__(self, pos, enemy, damage, speed, splash, groups):
        surface = pygame.image.load(join('Game', 'Assets', 'Towers', 'wizard_tower', 'projectiles', '0.png')).convert_alpha()
        width, height = surface.get_size()
        surface = pygame.transform.smoothscale(surface, (width, height))
        super().__init__(surface, pos, enemy, damage, speed, splash, groups)

class MagicaCannonProjectile(TowerProjectile):
    def __init__(self, pos, enemy, damage, speed, splash, groups):
        surface = pygame.image.load(join('Game', 'Assets', 'Towers', 'magic_cannon', 'projectiles', 'magic_cannonball', '0.png')).convert_alpha()
        width, height = surface.get_size()
        surface = pygame.transform.smoothscale(surface, (width, height))
        super().__init__(surface, pos, enemy, damage, speed, splash, groups)

class TornadoTowerProjectile(TowerProjectile):
    def __init__(self, pos, enemy, damage, speed, splash, groups):
        surface = pygame.image.load(join('Game', 'Assets', 'Towers', 'tornado_tower', 'projectiles', '0.png')).convert_alpha()
        width, height = surface.get_size()
        surface = pygame.transform.smoothscale(surface, (width, height))
        super().__init__(surface, pos, enemy, damage, speed, splash, groups)

class DrotikTowerProjectile(TowerProjectile):
    def __init__(self, pos, enemy, damage, speed, splash, groups):
        surface = pygame.image.load(join('Game', 'Assets', 'Towers', 'drotik_tower', 'projectiles', 'drotik', '0.png')).convert_alpha()
        width, height = surface.get_size()
        surface = pygame.transform.smoothscale(surface, (width * 0.65, height * 0.65))
        super().__init__(surface, pos, enemy, damage, speed, splash, groups)

class MegaXBowProjectile(TowerProjectile):
    def __init__(self, pos, enemy, damage, speed, splash, groups):
        surface = pygame.image.load(join('Game', 'Assets', 'Towers', 'mega_xbow', 'projectiles', 'mega_bolt', '0.png')).convert_alpha()
        width, height = surface.get_size()
        surface = pygame.transform.smoothscale(surface, (width * 2, height * 2))
        super().__init__(surface, pos, enemy, damage, speed, splash, groups)
        mask_surface = pygame.Surface(self._rect.size)
        mask_surface.fill((0, 0, 0))
        self._mask = pygame.mask.from_surface(self._image)