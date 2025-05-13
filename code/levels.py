from settings import *
from map_tiles import *
from sprites import Portal
from groups import LevelSprites, TowerSprites, EnemySprites, GameScreenSprites
from Towers.tower_types import Cannon
from enemies_types import *
from Interface import *

class Level:
    def __init__(self):
        self._display_surface = pygame.display.get_surface()
        self._clock = pygame.time.Clock()

        # groups 
        self._level_sprites = LevelSprites()
        self._collison_sprites = pygame.sprite.Group()
        self._tower_sprites = TowerSprites()
        self._enemy_sprites = EnemySprites()
        self._interface_sprites = GameScreenSprites()

        # tower grid
        self._tower_grid = [[]]
        for i in range(int(WINDOW_HEIGHT / TILE_SIZE)):
            for j in range(int(WINDOW_WIDTH / TILE_SIZE)):
                self._tower_grid[i].append(False)
            self._tower_grid.append([])

        self._setup()
    
    def _setup(self):
        map = load_pygame(join('Game', 'Map', 'Tower Defense map.tmx'))

        # Load terrain
        for x, y, image in map.get_layer_by_name('Ground').tiles():
            Ground(image, (x * TILE_SIZE, y * TILE_SIZE), self._level_sprites)

        for x, y, image in map.get_layer_by_name('River').tiles():
            River(image, (x * TILE_SIZE, y * TILE_SIZE), self._level_sprites)
        
        for x, y, image in map.get_layer_by_name('Path').tiles():
            Path(image, (x * TILE_SIZE, y * TILE_SIZE), self._level_sprites)

        for x, y, image in map.get_layer_by_name('Bridge').tiles():
            Bridge(image, (x * TILE_SIZE, y * TILE_SIZE), self._level_sprites)

        forests = [map.get_layer_by_name('The Forest').tiles(), 
                       map.get_layer_by_name('The Forest 2').tiles()]
        for forest in forests:
            for x, y, image in forest:
                Forest(image, (x * TILE_SIZE, y * TILE_SIZE), self._level_sprites)
        
        for x, y, image in map.get_layer_by_name('Castle').tiles():
            Castle(image, (x * TILE_SIZE, y * TILE_SIZE), self._level_sprites)

        for x, y, image in map.get_layer_by_name('Add').tiles():
            Decoration(image, (x * TILE_SIZE, y * TILE_SIZE), self._level_sprites)

        #Load objects
        self._turn_lines = [] 

        for obj in map.get_layer_by_name("Objects"):
            if obj.name == "Spawn":
                self._spawn_line = [(p[0], p[1]) for p in obj.points]
                
            elif obj.type in ("1", "2", "3"): 
                polygon_points = [(p[0], p[1]) for p in obj.points]
                turn_line = Turn_lines(polygon_points, obj.name, obj.type)
                self._turn_lines.append(turn_line)
        self._turn_lines.sort(key = lambda line: int(line.get_name()))


        # Load a portal
        portal_surf = pygame.image.load(join('Game', 'Assets', 'additional', 'Portal', 'portal.png')).convert_alpha()
        Portal(portal_surf, self._level_sprites)

        # Load interface
        right_panel_surf = pygame.image.load(join('Game', 'Assets', 'additional', 'Interface', 'Game_screen', 'Right_panel.png')).convert_alpha()
        RightPanel(right_panel_surf, self._interface_sprites)

        bottom_panel_surf = pygame.image.load(join('Game', 'Assets', 'additional', 'Interface', 'Game_screen', 'Bottom_panel.png')).convert_alpha()
        BottomPanel(bottom_panel_surf, self._interface_sprites)

    def run_the_level(self):
        dt = self._clock.tick() / 1000
  
        keys = pygame.key.get_just_pressed()
        if keys[pygame.K_o]:
            Cannon(self._tower_grid, (self._level_sprites, self._tower_sprites))
        if keys[pygame.K_p]:
            Loki(self._spawn_line, self._turn_lines, (self._level_sprites, self._enemy_sprites)) 
        if keys[pygame.K_1]:
            tankman(self._spawn_line, self._turn_lines, (self._level_sprites, self._enemy_sprites))
        if keys[pygame.K_2]:
            spearsman(self._spawn_line, self._turn_lines, (self._level_sprites, self._enemy_sprites))
        if keys[pygame.K_3]:
            fish(self._spawn_line, self._turn_lines, (self._level_sprites, self._enemy_sprites))
        if keys[pygame.K_4]:
            flying_snake(self._spawn_line, self._turn_lines, (self._level_sprites, self._enemy_sprites))
        if keys[pygame.K_5]:
            rogue(self._spawn_line, self._turn_lines, (self._level_sprites, self._enemy_sprites))
        if keys[pygame.K_6]:
            red_elemental(self._spawn_line, self._turn_lines, (self._level_sprites, self._enemy_sprites))
        if keys[pygame.K_7]:
            blue_slime(self._spawn_line, self._turn_lines, (self._level_sprites, self._enemy_sprites))
        if keys[pygame.K_8]:
            golem(self._spawn_line, self._turn_lines, (self._level_sprites, self._enemy_sprites))
        if keys[pygame.K_9]:
            ghost(self._spawn_line, self._turn_lines, (self._level_sprites, self._enemy_sprites))
        if keys[pygame.K_0]:
            bimba(self._spawn_line, self._turn_lines, (self._level_sprites, self._enemy_sprites))

        exit_button_surf = pygame.image.load(join('Game', 'Assets', 'additional', 'Interface', 'Game_screen', 'Exit_button.png')).convert_alpha()
        exit_button = ExitButton(exit_button_surf, self._interface_sprites)
        if pygame.mouse.get_just_pressed()[0] == True:
            if exit_button.get_rect().collidepoint(pygame.mouse.get_pos()):
                exit_button.press()
        
                    

        self._level_sprites.update(dt)
        self._tower_sprites.update(dt)
        self._interface_sprites.update(dt)

        self._display_surface.fill('#A020F0')
        self._level_sprites.draw()
        self._interface_sprites.draw()

        
        # # Проверка линий
        # for polygon in self._turn_lines:
        #     pygame.draw.polygon(self._display_surface, 'red', polygon.get_points(), 2)
        # # Отладка: рисуем линию спавна
        # pygame.draw.polygon(self._display_surface, 'blue', self._spawn_line, 2)

        pygame.display.flip()

