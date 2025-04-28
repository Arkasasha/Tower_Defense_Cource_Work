from settings import *
from levels import Level
from pytmx.util_pygame import load_pygame

from random import randint

@singleton
class Game:
    def __init__(self):
        pygame.init()
        self.running = True
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption('Tower Defence')

        self.setup()

    def setup(self):
        self.level = Level()


    def run_the_game(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.level.run_the_level()

        pygame.quit()


if __name__ == "__main__":
    game = Game()
    game.run_the_game()