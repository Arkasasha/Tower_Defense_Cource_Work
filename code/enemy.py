from settings import *
from numpy import sign

class Enemy(pygame.sprite.Sprite):
    def __init__(self, surf, spawn_line, turn_lines, groups):
        super().__init__(groups)
        self.isenemie = True
        
        start_points, end_points = spawn_line[0], spawn_line[1]

        t = random.random()
        spawn_x = random.randint(round(start_points[0]), round(end_points[0]))
        spawn_y = random.randint(round(start_points[1]), round(end_points[1]))
        
        self.image = surf
        # self.rect = pygame.FRect(0, 0, 16, 16)
        # self.rect.midbottom = (spawn_x, spawn_y)
        self.rect = self.image.get_frect(centerx = spawn_x, bottom = spawn_y)
        

        self.hitbox = pygame.FRect(self.rect)
        
        self.direction = pygame.Vector2(1, 0) # стартовое направление
        self.speed = 500

        # set lines
        self.next_line = 0
        self.turn_lines = turn_lines

        # set distance to next turn line
        self.set_next_line_distance()

        self.turned_lines = set()  # отслеживание уже использованных линий

    def move(self, dt):
        # Движение
        self.rect.center += self.direction * self.speed * dt
    
    def set_next_line_distance(self):
        turn_line_points = self.turn_lines[self.next_line].points
        bottom_center = self.rect.midbottom
        self.distance = ((turn_line_points[1][0] - turn_line_points[0][0]) * (turn_line_points[0][1] - bottom_center[1]) -
                            (turn_line_points[0][0] - bottom_center[0]) * (turn_line_points[1][1] - turn_line_points[0][1])
                        ) / math.sqrt(pow(turn_line_points[1][0] - turn_line_points[0][0], 2) 
                                        + pow(turn_line_points[1][1] - turn_line_points[0][1], 2))
    
    def make_a_turn(self):
            turn_line = self.turn_lines[self.next_line]

            if turn_line.type == "1" and self.direction.x == 1:           # шёл направо →
                self.direction = pygame.Vector2(0, 1)                # поворачивает вниз ↓

            elif turn_line.type == "1" and self.direction.x == -1:        # шёл налево ←
                self.direction = pygame.Vector2(0, -1)               # поворачивает вверх ↑

            elif turn_line.type == "1" and self.direction.y == 1:         # шёл вниз ↓
                self.direction = pygame.Vector2(1, 0)                # поворачивает направо →

            elif turn_line.type == "1" and self.direction.y == -1:        # шёл вверх ↑
                self.direction = pygame.Vector2(-1, 0)               # поворачивает налево ←
            

            elif turn_line.type == "2" and self.direction.x == 1:         # шёл направо →
                self.direction = pygame.Vector2(0, -1)               # поворачивает вверх ↑

            elif turn_line.type == "2" and self.direction.x == -1:        # шёл налево ←
                self.direction = pygame.Vector2(0, 1)                # поворачивает вниз ↓

            elif turn_line.type == "2" and self.direction.y == 1:         # шёл вниз ↓
                self.direction = pygame.Vector2(-1, 0)               # поворачивает налево ←

            elif turn_line.type == "2" and self.direction.y == -1:        # шёл вверх ↑
                self.direction = pygame.Vector2(1, 0)                # поворачивает направо →

            self.turned_lines.add(self.next_line)
            self.next_line = self.next_line + 1
            self.set_next_line_distance()

    def check_turn(self):
        if self.next_line not in self.turned_lines:
            turn_line = self.turn_lines[self.next_line]
            bottom_center = self.rect.midbottom

            turn_line_points = turn_line.points    # two point: beginning and end
            distance = ((turn_line_points[1][0] - turn_line_points[0][0]) * (turn_line_points[0][1] - bottom_center[1]) -
                            (turn_line_points[0][0] - bottom_center[0]) * (turn_line_points[1][1] - turn_line_points[0][1])
                        ) / math.sqrt(pow(turn_line_points[1][0] - turn_line_points[0][0], 2) 
                                        + pow(turn_line_points[1][1] - turn_line_points[0][1], 2))
            if sign(self.distance) != sign(distance):
                return True
            return False

    def update(self, dt):
        self.move(dt)
        if self.check_turn():
            if self.next_line + 1 == len(self.turn_lines):
                self.kill()
            else:
                self.make_a_turn()
            