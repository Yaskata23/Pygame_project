import pygame as pg


class Sound:
    def __init__(self, game):
        self.game = game
        pg.mixer.init()
        self.path = 'resources/sound/'
        # self.shotgun = pg.mixer.Sound(self.path + 'shotgun.wav')
        self.npc_pain = pg.mixer.Sound(self.path + 'npc_pain.wav')
        self.npc_death = pg.mixer.Sound(self.path + 'npc_death.wav')
        self.npc_shot = pg.mixer.Sound(self.path + 'npc_attack.wav')
        self.player_pain = pg.mixer.Sound(self.path + 'player_pain.wav')
        self.awp_shot = pg.mixer.Sound(self.path + 'awp_shot.mp3')
        # self.theme = pg.mixer.music.load(self.path + 'theme.mp3')
        self.sawed_off_shot = pg.mixer.Sound(self.path + 'sawed_off_shot.mp3')
        self.sawed_off_pullout = pg.mixer.Sound(self.path + 'sawed_off_pullout.mp3')
        self.awp_pullout = pg.mixer.Sound(self.path + 'awp_pullout.mp3')

        # VOLUME CORRECTION
        self.sawed_off_pullout.set_volume(1)
        self.sawed_off_shot.set_volume(0.3)
        self.awp_shot.set_volume(0.1)
        self.player_pain.set_volume(0.1)
        self.npc_shot.set_volume(0.1)
        self.npc_pain.set_volume(0.1)
        self.npc_death.set_volume(0.1)
        self.awp_pullout.set_volume(1)

        # pg.mixer.music.set_volume(1)