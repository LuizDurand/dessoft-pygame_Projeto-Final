import pygame
import random
pygame.init()

#Condições Iniciais
vidas = 3
high_score = []
placar = 0
Width = 900
Height = 680
janela = pygame.display.set_mode((Width,Height))

# cores
Branco = (255,255,255)
Vermelho = (255,0,0)
Azul = (0,0,255)
Preto = (0,0,0)
Verde = (0,0,255)
Amarelo = (255,255,0)

#Criando o boneco:
Ninja_Widht = 60
Ninja_Height = 60
class Ninja(pygame.sprite.Sprite):
    def __init__(self,img):
        pygame.sprite.Sprite.__init__(self)
        self.image = img 
        self.rect = self.image.get_rect()
        self.rect.centerx = Width / 2
        self.rect.bottom = Height -10
        self.speedx = 0
        self.speedy = 0
    def update(self): 
        self.rect.x = self.speedx
        self.rect.y = self.speedy
        if self.rect.right > Width:
            self.rect.right = Width
        if self.rect.left < 0:
            self.rect.left = 0

# dimensões do toco
toco_WIDTH = 60
toco_HEIGHT = 60


# criando classe do toco
class toco_de_madeira(pygame.sprite.Sprite):
    def __init__(self):
        self.image = pygame.image.load('assets/img/toco.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (toco_WIDTH, toco_HEIGHT))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, toco_WIDTH)
        self.rect.y = random.randint(-100, -toco_HEIGHT)
        self.speedx = random.randint(-3, 3)
        self.speedy = random.randint(2, 9)


BackgroundImage = pygame.image.load('ninja-village png.png').convert()
BackgroundImage = pygame.transform.scale(BackgroundImage, (Width,Height))
NinjaImage = pygame.image.load('ninja pixel.png').convert_alpha()
NinjaImage = pygame.transform.scale(NinjaImage, (Ninja_Widht,Ninja_Height))

pygame.display.set_caption('Fruit ninja boladão')
icone = pygame.image.load('ninja pixel.png')
pygame.display.set_icon(icone)

#Criando o jogador:
all_sprites = pygame.sprite.Group()
Jogador = Ninja(NinjaImage)
all_sprites.add(Jogador)

#Ajuste de velocidade do jogo:
FPS  = 30
clock = pygame.time.Clock()

#Loop Principal:
game = True
while game:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                Jogador.speedx -= 8
            if event.key == pygame.K_d:
                Jogador.speedx += 8
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                Jogador.speedy += 8
            if event.key == pygame.K_w:
                Jogador.speedy -= 8
    all_sprites.update()
    janela.fill((0,0,0))
    janela.blit(BackgroundImage,(0,0))
    all_sprites.draw(janela)
    pygame.display.update()
    
pygame.quit()