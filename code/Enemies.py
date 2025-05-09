from settings import *
from enemy import Enemy

class swordsman(Enemy):
    def __init__(self, surf, spawn_line, turn_lines, groups):
        super().__init__(surf, spawn_line, turn_lines, groups)
        self.movement_type = 'ground'
        self.attripute = 'normal'
        self.speed = 20
        self.health = 100
        self.damage = 10
        self.attack_cooldown = 1.0
        self.last_attack_time = 0.0
        self.attack_range = 50
        self.attack_maintower = 1


class tankman(Enemy):
    def __init__(self, surf, spawn_line, turn_lines, groups):
        super().__init__(surf, spawn_line, turn_lines, groups)
        self.movement_type = 'ground'
        self.attripute = 'normal'
        self.speed = 15
        self.health = 160
        self.damage = 20
        self.attack_cooldown = 1.5
        self.last_attack_time = 0.0
        self.attack_range = 50
        self.attack_maintower = 1


class rogue(Enemy):
    def __init__(self, surf, spawn_line, turn_lines, groups):
        super().__init__(surf, spawn_line, turn_lines, groups)
        self.movement_type = 'ground'
        self.attripute = 'normal'
        self.speed = 35
        self.health = 80
        self.damage = 8
        self.attack_cooldown = 0.5
        self.last_attack_time = 0.0
        self.attack_range = 50
        self.attack_maintower = 1

    
class spearsman(Enemy):
    def __init__(self, surf, spawn_line, turn_lines, groups):
        super().__init__(surf, spawn_line, turn_lines, groups)
        self.movement_type = 'ground'
        self.attripute = 'normal'
        self.speed = 15
        self.health = 120
        self.damage = 12
        self.attack_cooldown = 1.2
        self.last_attack_time = 0.0
        self.attack_range = 50
        self.attack_maintower = 1


class fish(Enemy):
    def __init__(self, surf, spawn_line, turn_lines, groups):
        super().__init__(surf, spawn_line, turn_lines, groups)
        self.movement_type = 'ground'
        self.attripute = 'blue'
        self.speed = 25
        self.health = 90
        self.damage = 7
        self.attack_cooldown = 1.0
        self.last_attack_time = 0.0
        self.attack_range = 50
        self.attack_maintower = 1


class flying_snake(Enemy):
    def __init__(self, surf, spawn_line, turn_lines, groups):
        super().__init__(surf, spawn_line, turn_lines, groups)
        self.movement_type = 'air'
        self.attripute = 'green'
        self.speed = 15
        self.health = 200
        self.damage = 24
        self.attack_cooldown = 1.5
        self.last_attack_time = 0.0
        self.attack_range = 50
        self.attack_maintower = 1


class golem(Enemy):
    def __init__(self, surf, spawn_line, turn_lines, groups):
        super().__init__(surf, spawn_line, turn_lines, groups)
        self.movement_type = 'ground'
        self.attripute = 'yellow'
        self.speed = 10
        self.health = 450
        self.damage = 60
        self.attack_cooldown = 2.5
        self.last_attack_time = 0.0
        self.attack_range = 50
        self.attack_maintower = 2


class bimba(Enemy):
    def __init__(self, surf, spawn_line, turn_lines, groups):
        super().__init__(surf, spawn_line, turn_lines, groups)
        self.movement_type = 'ground'
        self.attripute = 'red'
        self.speed = 50
        self.health = 45
        #self.damage = 100   
        #self.attack_cooldown = 1.0
        #self.last_attack_time = 0.0
        #self.attack_range = 50
        self.attack_maintower = 4


class red_elemental(Enemy):
    def __init__(self, surf, spawn_line, turn_lines, groups):
        super().__init__(surf, spawn_line, turn_lines, groups)
        self.movement_type = 'air'
        self.attripute = 'red'
        self.speed = 15
        self.health = 160
        self.damage = 22
        self.attack_cooldown = 2.0
        self.last_attack_time = 0.0
        self.attack_range = 50
        self.attack_maintower = 2


