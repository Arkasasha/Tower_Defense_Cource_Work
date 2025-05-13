from settings import *
from enemy import Enemy

class swordsman(Enemy):
    def __init__(self, spawn_line, turn_lines, groups):
        self._frame_index = 0
        self._load_images('swordsman', 1.3)
        surf = self._frames[0]
        super().__init__(surf, spawn_line, turn_lines, groups)

        self._stats_setup()

    def _stats_setup(self):
        self._movement_type = 'ground'
        self._elementatr = 'normal'
        self._speed = 20
        self._health = 100
        self._damage = 10
        self._attack_cooldown = 1.0
        self._last_attack_time = 0.0
        self._attack_range = 50
        self._attack_maintower = 1

class tankman(Enemy):
    def __init__(self, spawn_line, turn_lines, groups):
        self._frame_index = 0
        self._load_images('tankman', 1.4)
        surf = self._frames[0]
        super().__init__(surf, spawn_line, turn_lines, groups)

        self._stats_setup()

    def _stats_setup(self):
        self._movement_type = 'ground'
        self._elementatr = 'normal'
        self._speed = 15
        self._health = 160
        self._damage = 20
        self._attack_cooldown = 1.5
        self._last_attack_time = 0.0
        self._attack_range = 50
        self._attack_maintower = 1


class rogue(Enemy):
    def __init__(self, spawn_line, turn_lines, groups):
        self._frame_index = 0
        self._load_images('rogue', 1.3)
        surf = self._frames[0]
        super().__init__(surf, spawn_line, turn_lines, groups)

        self._stats_setup()

    def _stats_setup(self):
        self._movement_type = 'ground'
        self._elementatr = 'normal'
        self._speed = 35
        self._health = 80
        self._damage = 8
        self._attack_cooldown = 0.5
        self._last_attack_time = 0.0
        self._attack_range = 50
        self._attack_maintower = 1

    
class spearsman(Enemy):
    def __init__(self, spawn_line, turn_lines, groups):
        self._frame_index = 0
        self._load_images('spearsman', 1.4)
        surf = self._frames[0]
        super().__init__(surf, spawn_line, turn_lines, groups)

        self._stats_setup()

    def _stats_setup(self):
        self._movement_type = 'ground'
        self._elementatr = 'normal'
        self._speed = 15
        self._health = 120
        self._damage = 12
        self._attack_cooldown = 1.2
        self._last_attack_time = 0.0
        self._attack_range = 50
        self._attack_maintower = 1


class fish(Enemy):
    def __init__(self, spawn_line, turn_lines, groups):
        self._frame_index = 0
        self._load_images('fish', 1.5)
        surf = self._frames[0]
        super().__init__(surf, spawn_line, turn_lines, groups)

        self._stats_setup()

    def _stats_setup(self):
        self._movement_type = 'ground'
        self._elementatr = 'blue'
        self._speed = 25
        self._health = 90
        self._damage = 7
        self._attack_cooldown = 1.0
        self._last_attack_time = 0.0
        self._attack_range = 50
        self._attack_maintower = 1


class flying_snake(Enemy):
    def __init__(self, spawn_line, turn_lines, groups):
        self._frame_index = 0
        self._load_images('flying_snake', 1.2)
        surf = self._frames[0]
        super().__init__(surf, spawn_line, turn_lines, groups)

        self._stats_setup()

    def _stats_setup(self):
        self._movement_type = 'air'
        self._elementatr = 'green'
        self._speed = 15
        self._health = 200
        self._damage = 24
        self._attack_cooldown = 1.5
        self._last_attack_time = 0.0
        self._attack_range = 50
        self._attack_maintower = 1


class golem(Enemy):
    def __init__(self, spawn_line, turn_lines, groups):
        self._frame_index = 0
        self._load_images('golem', 1.8)
        surf = self._frames[0]
        super().__init__(surf, spawn_line, turn_lines, groups)

        self._stats_setup()

    def _stats_setup(self):
        self._movement_type = 'ground'
        self._elementatr = 'yellow'
        self._speed = 10
        self._health = 450
        self._damage = 60
        self._attack_cooldown = 2.5
        self._last_attack_time = 0.0
        self._attack_range = 50
        self._attack_maintower = 2


class bimba(Enemy):
    def __init__(self, spawn_line, turn_lines, groups):
        self._frame_index = 0
        self._load_images('bimba', 1.3)
        surf = self._frames[0]
        super().__init__(surf, spawn_line, turn_lines, groups)

        self._stats_setup()

    def _stats_setup(self):
        self._movement_type = 'ground'
        self._elementatr = 'red'
        self._speed = 50
        self._health = 45
        #self._damage = 100   
        #self._attack_cooldown = 1.0
        #self._last_attack_time = 0.0
        #self._attack_range = 50
        self._attack_maintower = 4


class red_elemental(Enemy):
    def __init__(self, spawn_line, turn_lines, groups):
        self._frame_index = 0
        self._load_images('red_elemental', 1.8)
        surf = self._frames[0]
        super().__init__(surf, spawn_line, turn_lines, groups)

        self._stats_setup()

    def _stats_setup(self):
        self._movement_type = 'air'
        self._elementatr = 'red'
        self._speed = 15
        self._health = 160
        self._damage = 22
        self._attack_cooldown = 2.0
        self._last_attack_time = 0.0
        self._attack_range = 50
        self._attack_maintower = 2


