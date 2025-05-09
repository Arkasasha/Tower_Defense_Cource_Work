from settings import *
from sprites import Terrain

@singleton
class LevelSprites(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self._display_surface = pygame.display.get_surface()
        self._offset = 0
    
    # getters and setters
    def get_offset(self):
        return self._offset
    

    def check_ground(self, tower_rect):
        tiles = [tile for tile in self if tower_rect.colliderect(tile.get_rect())]
        for tile in tiles:
            if issubclass(type(tile), Terrain):
                if not hasattr(tile, 'ground'):
                    return False
        return True

    def draw(self):
        terrain_sprites = [sprite for sprite in self if issubclass(type(sprite), Terrain)]
        portal_sprites = [sprite for sprite in self if hasattr(sprite, 'isportal')]
        range_sprites = [sprite for sprite in self if hasattr(sprite, 'istower_range')]
        hitbox_sprites = [sprite for sprite in self if hasattr(sprite, 'istower_hitbox')]
        tower_sprites = [sprite for sprite in self if hasattr(sprite, 'istower')]
        tower_heads = [sprite for sprite in self if hasattr(sprite, 'istower_head')]
        enemie_sprites = [sprite for sprite in self if hasattr(sprite, 'isenemie')]
        for layer in [terrain_sprites, portal_sprites, range_sprites, hitbox_sprites, tower_sprites, tower_heads, enemie_sprites]:
            for sprite in layer:
                if hasattr(sprite, "hasToBeShown"):
                    if not sprite.hasToBeShown:
                        continue
                self._display_surface.blit(sprite.get_image(), (sprite.get_rect().topleft[0] + self._offset, sprite.get_rect().topleft[1] + self._offset))

class TowerSprites(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self._display_surface = pygame.display.get_surface()

@singleton
class EnemySprites(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self._display_surface = pygame.display.get_surface()