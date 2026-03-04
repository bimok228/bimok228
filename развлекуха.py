import pygame
import sys

# Инициализация Pygame
pygame.init()

# Константы
WIDTH, HEIGHT = 600, 600
FPS = 60
WHITE = (255, 255, 255)
GREEN = (0, 128, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Создание окна
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Роналду бьёт по воротам!")
clock = pygame.time.Clock()

# Загрузка изображений
try:
    # Фон футбольного поля
    background = pygame.image.load("pngtree-green-football-stadium-field-png-image_6134302 (1).png").convert()
    background = pygame.transform.scale(background, (WIDTH, HEIGHT))

    # Спрайт Роналду
    ronaldo_img = pygame.image.load("555e71fc3786f4d133fc2d77a1c81d1d (1).jpg").convert_alpha()
    ronaldo_img = pygame.transform.scale(ronaldo_img, (80, 120))

    # Мяч
    ball_img = pygame.image.load("312-3121468_soccer-ball-svg-png-icon-free-download-soccer-ball-vector-png (1).png").convert_alpha()
    ball_img = pygame.transform.scale(ball_img, (30, 30))
except:
    # Резервные изображения, если файлы не найдены
    print("Изображения не найдены. Используются стандартные фигуры.")
    background = pygame.Surface((WIDTH, HEIGHT))
    background.fill(GREEN)
    pygame.draw.rect(background, WHITE, (50, 50, WIDTH - 100, HEIGHT - 100), 5)  # Разметка поля

    ronaldo_img = pygame.Surface((80, 120))
    ronaldo_img.fill(RED)

    ball_img = pygame.Surface((30, 30), pygame.SRCALPHA)
    pygame.draw.circle(ball_img, BLACK, (15, 15), 15)

# Позиции и скорости
ronaldo_x, ronaldo_y = 100, HEIGHT // 2 - 60
ball_x, ball_y = ronaldo_x + 80, ronaldo_y + 60
ball_speed_x = 0
ball_speed_y = 0
goal_x, goal_y = WIDTH - 200, HEIGHT // 2 - 75
goal_width, goal_height = 150, 150

# Флаг для отслеживания удара
ball_kicked = False
game_won = False
kick_cooldown = 0  # Задержка между ударами

# Шрифт для текста
font = pygame.font.Font(None, 74)
win_text = font.render("Вы победили!", True, WHITE)
win_rect = win_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))

# Главный игровой цикл
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not ball_kicked and kick_cooldown == 0:
                # Удар по мячу
                ball_speed_x = 12
                ball_speed_y = -2  # Лёгкий подъём мяча
                ball_kicked = True
                kick_cooldown = 30  # 0.5 секунды задержки (при 60 FPS)

    # Обновление задержки между ударами
    if kick_cooldown > 0:
        kick_cooldown -= 1

    # Обновление позиции мяча
    if ball_kicked:
        ball_x += ball_speed_x
        ball_y += ball_speed_y

        # Гравитация для реалистичности
        ball_speed_y += 0.2

        # Проверка попадания в ворота
        if (goal_x <= ball_x <= goal_x + goal_width and
                goal_y <= ball_y <= goal_y + goal_height):
            game_won = True

        # Остановка мяча за пределами экрана
        if ball_x > WIDTH or ball_y > HEIGHT:
            ball_kicked = False
            ball_x, ball_y = ronaldo_x + 80, ronaldo_y + 60
            ball_speed_x = 0
            ball_speed_y = 0

    # Отрисовка
    screen.blit(background, (0, 0))  # Фон

    # Ворота
    pygame.draw.rect(screen, BLACK, (goal_x, goal_y, goal_width, goal_height), 5)
    pygame.draw.line(screen, BLACK, (goal_x + goal_width // 2, goal_y),
                     (goal_x + goal_width // 2, goal_y + goal_height), 3)  # Сетка

    # Роналду
    screen.blit(ronaldo_img, (ronaldo_x, ronaldo_y))

    # Мяч
    screen.blit(ball_img, (ball_x, ball_y))

    # Текст победы
    if game_won:
        screen.blit(win_text, win_rect)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()
