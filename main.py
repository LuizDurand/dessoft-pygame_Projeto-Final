#importa bibliotecas 
import pygame
import random
import time 
#inicia o pygame
pygame.init()
#função para adcionar som ao jogo
pygame.mixer.init()

#Condições Iniciais
vidas = 3 # define vidas que o jogador vai ter 
streak = 0 # contador para acionar os combos
pontuacao = 0 # placar que será exibido durante a gameplay
placar = 0 # placar que será exibido durante a gameplay
Width = 900 # define a largura da tela 
Height = 680 # define a altura da tela 
janela = pygame.display.set_mode((Width,Height)) # cria a janela do jogo 

#Criando efeito de gravidade para os inimigos e o jogador:
g = 2

# dimensões do Ninja
Ninja_Widht = 60
Ninja_Height = 60

# dimensões do toco
toco_WIDTH = 60
toco_HEIGHT = 60

#criação do dicionário de assets:
assets = {}
# cria assets e armazena dentro do dicionário 
assets['BackgroundImage'] = pygame.image.load('ninja-village png.png').convert()
assets['BackgroundImage'] = pygame.transform.scale(assets['BackgroundImage'], (Width,Height))
assets['NinjaImage'] = pygame.image.load('ninja pixel.png').convert_alpha()
assets['NinjaImage'] = pygame.transform.scale(assets['NinjaImage'], (Ninja_Widht,Ninja_Height))
assets['Tocoimage'] = pygame.image.load('toquinho.png').convert_alpha()
assets['Tocoimage'] = pygame.transform.scale(assets['Tocoimage'], (toco_WIDTH, toco_HEIGHT))
pygame.font.init()
assets['Fonte_Placar'] = pygame.font.Font(None, 28)

# armazena todas as animações do corte dentro da lista Animacao_alimento
Animacao_alimento = []
for i in range(6):
    filename = 'Corte0{}.png'.format(i)
    img = pygame.image.load(filename).convert_alpha()
    img = pygame.transform.scale(img, (60,60))
    Animacao_alimento.append(img)
assets["Animacao_alimento"] = Animacao_alimento

# armazena todas as imagens dos inimigos dentro da lista ninjas 
Ninjas = []
for e in range(5):
    filesname = 'ninjja0{}.png'.format(e)
    img = pygame.image.load(filesname).convert_alpha()
    img = pygame.transform.scale(img, (60,60))
    Ninjas.append(img)
assets["Ninjas"] = Ninjas

#Definição do nome e símbolo do jogo:                       
pygame.display.set_caption('Ninja v Ninja')
icone = pygame.image.load('ninja pixel.png')
pygame.display.set_icon(icone)

#Carrega os sons do jogo:
pygame.mixer.music.load('DojoMusic.mp3')
pygame.mixer.music.set_volume(0.2)
assets['cut_sound'] = pygame.mixer.Sound('cutsound.mp3')

#Criando o boneco:
class Ninja(pygame.sprite.Sprite):
    def __init__(self,groups,assets):
        pygame.sprite.Sprite.__init__(self)
        self.image = assets['NinjaImage'] #imagem referente ao jogador
        self.rect = self.image.get_rect()
        self.rect.centerx = Width / 2 # faz o jogador aparecer no centro da tela no começo do jogo
        self.rect.bottom = Height -10
        self.speedx = 0 #velocidade inicial no eixo x
        self.speedy = 0 #velocidade inicial no eixo y
        self.groups = groups
        self.assets = assets

    def update(self): 
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.right > Width:
            self.rect.right = Width
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.top > Height:
            self.rect.top = Height
        if self.rect.bottom < 0:
            self.rect.bottom = 0
        


#Criando classe para os inimigos:          
class Inimigos(pygame.sprite.Sprite):
    def __init__(self,assets):
        pygame.sprite.Sprite.__init__(self)
        self.image = random.choice(assets['Ninjas'])
        self.image = pygame.transform.scale(self.image, (Ninja_Widht, Ninja_Height))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, Width)
        self.rect.y = 681
        self.speedx = random.randint(-3, 3)
        self.speedy = random.randint(-50, -42)

    def update(self):
        self.rect.x += self.speedx
        self.speedy += g
        self.rect.y += self.speedy
        if self.rect.top > Height or self.rect.right < 0 or self.rect.left > Width:
            self.rect.x = random.randint(0, Width)
            self.rect.y = 681
            self.speedx = random.randint(-3, 3)
            self.speedy = random.randint(-50, -42)


# criando classe do toco
class toco_de_madeira(pygame.sprite.Sprite):
    def __init__(self,assets):
        pygame.sprite.Sprite.__init__(self)
        self.image = assets['Tocoimage']
        self.image = pygame.transform.scale(self.image, (toco_WIDTH, toco_HEIGHT))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, Width)
        self.rect.y = 681
        self.speedx = random.randint(-3, 3)
        self.speedy = random.randint(-50, -42)

    def update(self):
        self.rect.x += self.speedx
        self.speedy += g
        self.rect.y += self.speedy
        if self.rect.top > Height or self.rect.right < 0 or self.rect.left > Width:
            self.rect.x = random.randint(0, Width)
            self.rect.y = 681
            self.speedx = random.randint(-3, 3)
            self.speedy = random.randint(-50, -42)


