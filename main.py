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
        if self.rect.top > Height:
            self.rect.top = Height
        if self.rect.bottom < 0:
            self.rect.bottom = 0
            
#Criando classe para os alimentos:          
class alimentos(pygame.sprite.Sprite):
    def __init__(self,img):
        pygame.sprite.Sprite.__init__(self)

# dimensões do toco
toco_WIDTH = 60
toco_HEIGHT = 60

# criando classe do toco
class toco_de_madeira(pygame.sprite.Sprite):
    def __init__(self):
        self.image = pygame.image.load('toco.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (toco_WIDTH, toco_HEIGHT))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, toco_WIDTH)
        self.rect.y = random.randint(-100, toco_HEIGHT)
        self.speedx = random.randint(-3, 3)
        self.speedy = random.randint(2, 9)

# Animacao do alimento cortado:
Animacao_Width = 60
Animacao_Height = 60
class alimento_cortado(pygame.sprite.Sprite):
    def __init__(self,center,assets):
        pygame.sprite.Sprite.__init__(self)
        self.Animacao_alimento = assets['Animacao_alimento']
        self.frame = 0
        self.image = self.animacao_alimento[self.frame]
        self.rect = self.image.get_rect 
        self.rect.center = center 
        self.last_update = pygame.time.get_ticks()
        self.frame_ticks = 50
    def update(self):
        now = pygame.time.get_ticks()
        elapsed_ticks = now = self.last_update
        if elapsed_ticks > self.frame_ticks:
            self.last_update = now
            self.frmae += 1
            if self.frame = len(self.Animacao_alimento):
                self.kill()
            else: center = self.rect.center
            self.image = self.Animacao_alimento[self.frame]
            self.rect = self.image.get_rect()
            self.rect.center = center
        

assets = {}
assets['BackgroundImage'] = pygame.image.load('assets/img/ninja-village png.png').convert()
assets['BackgroundImage'] = pygame.transform.scale(assets['BackgroundImage'], (Width,Height))
assets['NinjaImage'] = pygame.image.load('assets/img/Ninja_Tramontina.png').convert_alpha()
assets['NinjaImage'] = pygame.transform.scale(assets['NinjaImage'], (Ninja_Widht,Ninja_Height))


BackgroundImage = pygame.image.load('ninja-village png.png').convert()
BackgroundImage = pygame.transform.scale(BackgroundImage, (Width,Height))

NinjaImage = pygame.image.load('Ninja_Tramontina.png').convert_alpha()
NinjaImage = pygame.transform.scale(NinjaImage, (Ninja_Widht,Ninja_Height))

Animacao_alimento = pygame.image.load('corte.png').convert
Animacao_alimento = pygame.transform.scale(Animacao_alimento, (Animacao_Width, Animacao_Height))

Animacao_alimento = []
for i in range[9]:
    filename = 'assets/img/corte0{}.png'.format(i))
    img = pygame.image.load(filename).convert()
    img = pygame.transform.scale(img, (60,60))
    Animacao_alimento.append(img)
assets["Animacao_alimento"] = Animacao_alimento

                       
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

#Criação dos Grupos:
all_sprites = pygame.sprite.Group()
all_alimentos = pygame.sprite.Group()
groups = {}
groups['all_sprites'] = all_sprites
groups['all_alimentos'] = all_alimentos

#Loop Principal:

game = True
while game:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                move_left = True
            if move_left == True:
                Jogador.speedx -= 12
            if event.key == pygame.K_d:
                move_right = True
            if move_right == True:
                Jogador.speedx += 12
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                move_down = True
            if move_down == True:
                Jogador.speedy += 12
            if event.key == pygame.K_w:
                move_up = True
            if move_up == True:
                Jogador.speedy -= 12
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                move_left = False
            if event.key == pygame.K_d:
                move_right == False
                
    all_sprites.update()
    colisao = pygame.sprite.groupcollide(all_alimentos, Jogador,True,True)
    for alimento in colisao:
        
    janela.fill((0,0,0))
    janela.blit(BackgroundImage,(0,0))
    all_sprites.draw(janela)
    pygame.display.update()
   
pygame.quit()