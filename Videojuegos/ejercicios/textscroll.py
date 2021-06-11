import pygame


pygame.init()
size = [640,480]
red =(255,0,0)
deltaY=0
x= 30
y= 30

screen = pygame.display.set_mode(size, 0, 32)
pygame.display.set_caption("Text Scroll")
texto ="Este es mi texto y no se como saldra"
my_font = pygame.font.SysFont("Arial", 16)
text_surface = my_font.render(texto, True, (255,0,0), (255,255,255))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.KEYDOWN:   
            if event.key == pygame.K_ESCAPE:         
                pygame.quit()
                exit()

    screen.fill((0,0,0))
    
    deltaY += 0.3
    posicion =(x, y+deltaY)
    
    screen.blit(text_surface, posicion)
    pygame.display.update()

pygame.quit()