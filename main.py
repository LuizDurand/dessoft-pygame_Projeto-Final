#importa bibliotecas 
import pygame
import random
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
pygame.mixer.music.load('DojoMusic.mp3') # carrega a musica que vai ficar tocando durante a gameplay
pygame.mixer.music.set_volume(0.2) # define o volume da musica do jogo
assets['cut_sound'] = pygame.mixer.Sound('cutsound.mp3') # adciona os efeitos sonoros do corte 

#Criando o boneco:
class Ninja(pygame.sprite.Sprite):
    def __init__(self,groups,assets):
        pygame.sprite.Sprite.__init__(self)
        self.image = assets['NinjaImage'] #imagem referente ao jogador
        self.rect = self.image.get_rect() #?
        self.rect.centerx = Width / 2 # faz o jogador aparecer no centro da tela no começo do jogo
        self.rect.bottom = Height -10 #define onde o ninja vai nascer no começo do jogo no eixo y
        self.speedx = 0 #velocidade inicial no eixo x
        self.speedy = 0 #velocidade inicial no eixo y
        self.groups = groups
        self.assets = assets

    def update(self): 
        self.rect.x += self.speedx # a posição em x vai ser += a speedX
        self.rect.y += self.speedy # a posição em y vai ser += a speedY
        if self.rect.right > Width:
            self.rect.right = Width # define um limite para quanto personagem consegue se mexer no eixo x para a direita
        if self.rect.left < 0:
            self.rect.left = 0 # define um limite de quanto o personagem consegue se mexer no eixo x para a esquerda
        if self.rect.top > Height:
            self.rect.top = Height #d efine limite de altura no topo da tela 
        if self.rect.bottom < 0:
            self.rect.bottom = 0 # define limite de altura na parte inferior da tela 
        


#Criando classe para os inimigos:          
class Inimigos(pygame.sprite.Sprite):
    def __init__(self,assets):
        pygame.sprite.Sprite.__init__(self)
        self.image = random.choice(assets['Ninjas']) # define o self.image sendo a lista de imagens ninjas 
        self.image = pygame.transform.scale(self.image, (Ninja_Widht, Ninja_Height)) # define as dimenções dos inimigos
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, Width) # sorteia onde os inimigos vão nascer no eixo x
        self.rect.y = 681 # define que os inimigos vão sempre nascer nessa posição no eixo y
        self.speedx = random.randint(-3, 3) # sorteia a velocidade dos inimigos no eixo x
        self.speedy = random.randint(-50, -42) # sorteia a velocidade dos inimigos no eixo y

    def update(self):
        self.rect.x += self.speedx # posição em x += a velocidade em x
        self.speedy += g # gravidade dos inimigos 
        self.rect.y += self.speedy # posição em y += a velocidade em y
        if self.rect.top > Height or self.rect.right < 0 or self.rect.left > Width:
            # define os limites na tela 
            self.rect.x = random.randint(0, Width) 
            self.rect.y = 681
            # define velocidade em x e y
            self.speedx = random.randint(-3, 3)
            self.speedy = random.randint(-50, -42)


# criando classe do toco
class toco_de_madeira(pygame.sprite.Sprite):
    def __init__(self,assets):
        pygame.sprite.Sprite.__init__(self)
        self.image = assets['Tocoimage'] # define a imagem do toco
        self.image = pygame.transform.scale(self.image, (toco_WIDTH, toco_HEIGHT)) # define as dimenções do toco 
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, Width) # define em que parte do eixo x os tocos vão aparecerds
        self.rect.y = 681 # define a altura no eixo y em que os tocos vão aparecer 
        self.speedx = random.randint(-3, 3) # define os possiveis valores do self.speedx
        self.speedy = random.randint(-50, -42) # define os possiveis valores do self.speedy

    def update(self):
        self.rect.x += self.speedx # atualiza a posição no eixo x de acordo com o valor do self.speedx 
        self.speedy += g #adciona gravidade ao objeto toco
        self.rect.y += self.speedy # atualiza a posição no eixo y a partir do valor atribuido ao self.speedy
        if self.rect.top > Height or self.rect.right < 0 or self.rect.left > Width:
            self.rect.x = random.randint(0, Width) # define em que parte do eixo x os tocos vão aparecer
            self.rect.y = 681 # define onde os tocos vão aparecer na tela 
            self.speedx = random.randint(-3, 3) # define a velocidade no eixo x
            self.speedy = random.randint(-50, -42) # define a velocidade no eixo y


