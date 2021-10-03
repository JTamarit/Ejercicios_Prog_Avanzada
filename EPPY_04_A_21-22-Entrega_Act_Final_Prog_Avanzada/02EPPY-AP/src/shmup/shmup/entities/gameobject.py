import pygame

class GameObject(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()

        self.position = pygame.math.Vector2(0.0, 0.0)
        self.rect = pygame.Rect(0,0,0,0)
        self.render_rect = pygame.Rect(0,0,0,0)

    def handle_input(self, key, is_pressed):
        pass

    def update(self, delta_time):
        pass

    def render(self, surface):
        pass

    def quit(self):
        pass

    def _center(self):
        self.render_rect.center = self.position.xy
        self.rect.center = self.position.xy