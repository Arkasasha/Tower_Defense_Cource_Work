from settings import *
from sprites import Terrain

@singleton
class LevelSprites(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.offset = 0
    
    def check_ground(self, tower_rect):
        tiles = [tile for tile in self if tower_rect.colliderect(tile.rect)]
        for tile in tiles:
            if issubclass(type(tile), Terrain):
                if not hasattr(tile, 'ground'):
                    return False
        return True

    def draw(self):
        terrain_sprites = [sprite for sprite in self if issubclass(type(sprite), Terrain)]
        portal_sprites = [sprite for sprite in self if hasattr(sprite, 'portal')]
        range_sprites = [sprite for sprite in self if hasattr(sprite, 'isrange')]
        hitbox_sprites = [sprite for sprite in self if hasattr(sprite, 'hitbox')]
        tower_sprites = [sprite for sprite in self if hasattr(sprite, 'tower')]
        for layer in [terrain_sprites, portal_sprites, range_sprites, hitbox_sprites, tower_sprites]:
            for sprite in layer:
                self.display_surface.blit(sprite.image, (sprite.rect.topleft[0] + self.offset, sprite.rect.topleft[1] + self.offset))

class TowerSprites(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()