from settings import *
from map_tiles import *
from sprites import Portal
from groups import LevelSprites, TowerSprites, EnemySprites
from Towers.tower_types import *
from enemy import Enemy
from enemies_types import *

class Level:
    def __init__(self):
        self._display_surface = pygame.display.get_surface()
        self._clock = pygame.time.Clock()

        # groups 
        self._level_sprites = LevelSprites()
        self._collison_sprites = pygame.sprite.Group()
        self._tower_sprites = TowerSprites()
        self._enemy_sprites = EnemySprites()

        # tower grid
        self._tower_grid = [[]]
        for i in range(int(WINDOW_HEIGHT / TILE_SIZE)):
            for j in range(int(WINDOW_WIDTH / TILE_SIZE)):
                self._tower_grid[i].append(False)
            self._tower_grid.append([])

        # tower placing check
        self._tower_to_be_placed = None
        self._tower_is_being_placed = False

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

    def _check_tower_being_placed(self):
        if self._tower_is_being_placed:
            self._tower_to_be_placed.delete_tower()
            self._tower_to_be_placed = None
        else:
            self._tower_is_being_placed = True

    def run_the_level(self):
        dt = self._clock.tick() / 1000
        if self._tower_is_being_placed:
            if self._tower_to_be_placed.get_placement_state():
                self._tower_is_being_placed = False
                self._tower_to_be_placed = None

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
            swordsman(self._spawn_line, self._turn_lines, (self._level_sprites, self._enemy_sprites)) 

        self._level_sprites.update(dt)
        self._tower_sprites.update(dt)

        self._display_surface.fill('#A020F0')
        self._level_sprites.draw()
        
        # # Проверка линий
        # for polygon in self._turn_lines:
        #     pygame.draw.polygon(self._display_surface, 'red', polygon.get_points(), 2)
        # # Отладка: рисуем линию спавна
        # pygame.draw.polygon(self._display_surface, 'blue', self._spawn_line, 2)

        pygame.display.flip()