# Animacao do corte:
Animacao_Width = 60
Animacao_Height = 60
class alimento_cortado(pygame.sprite.Sprite):
    def __init__(self,center,assets):
        pygame.sprite.Sprite.__init__(self)
        self.Animacao_alimento = assets['Animacao_alimento']
        self.frame = 0
        self.image = self.Animacao_alimento[self.frame]
        self.rect = self.image.get_rect() 
        self.rect.center = center 
        self.last_update = pygame.time.get_ticks()
        self.frame_ticks = 50

    def update(self):
        now = pygame.time.get_ticks()
        elapsed_ticks = now = self.last_update
        if elapsed_ticks > self.frame_ticks:
            self.last_update = now
            self.frame += 1
            if self.frame == len(self.Animacao_alimento):
                self.kill()
            else: 
                center = self.rect.center
                self.image = self.Animacao_alimento[self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center
        



#Ajuste de velocidade do jogo:
FPS  = 30
clock = pygame.time.Clock()

#Criação dos Grupos:
all_sprites = pygame.sprite.Group()
all_inimigos = pygame.sprite.Group()
all_tocos = pygame.sprite.Group()

groups = {}
groups['all_sprites'] = all_sprites
groups['all_inimigos'] = all_inimigos
groups['all_tocos'] = all_tocos

#Criando o jogador:
all_sprites = pygame.sprite.Group()
Jogador = Ninja(groups,assets)
all_sprites.add(Jogador)

#Criando Inimigos:
for i in range(2):
    ninjas = Inimigos(assets)
    all_sprites.add(ninjas)
    all_inimigos.add(ninjas)
#Criando os Troncos:
for i in range(1):
    troncos = toco_de_madeira(assets)
    all_sprites.add(troncos)
    all_tocos.add(troncos)

#Loop Principal:
game = True
pygame.mixer.music.play(loops=-1)
while game:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                Jogador.speedx -= 23 # faz o boneco se mover para esquerda
            if event.key == pygame.K_d:
                Jogador.speedx += 23 # faz o boneco se mover para direita
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                Jogador.speedy += 23 # faz o boneco se mover para baixo 
            if event.key == pygame.K_w:
                Jogador.speedy -= 23 # faz o boneco se mover para cima 
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                Jogador.speedx += 23
            if event.key == pygame.K_d:
                Jogador.speedx -= 23
            if event.key == pygame.K_s:
                Jogador.speedy -= 23
            if event.key == pygame.K_w:
                Jogador.speedy += 23
                
                
    all_sprites.update()
    colisao = pygame.sprite.spritecollide(Jogador, all_inimigos,True) # cria a função de colisão entre jogador e inimigos
    for Ninjas in colisao:
        assets['cut_sound'].play()
        n = Inimigos(assets)
        all_sprites.add(n)
        all_inimigos.add(n) 
        animacao_corte = alimento_cortado(Ninjas.rect.center, assets)
        all_sprites.add(animacao_corte)
        streak += 1 # para cada inimigo morto, streak += 1
        # define combos com base no numero do contador streak
        if streak > 5 and streak <= 10:
            pontuacao += 150 # se o streak chegar a 5, ao matar um inimigo o jogador recebe 150 ao inves de 100
        if streak > 10 and streak <= 15:
            pontuacao += 200 # se streak for entre 10 e 15, pontuação do inimigo = 200
        if streak > 15 and streak <= 20:
            pontuacao += 250 # se streak for maior que 15 ou <= 20, pontuação do inimigo = 250
        if streak > 20:
            pontuacao += 300 #se streak > 20, pontuação do inimigo = 300
        else: 
            pontuacao += 100 #se streak não cumprir nenhum desses requisitos, o inimigo vai ter a puntuação normal = 100

    # define colisão entre jogador e tronco
    colisao_com_tronco = pygame.sprite.spritecollide(Jogador, all_tocos,True)
    for Toco_De_Madeira in colisao_com_tronco:
        assets['cut_sound'].play()
        u = toco_de_madeira(assets)
        all_sprites.add(u)
        all_tocos.add(u)
        animacao_corte = alimento_cortado(Ninjas.rect.center, assets)
        all_sprites.add(animacao_corte)
    if len(colisao_com_tronco) > 0:
        vidas -= 1 # se o jogador colidir com o tronco, contador vidas -= 1
        if vidas == 0:
            Jogador.kill() # se vidas chegar a 0 jogador morre
            game = False # se o jogador morrer, o jogo fecha 
            
    janela.fill((0,0,0))
    janela.blit(assets['BackgroundImage'] ,(0,0)) # adciona a imagem de fundo ao jogo
    all_sprites.draw(janela) # desenha todos os sprites na tela do jogo
    

    #Desenha o placar:
    text_surface = assets['Fonte_Placar'].render("{:08d}".format(pontuacao), True, (255,255,0))
    text_rect = text_surface.get_rect()
    text_rect.midtop = (Width / 2, 10)
    janela.blit(text_surface,text_rect)

    #Desenha as vidas:
    text_surface = assets['Fonte_Placar'].render(chr(9829) * vidas, True, (255, 0, 0))
    text_rect = text_surface.get_rect()
    text_rect.bottomleft = (10, Height - 10)
    janela.blit(text_surface, text_rect)
    pygame.display.update()

    #Desenha os Streaks:
    text_surface = assets['Fonte_Placar'].render("{:03d}".format(streak), True, (102,0,102))
    text_rect = text_surface.get_rect()
    text_rect.topright = (840, 10)
    janela.blit(text_surface,text_rect)


#Função que termina o pygame:    
pygame.quit()
