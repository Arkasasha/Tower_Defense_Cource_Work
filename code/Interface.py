from settings import *
from Castle import Castle

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

class ExitButton(pygame.sprite.Sprite):
    def __init__(self, surf, groups):
        super().__init__(groups)
        self._image = surf
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

    def press(self): 
        pygame.quit()
        sys.exit()

class GearButton(pygame.sprite.Sprite):
    def __init__(self, surf, groups):
        super().__init__(groups)
        self._image = surf
        self._rect = self._image.get_frect(
            topleft = pygame.Vector2(1305, 0))
        self.isgear_button = True

    # getters
    def get_image(self):
        return self._image

    def get_rect(self):
        return self._rect
    
    def press(self):
        return True

class Description(pygame.sprite.Sprite):
    def __init__(self, surf, groups):
        super().__init__(groups)
        self._image = surf

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

class OptionRamka(pygame.sprite.Sprite):
    def __init__(self, surf, groups):
        super().__init__(groups)
        self._image = surf
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
    def __init__(self, surf, groups):
        super().__init__(groups)
        self._image = surf
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
    def __init__(self, surf, groups):
        super().__init__(groups)
        self._image = surf
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
    def __init__(self, surf, groups):
        super().__init__(groups)
        self._image = surf
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

class GearButton(pygame.sprite.Sprite):
    def __init__(self, surf, groups):
        super().__init__(groups)
        self._image = surf
        self._rect = self._image.get_frect(
            topleft = pygame.Vector2(1305, 0))
        self.isgear_button = True

    # getters
    def get_image(self):
        return self._image

    def get_rect(self):
        return self._rect
    
    def press(self):
        return True

class Description(pygame.sprite.Sprite):
    def __init__(self, surf, groups):
        super().__init__(groups)
        self._image = surf

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

class OptionRamka(pygame.sprite.Sprite):
    def __init__(self, surf, groups):
        super().__init__(groups)
        self._image = surf
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
    def __init__(self, surf, groups):
        super().__init__(groups)
        self._image = surf
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
    def __init__(self, surf, groups):
        super().__init__(groups)
        self._image = surf
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
    def __init__(self, surf, groups):
        super().__init__(groups)
        self._image = surf
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


class TowerButton(pygame.sprite.Sprite):
    def __init__(self, surf, pos, tower_type, groups, offset = (0, 0)):
        super().__init__(groups)
        self._offset = offset
        self._pressed_state = False
        
        # set bachground image 
        background_image = pygame.image.load(join('Game', 'Assets', 'additional', 'Interface', 'Game_screen', 'Button.png'))
        width, height = background_image.get_size()
        background_image = pygame.transform.scale(background_image, (width * 0.7, height * 0.7))
        background_rect = background_image.get_frect(center = pos)

        # set button image
        self._image = background_image.copy()
        self._image.blit(surf, self._offset)
        self._rect = self._image.get_frect(center = pos)

        self._overlay_image = self._image.copy()
        mask = pygame.mask.from_surface(self._overlay_image)
        pressed_image = pygame.Surface(self._overlay_image.get_size(), pygame.SRCALPHA)
        
        for y in range(self._overlay_image.get_height()):
            for x in range(self._overlay_image.get_width()):
                if mask.get_at((x, y)):
                    pressed_image.set_at((x, y), (0, 0, 0, 100))  # black pixel, fully opaque
                else:
                    pressed_image.set_at((x, y), (0, 0, 0, 0))    # fully transparent
        
        self._overlay_image.blit(pressed_image, (0, 0))
        self._overlay_rect = self._overlay_image.get_frect(center = pos)
        

        self._tower_type = tower_type
        self.istower_button = True

    # getter images
    def get_image(self):
        return self._image

    def get_overlay_image(self):
        return self._overlay_image


    # get rects
    def get_rect(self):
        return self._rect
    
    def get_overlay_rect(self):
        return self._overlay_rect


    # other getters
    def get_offset(self):
        return self._offset

    def get_tower_type(self):
        return self._tower_type
    
    def get_pressed_state(self):
        return self._pressed_state
    
    # setters 
    def set_pressed_state(self, state):
        self._pressed_state = state