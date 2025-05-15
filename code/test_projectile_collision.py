# import sys
# sys.path.append("..")

from settings import *
from entity_factories import EnemySpawner
from Towers.tower_projectile_types import CannonProjectile
from map_tiles import Turn_lines
from groups import LevelSprites, EnemySprites
import unittest
import random

# This test checks for enemy and projectile collision (on 1000 each at the same time)
class EnemyProjectileCollision(unittest.TestCase):
    def test_projectile_enemy_collide(self):
        pygame.init()
        pygame.display.set_mode()
        map = load_pygame(join('Game', 'Map', 'Tower Defense map.tmx'))
        turn_lines = [] 
        spawn_line = None

        for obj in map.get_layer_by_name("Objects"):
            if obj.name == "Spawn":
                spawn_line = [(p[0], p[1]) for p in obj.points]
                
            elif obj.type in ("1", "2", "3"): 
                polygon_points = [(p[0], p[1]) for p in obj.points]
                turn_line = Turn_lines(polygon_points, obj.name, obj.type)
                turn_lines.append(turn_line)
        turn_lines.sort(key = lambda line: int(line.get_name()))

        display_surface = pygame.Surface((LEVEL_SCREEN_WIDTH, LEVEL_SCREEN_HEIGHT))
        level_sprites = LevelSprites(display_surface)
        enemy_sprites = EnemySprites(display_surface)

        enemy_types = ['bimba', 'blue_slime', 'fish', 'flying_snake', 'ghost', 
                        'golem', 'red_elemental', 'rogue', 'spearsman', 
                        'swordsman', 'tankman']
        enemies = []
        enemy_spawner = EnemySpawner(spawn_line, turn_lines, enemy_sprites, level_sprites)
        for i in range(1000):
            enemies.append(enemy_spawner.create_enemy(random.choice(enemy_types)))

        projectiles = []
        for i in range(1000):
            projectiles.append(CannonProjectile((100, 100), enemies[i], 1000, 300, None, level_sprites))

        clock = pygame.time.Clock()
        running = True
        if len(level_sprites) == 2:
            while running:
                dt = clock.tick() / 1000
                if len(level_sprites) == 0:
                    self.assertEqual(len(level_sprites), 0)
                    running = False
                level_sprites.update(dt)
                    

if __name__ == '__main__':
    unittest.main()
