import pygame

def create_gradients(width, height):
    red_scale_surface = pygame.surface.Surface((width, height))
    green_scale_surface = pygame.surface.Surface((width, height))
    blue_scale_surface = pygame.surface.Surface((width, height))

    color_step = 255. / float(width)
    current_step = 0.
    for x in range(width):
        red = (int(current_step), 0, 0)
        green = (0, int(current_step), 0)
        blue = (0, 0, int(current_step))
        current_step += color_step

        line_rect = pygame.Rect(x, 0, 1, height)
        pygame.draw.rect(red_scale_surface, red, line_rect)
        pygame.draw.rect(green_scale_surface, green, line_rect)
        pygame.draw.rect(blue_scale_surface, blue, line_rect)
    return red_scale_surface, green_scale_surface, blue_scale_surface

screen_size = (640,480)

pygame.init()

screen = pygame.display.set_mode(screen_size, 0, 32)

fps_clock = pygame.time.Clock()

slider_height = 80
red_scale, green_scale, blue_scale = create_gradients(screen_size[0], slider_height)

color = [127, 127, 127]
color_step = 255. / float(screen_size[0])

running = True
while running:
    fps_clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    x, y = pygame.mouse.get_pos()

    if pygame.mouse.get_pressed()[0]:
        for component in range(3):
            if y > component * slider_height and y < (component+1) * slider_height:
                color[component] = int(x * color_step)
                pygame.display.set_caption("PyGame Color Test - "+str(tuple(color)))

    screen.fill((0,0,0))

    screen.blit(red_scale, (0, 0))
    screen.blit(green_scale, (0, slider_height))
    screen.blit(blue_scale, (0, slider_height * 2))

    for component in range(3):
        pos = ( int(color[component] / color_step), component * slider_height + slider_height / 2)
        pygame.draw.circle(screen, (255, 255, 255), pos, 20)

    pygame.draw.rect(screen, tuple(color), (0, slider_height * 3, screen_size[0], slider_height* 3))

    pygame.display.update()

pygame.quit()