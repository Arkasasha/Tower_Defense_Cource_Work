from settings import *
import sys


class RightPanel(pygame.sprite.Sprite):
    def __init__(self, surf, groups):
        super().__init__(groups)
        self._image = surf
        self._rect = self._image.get_frect(
            topleft = pygame.Vector2(1280, 0))
        self.isright_panel = True

    # getters
    def get_image(self):
        return self._image

    def get_rect(self):
        return self._rect 

class BottomPanel(pygame.sprite.Sprite):
    def __init__(self, surf, groups):
        super().__init__(groups)
        self._image = surf
        self._rect = self._image.get_frect(
            topleft = pygame.Vector2(0, 594))
        self.isbottom_panel = True

    # getters
    def get_image(self):
        return self._image

    def get_rect(self):
        return self._rect

class ExitButton(pygame.sprite.Sprite):
    def __init__(self, surf, groups):
        super().__init__(groups)
        self._image = surf
        self._rect = self._image.get_frect(
            topleft = pygame.Vector2(1280, 0))
        self.isexit_button = True

    # getters
    def get_image(self):
        return self._image

    def get_rect(self):
        return self._rect

    def get_exit(self):
        return self.exit

    def press(self): 
        pygame.quit()
        sys.exit()