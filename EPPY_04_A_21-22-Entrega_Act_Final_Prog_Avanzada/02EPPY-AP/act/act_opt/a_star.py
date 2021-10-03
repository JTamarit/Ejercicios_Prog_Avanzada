import pygame
import math
from operator import attrgetter

import maze_utils as mz

class Node:
    def __init__(self, parent = None, position = None):
        self.parent = parent
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position

def calc_path(maze_matrix, start, end, heuristic_function):
    start_node = Node(None, start)
    start_node.g = start_node.h = start_node.f = 0

    end_node = Node(None, end)
    end_node.g = end_node.h = end_node.f = 0

    #Tu codigo aqui

    # test if goal is reached or not, if yes then return the path
    # if current_node == end_node:
    #     return return_path(current_node)

    #Tu codigo aqui
    
    # if no path is found return empty path
    return []

def heuristic_euclidean_distance(src, dst):
    x_dist = abs(src[0] - dst[0])
    y_dist = abs(src[1] - dst[1])
    return 10 * (math.sqrt((x_dist * x_dist) + (y_dist * y_dist)))
    # return (x_dist ** 2) + (y_dist ** 2)

def heuristic_manhattan_distance(src, dst):
    x_dist = abs(src[0] - dst[0])
    y_dist = abs(src[1] - dst[1])
    return 10 * (x_dist + y_dist)

def heuristic_diagonal_distance(src, dst):
    x_dist = abs(src[0] - dst[0])
    y_dist = abs(src[1] - dst[1])
    return (10 * (x_dist + y_dist)) + (-6 * min(x_dist, y_dist))

def return_path(current_node):
    path = []
    current = current_node
    while current is not None:
        path.append(current.position)
        current = current.parent

    # Return reversed path as we need to show from start to end path
    return path[::-1]

def path_to_img(maze_matrix, zoom, path):
    rows, cols = mz.get_maze_size(maze_matrix)
    maze_img = pygame.Surface((cols* zoom, rows * zoom), pygame.SRCALPHA, 32).convert_alpha()

    if path:
        for coord in path:
            point = mz.maze_coord_to_screen_point(zoom, coord)
            rect = pygame.Rect(point,(zoom, zoom))
            pygame.draw.rect(maze_img, (0, 0, 255, 255), rect)

    return maze_img

pygame.init()

zoom = 10
maze = mz.read_maze_img()
maze_img = mz.build_maze_image(maze, zoom)

screen_size = maze_img.get_size()
screen = pygame.display.set_mode(screen_size, 0, 32)

running = True
clock = pygame.time.Clock()

start_coord = (-1.0, -1.0)
end_coord = (-1.0, -1.0)
click_to_start = True

path_img = pygame.Surface(maze_img.get_size(), pygame.SRCALPHA, 32).convert_alpha()

start_img = pygame.Surface((zoom, zoom))
start_img.fill((0,255,0,255))
end_img = pygame.Surface((zoom, zoom))
end_img.fill((255,0,0,255))

while running:

    delta_time = clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                coord = mz.screen_point_to_maze_coord(zoom, event.pos)
                if not mz.maze_coord_is_walkable(maze, coord):
                    continue
                if click_to_start:
                    start_coord = coord
                    click_to_start = False
                else:
                    end_coord = coord
                    new_path = calc_path(maze, start_coord, end_coord, heuristic_euclidean_distance)
                    path_img = path_to_img(maze, zoom, new_path)
                    click_to_start = True

    screen.fill((200, 200, 200))

    screen.blit(maze_img, (0,0))
    screen.blit(path_img, (0,0))

    screen.blit(start_img, mz.maze_coord_to_screen_point(zoom, start_coord))
    screen.blit(end_img, mz.maze_coord_to_screen_point(zoom, end_coord))

    pygame.display.update()

pygame.quit()