class blue_elemental(Enemy):
    def __init__(self, spawn_line, turn_lines, groups):
        self._frame_index = 0
        self._load_images('blue_elemental', 1.8)
        surf = self._frames[0]
        super().__init__(surf, spawn_line, turn_lines, groups)

        self._stats_setup()

    def _stats_setup(self):
        self._movement_type = 'air'
        self._elementatr = 'blue'
        self._speed = 15
        self._health = 160
        self._damage = 22
        self._attack_cooldown = 2.0
        self._last_attack_time = 0.0
        self._attack_range = 50
        self._attack_maintower = 2


class green_elemental(Enemy):
    def __init__(self, spawn_line, turn_lines, groups):
        self._frame_index = 0
        self._load_images('green_elemental', 1.8)
        surf = self._frames[0]
        super().__init__(surf, spawn_line, turn_lines, groups)

        self._stats_setup()

    def _stats_setup(self):
        self._movement_type = 'air'
        self._elementatr = 'green'
        self._speed = 15
        self._health = 160
        self._damage = 22
        self._attack_cooldown = 2.0
        self._last_attack_time = 0.0
        self._attack_range = 50
        self._attack_maintower = 2


class yellow_elemental(Enemy):
    def __init__(self, spawn_line, turn_lines, groups):
        self._frame_index = 0
        self._load_images('yellow_elemental', 1.8)
        surf = self._frames[0]
        super().__init__(surf, spawn_line, turn_lines, groups)

        self._stats_setup()

    def _stats_setup(self):
        self._movement_type = 'air'
        self._elementatr = 'yellow'
        self._speed = 15
        self._health = 160
        self._damage = 22
        self._attack_cooldown = 2.0
        self._last_attack_time = 0.0
        self._attack_range = 50
        self._attack_maintower = 2


class red_slime(Enemy):
    def __init__(self, spawn_line, turn_lines, groups):
        self._frame_index = 0
        self._load_images('red_slime', 1)
        surf = self._frames[0]
        super().__init__(surf, spawn_line, turn_lines, groups)

        self._stats_setup()

    def _stats_setup(self):
        self._movement_type = 'ground'
        self._elementatr = 'red'
        self._speed = 25
        self._health = 70
        self._damage = 6
        self._attack_cooldown = 0.7
        self._last_attack_time = 0.0
        self._attack_range = 50
        self._attack_maintower = 1

    
class blue_slime(Enemy):
    def __init__(self, spawn_line, turn_lines, groups):
        self._frame_index = 0
        self._load_images('blue_slime', 1)
        surf = self._frames[0]
        super().__init__(surf, spawn_line, turn_lines, groups)

        self._stats_setup()

    def _stats_setup(self):
        self._movement_type = 'ground'
        self._elementatr = 'blue'
        self._speed = 25
        self._health = 70
        self._damage = 6
        self._attack_cooldown = 0.7
        self._last_attack_time = 0.0
        self._attack_range = 50
        self._attack_maintower = 1


class Loki(Enemy):
    def __init__(self, spawn_line, turn_lines, groups):
        self._frame_index = 0
        self._load_images('LOKI', 1.8)
        surf = self._frames[0]
        super().__init__(surf, spawn_line, turn_lines, groups)

        self._stats_setup()

    def _stats_setup(self):
        self._movement_type = 'ground'
        self._elementatr = 'normal'
        self._speed = 35
        self._health = 160
        self._damage = 24
        self._attack_cooldown = 0.5
        self._last_attack_time = 0.0
        self._attack_range = 50
        self._attack_maintower = 3


class ghost(Enemy):                                                # It is invisible for the towers, can be killed only by splash
    def __init__(self, spawn_line, turn_lines, groups):
        self._frame_index = 0
        self._load_images('ghost', 1.2)
        surf = self._frames[0]
        super().__init__(surf, spawn_line, turn_lines, groups)

        self._stats_setup()

    def _stats_setup(self):
        self._movement_type = 'ground'
        self._elementatr = 'normal'
        self._speed = 30
        self._health = 80
        #self._damage = 0
        #self._attack_cooldown = 1.0
        #self._last_attack_time = 0.0
        #self._attack_range = 50
        self._attack_maintower = 1


class wizard(Enemy):                                               # Can attack towers, from the far distance
    def __init__(self, spawn_line, turn_lines, groups):
        self._frame_index = 0
        self._load_images('wizard', 1.3)
        surf = self._frames[0]
        super().__init__(surf, spawn_line, turn_lines, groups)

        self._stats_setup()

    def _stats_setup(self):
        self._movement_type = 'ground'
        self._elementatr = 'normal'
        self._speed = 15
        self._health = 70
        self._damage = 15
        self._attack_cooldown = 2.0
        self._last_attack_time = 0.0
        self._attack_range = 50
        self._attack_maintower = 1


class BOSS(Enemy):
    def __init__(self, spawn_line, turn_lines, groups):
        self._frame_index = 0
        self._load_images('BOSS')
        surf = self._frames[0]
        super().__init__(surf, spawn_line, turn_lines, groups)

        self._stats_setup()

    def _stats_setup(self):
        self._movement_type = 'ground'
        self._elementatr = 'normal'
        self._speed = 10
        self._health = 1000
        self._damage = 50
        self._attack_cooldown = 2.0
        self._last_attack_time = 0.0
        self._attack_range = 50
        self._attack_maintower = 3