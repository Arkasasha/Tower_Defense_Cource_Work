from settings import *
from levels import Level
from pytmx.util_pygame import load_pygame

from random import randint

@singleton
class Game:
    def __init__(self):
        self._running = True
        self._display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption('Tower Defence')

        self._setup()

    def _setup(self):
        self._level = Level()

    def run_the_game(self):
        while self._running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self._running = False

            self._level.run_the_level()

        pygame.quit()


if __name__ == "__main__":
    game = Game()
    game.run_the_game()