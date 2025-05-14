from settings import *
from level import Level
from pytmx.util_pygame import load_pygame

from random import randint

@singleton
class Game:
    def __init__(self):
        self._running = True
        self._screen_surface = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self._SCREEN_WIDTH, self._SCREEN_HEIGHT = self._screen_surface.get_size()
        self._display_surface = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))
        self._display_surface.fill((240, 240, 240))
        pygame.display.set_caption('Tower Defence')

        self._setup()

    def _setup(self):
        self._level = Level()

    def _draw_game_menu(self):
        pass

    def _update_and_draw_screen(self):
        if self._level.get_running():
            self._display_surface = self._level.get_interface_surface()
        else:
            self._display_surface.fill((240, 240, 240))
            # self._draw_game_menu()
        scaled_surface = pygame.transform.scale(self._display_surface, (self._SCREEN_WIDTH, self._SCREEN_HEIGHT))
        self._screen_surface.blit(scaled_surface, (0, 0))
        pygame.display.update()

    def run_the_game(self):
        while self._running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self._running = False
            if self._level.get_running():
                self._level.run_the_level()
            
            self._update_and_draw_screen()

        pygame.quit()


if __name__ == "__main__":
    game = Game()
    game.run_the_game()