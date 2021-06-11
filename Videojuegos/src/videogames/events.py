import pygame
from sys import exit

pygame.init()

screen = pygame.display.set_mode([640, 480], 0, 32)

while True:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    pygame.display.update()

pygame.quit()