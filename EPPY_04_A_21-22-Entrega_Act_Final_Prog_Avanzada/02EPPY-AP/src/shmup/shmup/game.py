import pygame

from shmup.fpsstats import FPSStats
from shmup.config import Config
from shmup.entities.hero import Hero
from shmup.assets.assetmanager import AssetManager, AssetType
from shmup.entities.projectile import ProjectileType, Projectile
from shmup.assets.rendergroup import RenderGroup

class Game:

    def __init__(self):
        pygame.init()

        self.__screen = pygame.display.set_mode(Config.instance().data["screen_size"], 0, 32)
        pygame.display.set_caption(Config.instance().data["title"])

        self.__load_assets()

        self.__fps_clock = pygame.time.Clock()
        self.__fps_stats = FPSStats()     

        self.__hero = Hero(self)

        self.__allied_bullets = RenderGroup()

    def run(self):
        self.__running = True
        while self.__running:
            delta_time = self.__fps_clock.tick(Config.instance().data["fps"])
            self.__process_events()
            self.__update(delta_time)
            self.__fps_stats.update(delta_time)
            self.__render()            
        self.__quit()        

    def __process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.__running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.__running = False
                if event.key == pygame.K_F5:
                    Config.instance().debug = not Config.instance().debug
                self.__hero.handle_input(event.key, True)
            elif event.type == pygame.KEYUP:
                self.__hero.handle_input(event.key, False)

    def __update(self, delta_time):
        self.__hero.update(delta_time)
        self.__allied_bullets.update(delta_time)       

    def __render(self):
        self.__screen.fill(Config.instance().data["background_color"])
        self.__hero.render(self.__screen)  
        self.__allied_bullets.draw(self.__screen)             
        self.__fps_stats.render(self.__screen)

        pygame.display.update()

    def __quit(self):
        self.__hero.quit()
        pygame.quit()

    def __load_assets(self):
        AssetManager.instance().load(AssetType.SpriteSheet, 
            Config.instance().data["entities"]["name"], 
            Config.instance().data["entities"]["image_path"], 
            Config.instance().data["entities"]["image_filename"], 
            data_path = Config.instance().data["entities"]["data_path"], 
            data_filename = Config.instance().data["entities"]["data_filename"])
        AssetManager.instance().load(AssetType.Sound, 
            Config.instance().data["audio"]["allied_bullet"]["name"], 
            Config.instance().data["audio"]["allied_bullet"]["sound_path"], 
            Config.instance().data["audio"]["allied_bullet"]["sound_filename"])

    def spawn_bullet(self, projectile_type, position, velocity):
        if projectile_type == ProjectileType.AlliedBullet:
            self.__allied_bullets.add(Projectile(projectile_type, position, velocity))

            AssetManager.instance().get(AssetType.Sound, Config.instance().data["audio"]["allied_bullet"]["name"]).play()
