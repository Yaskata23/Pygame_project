from sprite_object import *

class Shotgun(AnimatedSprite):
    def __init__(self, game, path='resources/sprites/weapon/shotgun/shotgun_shot/1.png', scale=2.1, animation_time=50):
        super().__init__(game=game, path=path, scale=scale, animation_time=animation_time)
        self.images = deque(
            [pg.transform.smoothscale(img, (self.image.get_width() * scale, self.image.get_height() * scale))
             for img in self.images])
        # Add inspect images folder path
        self.inspect_path = 'resources/sprites/weapon/shotgun/shotgun_inspect'
        # Load inspect images
        self.inspect_images = self.get_images(self.inspect_path, scale=2.3)
        # Set initial inspect image
        self.inspect_image = self.inspect_images[0]
        # Set inspect animation parameters
        self.inspect_animation_time = 100  # Adjust as needed
        self.inspect_frame_counter = 0
        self.inspect_num_images = len(self.inspect_images)
        self.inspecting = False
        self.weapon_pos = (HALF_WIDTH - self.images[0].get_width() // 2, HEIGHT - self.images[0].get_height())
        self.reloading = False
        self.num_images = len(self.images)
        self.frame_counter = 0
        self.damage = 1000

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
                    self.inspecting = False  # Stop inspect animation on shot
                    
    
    def inspect(self):
        if not self.inspecting:
            # Start inspect animation
            self.inspecting = True
            self.inspect_frame_counter = 0
            self.animation_time_prev = pg.time.get_ticks()  # Reset animation time

    def animate_inspect(self):
        if self.inspecting:
            if self.animation_trigger:
                self.inspect_images.rotate(1)
                self.inspect_image = self.inspect_images[0]
                self.inspect_frame_counter += 1
                if self.inspect_frame_counter == self.inspect_num_images:
                    # Stop inspect animation
                    self.inspecting = False
                    self.inspect_frame_counter = 0

    def draw(self):
        if self.inspecting:
            inspect_width = self.inspect_image.get_width()
            inspect_height = self.inspect_image.get_height()
            inspect_x = HALF_WIDTH - inspect_width // 2
            inspect_y = HEIGHT - inspect_height
            inspect_pos = (inspect_x, inspect_y)
            self.game.screen.blit(self.inspect_image, inspect_pos)
        else:
            self.game.screen.blit(self.images[0], self.weapon_pos)


    def update(self):
        self.check_animation_time()
        self.animate_shot()
        self.animate_inspect()
        if self.inspecting:
            # Stop inspect animation after one full rotation
            if self.inspect_frame_counter == self.inspect_num_images:
                self.inspecting = False
                self.inspect_frame_counter = 0
