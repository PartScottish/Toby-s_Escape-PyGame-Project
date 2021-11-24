#Matthew Laws
#Memor Patris
#10/12/2020

import pygame
from pygame.locals import *
import random

#designing the ghost
class ghost(pygame.sprite.Sprite):

    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        self.index = 0
        self.counter = 0
        for num in range (1,3):
            #iterates through an index of images to for animation
            img = pygame.image.load(f'sprite/ghost{num}.png')
            self.images.append(img)
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = [x,y]

        
    def update(self):
        #handles ghost animation
        self.counter += 1
        #random image cooldown rate to randomise the animation of the ghosts
        image_cooldown = random.randint(20,50)
        if self.counter > image_cooldown:
            self.counter = 0
            self.index +=1
            if self.index >= len(self.images):
                self.index = 0
        self.image = self.images[self.index]