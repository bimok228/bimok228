import pygame
width = 500#ширина
height = 500#высота

fps = 60
clock = pygame.time.Clock()
pygame.init()
win = pygame.display.set_mode((width, height))

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("стив.jpg")
        self.image = self.image.convert_alpha()
        colorkey = self.image.get_at((0, 0))
        self.image.set_colorkey(colorkey)
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()
    def update(self):
        self.move_by_keys()
    def move_by_keys(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.rect.top -= 3
        if keys[pygame.K_s]:
            self.rect.top += 3
        if keys[pygame.K_a]:
            self.rect.left -= 3
        if keys[pygame.K_d]:
            self.rect.left += 3



class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("зомби.jpg")
        self.image = self.image.convert_alpha()
        colorkey = self.image.get_at((0, 0))
        self.image.set_colorkey(colorkey)
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()
    def update(self):
        global player
        if self.rect.top > player.rect.top:
            self.rect.top -= 2
        if self.rect.top < player.rect.top:
            self.rect.top += 2
        if self.rect.left > player.rect.left:
            self.rect.left -= 2
        if self.rect.left < player.rect.left:
            self.rect.left += 2


player = Player()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)
enemy = Enemy()
enemy_sprites = pygame.sprite.Group()
enemy_sprites.add(enemy)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()#выход


    win.fill((255, 255, 255))#заливаем задний фон белым цветом

    all_sprites.draw(win)
    all_sprites.update()
    enemy_sprites.draw(win)
    enemy_sprites.update()

    pygame.display.update()
    clock.tick(fps)#настраиваем фпс
