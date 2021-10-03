from enum import Enum
from importlib import resources

import pygame

from shmup.assets.spritesheet import SpriteSheet

class AssetType(Enum):
    Image = 0,
    SpriteSheet = 1,
    Font = 2,
    Sound = 3,
    Music = 4

class AssetManager:

    __instance = None

    @staticmethod
    def instance():
        if AssetManager.__instance is None:
            AssetManager()
        return AssetManager.__instance

    def __init__(self):
        if AssetManager.__instance is None:
            AssetManager.__instance = self

            self.__assets = {}
        else:
            raise exception("AssetManager cannot have multiple instances")

    def load(self, asset_type, asset_name, asset_path, asset_filename, font_size = 0, data_path = None, data_filename = None):
        with resources.path(asset_path, asset_filename) as asset_res:
            if asset_type == AssetType.Image:
                self.__assets[asset_name] = pygame.image.load(asset_res).convert_alpha()
            elif asset_type == AssetType.SpriteSheet:
                self.__assets[asset_name] = SpriteSheet(asset_path, asset_filename, data_path, data_filename)
            elif asset_type == AssetType.Font:
                self.__assets[asset_name] = pygame.font.Font(asset_res, font_size)
            elif asset_type == AssetType.Sound:
                self.__assets[asset_name] = pygame.mixer.Sound(asset_res)
            elif asset_type == AssetType.Music:
                self.__assets[asset_name] = asset_res
        pass

    def get(self, asset_type, asset_name, sheet_name = None):
        if asset_type == AssetType.SpriteSheet:
            if sheet_name in self.__assets:
                return self.__assets[sheet_name].get_image(asset_name)
        elif asset_type == AssetType.Image:
            if asset_name in self.__assets:
                return self.__assets[asset_name], self.__assets[asset_name].get_rect()
            return None, pygame.Rect(0,0,0,0)
        else:
            if asset_name in self.__assets:
                return self.__assets[asset_name]
            return None

    def clean(self):
        self.__assets = {}