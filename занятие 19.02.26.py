"""
import pygame as pg
import random

GRAY = [70] * 3
BLACK = [0] * 3
WHITE = [255] * 3
W, H = 500, 500

pg.init()
win = pg.display.set_mode((W, H))

while 1:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()

    for i in range(10):
        pg.draw.circle(win, GRAY,
        (random.randint(0, W), random.randint(0, H)), 1)

    pressed = pg.mouse.get_pressed()
    if pressed[0]:
        pos = pg.mouse.get_pos()
        pg.draw.circle(win, WHITE, pos, 5)
    pg.display.update()

    pg.time.delay(20)
"""
import random

import pygame as pg
drawing = False
GRAY = [70] * 3
BLACK = [0] * 3
WHITE = [255] * 3
W, H = 500, 500
share = "kvadrat"
size = 3
pg.init()
win = pg.display.set_mode((W, H))
flag = 1
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()
    keys = pg.key.get_pressed()
    pos = pg.mouse.get_pos()

    if keys[pg.K_SPACE]:
        win.fill((255, 255, 255))
    elif keys[pg.K_w]:
        share = "krug"
    elif keys[pg.K_q]:
        share = "kvadrat"
    if share == "krug":
        pg.draw.circle(win, random.choices(range(256), k=3), pos, size)
    if share == "kvadrat":
        pg.draw.rect(win, random.choices(range(256), k=3), (pos[0], pos[1], size, size))
    size += flag
    if size >= 100:
        flag = -1
    if size <= 15:
        flag = 1
    pg.display.update()
    pg.time.delay(10)
