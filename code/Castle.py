from settings import *
from enemies_types import *
from groups import EnemyInCastle, EnemyDeathMoney

class Castle:
    def __init__(self):
        self._health = 5
        self._money = 0
        self._enemy_in_castle = EnemyInCastle()
        self._enemy_death_money = EnemyDeathMoney()

    def take_damage(self):
        self._health -= self._enemy_in_castle.get_damage()
        if self._health <= 0:
            print('Game Over')
            pygame.quit
            sys.exit()
    
    def take_money(self):
        self._money += self._enemy_death_money.get_money()

    def get_money(self):
        return self._money
    
    def get_health(self):
        return self._health
    