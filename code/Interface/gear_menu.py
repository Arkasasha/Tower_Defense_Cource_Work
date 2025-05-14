from settings import *

class OptionRamka(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        self._image = pygame.image.load(join('Game', 'Assets', 'additional', 'Interface', 'Game_screen', 'Ramka.png')).convert_alpha()
        self._rect = self._image.get_frect(
            center = pygame.Vector2(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))
        self.isoption_ramka = True
        self.hasToBeShown = True

    # getters
    def get_image(self):
        return self._image

    def get_rect(self):
        return self._rect 

class ContinueButton(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        self._image = pygame.image.load(join('Game', 'Assets', 'additional', 'Interface', 'Game_screen', 'Continue.png')).convert_alpha()
        self._rect = self._image.get_frect(
            center = pygame.Vector2(WINDOW_WIDTH / 2 - 110, 170))
        self.iscontinue_button = True
        self.hasToBeShown = True

    # getters
    def get_image(self):
        return self._image

    def get_rect(self):
        return self._rect
    
    def press(self):
        return True
    
class SettingsButton(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        self._image = pygame.image.load(join('Game', 'Assets', 'additional', 'Interface', 'Game_screen', 'Settings.png')).convert_alpha()
        self._rect = self._image.get_frect(
            center = pygame.Vector2(WINDOW_WIDTH / 2 - 110, 340))
        self.issettings_button = True
        self.hasToBeShown = True

    # getters
    def get_image(self):
        return self._image

    def get_rect(self):
        return self._rect
    
    def press(self):
        return True
    
class QuitButton(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        self._image = pygame.image.load(join('Game', 'Assets', 'additional', 'Interface', 'Game_screen', 'Quit.png')).convert_alpha()
        self._rect = self._image.get_frect(
            center = pygame.Vector2(WINDOW_WIDTH / 2 - 110, 510))
        self.isquit_button = True
        self.hasToBeShown = True

    # getters
    def get_image(self):
        return self._image

    def get_rect(self):
        return self._rect
    
    def press(self):
        pygame.quit()
        sys.exit()
