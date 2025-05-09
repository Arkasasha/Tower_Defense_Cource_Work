from settings import *
from map_tiles import *
from sprites import Portal
from groups import LevelSprites, TowerSprites, EnemySprites
from Towers.tower_types import Cannon
from enemy import Enemy
from Enemies import *

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
                
            elif obj.type in ("1", "2"): 
                polygon_points = [(p[0], p[1]) for p in obj.points]
                turn_line = Turn_lines(polygon_points, obj.name, obj.type)
                self._turn_lines.append(turn_line)
        self._turn_lines.sort(key = lambda line: int(line.get_name()))


        # Load a portal
        portal_surf = pygame.image.load(join('Game', 'Assets', 'additional', 'Portal', 'portal.png')).convert_alpha()
        Portal(portal_surf, self._level_sprites)

        # enemy_surf = pygame.image.load(join('Game', 'Assets', 'Enemies', 'swordsman', 'movement', '0.png')).convert_alpha()
        # swordsman(enemy_surf, self.spawn_line, self.turn_lines, self.level_sprites)

        # enemy_surf = pygame.image.load(join('Game', 'Assets', 'Enemies', 'tankman', 'movement', '0.png')).convert_alpha()
        # tankman(enemy_surf, self.spawn_line, self.turn_lines, self.level_sprites)

        # enemy_surf = pygame.image.load(join('Game', 'Assets', 'Enemies', 'spearsman', 'movement', '0.png')).convert_alpha()
        # spearsman(enemy_surf, self.spawn_line, self.turn_lines, self.level_sprites)

        # enemy_surf = pygame.image.load(join('Game', 'Assets', 'Enemies', 'fish', 'movement', '0.png')).convert_alpha()
        # fish(enemy_surf, self.spawn_line, self.turn_lines, self.level_sprites)

        # enemy_surf = pygame.image.load(join('Game', 'Assets', 'Enemies', 'flying_snake', 'movement', '00.png')).convert_alpha()
        # flying_snake(enemy_surf, self.spawn_line, self.turn_lines, self.level_sprites)

        # enemy_surf = pygame.image.load(join('Game', 'Assets', 'Enemies', 'rogue', 'movement', '0.png')).convert_alpha()
        # rogue(enemy_surf, self.spawn_line, self.turn_lines, self.level_sprites)

    def run_the_level(self):
        dt = self.clock.tick() / 1000
        enemy_surf = pygame.image.load(join('Game', 'Assets', 'Enemies', 'bimba', 'movement', '0.png')).convert_alpha()
        
        keys = pygame.key.get_just_pressed()
        if keys[pygame.K_o]:
            Cannon(self._tower_grid, (self._level_sprites, self._tower_sprites))
        if keys[pygame.K_p]:
            Enemy(enemy_surf, self._spawn_line, self._turn_lines, (self._level_sprites, self._enemy_sprites)) 

        self._level_sprites.update(dt)
        self._tower_sprites.update(dt)

        self._display_surface.fill('#A020F0')
        self._level_sprites.draw()
        
        # Проверка линий
        for polygon in self._turn_lines:
            pygame.draw.polygon(self._display_surface, 'red', polygon.get_points(), 2)
        # Отладка: рисуем линию спавна
        pygame.draw.polygon(self._display_surface, 'blue', self._spawn_line, 2)

        pygame.display.flip()

