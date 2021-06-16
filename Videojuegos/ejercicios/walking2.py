import os
import sys

import pygame


class Animation:
    
    screen_size = (640,480)
    fps = 60
    speed = 0.1
    clock = pygame.time.Clock()
    
    def __init__(self):
        pygame.init()
        self.__screen = pygame.display.set_mode(Animation.screen_size, 0, 32)
        pygame.display.set_caption("Walking Girl")
        self.__fps_clock = pygame.time.Clock()
        self.__girl=Girl()

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

    def __update(self,delta_time):
       
        self.__girl.update(delta_time)

    def __render(self):

        self.__screen.fill((0,0,0))
        self.__girl.render(self.__screen)
        pygame.display.update()


    def __quit(self):

        pygame.quit()

class Girl:
    
    image_filename=['res','walking_animation.png']
    

    def __init__(self):

        self.__image_size = (64,128)
        self.__pos=pygame.math.Vector2(0,350)
        self.__end_pos=pygame.math.Vector2(0,200)
        self.__total_images = 20
        self.__images_x_line = 10
        self.__image=pygame.image.load(os.path.join(*Girl.image_filename))
        self.__speed=Animation.speed
        self.__index_image=0
        self.__counter_series=0
        

        self.__girl_images = dict()
        
        for i in range(self.__total_images):
            left = self.__image_size[0] * (i % self.__images_x_line)
            top = self.__image_size[1] * int(i / self.__images_x_line)
            self.__girl_images[i] = pygame.Rect(left, top, self.__image_size[0], self.__image_size[1])

    def update(self,delta_time):

        if Animation.clock.tick(12):
            self.__index_image += 1
        if (self.__counter_series % 2 ==0) and (0< self.__index_image <= 10):
             if self.__index_image == 10:
                self.__index_image = 1

        elif (self.__counter_series % 2  == 1) and (11 < self.__index_image<= 20):
            
            if self.__index_image == 20:
                self.__index_image = 12

        if (self.__counter_series % 2 == 0):
            self.__pos.x += self.__speed * delta_time
            if self.__pos.x > 590:
                self.__counter_series += 1
                self.__index_image = 12

        elif (self.__counter_series % 2 == 1):
           self.__pos.x -= self.__speed * delta_time
           if self.__pos.x < 0:
               self.__counter_series += 1
               self.__index_image = 1
    
        
    def render(self,destiny):
        
        destiny.blit(self.__image, self.__pos, self.__girl_images[self.__index_image])

def main(args=None):
    
    app = Animation()
    app.run()
    
if __name__=='__main__':
    sys.exit(main())