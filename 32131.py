import random
import pygame

pygame.init()

size = width, height = 700, 700
FPS = 60

win = pygame.display.set_mode(size)

def load_image(name):
    img = pygame.image.load("555e71fc3786f4d133fc2d77a1c81d1d (1).jpg")
    img = img.convert()  # Конвертирует в нужный формат
    colorkey = img.get_at((0, 0))
    img.set_colorkey(colorkey)
    return img

class Inginirium(pygame.sprite.Sprite):
    def __init__(self, *group):
        super().__init__(*group)
        self.image = load_image('Coba.png')
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(width)
        self.rect.y = random.randrange(height)

    def update(self):
        self.rect = self.rect.move(random.randrange(3) - 1, random.randrange(3) - 1)

all_sprites = pygame.sprite.Group()
for i in range(10):
    Inginirium(all_sprites)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    win.fill((255, 255, 255))
    all_sprites.draw(win)
    all_sprites.update()
    pygame.display.update()