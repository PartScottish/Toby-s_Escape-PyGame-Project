#Matthew Laws
#Memor Patris
#10/12/2020

import pygame
import os

from pygame.locals import *
from highscore import *

#initialisers for text and music
pygame.font.init()
pygame.mixer.init()

#handles resource pathing for OSs other than windows
data_py = os.path.abspath(os.path.dirname(__file__))
sprite_dir = os.path.normpath(os.path.join(data_py, 'sprite'))
def filepath(filename):	
    return os.path.join(sprite_dir, filename)

#Screen size variables
screen_width = 1200
screen_length = 960

bg = pygame.image.load(filepath('bg7.png'))
start_bg = pygame.image.load(filepath('start_bg2.png'))
death_bg = pygame.image.load(filepath('death_bg.png'))
game_icon = pygame.image.load(filepath('tinytoby.png'))
control_screen_bg = pygame.image.load(filepath('keyboard_layout_screen.png'))

#text variables
dungeonfont = filepath('dungeonfont.ttf')
textalpha = 175

#coordinate variables
bg_print_coord = 0,0

#Clock and Score variables
frame_rate = 60
player_score = 0
start_time = 90
clock = pygame.time.Clock()
WHITE = (255,255,255)
font = pygame.font.Font(dungeonfont, 30)
starting_score = 0 

#Game Over text elements
game_over = "GAME OVER"
game_over_font = pygame.font.Font(dungeonfont, 100) 
game_over_text = game_over_font.render(game_over, True, WHITE)
play_again = "Continue? y/n"
play_again_font = pygame.font.Font(dungeonfont, 50) 
play_again_text = play_again_font.render(play_again, True, WHITE)

#Start Screen text elements
press_any_key = "press any key to start!"
press_any_key_font = pygame.font.Font(dungeonfont, 50) 
press_any_key_text = press_any_key_font.render(press_any_key, True, WHITE)
name_credit = "by Matthew Laws"
name_credit_font = pygame.font.Font(dungeonfont, 25) 
name_credit_text = name_credit_font.render(name_credit, True, WHITE)
in_memory = "In loving memory of my father, Malcolm John Till"
in_memory_font = pygame.font.Font(dungeonfont, 17) 
in_memory_text = in_memory_font.render(in_memory, True, WHITE)

#Music
start_screen_music = filepath('start_screen.wav')
main_game_music = filepath('main_game.wav')
death_screen_music = filepath('death_screen.wav')

#Player variables
gravity_velocity = 3
player_start_x = 60
player_start_y = 100
jump_velocity = -50

#Platform variables
platform_speed = 1
tile_width = 80
tile_height = 100
tile_offset_amount = tile_width * -1

#Game condition variables
start_screen = "StartScreen"
control_screen = "ControlScreen"
game_playing = "GamePlayingScreen"
current_screen_state = start_screen
player_dead_state = "PlayerDead"
is_exited = False

#Group/Sprite setups
torch_group = pygame.sprite.Group()
player_group = pygame.sprite.Group()
platform_group = pygame.sprite.Group()
start_screen_group = pygame.sprite.Group()
end_screen_group = pygame.sprite.Group()

#Debug
#this allows infinite jumping
debug_mode = False