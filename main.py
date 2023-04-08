import pygame, sys
import time
import random

from pygame.locals import *
from game import menu

#display
gameDisplay = pygame.display.set_mode((800, 600),0,32)
pygame.display.set_caption('Fusquinha')

#musica 
pygame.mixer.music.set_volume(0.08)
background_music=pygame.mixer.music.load("wil8.mp3")
pygame.mixer.music.play(-1)

menu.main_menu(gameDisplay)