# Animacao do corte:
Animacao_Width = 60
Animacao_Height = 60
class alimento_cortado(pygame.sprite.Sprite):
    def __init__(self,center,assets):
        pygame.sprite.Sprite.__init__(self)
        self.Animacao_alimento = assets['Animacao_alimento'] # puxa a lista com as imagens do corte 
        self.frame = 0 #armazena o indice inicial da animacao
        self.image = self.Animacao_alimento[self.frame] #pega a imagem 
        self.rect = self.image.get_rect() 
        self.rect.center = center #Posiciona o centro da imagem
        self.last_update = pygame.time.get_ticks() # Guarda o tick da primeira imagem, ou seja, o momento em que a imagem foi mostrada
        self.frame_ticks = 50 #troca de image a cada 50 self.frame_ticks

    def update(self):
        now = pygame.time.get_ticks() #verifica o tick atual
        elapsed_ticks = now = self.last_update #verifica quantos ticks se passaram desde a ultima mudança de frame.
        if elapsed_ticks > self.frame_ticks:
            self.last_update = now #marca o tick da nova imagem 
            self.frame += 1 # avanca um quadro 
            if self.frame == len(self.Animacao_alimento): # verifica se já chegou no final da animação
                self.kill() #animação acaba
            else: # Se ainda não chegou ao final da animação, troca de imagem
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
pygame.mixer.music.play(loops=-1) #música toca em loop durante o jogo
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
                Jogador.speedx += 23 # quando a tecla para de ser precionada, o boneco para de se mexer para a esquerda
            if event.key == pygame.K_d:
                Jogador.speedx -= 23 # quando a tecla para de ser precionada, o boneco para de se mexer para a direita
            if event.key == pygame.K_s:
                Jogador.speedy -= 23 # quando a tecla para de ser precionada, o boneco para de se mexer para a baixo
            if event.key == pygame.K_w:
                Jogador.speedy += 23 # quando a tecla para de ser precionada, o boneco para de se mexer para a cima
                
                
    all_sprites.update()
    colisao = pygame.sprite.spritecollide(Jogador, all_inimigos,True) # cria a função de colisão entre jogador e inimigos
    for Ninjas in colisao:
        assets['cut_sound'].play() # toca o efeito do cortea
        n = Inimigos(assets)
        all_sprites.add(n) #adiciona os inimigos no grupo all_sprites quando há colisão
        all_inimigos.add(n) #adiciona os inimigos no grupo all_inimigos quando há colisão
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
        assets['cut_sound'].play() #define o som do corte
        u = toco_de_madeira(assets)
        all_sprites.add(u) #adiciona os tocos no grupo all_sprites quando há colisão
        all_tocos.add(u) #adiciona os tocos no grupo all_tocos quando há colisão
        animacao_corte = alimento_cortado(Ninjas.rect.center, assets) # parametro para a ativação do efeito do corte 
        all_sprites.add(animacao_corte) # quando ocorrer uma colisão a animação do corte é ativada 
    if len(colisao_com_tronco) > 0:
        vidas -= 1 # se o jogador colidir com o tronco, contador vidas -= 1
        streak = 0 # se o jogador colidir com o tronco, o streak é zerado
        if vidas == 0:
            Jogador.kill() # se vidas chegar a 0 jogador morre
            game = False # se o jogador morrer, o jogo fecha 
            
    janela.fill((0,0,0))
    janela.blit(assets['BackgroundImage'] ,(0,0)) # adciona a imagem de fundo ao jogo
    all_sprites.draw(janela) # desenha todos os sprites na tela do jogo
    

    #Desenha o placar:
    text_surface = assets['Fonte_Placar'].render("{:08d}".format(pontuacao), True, (255,255,0)) # escreve o placar na tela do jogo
    text_rect = text_surface.get_rect()
    text_rect.midtop = (Width / 2, 10) # define onde o placar vai ser desenhado
    janela.blit(text_surface,text_rect) #preenche, na localização definada, com a contagem dos pontos

    #Desenha as vidas:
    text_surface = assets['Fonte_Placar'].render(chr(9829) * vidas, True, (255, 0, 0)) # escreve as vidas na tela do jogo
    text_rect = text_surface.get_rect()
    text_rect.bottomleft = (10, Height - 10) # define onde o placar das vidas vai aparecer na tela 
    janela.blit(text_surface, text_rect) #preenche, na localização definada, com a contagem das vidas
    
    #Desenha os Streaks:
    text_surface = assets['Fonte_Placar'].render("{:03d}".format(streak), True, (102,0,102)) # escreve o streak na tela do jogo
    text_rect = text_surface.get_rect()
    text_rect.topright = (840, 10) # define onde o placar das streaks vai aparecer na tela
    janela.blit(text_surface,text_rect) #preenche, na localização definada, com a contagem dos streaks
    pygame.display.update() # atualiza as informações escritas na tela 


#Função que termina o pygame:    
pygame.quit()
