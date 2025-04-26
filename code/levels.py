from settings import *
from sprites import Terrain

class Level1:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()
        self.clock = pygame.time.Clock()

        # groups 
        self.level_sprites = pygame.sprite.Group()
        self.collison_sprites = pygame.sprite.Group()

        self.setup()
    
    def setup(self):
        map = load_pygame(join('Game', 'Map', 'Tower Defense map.tmx'))
        for x, y, image in map.get_layer_by_name('Ground').tiles():
            Terrain(image, (x * TILE_SIZE, y * TILE_SIZE), True, self.level_sprites)


    def run_the_level(self):
        dt = self.clock.tick() / 1000
        
        self.level_sprites.update(dt)

        self.display_surface.fill('#000000')
        self.level_sprites.draw(self.display_surface)
        pygame.display.flip()

