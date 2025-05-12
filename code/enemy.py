from settings import *
from numpy import sign
from groups import EnemySprites

class Enemy(pygame.sprite.Sprite):
    def __init__(self, surf, spawn_line, turn_lines, groups):
        super().__init__(groups)
        self.isenemie = True
        
        start_points, end_points = spawn_line[0], spawn_line[1]

        t = random.random()
        spawn_x = random.randint(round(start_points[0]), round(end_points[0]))
        spawn_y = random.randint(round(start_points[1]), round(end_points[1]))
        
        self._image = surf
        # self._rect = pygame.FRect(0, 0, 16, 16)
        # self._rect.midbottom = (spawn_x, spawn_y)
        self._rect = self._image.get_frect(centerx = spawn_x, bottom = spawn_y)
        

        self._hitbox = pygame.FRect(self._rect)
        
        self._direction = pygame.Vector2(1, 0) # стартовое направление
        self._speed = 10
        self._health = 100
        self._elementatr = 'normal' # элемент врага
        self._is_dead = False
        
        # set lines
        self._next_line = 0
        self._turn_lines = turn_lines

        # set distance to next turn line
        self._set_next_line_distance()

        self._turned_lines = set()  # отслеживание уже использованных линий
        self._traveled_distance = 0

    # getters and setters
    def get_image(self):
        return self._image
    
    def get_rect(self):
        return self._rect

    def get_traveled_distance(self):
        return self._traveled_distance
    
    def is_died(self):
        return self._is_dead
    
    # functions
    def deal_damage(self, damage, damage_type):
        if self._elementatr == 'normal' and damage_type == 'normal':
            damage = damage * 1.0
        elif self._elementatr == 'normal' and damage_type != 'normal':
            damage = damage * 0.7
        elif self._elementatr != 'normal' and damage_type == 'normal':
            damage = damage * 0.7

        elif (self._elementatr == 'red' and damage_type == 'green') or (
            self._elementatr == 'blue' and damage_type == 'red') or (
            self._elementatr == 'yellow' and damage_type == 'blue') or (
            self._elementatr == 'green' and damage_type == 'yellow'):
                damage = damage * 1.5
        elif (self._elementatr == 'red' and damage_type == 'blue') or (
            self._elementatr == 'blue' and damage_type == 'yellow') or (
            self._elementatr == 'yellow' and damage_type == 'green') or (
            self._elementatr == 'green' and damage_type == 'red'):
                damage = damage * 0.5
        elif (self._elementatr == 'red' and damage_type == 'red') or (
            self._elementatr == 'blue' and damage_type == 'blue') or (
            self._elementatr == 'yellow' and damage_type == 'yellow') or (
            self._elementatr == 'green' and damage_type == 'green'):
                damage = damage * 0.8
        elif (self._elementatr == 'red' and damage_type == 'yellow') or (
            self._elementatr == 'blue' and damage_type == 'green') or (
            self._elementatr == 'yellow' and damage_type == 'red') or (
            self._elementatr == 'green' and damage_type == 'blue'):
                damage = damage * 1.0

        self._health -= damage
        if self._health <= 0:
            self.kill()
            self._is_dead = True
            del self

    def _move(self, dt):
        # Движение
        current_pos = pygame.Vector2(self._rect.center)
        self._rect.center += self._direction * self._speed * dt
        new_pos = pygame.Vector2(self._rect.center)
        self._traveled_distance += new_pos.distance_to(current_pos)
    
    def _set_next_line_distance(self):
        turn_line_points = self._turn_lines[self._next_line].get_points()
        bottom_center = self._rect.midbottom
        self._distance = ((turn_line_points[1][0] - turn_line_points[0][0]) * (turn_line_points[0][1] - bottom_center[1]) -
                            (turn_line_points[0][0] - bottom_center[0]) * (turn_line_points[1][1] - turn_line_points[0][1])
                        ) / math.sqrt(pow(turn_line_points[1][0] - turn_line_points[0][0], 2) 
                                        + pow(turn_line_points[1][1] - turn_line_points[0][1], 2))
    
    def _make_a_turn(self):
            turn_line = self._turn_lines[self._next_line]

            if turn_line.get_type() == "1" and self._direction.x == 1:           # шёл направо →
                self._direction = pygame.Vector2(0, 1)                # поворачивает вниз ↓

            elif turn_line.get_type() == "1" and self._direction.x == -1:        # шёл налево ←
                self._direction = pygame.Vector2(0, -1)               # поворачивает вверх ↑

            elif turn_line.get_type() == "1" and self._direction.y == 1:         # шёл вниз ↓
                self._direction = pygame.Vector2(1, 0)                # поворачивает направо →

            elif turn_line.get_type() == "1" and self._direction.y == -1:        # шёл вверх ↑
                self._direction = pygame.Vector2(-1, 0)               # поворачивает налево ←
            

            elif turn_line.get_type() == "2" and self._direction.x == 1:         # шёл направо →
                self._direction = pygame.Vector2(0, -1)               # поворачивает вверх ↑

            elif turn_line.get_type() == "2" and self._direction.x == -1:        # шёл налево ←
                self._direction = pygame.Vector2(0, 1)                # поворачивает вниз ↓

            elif turn_line.get_type() == "2" and self._direction.y == 1:         # шёл вниз ↓
                self._direction = pygame.Vector2(-1, 0)               # поворачивает налево ←

            elif turn_line.get_type() == "2" and self._direction.y == -1:        # шёл вверх ↑
                self._direction = pygame.Vector2(1, 0)                # поворачивает направо →

            self._turned_lines.add(self._next_line)
            self._next_line = self._next_line + 1
            self._set_next_line_distance()

    def _check_turn(self):
        if self._next_line not in self._turned_lines:
            turn_line = self._turn_lines[self._next_line]
            bottom_center = self._rect.midbottom

            turn_line_points = turn_line.get_points()    # two point: beginning and end
            distance = ((turn_line_points[1][0] - turn_line_points[0][0]) * (turn_line_points[0][1] - bottom_center[1]) -
                            (turn_line_points[0][0] - bottom_center[0]) * (turn_line_points[1][1] - turn_line_points[0][1])
                        ) / math.sqrt(pow(turn_line_points[1][0] - turn_line_points[0][0], 2) 
                                        + pow(turn_line_points[1][1] - turn_line_points[0][1], 2))
            if sign(self._distance) != sign(distance):
                return True
            return False
    
    def _load_images(self, enemy_type, scale):
        self._frames = []
        for foldfer_path, sub_folders, file_names in walk(join('Game', 'Assets', 'Enemies', enemy_type, 'movement')):
            if file_names:
                for file_name in sorted(file_names, key = lambda name: int(name.split('.')[0])):
                    full_path = join(foldfer_path, file_name)
                    surf = pygame.image.load(full_path).convert_alpha()
                    width, height = surf.get_size()
                    surf = pygame.transform.scale(surf, (width * scale, height * scale))
                    self._frames.append(surf)
        print (self._frames)

    def _animate(self, dt):
        
        self._frame_index = self._frame_index + 5 * dt
        self._image = self._frames[int(self._frame_index) % len(self._frames)]
        if self._direction.x < 0:
            self._image = pygame.transform.flip(self._image, True, False)


    def attack(self, target):
        pass
        # current_time = pygame.time.get_ticks() / 1000.0
        # if current_time - self.last_attack_time >= self.attack_cooldown:
        #     target.health -= self.damage
        #     self.last_attack_time = current_time


    def update(self, dt):
        self._move(dt)
        self._animate(dt)
        if self._check_turn():
            if self._next_line + 1 == len(self._turn_lines):
                self.kill()
                self._is_dead = True
                del self
            else:
                self._make_a_turn()
            