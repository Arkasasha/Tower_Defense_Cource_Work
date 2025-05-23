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
        death_sprites = [sprite for sprite in self if hasattr(sprite, 'isdeath')]
        for layer in [terrain_sprites, portal_sprites, range_sprites, hitbox_sprites, tower_sprites,
                       tower_heads, enemie_sprites, projectile_sprites, death_sprites]:
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
    
    def draw(self):
        for sprite in self:
            self._display_surface.blit(sprite.get_image, sprite.get_rect)

@singleton
class EnemySprites(pygame.sprite.Group):
    def __init__(self, display_surface):
        super().__init__()
        self._display_surface = display_surface

    def draw(self):
        for sprite in self:
            self._display_surface.blit(sprite.get_image, sprite.get_rect)

@singleton     
class EnemyInCastle:
    def __init__(self):
        self._damages = []
    
    def add_damage(self, damage):
        self._damages.append(damage)
    
    def get_damage(self):
        overall_damage = 0
        for damage in self._damages:
            overall_damage += damage
        self._damages = []
        return overall_damage

@singleton
class EnemyDeathMoney:
    def __init__(self):
        self._money = []
    
    def add_money(self, money):
        self._money.append(money)
    
    def get_money(self):
        overall_money = 0
        for money in self._money:
            overall_money += money
        self._money = []
        return overall_money

class LevelScreenSprites(pygame.sprite.Group):
    def __init__(self, display_surface):
        super().__init__()
        self._display_surface = display_surface
        
    def draw(self):
        right_panel = [sprite for sprite in self if hasattr(sprite, 'isright_panel')]
        bottom_panel = [sprite for sprite in self if hasattr(sprite, 'isbottom_panel')]
        exit_button = [sprite for sprite in self if hasattr(sprite, 'isexit_button')]
        gear_button = [sprite for sprite in self if hasattr(sprite, 'isgear_button')]
        description = [sprite for sprite in self if hasattr(sprite, 'isdescription')]
        health_bar = [sprite for sprite in self if hasattr(sprite, 'ishealth_bar')]
        health_text = [sprite for sprite in self if hasattr(sprite, 'ishealth_text')]
        wave_num = [sprite for sprite in self if hasattr(sprite, 'iswave_num')]
        wave_text = [sprite for sprite in self if hasattr(sprite, 'iswave_text')]
        coin = [sprite for sprite in self if hasattr(sprite, 'iscoin')]
        money_num = [sprite for sprite in self if hasattr(sprite, 'ismoney_num')]
        option_ramka = [sprite for sprite in self if hasattr(sprite, 'isoption_ramka')]
        continue_button = [sprite for sprite in self if hasattr(sprite, 'iscontinue_button')]
        settings_button = [sprite for sprite in self if hasattr(sprite, 'issettings_button')]
        quit_button = [sprite for sprite in self if hasattr(sprite, 'isquit_button')]
        scroll_line = [sprite for sprite in self if hasattr(sprite, 'isscroll_line')]
        for layer in [bottom_panel, scroll_line, right_panel, health_bar, health_text, wave_num, wave_text, 
                      coin, money_num, description, gear_button, exit_button, 
                      option_ramka, quit_button, settings_button, continue_button]:
            for sprite in sorted(layer, key = lambda sprite: sprite.get_rect().centery):
                if hasattr(sprite, "hasToBeShown"):
                    if not sprite.hasToBeShown:
                        continue
                self._display_surface.blit(sprite.get_image(), (sprite.get_rect().topleft[0], 
                                                                sprite.get_rect().topleft[1]))

class TowerButtonSprites(pygame.sprite.Group):
    def __init__(self, display_surface):
        super().__init__()
        self._display_surface = display_surface
    
    def draw(self):
        for sprite in self:
            if not sprite.get_pressed_state():
                self._display_surface.blit(sprite.get_image(), sprite.get_rect().topleft)
            else:
                self._display_surface.blit(sprite.get_overlay_image(), sprite.get_overlay_rect().topleft)