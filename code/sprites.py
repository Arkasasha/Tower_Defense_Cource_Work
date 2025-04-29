from settings import *

class Terrain(pygame.sprite.Sprite):
    def __init__(self, surf, pos, groups):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_frect(topleft = pos)

class Ground(Terrain):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ground = True

class Bridge(Terrain):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.bridge = True

class River(Terrain):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.river = True

class Forest(Terrain):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.forest = True

class Path(Terrain):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.path = True
    
class Decoration(Terrain):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.decoration = True

class Portal(pygame.sprite.Sprite):
    def __init__(self, surf, groups):
        super().__init__(groups)
        self.orig_surf = surf
        self.image = surf
        self.rect = self.image.get_frect(
            center = pygame.Vector2(48, 128))
        self.portal = True

        self.rotation_speed = 300
        self.rotation_angle = 0
    
    def rotate(self, dt):
        self.rotation_angle += self.rotation_speed * dt
        self.image = pygame.transform.rotozoom(
            self.orig_surf, self.rotation_angle, 2.5)
        self.rect = self.image.get_frect(center = self.rect.center)
        
    def update(self, dt):
        self.rotate(dt)