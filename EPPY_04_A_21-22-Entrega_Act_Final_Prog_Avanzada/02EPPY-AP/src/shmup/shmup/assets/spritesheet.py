from importlib import resources
import json

import pygame

class SpriteSheet:

    def __init__(self, image_path, image_filename, data_path, data_filename):
        with resources.path(data_path, data_filename) as asset_data:
            with open(asset_data) as f:
                self.__dict = json.load(f)

        with resources.path(image_path, image_filename) as asset_res:
            self.__image = pygame.image.load(asset_res).convert_alpha()

    def get_image(self, image_name):
        if image_name in self.__dict:
            return self.__image, pygame.Rect(self.__dict[image_name])

    def get_clip(self, image_name):
        if image_name in self.__dict:
            return pygame.Rect(self.__dict[image_name])
