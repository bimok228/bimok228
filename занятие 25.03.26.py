import pygame
pygame.init()

width, height = 600, 600

win = pygame.display.set_mode((width, height))

okno = pygame.Surface((width, 200))
okno2 = pygame.Surface((width, 200))

font = pygame.font.Font(None, 100)
text = font.render("бр бр патапим", False, (0, 0, 0))
okno.fill((255, 0, 0))
okno2.fill((0, 0, 255))

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("555e71fc3786f4d133fc2d77a1c81d1d (1).jpg")
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.rect.top -= 3
        if keys[pygame.K_s]:
            self.rect.top += 3
        if keys[pygame.K_a]:
            self.rect.left -= 3
        if keys[pygame.K_d]:
            self.rect.left += 3
player = Player()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)
FPS = 60
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    win.fill((255, 255, 255))


    okno.fill((255, 0, 0))
    okno2.fill((255, 255, 0))
    if player.rect.bottom >= okno.get_rect().height:
        all_sprites.draw((okno2))
    else:
        all_sprites.draw((okno))
    okno.blit(text, (100, 0))
    win.blit(okno, (0, 0))
    win.blit(okno2, (0, 100))


    all_sprites.update()
    pygame.display.update()
    clock.tick(FPS)