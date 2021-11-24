import pygame
from pygame.locals import *


#designing the torches
class torch(pygame.sprite.Sprite):

    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        self.index = 0
        self.counter = 0
        for num in range (1,6):
            #iterates through an index of images to for animation
            img = pygame.image.load(f'sprite/torch{num}.png')
            self.images.append(img)
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = [x,y]
        

    def update(self):
        #handles torch animation
        self.counter += 1
        image_cooldown = 5
        if self.counter > image_cooldown:
            self.counter = 0
            self.index +=1
            if self.index >= len(self.images):
                self.index = 0
        self.image = self.images[self.index]