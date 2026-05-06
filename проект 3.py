import pygame
import sys
import random
pygame.init()
font = pygame.font.SysFont('Arial', 70)
width = 1200
height = 800
score_x = 10
score_y = 10
win = pygame.display.set_mode((width, height))
background_image = pygame.image.load("desert.jpg").convert()
background_scaled = pygame.transform.scale(background_image, (width, height))
distance = 1000
score = 0
speed = 14
start_time = pygame.time.get_ticks()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('dinozavr.png')
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()
        self.rect.center = (200, 500)
        self.is_jump = False
        self.jump_count = 15
        self.vertical_velocity = 0
        self.alive = True

    def move_by_keys(self):
        if not self.alive:
            return

        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and not self.is_jump:
            self.is_jump = True
            self.vertical_velocity = -8
            self.jump_count = 172

        if self.is_jump:
            if self.jump_count >= -17:
                if self.jump_count > 0:
                    self.rect.y -= (self.jump_count ** 2) * 0.2
                else:
                    self.rect.y += (self.jump_count ** 2) * 0.2
                self.jump_count -= 1
            else:
                self.is_jump = False
                self.jump_count = 1
                if self.rect.bottom > height:
                    self.rect.bottom = height


class Cactus(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('kactus.png')
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()
        self.rect.right = width + 100
        self.rect.centery = 500
        self.speed = 13
        self.passed = False
    def update(self, player):
        self.rect.x -= self.speed
        if self.rect.right < 0:
            self.rect.right = width + 100
            self.speed += 0.2
            self.passed = False
class Sterv(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('sterv.png')
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()
        self.rect.right = width + 100
        self.rect.center = (random.randint(300, 1000), 250)
        self.speed = 13
        self.passed = False
    def update(self, player):
        self.rect.x -= self.speed
        if self.rect.right < 0:
            self.rect.right = random.randint(600, 1000) + distance
            self.speed += 0.2
            print(self.speed)
            self.passed = False



FPS = 60
clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

Cactus_sprites = pygame.sprite.Group()
cactus = Cactus()
Cactus_sprites.add(cactus)

Sterv_sprites = pygame.sprite.Group()
sterv = Sterv()
Sterv_sprites.add(sterv)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    hits = pygame.sprite.spritecollide(player, Cactus_sprites, False)
    if hits:
        print("Игра окончена! Ваши очки",score)
        pygame.quit()
        sys.exit()
    hits = pygame.sprite.spritecollide(player, Sterv_sprites, False)
    if hits:
        print("Игра окончена! Ваши очки",score)
        pygame.quit()
        sys.exit()

    win.blit(background_scaled, (0, 0))
    player.move_by_keys()
    Cactus_sprites.update(player)
    Sterv_sprites.update(player)

    current_time = pygame.time.get_ticks()
    score = (current_time - start_time) // 55


    score_text = font.render(f'Очки: {score}', True, (0, 0, 0))
    win.blit(score_text, (score_x, score_y))

    all_sprites.draw(win)
    Cactus_sprites.draw(win)
    Sterv_sprites.draw(win)
    pygame.display.update()
    clock.tick(FPS)
