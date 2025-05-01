from settings import *

class Enemy(pygame.sprite.Sprite):
    def __init__(self, surf, spawn_line, turn_lines, groups):
        super().__init__(groups)

        
        start_x, start_y = spawn_line.x, spawn_line.y
        rel_points = spawn_line.points
        start = (start_x + rel_points[0][0], start_y + rel_points[0][1])
        end = (start_x + rel_points[1][0], start_y + rel_points[1][1])

        t = random.random()
        spawn_x = start[0] + t * (end[0] - start[0])
        spawn_y = start[1] + t * (end[1] - start[1])

        self.image = surf
        self.rect = pygame.FRect(0, 0, 16, 16)
        self.rect.center = (spawn_x, spawn_y)

        self.hitbox = pygame.FRect(self.rect)

        self.pos = pygame.Vector2(self.rect.centerx, self.rect.bottom)

        self.direction = pygame.Vector2(1, 0) # стартовое направление
        self.speed = 200

        self.turn_lines = turn_lines

        self.turned_lines = set()  # отслеживание уже использованных линий

    @staticmethod
    def point_in_polygon(point, polygon):
        # Чистая реализация ray casting алгоритма
        x, y = point
        inside = False

        n = len(polygon)
        px1, py1 = polygon[0]
        for i in range(n + 1):
            px2, py2 = polygon[i % n]
            if y > min(py1, py2):
                if y <= max(py1, py2):
                    if x <= max(px1, px2):
                        if py1 != py2:
                            xinters = (y - py1) * (px2 - px1) / (py2 - py1) + px1
                        if px1 == px2 or x <= xinters:
                            inside = not inside
            px1, py1 = px2, py2

        return inside

    def update(self, dt):
        # Движение
        self.pos += self.direction * self.speed * dt
        self.rect.center = (round(self.pos.x), round(self.pos.y))

        bottom_center = (self.rect.centerx, self.rect.bottom)

        # Повороты
        for polygon, turn_type in self.turn_lines:
            poly_id = id(polygon)
            if poly_id in self.turned_lines:
                continue

            if Enemy.point_in_polygon(bottom_center, polygon):
                if turn_type == "1" and self.direction.x == 1:           # шёл направо →
                    self.direction = pygame.Vector2(0, 1)                # поворачивает вниз ↓

                elif turn_type == "1" and self.direction.x == -1:        # шёл налево ←
                    self.direction = pygame.Vector2(0, -1)               # поворачивает вверх ↑

                elif turn_type == "1" and self.direction.y == 1:         # шёл вниз ↓
                    self.direction = pygame.Vector2(1, 0)                # поворачивает направо →

                elif turn_type == "1" and self.direction.y == -1:        # шёл вверх ↑
                    self.direction = pygame.Vector2(-1, 0)               # поворачивает налево ←
                

                elif turn_type == "2" and self.direction.x == 1:         # шёл направо →
                    self.direction = pygame.Vector2(0, -1)               # поворачивает вверх ↑

                elif turn_type == "2" and self.direction.x == -1:        # шёл налево ←
                    self.direction = pygame.Vector2(0, 1)                # поворачивает вниз ↓

                elif turn_type == "2" and self.direction.y == 1:         # шёл вниз ↓
                    self.direction = pygame.Vector2(-1, 0)               # поворачивает налево ←

                elif turn_type == "2" and self.direction.y == -1:        # шёл вверх ↑
                    self.direction = pygame.Vector2(1, 0)                # поворачивает направо →

                self.turned_lines.add(poly_id)