import random
import pygame
import sqlite3

con = sqlite3.connect("score.sqlite")
cur = con.cursor()

def create_table():
    que_create = """
        CREATE TABLE IF NOT EXISTS score(
            id INTEGER PRIMARY KEY,
            name TEXT,
            score INTEGER
        )
    """
    cur.execute(que_create)
    con.commit()

def insert_data(name, score):
    que_insert = """
        INSERT INTO score(name, score) VALUES
        ("{}", {})
    """
    cur.execute(que_insert.format(name, score))
    con.commit()

create_table()

pygame.init()

width, height = 600, 600

win = pygame.display.set_mode((width, height))

okno = pygame.Surface((width, 200))
okno2 = pygame.Surface((width, 200))

font = pygame.font.Font(None, 10)
text = font.render("бр бр патапим", False, (0, 0, 0))
okno.fill((255, 0, 0))
okno2.fill((0, 0, 255))

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("стив.jpg")
        self.image = pygame.transform.scale(self.image, (60, 60))
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

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("зомби.jpg")
        self.image = pygame.transform.scale(self.image, (60, 60))
        self.rect = self.image.get_rect()
        self.rect.left = random.randint(0, okno2.get_rect().width)
        self.rect.top = random.randint(0, okno2.get_rect().height)

enemy = Enemy()
enemy_sprites = pygame.sprite.Group()
enemy_sprites.add(enemy)
player = Player()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)
FPS = 60
clock = pygame.time.Clock()
currentSurface = 1
score = 0

name = input("введите имя:")
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            insert_data(name, score)
            exit()
    win.fill((255, 255, 255))


    okno.fill((255, 0, 0))
    okno2.fill((255, 255, 0))

    if currentSurface == 1:
        all_sprites.draw(okno)
    elif currentSurface == 2:
        all_sprites.draw(okno2)

    if currentSurface == 1:
        if player.rect.bottom >= okno.get_rect().height:
            currentSurface = 2
            player.rect.top = 2
        if  player.rect.top <= 0:
            player.rect.top = 0
        if player.rect.left <= 0:
            player.rect.left = 0
        if player.rect.right >= okno.get_rect().width:
            player.rect.right = okno.get_rect().width
    elif currentSurface == 2:
        if player.rect.top <= 0:
            currentSurface = 1
            player.rect.top = okno.get_rect().height - player.rect.height - 2
        if player.rect.left <= 0:
            player.rect.left = 0
        if player.rect.right >= okno2.get_rect().width:
            player.rect.right = okno2.get_rect().width
        if player.rect.bottom >= okno2.get_rect().height:
            player.rect.bottom = okno2.get_rect().height

    enemy_sprites.draw(okno2)
    enemy_sprites.update()

    okno.blit(text, (100, 0))
    win.blit(okno, (0, 0))
    win.blit(okno2, (0, 200))

    hits = pygame.sprite.spritecollide(player, enemy_sprites, False)
    if len(hits) > 0:
        score += 1
        hits[0].rect.left = random.randint(0, okno2.get_rect().width)
        hits[0].rect.top = random.randint(0, okno2.get_rect().height)
    all_sprites.update()
    pygame.display.update()
    clock.tick(FPS)
    print(score)