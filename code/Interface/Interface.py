from settings import *

class RightPanel(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        self._image = pygame.image.load(join('Game', 'Assets', 'additional', 'Interface', 'Game_screen', 'Right_panel.png')).convert_alpha()
        self._rect = self._image.get_frect(
            topleft = pygame.Vector2(1280, 0))
        self.isright_panel = True

    # getters
    def get_image(self):
        return self._image

    def get_rect(self):
        return self._rect 

class BottomPanel(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        self._image = pygame.image.load(join('Game', 'Assets', 'additional', 'Interface', 'Game_screen', 'Bottom_panel.png')).convert_alpha()
        self._rect = self._image.get_frect(
            topleft = pygame.Vector2(0, 594))
        self.isbottom_panel = True

    # getters
    def get_image(self):
        return self._image

    def get_rect(self):
        return self._rect
