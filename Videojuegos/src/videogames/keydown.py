import pygame

pygame.init()

screen = pygame.display.set_mode([640, 480], pygame.NOFRAME, 32)

circle = pygame.Surface((50,50))
pygame.draw.circle(circle, (60,139,210), (25, 25), 25)

x, y = screen.get_width()/2, screen.get_height()/2
move_x, move_y = 0, 0

full_screen = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.KEYDOWN:   
            if event.key == pygame.K_ESCAPE:         
                pygame.quit()
                exit()
            if event.key == pygame.K_LEFT:
                move_x = -0.1
            elif event.key == pygame.K_RIGHT:
                move_x = +0.1
            elif event.key == pygame.K_UP:
                move_y = -0.1
            elif event.key == pygame.K_DOWN:
                move_y = +0.1
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                move_x = 0
            elif event.key == pygame.K_RIGHT:
                move_x = 0
            elif event.key == pygame.K_UP:
                move_y = 0
            elif event.key == pygame.K_DOWN:
                move_y = 0

    x+= move_x
    y+= move_y

    screen.fill((0, 0, 0))

    screen.blit(circle, (x, y))

    pygame.display.update()

pygame.quit()