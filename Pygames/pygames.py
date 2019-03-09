import pygame
import random
import os

from sprite_example import img_folder

WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
HEIGHT = 300
WIDTH = 500
FPS = 60

#initalize
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT),0,32)
pygame.display.set_caption("My game")
clock = pygame.time.Clock()
#PLAYER
class Player(pygame.sprite.Sprite):
    def __init__ (self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50,40))
        self.image.fill(BLUE)
        self.image = pygame.image.load(os.path.join(img_folder, "layer 1.png")).convert()
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 20
        self.speedx = 0

    def update(self):
        self.rect.x += self.speedx

all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)
#Game loop
running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    screen.fill(BLACK)
    pygame.display.flip()


pygame.quit()