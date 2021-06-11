import pygame
from pygame.constants import BUTTON_X1

pygame.init()

radius = 25
colour=(255,0,0)

screen = pygame.display.set_mode([640, 480], 0, 32)
pygame.display.set_caption("Changing Circle")

circle = pygame.Surface((radius*2,radius*2))
pygame.draw.circle(circle, colour, (radius, radius), radius)

x, y = screen.get_width()/2, screen.get_height()/2
move_x, move_y = 0, 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.KEYDOWN:   
            if event.key == pygame.K_ESCAPE:         
                pygame.quit()
                exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                radius += 5

            if event.button == 3:
                radius -= 5
    circle = pygame.Surface((radius*2,radius*2))
    pygame.draw.circle(circle, colour, (radius, radius), radius)    
    screen.fill((0, 0, 0))
    x,y = pygame.mouse.get_pos()
    x -= radius
    y -= radius
    screen.blit(circle, (x, y))

    pygame.display.update()

pygame.quit()