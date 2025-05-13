from settings import *
from enemies_types import *
from groups import EnemyInCastle

class Castle:
    def __init__(self):
        self._health = 4
        self._money = 100
        self._enemies = EnemyInCastle()

    def get_damage(self):
        self._health -= self._enemies.get_damage()
        if self._health <= 0:
            print('Game Over')
            pygame.quit
            sys.exit()