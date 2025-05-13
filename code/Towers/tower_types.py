from settings import *
from Towers.tower import Tower
from groups import LevelSprites
from Towers.tower_projectile_types import *

class Cannon(Tower):
    def __init__(self, grid, groups):
        stats_path = join('Game', 'Tower_Stats', 'cannon.txt')
        self._set_stats(stats_path)
        tower_base_surf = pygame.image.load(join('Game', 'Assets', 'Towers', 'bottom_tower', 'tower.png')).convert_alpha()
        tower_head_surf = pygame.image.load(join('Game', 'Assets', 'Towers', 'cannon', 'tower', '0.png')).convert_alpha()
        tower_range_surf = pygame.image.load(join('Game', 'Assets', 'additional', 'radius', self._range, 'surface.png')).convert_alpha()
        tower_range_mask = pygame.image.load(join('Game', 'Assets', 'additional', 'radius', self._range, 'mask.png')).convert_alpha()
        tower_hitbox_surf = pygame.image.load(join('Game', 'Assets', 'additional', 'Hitbox', self._hitbox_size, 'surface.png')).convert_alpha()
        super().__init__(groups, grid, tower_base_surf, tower_head_surf,
                          tower_range_surf, tower_range_mask, tower_hitbox_surf)

        self._projectile_offset_direction = pygame.Vector2(-8, 2).normalize()
        self._projectile_offset_distance = 6
    
    def _create_projectile(self):
        CannonProjectile(self.get_projectile_pos(), self._enemyTracked, self._damage, LevelSprites())

class MegaCannon(Tower):
    def __init__(self, grid, groups):
        stats_path = join('Game', 'Tower_Stats', 'mega_cannon.txt')
        self._set_stats(stats_path)
        tower_base_surf = pygame.image.load(join('Game', 'Assets', 'Towers', 'bottom_tower', 'tower.png')).convert_alpha()
        tower_head_surf = pygame.image.load(join('Game', 'Assets', 'Towers', 'mega_cannon', 'tower', '0.png')).convert_alpha()
        # width, height = tower_head_surf.get_size()
        # tower_head_surf = pygame.transform.smoothscale(tower_head_surf, (width * 2, height * 2))
        tower_range_surf = pygame.image.load(join('Game', 'Assets', 'additional', 'radius', 'B', 'surface.png')).convert_alpha()
        tower_range_mask = pygame.image.load(join('Game', 'Assets', 'additional', 'radius', 'B', 'mask.png')).convert_alpha()
        tower_hitbox_surf = pygame.image.load(join('Game', 'Assets', 'additional', 'Hitbox', '1x1', 'surface.png')).convert_alpha()
        
        super().__init__(groups, grid, tower_base_surf, tower_head_surf, 
                         tower_range_surf, tower_range_mask, tower_hitbox_surf)

        self._projectile_offset_direction = pygame.Vector2(-9, 4).normalize()
        self._projectile_offset_distance = 6
    
    def _create_projectile(self):
        MegaCannonProjectile(self.get_projectile_pos(), self._enemyTracked, self._damage, LevelSprites())

class ReactiveCannon(Tower):
    def __init__(self, grid, groups):
        tower_base_surf = pygame.image.load(join('Game', 'Assets', 'Towers', 'bottom_tower', 'tower.png')).convert_alpha()
        tower_head_surf = pygame.image.load(join('Game', 'Assets', 'Towers', 'reactive_cannon', 'tower', '0.png')).convert_alpha()
        tower_range_surf = pygame.image.load(join('Game', 'Assets', 'additional', 'radius', 'B', 'surface.png')).convert_alpha()
        tower_range_mask = pygame.image.load(join('Game', 'Assets', 'additional', 'radius', 'B', 'mask.png')).convert_alpha()
        tower_hitbox_surf = pygame.image.load(join('Game', 'Assets', 'additional', 'Hitbox', '1x1', 'surface.png')).convert_alpha()
        super().__init__(groups, grid, tower_base_surf, tower_head_surf, tower_range_surf, tower_range_mask, tower_hitbox_surf)

        self._setup_stats()

    def _setup_stats(self):
        # Stats
        self._cooldown_time = 300
        self._damage = 100
    
    def _create_projectile(self):
        ReactiveCannonProjectile(self.get_projectile_pos(), self._enemyTracked, self._damage, LevelSprites())
    
    def get_projectile_pos(self):
        x = self._tower_head.get_rect().centerx
        y = self._tower_head.get_rect().centery
        if self._tower_head.get_direction().x >= 0:
            return (x + 4, y - 7.5)
        if self._tower_head.get_direction().x < 0:
            return (x - 4, y - 7.5)

