from settings import *

class Terrain(pygame.sprite.Sprite):
    def __init__(self, surf, pos, groups):
        super().__init__(groups)
        self._image = surf
        self._rect = self._image.get_frect(topleft = pos)
    
    # getters
    def get_image(self):
        return self._image

    def get_rect(self):
        return self._rect

class Portal(pygame.sprite.Sprite):
    def __init__(self, surf, groups):
        super().__init__(groups)
        self._orig_surf = surf
        self._image = surf
        self._rect = self._image.get_frect(
            center = pygame.Vector2(48, 128))
        self.isportal = True

        self._rotation_speed = 300
        self._rotation_angle = 0
    
    # getters
    def get_image(self):
        return self._image

    def get_rect(self):
        return self._rect


    def _rotate(self, dt):
        self._rotation_angle += self._rotation_speed * dt
        self._image = pygame.transform.rotozoom(
            self._orig_surf, self._rotation_angle, 2.5)
        self._rect = self._image.get_frect(center = self._rect.center)
        
    def update(self, dt):
        self._rotate(dt)

class Right_panel(pygame.sprite.Sprite):
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

class Bottom_panel(pygame.sprite.Sprite):
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