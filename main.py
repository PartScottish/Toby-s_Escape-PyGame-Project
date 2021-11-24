#Matthew Laws
#Memor Patris
#10/12/2020

import pygame
import random

#importing resources
from pygame.locals import *
from platform import *
from music import *
from utils import *
from torch import *
from player import *
from highscore import *
from ghost import *

#initialisers
pygame.init()
pygame.font.init()
pygame.mixer.init()

#screen drawing
screen = pygame.display.set_mode((screen_width, screen_length),)
pygame.display.set_caption("Toby's Escape!")
pygame.display.set_icon(game_icon)

#function imports
music = myMusic()
high_score_persister = high_score_persister()
pygame.time.Clock()


def initialise_game():
    #game initialisation allowing for restarting after death
    #TO-DO: remove all coordinate hard-coding.

    #drawing torches
    torch_group.empty()
    torch_group.add (torch(100,200))
    torch_group.add (torch(400,400))
    torch_group.add (torch(900,600))
    torch_group.add (torch(1100,350))

    #drawing torches to start screen
    start_screen_group.empty()
    start_screen_group.add (torch(200,250))
    start_screen_group.add (torch(1010,250))

    #drawing ghosts to end screen
    end_screen_group.empty()
    end_screen_group.add (ghost(200,400))
    end_screen_group.add (ghost(990,400))

    #drawing in the player
    player_group.empty()
    player_sprite.rect.x = player_start_x
    player_sprite.rect.y = player_start_y
    player_group.add(player_sprite)

    tile_offset = tile_offset_amount

    #Set initial platform positions
    platform_group.empty()
    platform_group.add(platform(1,500))
    platform_group.add(platform(150,350))
    platform_group.add(platform(200,650))
    platform_group.add(platform(400,100))
    platform_group.add(platform(600,700))
    platform_group.add(platform(750,200))
    platform_group.add(platform(800,400))
    platform_group.add(platform(1000,800))
    #last platforms set almost off-screen to balance a steady fall of platforms  
    platform_group.add(platform(300,1190))
    platform_group.add(platform(900,1190)) 

#player assignment 
player_sprite = player(player_start_x, player_start_y)

def keyboard_input(events):
    #setting up movement function event
    for event in events:
        if event.type == pygame.KEYDOWN:
            player_group.set_direction(event.key)

def print_score(score, x, y):
    #setting up score/highscore function
    player_score = font.render(score, True, WHITE)
    player_score.set_alpha(textalpha)
    screen.blit(player_score, [x, y])

initialise_game()
#starting the game

while is_exited != True:
#exit conditions and start screen setup
    events = pygame.event.get()

    for event in events:
        #exit event
        if event.type == pygame.QUIT:
            is_exited = True

    if current_screen_state == start_screen:
        #Background, sprite, music and text to draw to the start screen
        music.set_music(start_screen_music)
        screen.blit(start_bg,(bg_print_coord))
        press_any_key_text.set_alpha(textalpha)
        screen.blit(press_any_key_text, [275, 750])
        screen.blit(name_credit_text,[13, 920]) 
        name_credit_text.set_alpha(textalpha)
        screen.blit(in_memory_text, [725, 920])
        in_memory_text.set_alpha(textalpha)
        start_screen_group.draw(screen)
        start_screen_group.update()       
    
        for event in events:
            #event design for "any key"
            if event.type==KEYDOWN or event.type==MOUSEBUTTONDOWN:
                current_screen_state = control_screen

    elif current_screen_state == control_screen:
        #Background, sprite, music and text to draw to the controls screen
        music.set_music(start_screen_music)
        screen.blit(control_screen_bg,(bg_print_coord))
        press_any_key_text.set_alpha(textalpha)
        screen.blit(press_any_key_text, [275, 850])    
        
        for event in events:
            #event design for "any key"
            if event.type==KEYDOWN or event.type==MOUSEBUTTONDOWN:
                current_screen_state = game_playing  

    
    elif current_screen_state == game_playing:
    #main game loop
        #Background, sprite, music and text to draw to the main game screen
        music.set_music(main_game_music)
        screen.blit(bg,(bg_print_coord))
        torch_group.draw(screen)
        torch_group.update()
        platform_group.draw(screen)
        platform_group.update()
        
        #where p is platform
        for p in platform_group:
            p.change_height (platform_speed)

        #drawing and updating the player
        player_group.draw(screen)
        player_group.update()

        #checking for collisions between player and platforms
        player_sprite.check_collision(platform_group)

        for event in events:
            #handles jumping and movement function inputs     
            if event.type == pygame.KEYDOWN:
                player_sprite.set_direction(event.key)
                player_sprite.set_jump(event.key)
        player_sprite.set_movement(pygame.key.get_pressed())

        if player_sprite.sprite_dead():
            #handles game over state
            current_screen_state = player_dead_state
    

        #Handles Score - CONTRIB: Paul Vincent Craven - printing a per-second timer
        Score = "Score {0}".format(player_score)   
        print_score(Score, 50, 50)
        high_score  = "High Score {0}".format(high_score_persister.get_high_score()) 
        print_score(high_score, 50, 100)
        player_score += 1
        # Limit frames per second
        clock.tick(frame_rate)


    else:
    #handling death screen
        
        #Score handling
        high_score_persister.save_high_score(player_score)
        player_score = starting_score

        #Background, sprite, music and text to draw to the death screen
        music.set_music(death_screen_music)
        screen.blit(death_bg,(bg_print_coord))
        screen.blit(game_over_text, [300, 350])
        play_again_text.set_alpha(textalpha)
        screen.blit(play_again_text, [380, 600])
        end_screen_group.draw(screen)
        end_screen_group.update()

        
        for event in events:
            #Handles input for restarting the game or exiting to main menu
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_n:
                    current_screen_state = start_screen 
                    initialise_game()
                if event.key == pygame.K_y:
                    initialise_game()
                    current_screen_state = game_playing


    
    #updating the screen
    pygame.display.update()

pygame.quit()