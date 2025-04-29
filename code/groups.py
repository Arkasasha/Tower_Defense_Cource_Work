from settings import *
from sprites import Terrain

@singleton
class LevelSprites(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()
    
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
        hitbox_sprites = [sprite for sprite in self if hasattr(sprite, 'hitbox')]
        tower_sprites = [sprite for sprite in self if hasattr(sprite, 'tower')]
        for layer in [terrain_sprites, portal_sprites, hitbox_sprites, tower_sprites]:
            for sprite in layer:
                self.display_surface.blit(sprite.image, sprite.rect.topleft)

class TowerSprites(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()