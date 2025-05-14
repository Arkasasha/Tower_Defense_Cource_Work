from settings import *


class ExitButton(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        self._image = pygame.image.load(join('Game', 'Assets', 'additional', 'Interface', 'Game_screen', 'Exit_button.png')).convert_alpha()
        self._rect = self._image.get_frect(
            topleft = pygame.Vector2(1580, 0))
        self.isexit_button = True

    # getters
    def get_image(self):
        return self._image

    def get_rect(self):
        return self._rect

    def get_exit(self):
        return self.exit

class GearButton(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        self._image = pygame.image.load(join('Game', 'Assets', 'additional', 'Interface', 'Game_screen', 'Gear_button.png')).convert_alpha()
        self._rect = self._image.get_frect(
            topleft = pygame.Vector2(1305, 0))
        self.isgear_button = True

    # getters
    def get_image(self):
        return self._image

    def get_rect(self):
        return self._rect

class HealthBar(pygame.sprite.Sprite):
    def __init__(self, castle, groups):
        super().__init__(groups)
        self._castle = castle
        self._image = pygame.image.load(join('Game', 'Assets', 'additional', 'Interface', 'Game_screen', 'health_bar', '5.png')).convert_alpha()
        width, height = self._image.get_size()
        self._image = pygame.transform.scale(self._image, (width * 1.7, height * 1.7))
        self._rect = self._image.get_frect(
            topleft = pygame.Vector2(1420, 70))
        self.ishealth_bar = True


    # getters
    def get_image(self):
        return self._image

    def get_rect(self):
        return self._rect
    
    def update(self, dt):
        changed = False
        if self._castle.get_health() == 4:
            self._image = pygame.image.load(join('Game', 'Assets', 'additional', 'Interface', 'Game_screen', 'health_bar', '4.png')).convert_alpha()
            changed = True
        elif self._castle.get_health() == 3:
            self._image = pygame.image.load(join('Game', 'Assets', 'additional', 'Interface', 'Game_screen', 'health_bar', '3.png')).convert_alpha()
            changed = True
        elif self._castle.get_health() == 2:
            self._image = pygame.image.load(join('Game', 'Assets', 'additional', 'Interface', 'Game_screen', 'health_bar', '2.png')).convert_alpha()
            changed = True
        elif self._castle.get_health() == 1:
            self._image = pygame.image.load(join('Game', 'Assets', 'additional', 'Interface', 'Game_screen', 'health_bar', '1.png')).convert_alpha()
            changed = True
        elif self._castle.get_health() == 0:
            self._image = pygame.image.load(join('Game', 'Assets', 'additional', 'Interface', 'Game_screen', 'health_bar', '0.png')).convert_alpha()
            changed = True

        if changed:
            width, height = self._image.get_size()
            self._image = pygame.transform.scale(self._image, (width * 1.7, height * 1.7))
            self._rect = self._image.get_frect(center = self._rect.center)

class HealthText(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        font = pygame.font.Font(join('Game', 'Assets', 'additional', 'Interface', 'Game_screen', 'Oxanium-Bold.ttf'), 30)
        self._image = font.render("Health:", True, (0, 0, 0))
        self._rect = self._image.get_frect(topleft = (1305, 85))
        self.ishealth_text = True

    def get_image(self):
        return self._image

    def get_rect(self):
        return self._rect

class Description(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        self._image = pygame.image.load(join('Game', 'Assets', 'additional', 'Interface', 'Game_screen', 'description.png')).convert_alpha()

        width, height = self._image.get_size()
        self._image = pygame.transform.scale(self._image, (width * 1.5, height * 1.5))

        self._rect = self._image.get_frect(
            topleft = pygame.Vector2(1325, 200))
        self.isdescription = True

    # getters
    def get_image(self):
        return self._image

    def get_rect(self):
        return self._rect

class WaveNum(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        self._font = pygame.font.Font(join('Game', 'Assets', 'additional', 'Interface', 'Game_screen', 'Oxanium-Bold.ttf'), 40)
        self._image = self._font.render("0", True, (0, 0, 0))
        self._rect = self._image.get_frect(topleft = (1460, 135))
        self.iswave_num = True

    def get_image(self):
        return self._image

    def get_rect(self):
        return self._rect
    
    def update(self, dt):
        current_time = pygame.time.get_ticks() // 100
        self._image = self._font.render(str(current_time), True, (0, 0, 0))
        self._rect = self._image.get_frect(topleft = (1460, 135))

class WaveText(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        font = pygame.font.Font(join('Game', 'Assets', 'additional', 'Interface', 'Game_screen', 'Oxanium-Bold.ttf'), 30)
        self._image = font.render("Wave:", True, (0, 0, 0))
        self._rect = self._image.get_frect(topleft = (1305, 140))
        self.iswave_text = True

    def get_image(self):
        return self._image

    def get_rect(self):
        return self._rect

class MoneyNum(pygame.sprite.Sprite):
    def __init__(self, castle, groups):
        super().__init__(groups)
        self._font = pygame.font.Font(join('Game', 'Assets', 'additional', 'Interface', 'Game_screen', 'Oxanium-Bold.ttf'), 40)
        self._castle = castle
        
        self._money_num = 0
        self._image = self._font.render(f'Money: {self._money_num}', True, (0, 0, 0))
        self._rect = self._image.get_frect(topleft = (1305, 705))
        self.ismoney_num = True

    def get_image(self):
        return self._image

    def get_rect(self):
        return self._rect
    
    def update(self, dt):
        self._new_money_num = self._castle.get_money()
        self._image = self._font.render(f'Money: {self._new_money_num}', True, (0, 0, 0))
        self._rect = self._image.get_frect(topleft = (1305, 705))

class Coin(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        self._load_images()
        self._image = self._frames[0]

        self._rect = self._image.get_frect(
            topleft = pygame.Vector2(1530, 685))
        self.iscoin = True

        self._frame_index = 0

    # getters
    def get_image(self):
        return self._image

    def get_rect(self):
        return self._rect
    
    def _load_images(self):
        self._frames = []
        for foldfer_path, sub_folders, file_names in walk(join('Game', 'Assets', 'additional', 'Interface', 'Game_screen', 'Coin')):
            if file_names:
                for file_name in sorted(file_names, key = lambda name: int(name.split('.')[0])):
                    full_path = join(foldfer_path, file_name)
                    surf = pygame.image.load(full_path).convert_alpha()
                    width, height = surf.get_size()
                    surf = pygame.transform.scale(surf, (width * 0.3, height * 0.3))
                    self._frames.append(surf)

    def _animate(self, dt):
        
        self._frame_index = self._frame_index + 5 * dt
        self._image = self._frames[int(self._frame_index) % len(self._frames)]

    def update(self, dt):
        self._animate(dt)
