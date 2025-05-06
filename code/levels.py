from settings import *
from map_tiles import *
from sprites import Portal
from groups import LevelSprites, TowerSprites
from tower import Tower
from tower_types import Cannon
from enemy import Enemy

class Level:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()
        self.clock = pygame.time.Clock()

        # groups 
        self.level_sprites = LevelSprites()
        self.collison_sprites = pygame.sprite.Group()
        self.tower_sprites = TowerSprites()

        # tower grid
        self.tower_grid = [[]]
        for i in range(int(WINDOW_HEIGHT / TILE_SIZE)):
            for j in range(int(WINDOW_WIDTH / TILE_SIZE)):
                self.tower_grid[i].append(False)
            self.tower_grid.append([])

        self.setup()
    
    def setup(self):
        map = load_pygame(join('Game', 'Map', 'Tower Defense map.tmx'))

        # Load terrain
        for x, y, image in map.get_layer_by_name('Ground').tiles():
            Ground(image, (x * TILE_SIZE, y * TILE_SIZE), self.level_sprites)

        for x, y, image in map.get_layer_by_name('River').tiles():
            River(image, (x * TILE_SIZE, y * TILE_SIZE), self.level_sprites)
        
        for x, y, image in map.get_layer_by_name('Path').tiles():
            Path(image, (x * TILE_SIZE, y * TILE_SIZE), self.level_sprites)

        for x, y, image in map.get_layer_by_name('Bridge').tiles():
            Bridge(image, (x * TILE_SIZE, y * TILE_SIZE), self.level_sprites)

        forests = [map.get_layer_by_name('The Forest').tiles(), 
                       map.get_layer_by_name('The Forest 2').tiles()]
        for forest in forests:
            for x, y, image in forest:
                Forest(image, (x * TILE_SIZE, y * TILE_SIZE), self.level_sprites)
        
        for x, y, image in map.get_layer_by_name('Castle').tiles():
            Castle(image, (x * TILE_SIZE, y * TILE_SIZE), self.level_sprites)

        for x, y, image in map.get_layer_by_name('Add').tiles():
            Decoration(image, (x * TILE_SIZE, y * TILE_SIZE), self.level_sprites)

        #Load objects
        self.turn_lines = [] 

        for obj in map.get_layer_by_name("Objects"):
            if obj.name == "Spawn":
                self.spawn_line = [(p[0], p[1]) for p in obj.points]
                
            elif obj.type in ("1", "2"): 
                polygon_points = [(p[0], p[1]) for p in obj.points]
                turn_line = Turn_lines(polygon_points, obj.name, obj.type)
                self.turn_lines.append(turn_line)
        self.turn_lines.sort(key = lambda line: int(line.name))


        # Load a portal
        portal_surf = pygame.image.load(join('Game', 'Assets', 'Enemies', 'bimba', 'movement', '0.png')).convert_alpha()
        Portal(portal_surf, self.level_sprites)

        enemy_surf = pygame.image.load(join('Game', 'Assets', 'Enemies', 'bimba', 'movement', '0.png')).convert_alpha()
        Enemy(enemy_surf, self.spawn_line, self.turn_lines, self.level_sprites)  

    def run_the_level(self):
        dt = self.clock.tick() / 1000
        
        keys = pygame.key.get_just_pressed()
        if keys[pygame.K_o]:
            Cannon(self.tower_grid, (self.level_sprites, self.tower_sprites))

        self.level_sprites.update(dt)
        self.tower_sprites.update(dt)

        self.display_surface.fill('#A020F0')
        self.level_sprites.draw()
        
        # Проверка линий
        for polygon in self.turn_lines:
            pygame.draw.polygon(self.display_surface, 'red', polygon.points, 2)
        # Отладка: рисуем линию спавна
        pygame.draw.polygon(self.display_surface, 'blue', self.spawn_line, 2)

        pygame.display.flip()

