import pygame

class Fusca:

    def __init__(self, x,y, width, height):
        self.x = x 
        self.y = y
        self.width = width
        self.height = height
        self.vel = 4
        self.img = pygame.image.load('gfx/carro_novo.png')
        self.hitbox = (self.x, self.y, self.width, self.height)

    def draw_fusca(self, gameDisplay):
        gameDisplay.blit(self.img, (self.x, self.y))
        self.hitbox = (self.x, self.y, self.width, self.height)
        #pygame.draw.rect(gameDisplay, (255,0,0), self.hitbox, 2)  
        
    def movimentacao(self, keys, display_width, display_height):
        if keys[pygame.K_LEFT] and self.x > (display_width * 0.2) + 10: 
            self.x -= self.vel
        if keys[pygame.K_RIGHT] and self.x < (display_width * 0.8) - self.width - 10:
            self.x += self.vel
        if keys[pygame.K_UP] and self.y > self.vel:
            self.y -= self.vel
        if keys[pygame.K_DOWN] and self.y < display_height - self.height:
           self.y += self.vel