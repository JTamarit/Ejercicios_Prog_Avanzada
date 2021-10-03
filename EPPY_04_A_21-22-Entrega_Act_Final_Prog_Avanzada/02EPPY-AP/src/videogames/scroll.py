import pygame
import sys
import os


class Game:

    screen_size = (640,480)

    def __init__(self):
        pygame.init()

        self.__screen = pygame.display.set_mode(Game.screen_size, 0, 32)

        self.__fps_clock = pygame.time.Clock()
        self.__scroll = Scroll("De hecho se puede crear cualquier color mezclando los colores primarios rojo amarillo y azul en distintas proporciones.", Game.screen_size)

    def run(self):
        self.__running = True
        while self.__running:
            delta_time = self.__fps_clock.tick(60)
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

    def __update(self, delta_time):
        self.__scroll.update(delta_time)

    def __render(self):
        self.__screen.fill((0,0,0))
        self.__scroll.render(self.__screen)
        pygame.display.update()

    def __quit(self):
        pygame.quit()

class BitmapFont:

    def __init__(self, filename, letter_size, total_letters, letters_x_line):
        self.__image  =pygame.image.load(os.path.join(*filename)).convert_alpha()
        self.__letter_size = letter_size
        self.__font = dict()

        for i in range(total_letters):
            left = self.__letter_size[0] * (i % letters_x_line)
            top = self.__letter_size[1] * int(i / letters_x_line)
            self.__font[self.__translate(i)] = pygame.Rect(left, top, self.__letter_size[0], self.__letter_size[1])
    
    def render(self, surface_dest, letter, pos):
        surface_dest.blit(self.__image, pos, self.__font[letter.upper()])

    def __translate(self, number):
        if number >=0 and number <=25:
            char = chr(number + 65)
        elif number >= 26 and number <= 34:
            char = chr(number + 23)
        else:
            rest = ['0', '-', '.', ':', '?', '!', '(', ')', ' ', '+']
            char = rest[number-35]

        return char

class Scroll:

    font_filename = ["agents.png"]
    font_letter_size = (20,28)
    font_total_letters = 45
    font_letters_x_line = 15
    speed = 0.2

    def __init__(self, text, window_size):
        self.__text = list(text)
        self.__current_letter_index = 0
        self.__pos = pygame.math.Vector2(window_size[0]/2, window_size[1]/2)

        self.__font = BitmapFont(Scroll.font_filename, Scroll.font_letter_size, Scroll.font_total_letters, Scroll.font_letters_x_line)
        self.__window_size = window_size
        
    def update(self, delta_time):
        self.__pos.x -= Scroll.speed * delta_time
        if self.__pos.x <= -Scroll.font_letter_size[0]:
            self.__pos.x = 0
            self.__current_letter_index += 1

    def render(self, surface_dest):
        letters_in_screen = int((self.__window_size[0] - self.__pos.x) / Scroll.font_letter_size[0]) + 1
        for i in range(letters_in_screen):
            index = (self.__current_letter_index + i) % len(self.__text)
            self.__font.render(surface_dest, self.__text[index],(self.__pos.x + (Scroll.font_letter_size[0] * i), self.__pos.y))

def main(args=None):
    app = Game()
    app.run()
    
if __name__=='__main__':
    sys.exit(main())
