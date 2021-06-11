from importlib import resources

import pygame

from shmup.fpsstats import FPSStats

class Game:

    hero_image_path, hero_image_filename = "shmup.assets.images", "hero.png"
    
    screen_size = (640,480)
    fps = 60

    def __init__(self):
        pygame.init()

        self.__screen = pygame.display.set_mode(Game.screen_size, 0, 32)
        pygame.display.set_caption("Hello")

        with resources.path(Game.hero_image_path, Game.hero_image_filename) as hero_path:
            self.__hero_image = pygame.image.load(hero_path).convert_alpha()

        self.__is_moving_up = False
        self.__is_moving_down = False
        self.__is_moving_left = False
        self.__is_moving_right = False

        self.__hero_position = pygame.math.Vector2(self.__screen.get_width()/2 - self.__hero_image.get_width()/2, self.__screen.get_height()/2 - self.__hero_image.get_height()/2)

        self.__fps_clock = pygame.time.Clock()

        self.__fps_stats = FPSStats()

    def run(self):
        self.__running = True
        while self.__running:
            delta_time = self.__fps_clock.tick(Game.fps)
            self.__process_events()
            self.__update(delta_time)
            self.__fps_stats.update(delta_time)
            self.__render()            
        self.__quit()        

    def __process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.__running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.__running = False
                self.__handle_player_input(event.key, True)
            elif event.type == pygame.KEYUP:
                self.__handle_player_input(event.key, False)

    def __handle_player_input(self, key, is_pressed):
        if key == pygame.K_UP:
            self.__is_moving_up = is_pressed
        elif key == pygame.K_DOWN:
            self.__is_moving_down = is_pressed
        elif key == pygame.K_LEFT:
            self.__is_moving_left = is_pressed
        elif key == pygame.K_RIGHT:
            self.__is_moving_right = is_pressed

    def __update(self, delta_time):
        movement = pygame.math.Vector2(0.0, 0.0)

        if self.__is_moving_up:
            movement.y -= 0.4
        if self.__is_moving_down:
            movement.y += 0.4
        if self.__is_moving_left:
            movement.x -= 0.4
        if self.__is_moving_right:
            movement.x += 0.4

        self.__hero_position += movement * delta_time

    def __render(self):
        self.__screen.fill((100,100,100))

        self.__screen.blit(self.__hero_image, self.__hero_position.xy)        
        self.__fps_stats.render(self.__screen)

        pygame.display.update()

    def __quit(self):
        pygame.quit()