import pygame
import random

# dimensões do toco
toco_WIDTH = 60
toco_HEIGHT = 60


# criando classe do toco
class toco_de_madeira(pygame.sprite.Sprite):
    def __init__(self):
        self.image = pygame.image.load('assets/img/toco.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (toco_WIDTH, toco_HEIGHT))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, WIDTH-toco_WIDTH)
        self.rect.y = random.randint(-100, -toco_HEIGHT)
        self.speedx = random.randint(-3, 3)
        self.speedy = random.randint(2, 9)

