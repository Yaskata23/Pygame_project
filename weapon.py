from spriteobjectforguns import *

class Weapon(AnimatedSprite):
    def __init__(self, game, path='resources/sprites/weapon/awp/awp_shot/0.png', scale=2.3, animation_time=100, inspect_animation_time=100, pullout_animation_time=45):
        super().__init__(game=game, path=path, scale=scale, animation_time=animation_time)
        self.images = self.get_images(self.path + '/gun_shot', scale=2.3)
        self.weapon_pos = (HALF_WIDTH - self.images[0].get_width() // 2, HEIGHT - self.images[0].get_height())
        self.reloading = False
        self.num_images = len(self.images)
        self.frame_counter = 0
        self.damage = 1000
        #INSPECTING
        self.inspect_images = self.get_images(self.path + '/gun_inspect', scale=2.3)
        self.inspect_image = self.inspect_images[0]
        self.inspect_animation_time = inspect_animation_time
        self.inspect_frame_counter = 0
        self.inspect_num_images = len(self.inspect_images)
        self.inspecting = False
        #PULLINGOUT
        self.pullout_images = self.get_images(self.path + '/gun_pullout', scale=2.3)
        self.pullout_image = self.pullout_images[0]
        self.pullout_animation_time = pullout_animation_time
        self.pullout_frame_counter = 0
        self.pullout_num_images = len(self.pullout_images)
        self.pullingout = False

    def shoot(self):
        if not self.reloading:
            self.reloading = True
            self.animation_time_prev = pg.time.get_ticks()

    def animate_shot(self):
        if self.reloading:
            self.game.player.shot = False
            if self.animation_trigger:
                self.images.rotate(1)
                self.image = self.images[0]
                self.frame_counter += 1
                if self.frame_counter == self.num_images:
                    self.reloading = False
                    self.frame_counter = 0
                    self.inspect_frame_counter = 0

    def inspect(self):
        if not self.inspecting and not self.reloading:
            self.inspecting = True
            # self.inspect_images = self.get_images(self.inspect_path, scale=2.3)
            # self.inspect_image = self.inspect_images[0]
            self.animation_time_prev = pg.time.get_ticks()  # Reset animation time

    def animate_inspect(self):
        if self.inspecting:
            if self.animation_trigger:
                self.inspect_images.rotate(-1)
                self.inspect_image = self.inspect_images[0]
                self.inspect_frame_counter += 1
                if self.inspect_frame_counter == self.inspect_num_images:
                    self.inspecting = False
                    self.inspect_frame_counter = 0

    def pullout(self):
        if not self.pullingout and not self.reloading:
            self.pullingout = True
            # self.pullout_images = self.get_images(self.pullout_path, scale=2.3)
            # self.pullout_image = self.pullout_images[0]
            self.animation_time_prev = pg.time.get_ticks() 

    def animate_pullout(self):
        if self.pullingout:
            if self.animation_trigger:
                self.pullout_images.rotate(-1)
                self.pullout_image = self.pullout_images[0]
                self.pullout_frame_counter += 1
                if self.pullout_frame_counter == self.pullout_num_images:
                    self.pullingout = False
                    self.pullout_frame_counter = 0

    def draw(self):
        if self.inspecting:
            inspect_width = self.inspect_image.get_width()
            inspect_height = self.inspect_image.get_height()
            inspect_x = HALF_WIDTH - inspect_width // 2
            inspect_y = HEIGHT - inspect_height
            inspect_pos = (inspect_x, inspect_y)
            self.game.screen.blit(self.inspect_image, inspect_pos)
        elif self.pullingout:
            pullout_width = self.pullout_image.get_width()
            pullout_height = self.pullout_image.get_height()
            pullout_x = HALF_WIDTH - pullout_width // 2
            pullout_y = HEIGHT - pullout_height
            pullout_pos = (pullout_x, pullout_y)
            self.game.screen.blit(self.pullout_image, pullout_pos)
        else:
            self.inspect_image = self.inspect_images[0]
            self.inspect_frame_counter += 1
            self.inspecting = False
            self.game.screen.blit(self.images[0], self.weapon_pos)

    def update(self):
        self.check_animation_time()
        self.animate_shot()
        self.animate_inspect()
        self.animate_pullout()

class Shotgun(Weapon):
    def __init__(self, game, path='resources/sprites/weapon/shotgun/0.png', scale=2.3, animation_time = 50, inspect_animation_time = 70, pullout_animation_time = 50):
        super().__init__(game, path, scale, animation_time, inspect_animation_time, pullout_animation_time)
        self.damage = 50

class Awp(Weapon):
    def __init__(self, game, path='resources/sprites/weapon/awp/0.png', scale=2.3, animation_time = 100, inspect_animation_time = 100, pullout_animation_time = 45):
        super().__init__(game, path, scale, animation_time, inspect_animation_time, pullout_animation_time)
        self.damage = 1000
        
class Deagle(Weapon):
    def __init__(self, game, path='resources/sprites/weapon/deagle/0.png', scale=2.3, animation_time = 70, inspect_animation_time = 90, pullout_animation_time = 40):
        super().__init__(game, path, scale, animation_time, inspect_animation_time, pullout_animation_time)
        self.damage = 40

     
