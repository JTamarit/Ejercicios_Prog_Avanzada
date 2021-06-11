import pygame
import sys

class Lluvia_Letras:
    size = width, height = 800, 600
    prog_title = "Lluvia letras"
    

    def __init__(self):
        self.posx = Lluvia_Letras.size[0] / 2
        self.posy = 20
        self.letra = 'a'
        pygame.init()
        self.screen = pygame.display.set_mode(Lluvia_Letras.size)
        pygame.display.set_caption(Lluvia_Letras.prog_title)

        self.font = pygame.font.SysFont(None, 48)

        clock = pygame.time.Clock()

    
    def process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                self.running = False
            if event.type == pygame.KEYDOWN:
                self.letra = event.unicode
                self.posy = 0
                

    def render(self):
        self.screen.fill((0, 0, 0))
        self.imagen_letra = self.font.render(self.letra, True, (0, 128, 0))
        self.screen.blit(self.imagen_letra, (self.posx, self.posy))
        pygame.display.update()

    def quit(self):
        pygame.quit()

    def run(self):
        self.running = True

        while self.running:
            self.process_events()
            self.posy += 0.2
            self.render()
            
        self.quit()

def main(args=None):
    if args is None:
        args = sys.argv[1:]
    app = Lluvia_Letras()
    app.run()

    

if __name__ == '__main__':
    sys.exit(main())