class blue_elemental(Enemy):
    def __init__(self, surf, spawn_line, turn_lines, groups):
        super().__init__(surf, spawn_line, turn_lines, groups)
        self.movement_type = 'air'
        self.attripute = 'blue'
        self.speed = 15
        self.health = 160
        self.damage = 22
        self.attack_cooldown = 2.0
        self.last_attack_time = 0.0
        self.attack_range = 50
        self.attack_maintower = 2


class green_elemental(Enemy):
    def __init__(self, surf, spawn_line, turn_lines, groups):
        super().__init__(surf, spawn_line, turn_lines, groups)
        self.movement_type = 'air'
        self.attripute = 'green'
        self.speed = 15
        self.health = 160
        self.damage = 22
        self.attack_cooldown = 2.0
        self.last_attack_time = 0.0
        self.attack_range = 50
        self.attack_maintower = 2


class yellow_elemental(Enemy):
    def __init__(self, surf, spawn_line, turn_lines, groups):
        super().__init__(surf, spawn_line, turn_lines, groups)
        self.movement_type = 'air'
        self.attripute = 'yellow'
        self.speed = 15
        self.health = 160
        self.damage = 22
        self.attack_cooldown = 2.0
        self.last_attack_time = 0.0
        self.attack_range = 50
        self.attack_maintower = 2


class red_slime(Enemy):
    def __init__(self, surf, spawn_line, turn_lines, groups):
        super().__init__(surf, spawn_line, turn_lines, groups)
        self.movement_type = 'ground'
        self.attripute = 'red'
        self.speed = 25
        self.health = 70
        self.damage = 6
        self.attack_cooldown = 0.7
        self.last_attack_time = 0.0
        self.attack_range = 50
        self.attack_maintower = 1

    
class blue_slime(Enemy):
    def __init__(self, surf, spawn_line, turn_lines, groups):
        super().__init__(surf, spawn_line, turn_lines, groups)
        self.movement_type = 'ground'
        self.attripute = 'blue'
        self.speed = 25
        self.health = 70
        self.damage = 6
        self.attack_cooldown = 0.7
        self.last_attack_time = 0.0
        self.attack_range = 50
        self.attack_maintower = 1


class Loki(Enemy):
    def __init__(self, surf, spawn_line, turn_lines, groups):
        super().__init__(surf, spawn_line, turn_lines, groups)
        self.movement_type = 'ground'
        self.attripute = 'normal'
        self.speed = 35
        self.health = 160
        self.damage = 24
        self.attack_cooldown = 0.5
        self.last_attack_time = 0.0
        self.attack_range = 50
        self.attack_maintower = 3


class ghost(Enemy):                                                # It is invisible for the towers, can be killed only by splash
    def __init__(self, surf, spawn_line, turn_lines, groups):
        super().__init__(surf, spawn_line, turn_lines, groups)
        self.movement_type = 'ground'
        self.attripute = 'normal'
        self.speed = 30
        self.health = 80
        #self.damage = 0
        #self.attack_cooldown = 1.0
        #self.last_attack_time = 0.0
        #self.attack_range = 50
        self.attack_maintower = 1


class wizard(Enemy):                                               # Can attack towers, from the far distance
    def __init__(self, surf, spawn_line, turn_lines, groups):
        super().__init__(surf, spawn_line, turn_lines, groups)
        self.movement_type = 'ground'
        self.attripute = 'normal'
        self.speed = 15
        self.health = 70
        self.damage = 15
        self.attack_cooldown = 2.0
        self.last_attack_time = 0.0
        self.attack_range = 50
        self.attack_maintower = 1


class BOSS(Enemy):
    def __init__(self, surf, spawn_line, turn_lines, groups):
        super().__init__(surf, spawn_line, turn_lines, groups)
        self.movement_type = 'ground'
        self.attripute = 'normal'
        self.speed = 10
        self.health = 1000
        self.damage = 50
        self.attack_cooldown = 2.0
        self.last_attack_time = 0.0
        self.attack_range = 50
        self.attack_maintower = 3