import random

import pygame

pygame.init()

width = 700
height = 700

win = pygame.display.set_mode((width, height))
class inginerium(pygame.sprite.Sprite):
    def __init__(self, *group):
        super().__init__(*group)
        self.image = pygame.image.load("555e71fc3786f4d133fc2d77a1c81d1d (1).jpg")
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(width)
        self.rect.y = random.randrange(height)
    def update(self):
        self.rect = self.rect.move(random.randrange(112) - 55,
                                   random.randrange(112) - 55)
all_sprites = pygame.sprite.Group()
for i in range(500):
    inginerium(all_sprites)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    win.fill((255, 255, 255))
    all_sprites.draw(win)
    all_sprites.update()
    pygame.display.update()