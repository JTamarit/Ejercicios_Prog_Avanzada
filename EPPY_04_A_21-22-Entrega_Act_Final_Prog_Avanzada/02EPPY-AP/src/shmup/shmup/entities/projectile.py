import pygame
from enum import Enum

from shmup.entities.gameobject import GameObject
from shmup.config import Config
from shmup.assets.assetmanager import AssetManager, AssetType

class ProjectileType(Enum):
    AlliedBullet = 0,
    EnemyBullet = 1

class Projectile(GameObject):

    def __init__(self, projectile_type, position, velocity):
        super().__init__()

        self.__type = projectile_type
        self.position = pygame.math.Vector2(position)
        self.velocity = velocity

        if self.__type == ProjectileType.AlliedBullet:
            self.__name = Config.instance().data["entities"]["allied_projectile"]["name"]
        elif self.__type == ProjectileType.EnemyBullet:
            self.__name = Config.instance().data["entities"]["enemy_bullet"]["name"]

        _, clip = AssetManager.instance().get(AssetType.SpriteSheet, self.__name, Config.instance().data["entities"]["name"])
        
        self.rect = clip.copy()
        self.render_rect = clip.copy()
        self._center()

    def update(self, delta_time):
        self.position += self.velocity * delta_time
        self._center()

        if (self.position.y < (0 - self.render_rect.height)) or (self.position.y > (Config.instance().data["screen_size"][1] + self.render_rect.height)):
                self.kill()

    def render(self, surface):
        image, clip = AssetManager.instance().get(AssetType.SpriteSheet, self.__name, Config.instance().data["entities"]["name"])
        surface.blit(image, self.render_rect, clip)

        if Config.instance().debug:
            pygame.draw.rect(surface, (255,0,0), self.rect, 1)
            pygame.draw.rect(surface, (0,255,0), self.render_rect, 1)