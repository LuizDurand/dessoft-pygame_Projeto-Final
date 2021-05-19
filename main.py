import pygame 
import random
pygame.init()

janela = pygame.display.set_mode((800,600))

pygame.display.set_caption('abc')
icone = pygame.image.load('ninja.png')
pygame.display.set_icon(icone)

janela_aberta = True
while janela_aberta:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            janela_aberta = False
            
   