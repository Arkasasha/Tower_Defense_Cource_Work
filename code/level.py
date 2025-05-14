from settings import *
from map_tiles import *
from sprites import Portal
from groups import *
from entity_factories import EnemySpawner, TowerSpawner
from Interface.Interface import *
from Interface.right_panel import *
from Interface.tower_button import *
from Interface.gear_menu import *
from Castle import Castle

class Level:
    def __init__(self):
        self._running = True
        self._display_surface = pygame.Surface((LEVEL_SCREEN_WIDTH, LEVEL_SCREEN_HEIGHT))
        self._interface_surface = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))
        self._clock = pygame.time.Clock()

        # groups 
        self._level_sprites = LevelSprites(self._display_surface)
        self._tower_sprites = TowerSprites(self._display_surface)
        self._enemy_sprites = EnemySprites(self._display_surface)
        self._interface_sprites = LevelScreenSprites(self._interface_surface)
        self._tower_button_sprites = TowerButtonSprites(self._interface_surface)

        # tower grid
        self._tower_grid = [[]]
        for i in range(int(LEVEL_SCREEN_HEIGHT / TILE_SIZE)):
            for j in range(int(LEVEL_SCREEN_WIDTH / TILE_SIZE)):
                self._tower_grid[i].append(False)
            self._tower_grid.append([])

        # tower placing check
        self._tower_to_be_placed = None
        self._tower_is_being_placed = False
        self._pressed_tower_button = None

        # castle
        self._castle = Castle()

        # enemy spawning
        self._next_enemy_id = 0
        self._last_enemy_spawn_time = pygame.time.get_ticks()
        self._setup()

        # settings menu
        self._settings_menu_status = False

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
        Portal(self._level_sprites)

        # Load interface
        RightPanel(self._interface_sprites)

        BottomPanel(self._interface_sprites)

        Description(self._interface_sprites)

        
        HealthBar(self._castle ,self._interface_sprites)
        HealthText(self._interface_sprites)

        WaveNum(self._interface_sprites)
        WaveText(self._interface_sprites)

        
        Coin(self._interface_sprites)
        MoneyNum(self._castle, self._interface_sprites)

        self._gear_button = GearButton(self._interface_sprites)

        self._exit_button = ExitButton(self._interface_sprites)

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
        
        tower_button_point = [80, 740]
        for i in range(8):
            if i == 0:
                CannonButton(tower_button_point, self._tower_button_sprites)
            if i == 1:
                MegaCannonButton(tower_button_point, self._tower_button_sprites)
            if i == 2:
                ReactiveCannonButton(tower_button_point, self._tower_button_sprites)
            if i == 3:
                XBowButton(tower_button_point, self._tower_button_sprites)
            if i == 4:
                WizardTowerButton(tower_button_point, self._tower_button_sprites)
            if i == 5:
                MagicaCanononButton(tower_button_point, self._tower_button_sprites)
            if i == 6:
                DrotikTowerButton(tower_button_point, self._tower_button_sprites)
            if i == 7:
                MegaXBowButton(tower_button_point, self._tower_button_sprites)
            tower_button_point[0] += 150

    # getters
    def get_level_sprites(self):
        return self._level_sprites

    def get_interface_surface(self):
        return self._interface_surface

    def get_running(self):
        return self._running

    # setters
    def set_running(self, state):
        self._running = state

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

    def _spawn_tower(self):
        tower_type = None
        if isinstance(self._pressed_tower_button, CannonButton):
            tower_type = 'cannon'
        if isinstance(self._pressed_tower_button, MegaCannonButton):
            tower_type = 'mega_cannon'
        if isinstance(self._pressed_tower_button, ReactiveCannonButton):
            tower_type = 'reactive_cannon'
        if isinstance(self._pressed_tower_button, XBowButton):
            tower_type = 'Xbow'
        if isinstance(self._pressed_tower_button, WizardTowerButton):
            tower_type = 'wizard_tower'
        if isinstance(self._pressed_tower_button, MagicaCanononButton):
            tower_type = 'magic_cannon'
        if isinstance(self._pressed_tower_button, DrotikTowerButton):
            tower_type = 'drotik_tower'
        if isinstance(self._pressed_tower_button, MegaXBowButton):
            tower_type = 'mega_xbow'
        if tower_type != None:
            self._check_tower_being_placed()
            self._tower_to_be_placed = self._tower_factory.create_tower(tower_type)

    def _click_on_bottom_panel(self):
        mouse_pos = get_fixed_mouse_pos()
        if mouse_pos[0] >= 0 and mouse_pos[0] < 1280:
            if mouse_pos[1] > 640 and mouse_pos[1] <= WINDOW_HEIGHT:
                return True
        return False

    def _click_on_right_panel(self):
        mouse_pos = get_fixed_mouse_pos()
        if mouse_pos[0] >= 1280 and mouse_pos[0] < WINDOW_WIDTH:
                return True
        return False

    def _tower_button_got_pressed(self):
        mouse_pos = get_fixed_mouse_pos()
        for sprite in self._tower_button_sprites:
            if sprite.get_rect().collidepoint(mouse_pos):
                if self._pressed_tower_button != None:
                    self._pressed_tower_button.set_pressed_state(False)
                sprite.set_pressed_state(True)
                self._pressed_tower_button = sprite
                return True
        return False

    def _update_and_draw_screen(self, dt):
        # stops the game when settings menu opened
        if not self._settings_menu_status:
            self._level_sprites.update(dt)
            self._tower_sprites.update(dt)
            self._interface_sprites.update(dt)
            self._tower_button_sprites.update(dt)

        self._display_surface.fill('#A020F0')
        self._level_sprites.draw()
        self._interface_surface.blit(self._display_surface, (0, 0))
        self._interface_sprites.draw()
        self._tower_button_sprites.draw()

    def run_the_level(self):
        dt = self._clock.tick() / 1000

        # exit the game
        if pygame.mouse.get_just_pressed()[0]:
            if self._exit_button.get_rect().collidepoint(get_fixed_mouse_pos()):
                self._running = False
                
        # check if tower is still placing
        if self._tower_is_being_placed:
            if self._tower_to_be_placed.get_placement_state():
                self._tower_is_being_placed = False
                self._tower_to_be_placed = None
                self._pressed_tower_button.set_pressed_state(False)
                self._pressed_tower_button = None
        
        # stop placing tower
        if pygame.mouse.get_just_pressed()[2] == True:
            if self._tower_is_being_placed:
                self._tower_is_being_placed = False
                self._tower_to_be_placed.delete_tower()
                self._tower_to_be_placed = None
                self._pressed_tower_button.set_pressed_state(False)
                self._pressed_tower_button = None

        if pygame.mouse.get_just_pressed()[0] == True:
            # check if settings menu is opened
            if self._settings_menu_status:
                # setting menu functionallity
                if self._continue_button.get_rect().collidepoint(get_fixed_mouse_pos()):
                    self._settings_menu_status = False
                    self._option_ramka.hasToBeShown = False
                    self._continue_button.hasToBeShown = False
                    self._settings_button.hasToBeShown = False
                    self._quit_button.hasToBeShown = False
                        
                elif self._settings_button.get_rect().collidepoint(get_fixed_mouse_pos()):
                    pass

                elif self._quit_button.get_rect().collidepoint(get_fixed_mouse_pos()):
                    self._running = False
                return None
            
            # check tower button press
            if self._click_on_bottom_panel():
                # bottom panel functionality
                if self._tower_button_got_pressed():
                    self._spawn_tower()
                    return None
                return None

            # check right panel press
            if self._click_on_right_panel():
                # right panel functionality
                if self._gear_button.get_rect().collidepoint(get_fixed_mouse_pos()):
                    self._settings_menu_status = True
                    self._option_ramka = OptionRamka(self._interface_sprites)
                    self._continue_button = ContinueButton(self._interface_sprites)
                    self._settings_button = SettingsButton(self._interface_sprites)
                    self._quit_button = QuitButton(self._interface_sprites)
        

        self._castle.take_damage()
        self._castle.take_money()

        # spawn enemies
        self._enemy_spawn_timer()
        # self._spawn_entity()

        self._update_and_draw_screen(dt) 
