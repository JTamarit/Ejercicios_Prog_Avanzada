import os
import sys

import pygame


class Animation:
    font_filename_path = "/Users/Javi/Desktop/VIU/Apuntes_clase_Python/Videojuegos/ejercicios/letterfont.png"
    screen_size = (640,480)
    fps = 60
    speed = 0.5
    letras=[
        [' ','!','"', 'cuadro1','cuadro2','cuadro3','cuadro4',"'",'[',']'],
        ['cuadro5','+',',','-','.','/','0','1','2','3'],
        ['4','5','6','7','8','9',':',';','cuadro6','cuadro7'],
        ['cuadro8','?','cuadro9','a','b','c','d','e','f','g'],
        ['h','i','j','k','l','m','n','o','p','q'],
        ['r','s','t','u','v','w','x','y','z']
    ]
    texto= "hola"
    init_pos=(650,200)
    end_pos=(0,100)

    def __init__(self):
        pygame.init()
        self.__screen = pygame.display.set_mode(Animation.screen_size, 0, 32)
        pygame.display.set_caption("Animación 1")
        self.__font_image=pygame.image.load(Animation.font_filename_path)
        self.__fps_clock = pygame.time.Clock()
        self.__mitexto =list(Animation.texto)
        self.__position_x=0
        self.__mitraduccion =[]
        self.__images_letters = {}
        self.__cargar_alfabeto()
        self.__switch()

    
    def __cargar_alfabeto(self):

        n=0
        m=0
        for n in range(5):
            for m in range(9):
                self.__images_letters[Animation.letras[n][m]] = self.__font_image.subsurface((32*m,32*n), (32,32))
                m += 1
            n += 1
    
    def __switch(self):
        
        for elemento in self.__mitexto:
            self.__mitraduccion.append(self.__images_letters[elemento])


        

    def run(self):
        self.__running = True
        while self.__running:
            delta_time = self.__fps_clock.tick(Animation.fps)
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
        self.__position_x -=(delta_time)*0.05
        if self.__position_x < -(Animation.screen_size[0]+len(self.__mitraduccion)*32):

            self.__position_x = 0
        

    def __render(self):
        self.__screen.fill((0,0,0))
        n=0
        for elemento in self.__mitraduccion:
            positionx = Animation.init_pos[0] + self.__position_x+(35*n)
            self.__screen.blit(elemento,(positionx,Animation.init_pos[1]))
            n+=1
    
        pygame.display.update()


    def __quit(self):
        pygame.quit()

def main(args=None):
    
    app = Animation()
    app.run()
    
if __name__=='__main__':
    sys.exit(main())