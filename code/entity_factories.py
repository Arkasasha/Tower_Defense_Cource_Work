from settings import *
from Towers.tower_types import *
from enemies_types import *

class EnemySpawner:
    def __init__(self, spawn_line, turn_lines, enemy_sprites, level_sprites):
        self._enemy_sprites = enemy_sprites
        self._level_sprites = level_sprites

        self._spawn_line = spawn_line
        self._turn_lines = turn_lines

    def create_enemy(self, enemy_type):
        if enemy_type == 'LOKI':
            Loki(self._spawn_line, self._turn_lines, (self._level_sprites, self._enemy_sprites)) 
        elif enemy_type == 'tankman':
            tankman(self._spawn_line, self._turn_lines, (self._level_sprites, self._enemy_sprites))
        elif enemy_type == 'spearsmen':
            spearsman(self._spawn_line, self._turn_lines, (self._level_sprites, self._enemy_sprites))
        elif enemy_type == 'fish':
            fish(self._spawn_line, self._turn_lines, (self._level_sprites, self._enemy_sprites))
        elif enemy_type == 'flying_snake':
            flying_snake(self._spawn_line, self._turn_lines, (self._level_sprites, self._enemy_sprites))
        elif enemy_type == 'rogue':
            rogue(self._spawn_line, self._turn_lines, (self._level_sprites, self._enemy_sprites))
        elif enemy_type == 'red_elemental':
            red_elemental(self._spawn_line, self._turn_lines, (self._level_sprites, self._enemy_sprites))
        elif enemy_type == 'blue_slime':
            blue_slime(self._spawn_line, self._turn_lines, (self._level_sprites, self._enemy_sprites))
        elif enemy_type == 'golem':
            golem(self._spawn_line, self._turn_lines, (self._level_sprites, self._enemy_sprites))
        elif enemy_type == 'ghost':
            ghost(self._spawn_line, self._turn_lines, (self._level_sprites, self._enemy_sprites))
        elif enemy_type == 'bimba':
            bimba(self._spawn_line, self._turn_lines, (self._level_sprites, self._enemy_sprites))
        else:
            raise ValueError(f"Unknown enemy type: {enemy_type}")

class TowerSpawner:
    def __init__(self, tower_grid, level_sprites, tower_sprites):
        self._tower_grid = tower_grid
        self._level_sprites = level_sprites
        self._tower_sprites = tower_sprites

    def create_tower(self, tower_type):
        if tower_type == 'cannon':
            return Cannon(self._tower_grid, (self._level_sprites, self._tower_sprites))
        elif tower_type == 'mega_cannon':
            return MegaCannon(self._tower_grid, (self._level_sprites, self._tower_sprites))
        elif tower_type == 'reactive_cannon':
            return ReactiveCannon(self._tower_grid, (self._level_sprites, self._tower_sprites))
        elif tower_type == 'Xbow':
            return XBow(self._tower_grid, (self._level_sprites, self._tower_sprites))
        elif tower_type == 'wizard_tower':
            return WizardTower(self._tower_grid, (self._level_sprites, self._tower_sprites))
        elif tower_type == 'magic_cannon':
            return MagicaCannon(self._tower_grid, (self._level_sprites, self._tower_sprites))
        elif tower_type == 'drotik_tower':
            return DrotikTower(self._tower_grid, (self._level_sprites, self._tower_sprites))
        elif tower_type == 'mega_xbow':
            return MegaXBow(self._tower_grid, (self._level_sprites, self._tower_sprites))
        else:
            raise ValueError(f"Unknown tower type: {tower_type}")







