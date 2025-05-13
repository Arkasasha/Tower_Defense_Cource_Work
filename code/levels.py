from settings import *
from map_tiles import *
from sprites import Portal
from groups import LevelSprites, TowerSprites, EnemySprites, LevelScreenSprites
from Towers.tower_types import *
from enemies_types import *
from Interface import *
from Castle import Castle

class Level:
    def __init__(self):
        self._screen_surface = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self._SCREEN_WIDTH, self._SCREEN_HEIGHT = self._screen_surface.get_size()
        self._display_surface = pygame.Surface((LEVEL_SCREEN_WIDTH, LEVEL_SCREEN_HEIGHT))
        self._interface_surface = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))
        self._clock = pygame.time.Clock()

        # groups 
        self._level_sprites = LevelSprites(self._display_surface)
        self._tower_sprites = TowerSprites(self._display_surface)
        self._enemy_sprites = EnemySprites(self._display_surface)
        self._interface_sprites = LevelScreenSprites(self._interface_surface)

        # tower grid
        self._tower_grid = [[]]
        for i in range(int(LEVEL_SCREEN_HEIGHT / TILE_SIZE)):
            for j in range(int(LEVEL_SCREEN_WIDTH / TILE_SIZE)):
                self._tower_grid[i].append(False)
            self._tower_grid.append([])

        # tower placing check
        self._tower_to_be_placed = None
        self._tower_is_being_placed = False

        self._castle = Castle()

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
            CastleSprite(image, (x * TILE_SIZE, y * TILE_SIZE), self._level_sprites)

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

        exit_button_surf = pygame.image.load(join('Game', 'Assets', 'additional', 'Interface', 'Game_screen', 'Exit_button.png')).convert_alpha()
        self._exit_button = ExitButton(exit_button_surf, self._interface_sprites)
        
    def _check_tower_being_placed(self):
        if self._tower_is_being_placed:
            self._tower_to_be_placed.delete_tower()
            self._tower_to_be_placed = None
        else:
            self._tower_is_being_placed = True

    def _spawn_entity(self):
        keys = pygame.key.get_just_pressed()
        if keys[pygame.K_q]:
            self._check_tower_being_placed()
            self._tower_to_be_placed =  Cannon(self._tower_grid, (self._level_sprites, self._tower_sprites))
        if keys[pygame.K_w]:
            self._check_tower_being_placed()
            self._tower_to_be_placed = MegaCannon(self._tower_grid, (self._level_sprites, self._tower_sprites))
        if keys[pygame.K_e]:
            self._check_tower_being_placed()
            self._tower_to_be_placed = ReactiveCannon(self._tower_grid, (self._level_sprites, self._tower_sprites))
        if keys[pygame.K_r]:
            self._check_tower_being_placed()
            self._tower_to_be_placed = XBow(self._tower_grid, (self._level_sprites, self._tower_sprites))
        if keys[pygame.K_t]:
            self._check_tower_being_placed()
            self._tower_to_be_placed = WizardTower(self._tower_grid, (self._level_sprites, self._tower_sprites))
        if keys[pygame.K_y]:
            self._check_tower_being_placed()
            self._tower_to_be_placed = MagicaCannon(self._tower_grid, (self._level_sprites, self._tower_sprites))
        if keys[pygame.K_y]:
            self._check_tower_being_placed()
            self._tower_to_be_placed = MagicaCannon(self._tower_grid, (self._level_sprites, self._tower_sprites))
        if keys[pygame.K_u]:
            self._check_tower_being_placed()
            self._tower_to_be_placed = DrotikTower(self._tower_grid, (self._level_sprites, self._tower_sprites))
        if keys[pygame.K_i]:
            self._check_tower_being_placed()
            self._tower_to_be_placed = MegaXBow(self._tower_grid, (self._level_sprites, self._tower_sprites))

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

    def _update_and_draw_screen(self, dt):
        self._level_sprites.update(dt)
        self._tower_sprites.update(dt)
        self._interface_sprites.update(dt)

        self._display_surface.fill('#A020F0')
        self._level_sprites.draw()
        self._interface_surface.blit(self._display_surface, (0, 0))
        self._interface_sprites.draw()

        scaled_surface = pygame.transform.scale(self._interface_surface, (self._SCREEN_WIDTH, self._SCREEN_HEIGHT))
        self._screen_surface.blit(scaled_surface, (0, 0))
        pygame.display.flip()

    def run_the_level(self):
        dt = self._clock.tick() / 1000
        if self._tower_is_being_placed:
            if self._tower_to_be_placed.get_placement_state():
                self._tower_is_being_placed = False
                self._tower_to_be_placed = None

        self._spawn_entity()

        # exit the game
        if pygame.mouse.get_just_pressed()[0] == True:
            print(get_fixed_mouse_pos())
            if self._exit_button.get_rect().collidepoint(get_fixed_mouse_pos()):
                print("Exit game")
                self._exit_button.press()

        # stop placing tower
        if pygame.mouse.get_just_pressed()[2] == True:
            if self._tower_is_being_placed:
                self._tower_is_being_placed = False
                self._tower_to_be_placed.delete_tower()
                self._tower_to_be_placed = None

        self._castle.get_damage()

        self._update_and_draw_screen(dt) 
