import pygame
import sys

pygame.init()
font = pygame.font.SysFont('Arial', 36)
width = 1200
height = 800
score_x = 10
score_y = 10
win = pygame.display.set_mode((width, height))
background_image = pygame.image.load("desert.jpg").convert()
background_scaled = pygame.transform.scale(background_image, (width, height))

# Инициализируем счёт здесь
score = 0
start_time = pygame.time.get_ticks()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('dinozavr.png')
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()
        self.rect.center = (200, 530)
        # Убираем лишнюю инициализацию self.score и self.rect
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
            self.jump_count = 17

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

    def die(self):
        self.alive = False
        self.kill()

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('kactus.png')
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()
        # Исправляем некорректную инициализацию rect
        self.rect.right = width + 100
        self.rect.centery = 500
        self.speed = 13
        self.passed = False  # Флаг для отслеживания прохождения динозавра

    def update(self, player):
        self.rect.x -= self.speed

        # Проверяем, прошёл ли кактус динозавра
        if self.rect.right < player.rect.left and not self.passed:
            self.passed = True
            global score
            score += 10  # Добавляем 10 очков за каждый успешно пройденный кактус

        if self.rect.right < 0:
            self.rect.right = width + 100
            self.speed += 0.2
            self.passed = False  # Сбрасываем флаг для следующего прохода


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
            pygame.quit()
            sys.exit()

    hits = pygame.sprite.spritecollide(player, enemy_sprites, False)
    if hits:
        print("Игра окончена! Столкновение с кактусом.")
        pygame.quit()
        sys.exit()

    win.blit(background_scaled, (0, 0))
    player.move_by_keys()
    enemy_sprites.update(player)

    # Отрисовка счёта — сначала обновляем счёт, потом рисуем
    current_time = pygame.time.get_ticks()
    score = (current_time - start_time) // 1000  # Обновляем счёт (по времени)
    score_text = font.render(f'Очки: {score}', True, (255, 255, 255))  # белый цвет
    win.blit(score_text, (score_x, score_y))

    all_sprites.draw(win)
    enemy_sprites.draw(win)

    pygame.display.update()
    clock.tick(FPS)
