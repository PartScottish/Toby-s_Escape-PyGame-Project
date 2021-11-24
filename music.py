#Matthew Laws
#Memor Patris
#10/12/2020

import pygame
from pygame.locals import *

#designing music application/class
class myMusic():

    def __init__(self):
        self.current_track = ''

    def set_music(self, track):
        #handles track loading, volume and fade-in of sound
        if self.current_track != track:
            self.stop_music()
            pygame.mixer.music.load(track)
            pygame.mixer.music.set_volume(0.2)
            pygame.mixer.music.play(-1, 0.0, 2500)
            self.current_track = track

    def stop_music(self):
        #handles stopping previous track on screen change and unloads unused resources to save memory
        pygame.mixer.music.stop()
        pygame.mixer.music.unload()
