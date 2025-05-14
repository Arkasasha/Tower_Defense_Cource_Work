from settings import *
from map_tiles import *
from sprites import Portal
from groups import LevelSprites, TowerSprites, EnemySprites, LevelScreenSprites
from entity_factories import EnemySpawner, TowerSpawner
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

        # enemy spawning
        self._next_enemy_id = 0
        self._last_enemy_spawn_time = pygame.time.get_ticks()
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

        # factories
        self._enemy_factory = EnemySpawner(self._spawn_line, self._turn_lines, self._enemy_sprites, self._level_sprites)
        self._tower_factory = TowerSpawner(self._tower_grid, self._level_sprites, self._tower_sprites)

        # Load a portal
        portal_surf = pygame.image.load(join('Game', 'Assets', 'additional', 'Portal', 'portal.png')).convert_alpha()
        Portal(portal_surf, self._level_sprites)

        # Load interface
        right_panel_surf = pygame.image.load(join('Game', 'Assets', 'additional', 'Interface', 'Game_screen', 'Right_panel.png')).convert_alpha()
        RightPanel(right_panel_surf, self._interface_sprites)

        bottom_panel_surf = pygame.image.load(join('Game', 'Assets', 'additional', 'Interface', 'Game_screen', 'Bottom_panel.png')).convert_alpha()
        BottomPanel(bottom_panel_surf, self._interface_sprites)

        description_surf = pygame.image.load(join('Game', 'Assets', 'additional', 'Interface', 'Game_screen', 'description.png')).convert_alpha()
        Description(description_surf, self._interface_sprites)

        
        HealthBar(self._castle ,self._interface_sprites)
        HealthText(self._interface_sprites)

        WaveNum(self._interface_sprites)
        WaveText(self._interface_sprites)

        
        Coin(self._interface_sprites)
        MoneyNum(self._castle, self._interface_sprites)

        gear_button_surf = pygame.image.load(join('Game', 'Assets', 'additional', 'Interface', 'Game_screen', 'Gear_button.png')).convert_alpha()
        self._gear_button = GearButton(gear_button_surf, self._interface_sprites)

        exit_button_surf = pygame.image.load(join('Game', 'Assets', 'additional', 'Interface', 'Game_screen', 'Exit_button.png')).convert_alpha()
        self._exit_button = ExitButton(exit_button_surf, self._interface_sprites)

        self._enemy_timings = []
        with open(join("Game","enemy_spawn_list.txt"), "r") as file:
            for line in file:
                parts = line.strip().split()
                if len(parts) == 3:
                    parts[0] = int(parts[0])
                    parts[2] = int(parts[2])
                    self._enemy_timings.append(tuple(parts))
                else:
                    raise ValueError(f"Skipping line (doesn't have 3 parts): {line}")

    # getters
    def get_level_sprites(self):
        return self._level_sprites
    
    def get_level_sprites(self):
        return self._level_sprites

    # main functionality
    def _enemy_spawn_timer(self):
        current_time = pygame.time.get_ticks()
        if self._next_enemy_id <= len(self._enemy_timings):
            if current_time - self._last_enemy_spawn_time >= self._enemy_timings[self._next_enemy_id][2]:
                self._enemy_factory.create_enemy(self._enemy_timings[self._next_enemy_id][1])
                self._next_enemy_id += 1
                self._last_enemy_spawn_time = current_time

    def _check_tower_being_placed(self):
        if self._tower_is_being_placed:
            self._tower_to_be_placed.delete_tower()
            self._tower_to_be_placed = None
        else:
            self._tower_is_being_placed = True

    def _spawn_entity(self):
        keys = pygame.key.get_just_pressed()
        tower_type = None
        if keys[pygame.K_q]:
            tower_type = 'cannon'
        if keys[pygame.K_w]:
            tower_type = 'mega_cannon'
        if keys[pygame.K_e]:
            tower_type = 'reactive_cannon'
        if keys[pygame.K_r]:
            tower_type = 'Xbow'
        if keys[pygame.K_t]:
            tower_type = 'wizard_tower'
        if keys[pygame.K_y]:
            tower_type = 'magic_cannon'
        if keys[pygame.K_u]:
            tower_type = 'drotik_tower'
        if keys[pygame.K_i]:
            tower_type = 'mega_xbow'
        if tower_type != None:
            self._check_tower_being_placed()
            self._tower_to_be_placed = self._tower_factory.create_tower(tower_type)


        enemy_type = None
        if keys[pygame.K_p]:
            enemy_type = 'LOKI'
        if keys[pygame.K_1]:
            enemy_type = 'tankman'
        if keys[pygame.K_2]:
            enemy_type = 'spearsman'
        if keys[pygame.K_3]:
            enemy_type = 'fish'
        if keys[pygame.K_4]:
            enemy_type = 'flying_snake'
        if keys[pygame.K_5]:
            enemy_type = 'rogue'
        if keys[pygame.K_6]:
            enemy_type = 'red_elemental'
        if keys[pygame.K_7]:
            enemy_type = 'blue_slime'
        if keys[pygame.K_8]:
            enemy_type = 'golem'
        if keys[pygame.K_9]:
            enemy_type = 'ghost'
        if keys[pygame.K_0]:
            enemy_type = 'bimba'
        if enemy_type != None:
            self._enemy_factory.create_enemy(enemy_type)

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

        # exit the game
        if pygame.mouse.get_just_pressed()[0]:
            if self._exit_button.get_rect().collidepoint(get_fixed_mouse_pos()):
                self._exit_button.press()

            elif self._gear_button.get_rect().collidepoint(get_fixed_mouse_pos()):
                if self._gear_button.press():
                    option_ramka_surf = pygame.image.load(join('Game', 'Assets', 'additional', 'Interface', 'Game_screen', 'Ramka.png')).convert_alpha()
                    self._option_ramka = OptionRamka(option_ramka_surf, self._interface_sprites)

                    continue_button_surf = pygame.image.load(join('Game', 'Assets', 'additional', 'Interface', 'Game_screen', 'Continue.png')).convert_alpha()
                    self._continue_button = ContinueButton(continue_button_surf, self._interface_sprites)

                    settings_button_surf = pygame.image.load(join('Game', 'Assets', 'additional', 'Interface', 'Game_screen', 'Settings.png')).convert_alpha()
                    self._settings_button = SettingsButton(settings_button_surf, self._interface_sprites)

                    quit_button_surf = pygame.image.load(join('Game', 'Assets', 'additional', 'Interface', 'Game_screen', 'Quit.png')).convert_alpha()
                    self._quit_button = QuitButton(quit_button_surf, self._interface_sprites)

            elif self._continue_button.get_rect().collidepoint(get_fixed_mouse_pos()):
                if self._continue_button.press():
                    self._option_ramka.hasToBeShown = False
                    self._continue_button.hasToBeShown = False
                    self._settings_button.hasToBeShown = False
                    self._quit_button.hasToBeShown = False
                    
            elif self._settings_button.get_rect().collidepoint(get_fixed_mouse_pos()):
                if self._settings_button.press:
                    pass

            elif self._quit_button.get_rect().collidepoint(get_fixed_mouse_pos()):
                self._quit_button.press()




        
        # check if tower is still placing
        if self._tower_is_being_placed:
            if self._tower_to_be_placed.get_placement_state():
                self._tower_is_being_placed = False
                self._tower_to_be_placed = None
        
        # stop placing tower
        if pygame.mouse.get_just_pressed()[2] == True:
            if self._tower_is_being_placed:
                self._tower_is_being_placed = False
                self._tower_to_be_placed.delete_tower()
                self._tower_to_be_placed = None

        self._castle.take_damage()
        self._castle.take_money()

        # spawn enemies
        self._enemy_spawn_timer()
        self._spawn_entity()

        self._update_and_draw_screen(dt) 
