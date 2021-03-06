import os
import sys
from config import Config
import pygame


class Animation:
    
    def __init__(self):
        pygame.init()
        self.__screen = pygame.display.set_mode(Config.screen_size, 0, 32)
        pygame.display.set_caption(Config.title)
        self.__fps_clock = pygame.time.Clock()
        self.__walk=Walk(self.__fps_clock)

    def run(self):
        self.__running = True
        while self.__running:
            delta_time = self.__fps_clock.tick(Config.fps)
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
       
        self.__walk.update(delta_time)

    def __render(self):

        self.__screen.fill(Config.background_color)
        self.__walk.render(self.__screen)
        pygame.display.update()


    def __quit(self):

        pygame.quit()

class Girl:
    
    def __init__(self, filename, image_size, total_images, images_x_line, pos, index_image):

        self.__image=pygame.image.load(os.path.join(*filename))
        self.__image_size= image_size
        self.__total_images = total_images
        self.__images_x_line = images_x_line
        self.__pos= pos
        self.__index_image = index_image
        self.__girl_images = dict()

        for i in range(self.__total_images):
            left = self.__image_size[0] * (i % self.__images_x_line)
            top = self.__image_size[1] * int(i / self.__images_x_line)
            self.__girl_images[i] = pygame.Rect(left, top, self.__image_size[0], self.__image_size[1])
    def render (self, destiny,index_image):
        destiny.blit(self.__image, self.__pos, self.__girl_images[index_image])
 
        
class Walk:

    def __init__(self, clock):

        self.__pos = pygame.math.Vector2(Config.init_pos)
        self.__index_image = 1
        self.__girl = Girl(Config.filename, Config.image_size, Config.total_images, Config.images_x_line, self.__pos, self.__index_image)
        self.__counter_series = 0
        self.__clock = clock
        
    def update (self, delta_time):

        # Change the speed of girl images.

        if self.__clock.tick(Config.image_speed):
            self.__index_image += 1

        # Change the images way when pos arrives to the end of the screen.

        if (self.__counter_series % 2 ==0) and (0< self.__index_image <= 10):
             if self.__index_image == 10:
                self.__index_image = 1

        elif (self.__counter_series % 2  == 1) and (11 < self.__index_image<= 20):
            
            if self.__index_image == 20:
                self.__index_image = 12

        # Change the walking way, based on "__counter_series" is even or odd.

        if (self.__counter_series % 2 == 0):
            self.__pos.x += Config.speed * delta_time
            if self.__pos.x > 590:
                self.__counter_series += 1
                self.__index_image = 12

        elif (self.__counter_series % 2 == 1):
           self.__pos.x -= Config.speed * delta_time
           if self.__pos.x < 0:
               self.__counter_series += 1
               self.__index_image = 1
    
    def render (self, destiny):
        self.__girl.render(destiny, self.__index_image)
        

def main(args=None):
    
    app = Animation()
    app.run()
    
if __name__=='__main__':
    sys.exit(main())