class XBow(Tower):
    def __init__(self, grid, groups):
        tower_base_surf = pygame.image.load(join('Game', 'Assets', 'Towers', 'bottom_tower', 'tower.png')).convert_alpha()
        tower_head_surf = pygame.image.load(join('Game', 'Assets', 'Towers', 'Xbow', 'tower', '0.png')).convert_alpha()
        tower_range_surf = pygame.image.load(join('Game', 'Assets', 'additional', 'radius', 'B', 'surface.png')).convert_alpha()
        tower_range_mask = pygame.image.load(join('Game', 'Assets', 'additional', 'radius', 'B', 'mask.png')).convert_alpha()
        tower_hitbox_surf = pygame.image.load(join('Game', 'Assets', 'additional', 'Hitbox', '1x1', 'surface.png')).convert_alpha()
        super().__init__(groups, grid, tower_base_surf, tower_head_surf, tower_range_surf, tower_range_mask, tower_hitbox_surf)

        self._setup_stats()

    def _setup_stats(self):
        # Stats
        self._cooldown_time = 300
        self._damage = 100

    def _create_projectile(self):
        XBowProjectile(self.get_projectile_pos(), self._enemyTracked, self._damage, LevelSprites())

    def get_projectile_pos(self):
        x = self._tower_head.get_rect().centerx
        y = self._tower_head.get_rect().centery
        if self._tower_head.get_direction().x >= 0:
            return (x + 4, y - 7.5)
        if self._tower_head.get_direction().x < 0:
            return (x - 4, y - 7.5)

class Tesla(Tower):
    def __init__(self, grid, groups):
        tower_base_surf = pygame.image.load(join('Game', 'Assets', 'Towers', 'bottom_tower', 'tower.png')).convert_alpha()
        tower_head_surf = pygame.image.load(join('Game', 'Assets', 'Towers', 'tesla', 'tower', '0.png')).convert_alpha()
        tower_range_surf = pygame.image.load(join('Game', 'Assets', 'additional', 'radius', 'C', 'surface.png')).convert_alpha()
        tower_range_mask = pygame.image.load(join('Game', 'Assets', 'additional', 'radius', 'C', 'mask.png')).convert_alpha()
        tower_hitbox_surf = pygame.image.load(join('Game', 'Assets', 'additional', 'Hitbox', '1x1', 'surface.png')).convert_alpha()
        super().__init__(groups, grid, tower_base_surf, tower_head_surf, tower_range_surf, tower_range_mask, tower_hitbox_surf)

        self._setup_stats()

    def _setup_stats(self):
        # Stats
        self._cooldown_time = 300
        self._damage = 100
    
    def _create_projectile(self):
        TeslaProjectile(self.get_projectile_pos(), self._enemyTracked, self._damage, LevelSprites())
    
    def get_projectile_pos(self):
        x = self._tower_head.get_rect().centerx
        y = self._tower_head.get_rect().centery
        if self._tower_head.get_direction().x >= 0:
            return (x + 4, y - 7.5)
        if self._tower_head.get_direction().x < 0:
            return (x - 4, y - 7.5)

class Arta(Tower):
    pass

class ArtaSon(Tower):
    pass

