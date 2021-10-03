import os
import sys
import random

import pygame

class Letter:
    def __init__(self, letter, font, init_pos, end_pos,color1,color2,color3):
        self.__image = font.render(f"{letter}", True, (color1,color2,color3), (0,0,0))
        self.__position = init_pos
        self.__end_position = end_pos
        self.__alive = True
        self.__speed = random.uniform(0.2, 0.8)
        self.__color1= color1
        self.__color2= color2
        self.__color3= color3

    def update(self, delta_time):
        self.__position.y += self.__speed * delta_time
        if self.__position.y >= self.__end_position.y:
            self.__alive = False

    def render(self, surface_dest):
        surface_dest.blit(self.__image, self.__position.xy)

    def is_alive(self):
        return self.__alive


class Game:
    font_filename_path = ['..', 'shmup', 'shmup', 'assets', 'fonts', 'Sansation.ttf']
    screen_size = (640,480)
    fps = 60
    speed = 0.5

    def __init__(self):
        pygame.init()

        self.__screen = pygame.display.set_mode(Game.screen_size, 0, 32)
        pygame.display.set_caption("FallingLetters")

        self.__my_font = pygame.font.Font(os.path.join(*Game.font_filename_path), 50)
        self.__letters = []

        self.__fps_clock = pygame.time.Clock()

    def run(self):
        self.__running = True
        while self.__running:
            delta_time = self.__fps_clock.tick(Game.fps)
            self.__process_events()
            self.__update(delta_time)
            self.__render()            
        self.__quit()        

    def __process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.__running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.__running = False
                self.__spawn_letter(event.unicode)

    def __update(self, delta_time):
        for letter in list(self.__letters):
            if not letter.is_alive():
                self.__letters.remove(letter)
            else:
                letter.update(delta_time)

    def __render(self):
        self.__screen.fill((0,0,0))

        for letter in self.__letters:
            letter.render(self.__screen)    

        pygame.display.update()

    def __quit(self):
        pygame.quit()

    def __spawn_letter(self, letter):
        self.__color1 = random.randint(0,255)
        self.__color2 = random.randint(0,255)
        self.__color3 = random.randint(0,255)
        color1 = self.__color1
        color2 = self.__color2
        color3 = self.__color3
        x_init = random.randrange(50, Game.screen_size[0] - 50)
        init_pos = pygame.math.Vector2(x_init, -50)
        end_pos = pygame.math.Vector2(x_init, Game.screen_size[1] + 50)
        self.__letters.append(Letter(letter, self.__my_font, init_pos, end_pos,color1,color2,color3))

def main(args=None):
    app = Game()
    app.run()
    
if __name__=='__main__':
    sys.exit(main())