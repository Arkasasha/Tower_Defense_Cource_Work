from settings import *

class LevelButton:
    def __init__(self, surf, pos, id = None):
        self._image = surf
        self._rect = self._image.get_frect(center = pos)
        self._id = id
    
    def get_image(self):
        return self._image
    
    def get_rect(self):
        return self._rect
    
    def get_id(self):
        return self._id