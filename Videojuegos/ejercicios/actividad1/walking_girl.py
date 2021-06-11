import pygame
import sys
import os


class Game:

    screen_size = (640,480)

    def __init__(self):
        pygame.init()

        self.__screen = pygame.display.set_mode(Game.screen_size, 0, 32)
        self.__walk= Walking(Game.screen_size)
        self.__fps_clock = pygame.time.Clock()

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
        self.__walk.update(delta_time)

    def __render(self):
        self.__screen.fill((0,0,0))
        self.__walk.render(self.__screen)
        pygame.display.update()

    def __quit(self):
        pygame.quit()

class Girl:

    def __init__(self, filename, image_size, total_images, images_x_line):
        self.__image  =pygame.image.load(os.path.join(*filename)).convert_alpha()
        self.__image_size = image_size
        self.__girl_images= dict()

        for i in range(total_images):
            left = self.__image_size[0] * (i % images_x_line)
            top = self.__image_size[1] * int(i / images_x_line)
            self.__girl_images[i] = pygame.Rect(left, top, self.__image_size[0], self.__image_size[1])
    
    def render(self, surface_dest, image, pos):
        surface_dest.blit(self.__image, pos, self.__girl_images[image])

    
class Walking:

    image_filename = ["walking_animation.png"]
    image_size = (64,128)
    total_images = 20
    images_x_line = 10
    speed = 0.2

    def __init__(self, window_size):
        
        self.__pos = pygame.math.Vector2(window_size[0]/2, window_size[1]/2)
        self.__image = Girl(Walking.image_filename, Walking.image_size, Walking.total_images, Walking.images_x_line)
        self.__window_size = window_size
        
    def update(self, delta_time):
        self.__pos.x -= Walking.speed * delta_time
     

    def render(self, surface_dest):
        for i in range(20):
            self.__image.render(surface_dest, Girl.__girl_images[i],(self.__pos.x + Girl.__image_size[0] * i), self.__pos.y)

def main(args=None):
    app = Game()
    app.run()
    
if __name__=='__main__':
    sys.exit(main())
