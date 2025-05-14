from settings import *
from Interface import TowerButton

class CannonButton(TowerButton):
    type = 'cannon'

    def _get_type(cls):
        return cls.type

    def __init__(self, pos, groups):
        surf = pygame.image.load(join('Game', 'Assets', 'Towers', self._get_type(), 'tower', '0.png')).convert_alpha()
        width, height = surf.get_size()
        surf = pygame.transform.scale(surf, (width * 3, height * 3))
        super().__init__(surf, pos, self._get_type(), groups)

class MegaCannonButton(TowerButton):
    type = 'mega_cannon'

    def _get_type(cls):
        return cls.type

    def __init__(self, pos, groups):
        surf = pygame.image.load(join('Game', 'Assets', 'Towers', self._get_type(), 'tower', '0.png')).convert_alpha()
        width, height = surf.get_size()
        surf = pygame.transform.scale(surf, (width * 3, height * 3))
        super().__init__(surf, pos, self._get_type(), groups)
        self._offset = (0, 10)

class ReactiveCannonButton(TowerButton):
    type = 'reactive_cannon'

    def _get_type(cls):
        return cls.type

    def __init__(self, pos, groups):
        surf = pygame.image.load(join('Game', 'Assets', 'Towers', self._get_type(), 'tower', '0.png')).convert_alpha()
        width, height = surf.get_size()
        surf = pygame.transform.scale(surf, (width * 3, height * 3))
        super().__init__(surf, pos, self._get_type(), groups)
        self._offset = (0, 10)

class XBowButton(TowerButton):
    type = 'Xbow'

    def _get_type(cls):
        return cls.type

    def __init__(self, pos, groups):
        surf = pygame.image.load(join('Game', 'Assets', 'Towers', self._get_type(), 'tower', '0.png')).convert_alpha()
        width, height = surf.get_size()
        surf = pygame.transform.scale(surf, (width * 3, height * 3))
        super().__init__(surf, pos, self._get_type(), groups)
        self._offset = (-6, 0)

class WizardTowerButton(TowerButton):
    type = 'wizard_tower'

    def _get_type(cls):
        return cls.type

    def __init__(self, pos, groups):
        surf = pygame.image.load(join('Game', 'Assets', 'Towers', self._get_type(), 'tower', '0.png')).convert_alpha()
        width, height = surf.get_size()
        surf = pygame.transform.scale(surf, (width * 2, height * 2))
        super().__init__(surf, pos, self._get_type(), groups)

class MagicaCanononButton(TowerButton):
    type = 'magic_cannon'

    def _get_type(cls):
        return cls.type

    def __init__(self, pos, groups):
        surf = pygame.image.load(join('Game', 'Assets', 'Towers', self._get_type(), 'tower', '0.png')).convert_alpha()
        width, height = surf.get_size()
        surf = pygame.transform.scale(surf, (width * 3, height * 3))
        super().__init__(surf, pos, self._get_type(), groups)
        self._offset = (0, 10)

class DrotikTowerButton(TowerButton):
    type = 'drotik_tower'

    def _get_type(cls):
        return cls.type

    def __init__(self, pos, groups):
        surf = pygame.image.load(join('Game', 'Assets', 'Towers', self._get_type(), 'tower', '0.png')).convert_alpha()
        width, height = surf.get_size()
        surf = pygame.transform.scale(surf, (width * 1.7, height * 1.7))
        super().__init__(surf, pos, self._get_type(), groups)

class MegaXBowButton(TowerButton):
    type = 'mega_xbow'

    def _get_type(cls):
        return cls.type

    def __init__(self, pos, groups):
        surf = pygame.image.load(join('Game', 'Assets', 'Towers', self._get_type(), 'tower', '0.png')).convert_alpha()
        width, height = surf.get_size()
        surf = pygame.transform.scale(surf, (width * 2.5, height * 2.5))
        super().__init__(surf, pos, self._get_type(), groups)