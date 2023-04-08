import pygame
import random

class Carro:

    def __init__(self, width, height):
        self.carro_startx = random.choice([200, 360, 520])
        self.carro_starty = 0
        self.carro_speed = 4
        self.width = width
        self.height = height
        self.img = pygame.image.load('gfx/kadett.png')
        self.hitbox = (self.carro_startx, self.carro_starty, self.width, self.height)


    def draw_carro(self, gameDisplay):
        gameDisplay.blit(self.img, (self.carro_startx, self.carro_starty))
        self.hitbox = (self.carro_startx, self.carro_starty, self.width, self.height)
        #pygame.draw.rect(gameDisplay, (255,0,0), self.hitbox, 2)

    def movimentacao_carro(self, display_height):
        if self.carro_starty > display_height:
            self.carro_startx = random.choice([200, 360, 520])
            self.carro_starty = -200
            self.carro_speed += 0.08
        
        self.carro_starty += self.carro_speed
        
class Motoca:

    def __init__(self, width, height):
        self.moto_startx = random.choice([320, 480])
        self.moto_starty = -350
        self.width = width
        self.height = height
        self.moto_speed = 2
        self.img = pygame.image.load('gfx/cg400.png')
        self.hitbox = (self.moto_startx, self.moto_starty, self.width, self.height)


    def draw_moto(self, gameDisplay):
        gameDisplay.blit(self.img, (self.moto_startx, self.moto_starty))
        self.hitbox = (self.moto_startx, self.moto_starty, self.width, self.height)
        #pygame.draw.rect(gameDisplay, (255,0,0), self.hitbox, 2)

    def movimentacao_moto(self, display_height):
        if self.moto_starty > display_height:
            self.moto_startx = random.choice([300, 460])
            self.moto_starty = -350
            self.moto_speed += 0.01
        
        self.moto_starty += self.moto_speed