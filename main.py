import pygame 
import random
pygame.init()

#Condições Iniciais
vidas = 3
high_score = []
placar = 0
janela = pygame.display.set_mode((1920,1080))
# cores
Branco = (255,255,255)
Vermelho = (255,0,0)
Azul = (0,0,255)
Preto = (0,0,0)
Verde = (0,0,255)
Amarelo = (255,255,0)
BackgroundImage = pygame.image.load('')

pygame.display.set_caption('ViniciusNinja')
icone = pygame.image.load('ninja.png')
pygame.display.set_icon(icone)

game = True
while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

pygame.quit()
            