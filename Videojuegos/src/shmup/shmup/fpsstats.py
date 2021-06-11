from importlib import resources

import pygame

class FPSStats:

    font_path, font_filename = "shmup.assets.fonts", "Sansation.ttf"  
    refresh_stats_time = 1000  

    def __init__(self):
        self.__update_time = 0
        self.__frames = 0

        with resources.path(FPSStats.font_path, FPSStats.font_filename) as font_path:
            self.__my_font = pygame.font.Font(font_path, 20)

        self.__set_fps_surface()

    def update(self, delta_time):
        self.__update_time += delta_time
        self.__frames += 1

        if self.__update_time >= FPSStats.refresh_stats_time:
            self.__set_fps_surface()
            self.__update_time -= FPSStats.refresh_stats_time
            self.__frames = 0

    def render(self, surface_dest):
        surface_dest.blit(self.__fps, (0,0))

    def __set_fps_surface(self):
        self.__fps = self.__my_font.render(f"{self.__frames} fps", True, (255, 255, 255), (0,0,0))