class WizardTower(Tower):
    def __init__(self, grid, groups):
        tower_base_surf = pygame.image.load(join('Game', 'Assets', 'Towers', 'bottom_tower', 'tower.png')).convert_alpha()
        tower_head_surf = pygame.image.load(join('Game', 'Assets', 'Towers', 'wizard_tower', 'tower', '0.png')).convert_alpha()
        tower_range_surf = pygame.image.load(join('Game', 'Assets', 'additional', 'radius', 'A', 'surface.png')).convert_alpha()
        tower_range_mask = pygame.image.load(join('Game', 'Assets', 'additional', 'radius', 'A', 'mask.png')).convert_alpha()
        tower_hitbox_surf = pygame.image.load(join('Game', 'Assets', 'additional', 'Hitbox', '1x1', 'surface.png')).convert_alpha()
        super().__init__(groups, grid, tower_base_surf, tower_head_surf, tower_range_surf, tower_range_mask, tower_hitbox_surf)

        self._setup_stats()

    def _setup_stats(self):
        # Stats
        self._cooldown_time = 300
        self._damage = 100
    
    def _create_projectile(self):
        WizardTowerProjectile(self.get_projectile_pos(), self._enemyTracked, self._damage, LevelSprites())

    def get_projectile_pos(self):
        x = self._tower_head.get_rect().centerx
        y = self._tower_head.get_rect().centery
        if self._tower_head.get_direction().x >= 0:
            return (x + 4, y - 7.5)
        if self._tower_head.get_direction().x < 0:
            return (x - 4, y - 7.5)

class MagicaCannon(Tower):
    def __init__(self, grid, groups):
        tower_base_surf = pygame.image.load(join('Game', 'Assets', 'Towers', 'bottom_tower', 'tower.png')).convert_alpha()
        tower_head_surf = pygame.image.load(join('Game', 'Assets', 'Towers', 'magic_cannon', 'tower', '0.png')).convert_alpha()
        tower_range_surf = pygame.image.load(join('Game', 'Assets', 'additional', 'radius', 'B', 'surface.png')).convert_alpha()
        tower_range_mask = pygame.image.load(join('Game', 'Assets', 'additional', 'radius', 'B', 'mask.png')).convert_alpha()
        tower_hitbox_surf = pygame.image.load(join('Game', 'Assets', 'additional', 'Hitbox', '1x1', 'surface.png')).convert_alpha()
        super().__init__(groups, grid, tower_base_surf, tower_head_surf, tower_range_surf, tower_range_mask, tower_hitbox_surf)

        self._setup_stats()

    def _setup_stats(self):
        # Stats
        self._cooldown_time = 300
        self._damage = 100
    
    def _create_projectile(self):
        MagicaCannonProjectile(self.get_projectile_pos(), self._enemyTracked, self._damage, LevelSprites())

    def get_projectile_pos(self):
        x = self._tower_head.get_rect().centerx
        y = self._tower_head.get_rect().centery
        if self._tower_head.get_direction().x >= 0:
            return (x + 4, y - 7.5)
        if self._tower_head.get_direction().x < 0:
            return (x - 4, y - 7.5)

class TornadoTower(Tower):
    def __init__(self, grid, groups):
        tower_base_surf = pygame.image.load(join('Game', 'Assets', 'Towers', 'bottom_tower', 'tower.png')).convert_alpha()
        tower_head_surf = pygame.image.load(join('Game', 'Assets', 'Towers', 'tornado_tower', 'tower', '0.png')).convert_alpha()
        tower_range_surf = pygame.image.load(join('Game', 'Assets', 'additional', 'radius', 'B', 'surface.png')).convert_alpha()
        tower_range_mask = pygame.image.load(join('Game', 'Assets', 'additional', 'radius', 'B', 'mask.png')).convert_alpha()
        tower_hitbox_surf = pygame.image.load(join('Game', 'Assets', 'additional', 'Hitbox', '1x1', 'surface.png')).convert_alpha()
        super().__init__(groups, grid, tower_base_surf, tower_head_surf, tower_range_surf, tower_range_mask, tower_hitbox_surf)

        self._setup_stats()

    def _setup_stats(self):
        # Stats
        self._cooldown_time = 300
        self._damage = 100
    
    def _create_projectile(self):
        TornadoTowerProjectile(self.get_projectile_pos(), self._enemyTracked, self._damage, LevelSprites())

    def get_projectile_pos(self):
        x = self._tower_head.get_rect().centerx
        y = self._tower_head.get_rect().centery
        if self._tower_head.get_direction().x >= 0:
            return (x + 4, y - 7.5)
        if self._tower_head.get_direction().x < 0:
            return (x - 4, y - 7.5)

