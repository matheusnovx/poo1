import pygame

class Linhas:

    def __init__(self):
        self.trafego_startx = 320
        self.trafego_startx2 = 480
        self.trafego_starty1 = -500
        self.trafego_starty2 = -250
        self.trafego_starty3 = 0
        self.trafego_speed = 7
    
    #def trafegos(trafegox, trafegoy, trafegow, trafegoh, color)
    def draw_linhatrafego(self, gameDisplay): #fazendo um retangulo pra representar a linha de trafego
        pygame.draw.rect(gameDisplay, (255,255,255), [self.trafego_startx, self.trafego_starty1, 2, 120])
        pygame.draw.rect(gameDisplay, (255,255,255), [self.trafego_startx, self.trafego_starty2, 2, 120])
        pygame.draw.rect(gameDisplay, (255,255,255), [self.trafego_startx, self.trafego_starty3, 2, 120])
        pygame.draw.rect(gameDisplay, (255,255,255), [self.trafego_startx2, self.trafego_starty1, 2, 120])
        pygame.draw.rect(gameDisplay, (255,255,255), [self.trafego_startx2, self.trafego_starty2, 2, 120])
        pygame.draw.rect(gameDisplay, (255,255,255), [self.trafego_startx2, self.trafego_starty3, 2, 120])

    def movimentacao_trafego(self, display_height):
        if self.trafego_starty1 > display_height:
            self.trafego_starty1 = 0 - 100
            self.trafego_speed += 0.01
        if self.trafego_starty2 > display_height:
            self.trafego_starty2 = 0 - 100
            self.trafego_speed += 0.01
        if self.trafego_starty3 > display_height:
            self.trafego_starty3 = 0 - 100
            self.trafego_speed += 0.01

        #meu deus - linhas de trafego
        self.trafego_starty1 += self.trafego_speed
        self.trafego_starty2 += self.trafego_speed
        self.trafego_starty3 += self.trafego_speed