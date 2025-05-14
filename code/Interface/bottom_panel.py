from settings import *


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