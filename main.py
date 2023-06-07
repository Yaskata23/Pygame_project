import pygame as pg
import sys
from settings import *
from map import *
from player import *
from raycasting import *
from object_renderer import *
from sprite_object import *
from object_handler import *
from shotgun import *
from awp import *
from sound import *
from pathfinding import *


class Game:
    def __init__(self):
        pg.init()
        pg.mouse.set_visible(False)
        self.screen = pg.display.set_mode(RES)
        pg.event.set_grab(True)
        self.clock = pg.time.Clock()
        self.delta_time = 1
        self.global_trigger = False
        self.current_weapon = "shotgun"
        self.global_event = pg.USEREVENT + 0
        pg.time.set_timer(self.global_event, 40)
        self.new_game()

    def new_game(self):
        self.map = Map(self)
        self.player = Player(self)
        self.object_renderer = ObjectRenderer(self)
        self.raycasting = RayCasting(self)
        self.object_handler = ObjectHandler(self)
        self.shotgun = Shotgun(self)
        self.awp = Awp(self)
        self.sound = Sound(self)
        self.pathfinding = PathFinding(self)

    def update(self):
        self.player.update()
        self.raycasting.update()
        self.object_handler.update()
        self.shotgun.update()
        self.awp.update()
        pg.display.flip()
        self.delta_time = self.clock.tick(FPS)
        pg.display.set_caption(f'{self.clock.get_fps() :.1f}')

    def draw(self):
        # self.screen.fill('black')
        self.object_renderer.draw()
        if self.current_weapon == "shotgun":
            self.shotgun.draw()
        if self.current_weapon == "awp":
            self.awp.draw()
        # self.map.draw()
        # self.player.draw()

    def check_events(self):
        self.global_trigger = False
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()
            elif event.type == self.global_event:
                self.global_trigger = True
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_f:
                    if self.current_weapon == "awp":
                        self.awp.inspect()
                    if self.current_weapon == "shotgun":
                        self.shotgun.inspect()
                elif event.key == pg.K_2:
                    if self.current_weapon != "awp":
                        self.current_weapon = "awp"
                        self.shotgun.inspecting = False  # Stop inspect animation when switching to AWP
                elif event.key == pg.K_1:
                    if self.current_weapon != "shotgun":
                        self.current_weapon = "shotgun"
                        self.shotgun.inspecting = False  # Stop inspect animation when switching to AWP
                        self.awp.inspecting = False  # Reset inspect animation when switching to shotgun
            self.player.single_fire_event(event)


    def run(self):
        while True:
            self.check_events()
            self.update()
            self.draw()


if __name__ == "__main__":
    game = Game()
    game.run()