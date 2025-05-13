from settings import *
from sprites import Terrain

@singleton
class LevelSprites(pygame.sprite.Group):
    def __init__(self, display_surface):
        super().__init__()
        self._display_surface = display_surface
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
        projectile_sprites = [sprite for sprite in self if hasattr(sprite, 'isprojectile')]
        for layer in [terrain_sprites, portal_sprites, range_sprites, hitbox_sprites, tower_sprites,
                       tower_heads, enemie_sprites, projectile_sprites]:
            for sprite in sorted(layer, key = lambda sprite: sprite.get_rect().centery):
                if hasattr(sprite, "hasToBeShown"):
                    if not sprite.hasToBeShown:
                        continue
                self._display_surface.blit(sprite.get_image(), (sprite.get_rect().topleft[0] + self._offset, 
                                                                sprite.get_rect().topleft[1] + self._offset))

class TowerSprites(pygame.sprite.Group):
    def __init__(self, display_surface):
        super().__init__()
        self._display_surface = display_surface

@singleton
class EnemySprites(pygame.sprite.Group):
    def __init__(self, display_surface):
        super().__init__()
        self._display_surface = display_surface

class InterfaceSprites(pygame.sprite.Group):
    def __init__(self, display_surface):
        super().__init__()
        self._display_surface = display_surface
        
    def draw(self):
        right_panel = [sprite for sprite in self if hasattr(sprite, 'isright_panel')]
        bottom_panel = [sprite for sprite in self if hasattr(sprite, 'isbottom_panel')]
        for layer in [bottom_panel, right_panel]:
            for sprite in sorted(layer, key = lambda sprite: sprite.get_rect().centery):
                if hasattr(sprite, "hasToBeShown"):
                    if not sprite.hasToBeShown:
                        continue
                self._display_surface.blit(sprite.get_image(), (sprite.get_rect().topleft[0], 
                                                                sprite.get_rect().topleft[1]))