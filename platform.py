#Matthew Laws
#Memor Patris
#10/12/2020

import pygame
from pygame.locals import *
from utils import *
import random
     

class platform(pygame.sprite.Sprite):
    #Setting the platform image - intentionally not set in utils
    platform_image = pygame.image.load('sprite/platform8.png')

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = self.platform_image
        self.rect = self.image.get_rect()
        self.rect.topleft = [x,y]


    def change_height(self, difference):
        self.rect.y += difference +2


    def update(self):
        #handling platform re-drawing from bottom to top of screen
        if self.rect.top > screen_length:
            self.rect.bottom = 0
            x_pos = random.randint(0,1000)
            self.rect.x = x_pos
            y_pos = self.set_platform_height()
            self.rect.y = y_pos
            self.check_col()


    def set_platform_height(self):     
        #determines y position to redraw platforms in the update function
        our_minimum_y = -100
        for platform in platform_group:
            our_minimum_y = min(our_minimum_y, platform.rect.y -30) 
        y_pos = random.randint(our_minimum_y, -100)
        return y_pos


    def check_platform_collision(self):
        #ensures the platform does not check itself for collision
        for platform in platform_group:
            if platform == self:
                continue
            if self.rect.colliderect(platform.rect):
                #moves colliding platform to a new x position recursively              
                self.rect.x += 150
                self.check_platform_collision()
 

    def check_col(self):
        #handles ensuring platforms do not redraw/respawn on top of one another on the x axis(col/columns) and calls check_platform_collision() recursively to redraw
        for platform in platform_group:
            if platform == self:
                #ensures the platform does not check itself for collision
                continue
            if self.rect.colliderect(platform.rect):
                self.rect.x += 150
                self.check_col()
            if self.rect.left > platform.rect.left and self.rect.left < platform.rect.right:
                self.rect.left = platform.rect.right
                self.check_col()
            elif self.rect.right > platform.rect.left and self.rect.right < platform.rect.right:
                self.rect.left = platform.rect.right
                self.check_col()


    def check_platform_column(self):
        #handles platforms do not redraw/respawn on top of one another on the y axis and calls check_platform_collision() recursively to redraw
        for platform in platform_group:
            if platform == self:
                #ensures the platform does not check itself for collision
                continue
            if self.rect.left > platform.rect.left and self.rect.left < platform.rect.right:
                self.rect.left = platform.rect.right
                self.check_platform_column()
            elif self.rect.right > platform.rect.left and self.rect.right < platform.rect.right:
                self.rect.left = platform.rect.right
                self.check_platform_column()
