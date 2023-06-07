import pygame as pg
from settings import *
import os
from collections import deque
from sprite_object import *

class AnimatedSprite(SpriteObject):
    def __init__(self, game, path='resources/sprites/animated_sprites/green_light/0.png', pos=(11.5,3.5), scale=0.8, shift=0.15, animation_time=120, inspect_animation_time=120, pullout_animation_time=120):
        super().__init__(game, path, pos, scale, shift)
        self.animation_time = animation_time
        self.inspect_animation_time = inspect_animation_time
        self.pullout_animation_time = pullout_animation_time
        self.path = path.rsplit('/', 1)[0]
        self.images = self.get_images(self.path)
        self.animation_time_prev = pg.time.get_ticks()
        self.animation_trigger = False
    def update(self):
        super().update()
        self.check_animation_time()
        self.animate(self.images)

    def animate(self, images):
        if self.animation_trigger == True:
            images.rotate(-1)
            self.image = images[0]
    
    def check_animation_time(self):
        self.animation_trigger = False
        time_now = pg.time.get_ticks()
        if self.game.current_weapon == "awp":
            if self.game.awp.reloading == True:
                if time_now - self.animation_time_prev > self.animation_time:
                    self.animation_time_prev = time_now
                    self.animation_trigger = True
            if self.game.awp.inspecting == True:
                if time_now - self.animation_time_prev > self.inspect_animation_time:
                    self.animation_time_prev = time_now
                    self.animation_trigger = True
            if self.game.awp.pullingout == True:
                if time_now - self.animation_time_prev > self.pullout_animation_time:
                    self.animation_time_prev = time_now
                    self.animation_trigger = True
        if self.game.current_weapon == "shotgun":
            if self.game.shotgun.reloading == True:
                if time_now - self.animation_time_prev > self.animation_time:
                    self.animation_time_prev = time_now
                    self.animation_trigger = True
            if self.game.shotgun.inspecting == True:
                if time_now - self.animation_time_prev > self.inspect_animation_time:
                    self.animation_time_prev = time_now
                    self.animation_trigger = True
            if self.game.shotgun.pullingout == True:
                if time_now - self.animation_time_prev > self.pullout_animation_time:
                    self.animation_time_prev = time_now
                    self.animation_trigger = True
            
    

    def get_images(self, path, scale=1.0):
        images = deque()
        for file_name in os.listdir(path):
            if os.path.isfile(os.path.join(path, file_name)):
                img = pg.image.load(path + '/' + file_name).convert_alpha()
                img = pg.transform.scale(img, (int(img.get_width() * scale), int(img.get_height() * scale)))
                images.append(img)
        return images










