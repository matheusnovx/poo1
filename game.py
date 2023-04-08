import pygame, sys

from transito import Carro, Motoca
from fusquinha import Fusca
from trafego import Linhas
from pygame.locals import *

pygame.init()

#display
display_width = 800
display_height = 600
gameDisplay = pygame.display.set_mode((800, 600),0,32)
pygame.display.set_caption('Fusquinha')

bg_image = pygame.image.load('gfx/bg.png')#imagem de fundo 
mainClock = pygame.time.Clock()
font = pygame.font.SysFont(None, 20)

class Menu:
    #menu 
    def __init__(self):
        self.bg_image = pygame.image.load('gfx/bg.png')
        self.titulo =  titulo = pygame.image.load('gfx/titulo.png')
        self.jogar_img =  pygame.image.load('gfx/jogar.png')
        self.sair_img =  pygame.image.load('gfx/sair.png')

    def main_menu(self, gameDisplay):
        
        click = False
        while True:
            
            gameDisplay.blit(self.bg_image, (0,0)) #colocando o fundo no menu
            gameDisplay.blit(self.titulo, (160,0)) #imagem do titulo
            
            #localização mouse
            mx, my = pygame.mouse.get_pos()

            #os botões
            button_1 = pygame.Rect(300, 300, 200, 50)
            button_2 = pygame.Rect(300, 400, 200, 50)

            if button_1.collidepoint((mx, my)):
                if click:
                    game()
            if button_2.collidepoint((mx, my)):
                if click:
                    pygame.quit()
                    sys.exit()

            click = False
            
            gameDisplay.blit(self.jogar_img, button_1)
            gameDisplay.blit(self.sair_img, button_2)
    
            
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click = True
    
            pygame.display.update()
            mainClock.tick(60)

def game():

    #carrito 
    fusquinha = Fusca((display_width * 0.45),(display_height * 0.8),85,140)

    #transito - carro
    carro = Carro(85, 140)
    motoca = Motoca(30, 100)

    #linhas de trafego
    linhas = Linhas()

    gameExit = False
    
    while not gameExit:

        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        keys = pygame.key.get_pressed() 
        
        gameDisplay.blit(bg_image, (0,0))

        #desenhando e movimentando linhas de trafego
        linhas.draw_linhatrafego(gameDisplay)
        linhas.movimentacao_trafego(display_height)

        #desenhando e movimentando o transito
        carro.draw_carro(gameDisplay)
        carro.movimentacao_carro(display_height)

        motoca.draw_moto(gameDisplay)
        motoca.movimentacao_moto(display_height)

        #movimentando, e desenhando  o fusquinha 
        fusquinha.draw_fusca(gameDisplay)
        fusquinha.movimentacao(keys, display_width, display_height)



        #definindo colisão 
        if (fusquinha.y  < carro.hitbox[1] + carro.hitbox[3] and fusquinha.y + 135 > carro.hitbox[1]) and (fusquinha.x  < carro.hitbox[0] + carro.hitbox[2] and fusquinha.x + 80> carro.hitbox[0]) :
            menu.main_menu(gameDisplay)
            
        if (fusquinha.y  < motoca.hitbox[1] + motoca.hitbox[3] and fusquinha.y + 135 > motoca.hitbox[1]) and (fusquinha.x  < motoca.hitbox[0] + motoca.hitbox[2] and fusquinha.x + 80> motoca.hitbox[0]) :
            menu.main_menu(gameDisplay)
        
        pygame.display.update()
        mainClock.tick(60)


menu = Menu()