class Barracks(Tower):
    pass

class EliteBarracks(Tower):
    pass

class DrotikTower(Tower):
    def __init__(self, grid, groups):
        tower_base_surf = pygame.image.load(join('Game', 'Assets', 'Towers', 'bottom_tower', 'tower.png')).convert_alpha()
        tower_head_surf = pygame.image.load(join('Game', 'Assets', 'Towers', 'drotik_tower', 'tower', '0.png')).convert_alpha()
        tower_head_surf = pygame.transform.flip(tower_head_surf, True, False)
        tower_range_surf = pygame.image.load(join('Game', 'Assets', 'additional', 'radius', 'B', 'surface.png')).convert_alpha()
        tower_range_mask = pygame.image.load(join('Game', 'Assets', 'additional', 'radius', 'B', 'mask.png')).convert_alpha()
        tower_hitbox_surf = pygame.image.load(join('Game', 'Assets', 'additional', 'Hitbox', '1x1', 'surface.png')).convert_alpha()
        super().__init__(groups, grid, tower_base_surf, tower_head_surf, tower_range_surf, tower_range_mask, tower_hitbox_surf)

        self._setup_stats()

    def _setup_stats(self):
        # Stats
        self._cooldown_time = 300
        self._damage = 100

    def _create_projectile(self):
        DrotikTowerProjectile(self.get_projectile_pos(), self._enemyTracked, self._damage, LevelSprites())

    def get_projectile_pos(self):
        x = self._tower_head.get_rect().centerx
        y = self._tower_head.get_rect().centery
        if self._tower_head.get_direction().x >= 0:
            return (x + 4, y - 7.5)
        if self._tower_head.get_direction().x < 0:
            return (x - 4, y - 7.5)

class MegaXBow(Tower):
    def __init__(self, grid, groups):
        tower_base_surf = pygame.image.load(join('Game', 'Assets', 'Towers', 'bottom_tower', 'tower.png')).convert_alpha()
        width, height = tower_base_surf.get_size()
        tower_base_surf = pygame.transform.smoothscale(tower_base_surf, (width * 2, height * 2))

        tower_head_surf = pygame.image.load(join('Game', 'Assets', 'Towers', 'mega_xbow', 'tower', '0.png')).convert_alpha()
        width, height = tower_head_surf.get_size()
        tower_head_surf = pygame.transform.smoothscale(tower_head_surf, (width * 2, height * 2))

        tower_range_surf = pygame.image.load(join('Game', 'Assets', 'additional', 'radius', 'A', 'surface.png')).convert_alpha()
        tower_range_mask = pygame.image.load(join('Game', 'Assets', 'additional', 'radius', 'A', 'mask.png')).convert_alpha()
        tower_hitbox_surf = pygame.image.load(join('Game', 'Assets', 'additional', 'Hitbox', '2x2', 'surface.png')).convert_alpha()
        super().__init__(groups, grid, tower_base_surf, tower_head_surf, tower_range_surf, tower_range_mask, tower_hitbox_surf, type2x2 = True)

        self._setup_stats()

    def _setup_stats(self):
        # Stats
        self._cooldown_time = 1000
        self._damage = 100
    
    def _create_projectile(self):
        MegaXBowProjectile(self.get_projectile_pos(), self._enemyTracked, self._damage, LevelSprites())

    def get_projectile_pos(self):
        x = self._tower_head.get_rect().centerx
        y = self._tower_head.get_rect().centery
        # if self._tower_head.get_direction().x >= 0:
        #     return (x, y - 4)
        # if self._tower_head.get_direction().x < 0:
        #     return (x, y)
        return (x, y)
   