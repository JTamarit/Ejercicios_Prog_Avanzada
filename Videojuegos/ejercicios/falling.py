import pygame

pygame.init()
size = [640,480]
x = 30
y = 30
deltaY = 0
deltaX = 0
tecla = 'a'


screen = pygame.display.set_mode(size, 0, 32)
pygame.display.set_caption("Falling")
my_font = pygame.font.SysFont("Arial", 30)


while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.KEYDOWN:   
            if event.key == pygame.K_ESCAPE:         
                pygame.quit()
                exit()
            tecla =pygame.key.name(event.key)
            y=30
            deltaX += 10
    
    screen.fill((0, 0, 0))
    deltaY += 0.2
    posicion =(x+deltaX, y+deltaY)
    text_surface = my_font.render(tecla, True, (255,0,0), (0,0,0))  
    screen.blit(text_surface, posicion)

    pygame.display.update()


pygame.quit()