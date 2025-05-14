from settings import *


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

class TowerButton(pygame.sprite.Sprite):
    def __init__(self, surf, pos, tower_type, groups):
        super().__init__(groups)
        self._offset = (0, 0)
        self._image1 = pygame.image.load(join('Game', 'Assets', 'additional', 'Interface', 'Game_screen', 'Button.png'))
        width, height = self._image1.get_size()
        self._image1 = pygame.transform.scale(self._image1, (width * 0.7, height * 0.7))
        self._image2 = surf
        self._rect1 = self._image1.get_frect(center = pos)
        self._rect2 = self._image2.get_frect(center = pos)
        self._tower_type = tower_type
        self.istower_button = True

    # getters
    def get_background_image(self):
        return self._image1
    
    def get_button_image(self):
        return self._image2
    
    def get_background_rect(self):
        return self._rect1

    def get_button_rect(self):
        return self._rect2
    
    def get_offset(self):
        return self._offset

    def get_tower_type(self):
        return self._tower_type