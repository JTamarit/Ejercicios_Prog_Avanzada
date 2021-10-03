import pygame

from shmup.config import Config
from shmup.assets.assetmanager import AssetManager, AssetType
from shmup.entities.gameobject import GameObject
from shmup.entities.projectile import ProjectileType

class Hero(GameObject):

    def __init__(self, game):
        super().__init__()

        self.__game = game

        self.__is_moving_up = False
        self.__is_moving_down = False
        self.__is_moving_left = False
        self.__is_moving_right = False

        _, clip = AssetManager.instance().get(AssetType.SpriteSheet, Config.instance().data["entities"]["hero"]["name"] , Config.instance().data["entities"]["name"])

        self.position = pygame.math.Vector2(Config.instance().data["screen_size"][0]/2, 
            Config.instance().data["screen_size"][1] - Config.instance().data["screen_size"][1]/3)
        self.rect = clip.copy()
        self.rect.inflate_ip(self.rect.width * -0.60, self.rect.height * -0.20)
        self.render_rect = clip.copy()

        self._center()

    def handle_input(self, key, is_pressed):
        if key == pygame.K_UP:
            self.__is_moving_up = is_pressed
        elif key == pygame.K_DOWN:
            self.__is_moving_down = is_pressed
        elif key == pygame.K_LEFT:
            self.__is_moving_left = is_pressed
        elif key == pygame.K_RIGHT:
            self.__is_moving_right = is_pressed
        elif key == pygame.K_SPACE:
            self.__fire_bullet()

    def update(self, delta_time):
        movement = pygame.math.Vector2(0.0, 0.0)

        if self.__is_moving_up:
            movement.y -= Config.instance().data["entities"]["hero"]["speed"]
        if self.__is_moving_down:
            movement.y += Config.instance().data["entities"]["hero"]["speed"]
        if self.__is_moving_left:
            movement.x -= Config.instance().data["entities"]["hero"]["speed"]
        if self.__is_moving_right:
            movement.x += Config.instance().data["entities"]["hero"]["speed"]

        self.position += movement * delta_time
        self._center()

    def render(self, surface_dest):
        if self.__is_moving_left:
            hero_name = Config.instance().data["entities"]["hero"]["left_name"]
        elif self.__is_moving_right:
            hero_name = Config.instance().data["entities"]["hero"]["right_name"]
        else:
            hero_name = Config.instance().data["entities"]["hero"]["name"]

        image, rect = AssetManager.instance().get(AssetType.SpriteSheet, hero_name, Config.instance().data["entities"]["name"])

        surface_dest.blit(image, self.render_rect, rect)

        if Config.instance().debug:
            pygame.draw.rect(surface_dest, (255,0,0), self.rect, 1)
            pygame.draw.rect(surface_dest, (0,255,0), self.render_rect, 1)

    def quit(self):
        pass

    def __fire_bullet(self):
        self.__game.spawn_bullet(ProjectileType.AlliedBullet, self.render_rect.midtop, pygame.math.Vector2(0.0, -Config.instance().data["entities"]["allied_projectile"]["speed"]))
