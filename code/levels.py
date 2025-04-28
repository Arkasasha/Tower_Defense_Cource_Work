from settings import *
from sprites import Terrain, Portal
from groups import LevelSprites, TowerSprites
from towers import Tower

class Level:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()
        self.clock = pygame.time.Clock()

        # groups 
        self.level_sprites = LevelSprites()
        self.collison_sprites = pygame.sprite.Group()
        self.tower_sprites = TowerSprites()

        self.setup()
    
    def setup(self):
        map = load_pygame(join('Game', 'Map', 'Tower Defense map.tmx'))

        # Load terrain
        for x, y, image in map.get_layer_by_name('Ground').tiles():
            Terrain(image, (x * TILE_SIZE, y * TILE_SIZE), True, self.level_sprites)

        for x, y, image in map.get_layer_by_name('River').tiles():
            Terrain(image, (x * TILE_SIZE, y * TILE_SIZE), False, self.level_sprites)
        
        for x, y, image in map.get_layer_by_name('Path').tiles():
            Terrain(image, (x * TILE_SIZE, y * TILE_SIZE), False, self.level_sprites)

        for x, y, image in map.get_layer_by_name('Bridge').tiles():
            Terrain(image, (x * TILE_SIZE, y * TILE_SIZE), False, self.level_sprites)

        forests = [map.get_layer_by_name('The Forest').tiles(), 
                       map.get_layer_by_name('The Forest 2').tiles()]
        for forest in forests:
            for x, y, image in forest:
                Terrain(image, (x * TILE_SIZE, y * TILE_SIZE), False, self.level_sprites)
        
        for x, y, image in map.get_layer_by_name('Add').tiles():
            Terrain(image, (x * TILE_SIZE, y * TILE_SIZE), False, self.level_sprites)
        
        # Load a portal
        portal_surf = pygame.image.load(join('Game', 'Assets', 'additional', 'Portal', 'portal.png')).convert_alpha()
        Portal(portal_surf, self.level_sprites)

        tower_surf = pygame.image.load(join('Game', 'Assets', 'Towers', 'Tower', 'tower.png')).convert_alpha()
        Tower(tower_surf, (self.level_sprites, self.tower_sprites))

    def run_the_level(self):
        dt = self.clock.tick() / 1000
        
        self.level_sprites.update(dt)

        self.display_surface.fill('#000000')
        self.level_sprites.draw(self.display_surface)
        pygame.display.flip()

