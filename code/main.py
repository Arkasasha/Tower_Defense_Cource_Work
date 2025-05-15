from settings import *
from level import Level
from pytmx.util_pygame import load_pygame
from level_button import LevelButton

from random import randint

class Game:
    def __init__(self):
        self._running = True
        self._screen_surface = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self._SCREEN_WIDTH, self._SCREEN_HEIGHT = self._screen_surface.get_size()
        self._display_surface = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))
        self._display_surface.fill((240, 240, 240))
        pygame.display.set_caption('Tower Defence')
        self._level = None
        self._level_select_state = False

        self._setup()

    def _setup(self):
        self._image = pygame.image.load(join('Game', 'Assets', 'additional', 'Interface', 
                                             'Title_screen', 'Background.png')).convert_alpha()
        self._rect = self._image.get_frect(topleft = (0, 0))

        # draws buttons on main screen
        self._settings_button = pygame.image.load(join('Game', 'Assets', 'additional', 'Interface', 
                                                       'Title_screen', 'Setting_button.png')).convert_alpha()
        self._settings_button_rect = self._settings_button.get_frect(center = (WINDOW_WIDTH / 2, 
                                                                               WINDOW_HEIGHT / 2 + 50))

        self._play_button = pygame.image.load(join('Game', 'Assets', 'additional', 'Interface', 
                                                   'Title_screen', 'Play_button.png')).convert_alpha()
        self._play_button_rect = self._play_button.get_frect(center = (self._settings_button_rect.centerx, 
                                                                       self._settings_button_rect.centery - 150))

        self._quit_button = pygame.image.load(join('Game', 'Assets', 'additional', 'Interface', 
                                                   'Title_screen', 'Quit_button.png')).convert_alpha()
        self._quit_button_rect = self._quit_button.get_frect(center = (self._settings_button_rect.centerx, 
                                                                self._settings_button_rect.centery + 150))

        self._image.blit(self._settings_button, self._settings_button_rect)
        self._image.blit(self._play_button, self._play_button_rect)
        self._image.blit(self._quit_button, self._quit_button_rect)

        # draws buttons on level select screen
        self._levels_screen = pygame.image.load(join('Game', 'Assets', 'additional', 'Interface', 
                                             'Levels_screen', 'Background.png')).convert_alpha()
        self._levels_screen_rect = self._levels_screen.get_frect(topleft = (0, 0))

        # levels_background_surf = pygame.image.load(join('Game', 'Assets', 'additional', 'Interface', 
        #                                      'Levels_screen', 'Ramka.png')).convert_alpha()
        # levels_background_rect = levels_background_surf.get_frect(center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))
        # self._levels_screen.blit(levels_background_surf, levels_background_rect)

        back_button_surf = pygame.image.load(join('Game', 'Assets', 'additional', 'Interface', 
                                             'Levels_screen', 'back.png')).convert_alpha()
        back_button_rect = back_button_surf.get_frect(bottomright = (WINDOW_WIDTH - 100, WINDOW_HEIGHT - 50))
        self._levels_back_button = LevelButton(back_button_surf, back_button_rect.center)
        self._levels_screen.blit(self._levels_back_button.get_image(), self._levels_back_button.get_rect())

        self._level_buttons = []
        starting_pos = [WINDOW_WIDTH / 2 - 400, WINDOW_HEIGHT / 2 - 90]
        for i in range(1, 11):
            surf = pygame.image.load(join('Game', 'Assets', 'additional', 'Interface',
                                                        'Levels_screen', f'{i}.png')).convert_alpha()
            level_button = LevelButton(surf, starting_pos, id = i)
            self._level_buttons.append(level_button)
            self._levels_screen.blit(level_button.get_image(), level_button.get_rect())

            starting_pos[0] += 200
            if i == 5:
                starting_pos[0] = WINDOW_WIDTH / 2 - 400
                starting_pos[1] += 180
        
        locked_levels = []
        for i in range(10):
            locked_levels.append(True)
        locked_levels[0] = False
        
        self._locked_level_buttons = []
        locked_level_surf = pygame.image.load(join('Game', 'Assets', 'additional', 'Interface',
                                                        'Levels_screen', 'Lock.png')).convert_alpha()
        starting_pos = [WINDOW_WIDTH / 2 - 400, WINDOW_HEIGHT / 2 - 90]
        for i in range(10):
            if locked_levels[i]:
                locked_button = LevelButton(locked_level_surf, starting_pos, id = i + 1)
                self._locked_level_buttons.append(locked_button)

            starting_pos[0] += 200
            if i == 4:
                starting_pos[0] = WINDOW_WIDTH / 2 - 400
                starting_pos[1] += 180

    def _check_level_button_collisions(self, pos):
        collisions = []
        for button in self._level_buttons:
            if button.get_rect().collidepoint(pos):
                collisions.append(button)
        return collisions
    
    def _check_locked_level_button_collisions(self, pos):
        collisions = []
        for button in self._locked_level_buttons:
            if button.get_rect().collidepoint(pos):
                collisions.append(button)
        return collisions

    def _update_screen(self):
        if self._level_select_state:
            if pygame.mouse.get_just_pressed()[0]:
                mouse_pos = get_fixed_mouse_pos()
                pressed_level_buttons = self._check_level_button_collisions(mouse_pos)
                pressed_locked_buttons = self._check_locked_level_button_collisions(mouse_pos)
                if len(pressed_level_buttons) == 1 and len(pressed_locked_buttons) == 0:
                    if pressed_level_buttons[0].get_id() == 1:
                        reset_singleton()
                        self._level_select_state = False
                        self._level = Level()
                        self._level.set_running(True)
                if self._levels_back_button.get_rect().collidepoint(mouse_pos):
                    self._level_select_state = False
                
        else:
            if pygame.mouse.get_just_pressed()[0]:
                mouse_pos = get_fixed_mouse_pos()
                if self._play_button_rect.collidepoint(mouse_pos):
                    self._level_select_state = True
                elif self._settings_button_rect.collidepoint(mouse_pos):
                    pass
                if self._quit_button_rect.collidepoint(mouse_pos):
                    pygame.quit()
                    sys.exit()

    def _update_and_draw_screen(self):
        show_level = False
        if self._level != None:
            if self._level.get_running():
                self._level.run_the_level()
                self._display_surface = self._level.get_interface_surface()
                show_level = True

        if not show_level:
            if self._level_select_state:
                for button in self._locked_level_buttons:
                    self._levels_screen.blit(button.get_image(), button.get_rect())
                self._display_surface.blit(self._levels_screen, self._levels_screen_rect)
            else:
                self._display_surface.blit(self._image, self._rect)
            self._update_screen()
        
        scaled_surface = pygame.transform.scale(self._display_surface, (self._SCREEN_WIDTH, self._SCREEN_HEIGHT))
        self._screen_surface.blit(scaled_surface, (0, 0))
        pygame.display.flip()

    def run_the_game(self):
        while self._running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self._running = False
            
            self._update_and_draw_screen()

        pygame.quit()


if __name__ == "__main__":
    game = Game()
    game.run_the_game()