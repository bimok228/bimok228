import random

import pygame

pygame.init()

width, height = 500, 500
a = 3
b = 3
c = 3
d = 3
win = pygame.display.set_mode((width, height))
class player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("стив.jpg")
        self.image = pygame.transform.scale(self.image, (100, 150))
        self.rect = self.image.get_rect()
    def update(self):
        self.move_by_keys()
    def move_by_keys(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.rect.left -= a
        if keys[pygame.K_d]:
            self.rect.left += b
        if keys[pygame.K_w]:
            self.rect.top -= c
        if keys[pygame.K_s]:
            self.rect.top += d
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("зомби.jpg")
        self.image = pygame.transform.scale(self.image, (100, 150))
        self.rect = self.image.get_rect()
        self.rect.right = width
        self.rect.top = random.randint(0, height - self.rect.height)

all_sprites = pygame.sprite.Group()
Player = player()
all_sprites.add(Player)

Enemy_sprites = pygame.sprite.Group()
enemy = Enemy()
Enemy_sprites.add(enemy)
fps = 60
clock = pygame.time.Clock()
score = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    win.fill((255, 255, 255))

    """if enemy.rect.left < Player.rect.right and \
        enemy.rect.top < Player.rect.bottom and \
        enemy.rect.bottom > Player.rect.top and \
        enemy.rect.right > Player.rect.left:
        print("Столкнулись")
        enemy.rect.left = random.randint(0, width - enemy.rect.width)
        enemy.rect.top = random.randint(0, height - enemy.rect.height)
    """
    hits = pygame.sprite.spritecollide(Player, Enemy_sprites, False)
    if len(hits) > 0:
        new_left = hits[0].rect.left = random.randint(0, width - hits[0].rect.width)
        new_top = hits[0].rect.top = random.randint(0, height - hits[0].rect.height)
        while new_left >= Player.rect.left and new_left <= Player.rect.right:
            new_left = random.randint(0, width - hits[0].rect.width)

        while new_top >= Player.rect.top and new_top <= Player.rect.bottom:
            new_top = random.randint(0, height - hits[0].rect.height)
        hits[0].rect.left = new_left
        hits[0].rect.top = new_top
        score += 1
        print("очков " + str(score))
        if score == 10:
            a, b, d, c =+ 2(int)
    all_sprites.draw(win)
    Enemy_sprites.draw(win)
    all_sprites.update()
    Enemy_sprites.update()
    pygame.display.update()
    clock.tick(fps)