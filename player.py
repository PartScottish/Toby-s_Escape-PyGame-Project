#Matthew Laws
#Memor Patris
#10/12/2020

import pygame
from pygame.locals import *
from utils import *

#designing the player
class player(pygame.sprite.Sprite):

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        self.index = 0
        self.counter = 0
        for num in range (1,5):
            #iterates through an index of images to for animation
            player_image = pygame.image.load(f'sprite/toby{num}.png')
            self.images.append(player_image)
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = [x,y]
        self.vel = 0
        self.face_right = True
        self.can_jump = False


    def set_direction(self, key_press):
        #Starts the character facing right
        self.face_right = key_press == pygame.K_RIGHT
 

    def set_jump(self, key_press):
        #handles for only allowing one jump and only when on a platform
        if self.can_jump:
            if key_press == pygame.K_SPACE:
                self.vel = jump_velocity
            #handles animation when jumping
            self.counter += 1
            image_cooldown = 50
            if self.counter > image_cooldown:
                self.counter = 0
                if self.vel == 0:
                    self.index = 0
                else:
                    self.index = (self.index + 1) % (len(self.images))

            
    def set_movement(self, key_state):
        #handles player sprite movement
        current_position = self.rect.center
        if pygame.key.get_pressed()[pygame.K_RIGHT]:
            self.rect.center = [current_position[0] + 10, current_position[1]]
        if pygame.key.get_pressed()[pygame.K_LEFT]:
            self.rect.center = [current_position[0] - 10, current_position[1]]
    

    def check_collision(self, collidables):
        #handles player collisions with objects
        for collidable in collidables:
            if self.rect.colliderect(collidable):               
                if self.rect.top < collidable.rect.bottom and self.rect.top > collidable.rect.top:
                    self.rect.top = collidable.rect.bottom
                    self.vel = 0
                if self.rect.bottom < collidable.rect.bottom and self.rect.bottom > collidable.rect.top:
                    self.rect.bottom = collidable.rect.top
                    self.can_jump = True
                return
        self.can_jump = debug_mode #set debug_mode to true to enable infinite jumping in debug


    def update(self):
        #starts facing right
        self.image = pygame.transform.flip(self.images[self.index],self.face_right,False)
        #handles "gravity"
        self.vel += 3
        if self.vel > 25:
            self.vel = 25
        updated_position = self.rect.y + self.vel
        self.rect.y = updated_position
       
       #handles world wrapping
        if self.rect.right <= 0:
            self.rect.x = screen_width -1
        if self.rect.x >= screen_width:
            self.rect.right = 1

        #handles animation animation of sprite's legs
        self.counter += 1
        image_cooldown = 30
        if self.counter > image_cooldown:
            self.counter = 0
            if self.vel == 0:
                self.index = 0
            else:
                self.index = (self.index + 1) % (len(self.images))


    def sprite_dead(self):
        #game over case
        return self.rect.top > screen_length