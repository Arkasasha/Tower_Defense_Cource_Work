from sprites import Terrain

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

class CastleSprite(Terrain):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.castle = True

class Spawn_line():
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.decoration = True

class Turn_lines():
    def __init__(self, polygon_points, name, type):
        self._points = polygon_points
        self._name = name
        self._type = type
    
    # getters
    def get_name(self):
        return self._name

    def get_points(self):
        return self._points

    def get_type(self):
        return self._type