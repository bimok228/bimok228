import pygame
pygame.init()
width = 1200
height = 800

win = pygame.display.set_mode((width, height))
background_image = pygame.image.load("desert.jpg").convert()
background_scaled = pygame.transform.scale(background_image, (width, height))

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('dinozavr.png')
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()
        self.rect.center = (200, 470)
        self.is_jump = False
        self.jump_count = 10
        self.vertical_velocity = 0
        self.alive = True

    def move_by_keys(self):
        if not self.alive:
            return

        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and not self.is_jump: 
            self.is_jump = True
            self.vertical_velocity = -8
            self.jump_count = 15

        if self.is_jump:
            if self.jump_count >= -15:
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

    def die(self):
        self.alive = False
        self.kill()

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('kactus.png')
        self.image = pygame.transform.scale(self.image, (140, 140))
        self.rect = self.image.get_rect()
        self.rect.right = width + 100
        self.rect.centery = 470
        self.speed = 9

    def update(self, player):
        self.rect.x -= self.speed

        if self.rect.right < 0:
            self.rect.right = width + 100
            self.speed += 0.2
FPS = 60
clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

enemy_sprites = pygame.sprite.Group()
enemy = Enemy()
enemy_sprites.add(enemy)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    hits = pygame.sprite.spritecollide(player, enemy_sprites, False)  # False — не удаляем кактус

    if hits and player.alive:
        player.die()

    win.blit(background_scaled, (0, 0))

    player.move_by_keys()
    enemy_sprites.update(player)

    all_sprites.draw(win)
    enemy_sprites.draw(win)

    pygame.display.update()
    clock.tick(FPS)