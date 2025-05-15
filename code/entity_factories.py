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
        if enemy_type == 'bimba':
            return bimba(self._spawn_line, self._turn_lines, (self._level_sprites, self._enemy_sprites))
        elif enemy_type == 'blue_elemental':
            pass
        elif enemy_type == 'blue_slime':
            return blue_slime(self._spawn_line, self._turn_lines, (self._level_sprites, self._enemy_sprites))
        elif enemy_type == 'fish':
            return fish(self._spawn_line, self._turn_lines, (self._level_sprites, self._enemy_sprites))
        elif enemy_type == 'flying_snake':
            return flying_snake(self._spawn_line, self._turn_lines, (self._level_sprites, self._enemy_sprites))
        elif enemy_type == 'ghost':
            return ghost(self._spawn_line, self._turn_lines, (self._level_sprites, self._enemy_sprites))
        elif enemy_type == 'golem':
            return golem(self._spawn_line, self._turn_lines, (self._level_sprites, self._enemy_sprites))
        elif enemy_type == 'green_elemental':
            pass  
        elif enemy_type == 'LOKI':
            return Loki(self._spawn_line, self._turn_lines, (self._level_sprites, self._enemy_sprites))
        elif enemy_type == 'red_elemental':
            return red_elemental(self._spawn_line, self._turn_lines, (self._level_sprites, self._enemy_sprites))
        elif enemy_type == 'red_slime':
            pass
        elif enemy_type == 'rogue':
            return rogue(self._spawn_line, self._turn_lines, (self._level_sprites, self._enemy_sprites))
        elif enemy_type == 'spearsman':
            return spearsman(self._spawn_line, self._turn_lines, (self._level_sprites, self._enemy_sprites))
        elif enemy_type == 'swordsman':
            return swordsman(self._spawn_line, self._turn_lines, (self._level_sprites, self._enemy_sprites))
        elif enemy_type == 'tankman':
            return tankman(self._spawn_line, self._turn_lines, (self._level_sprites, self._enemy_sprites))
        elif enemy_type == 'wizard':
            pass
        elif enemy_type == 'yellow_elemental':
            pass
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







