import pygame

class RenderGroup(pygame.sprite.Group):

    def draw(self, surface):
        for sprite in self.sprites():
            sprite.render(surface)