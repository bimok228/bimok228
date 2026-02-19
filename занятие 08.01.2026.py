"""
import pygame
pygame.init()

win = pygame.display.set_mode((500, 500))
x = 0
y = 70
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    color = (255, 255, 255)
    win.fill(color)
    x = x + 10 + 10 + 10 + 10
    if x > 430:
        x = 0
    pygame.draw.rect(win, (255, 255, 0), (x, y, 150, 100))

    pygame.draw.circle(win, (0, 0, 0), (30, 20), 1 + 1)

    pygame.display.update()
    pygame.time.delay(10)
"""
import pygame
pygame.init()
win = pygame.display.set_mode((500, 500))
b = 1
n = 1
v = 3
x = 1
y = 250
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    color = (255, 255, 255)
    win.fill(color)
    x = x + v
    if x > 500:
        v = -3
    if x < 0:
        v = +3
    if n < 500:
        n = + 1

    pygame.draw.rect(win, (255, 255, 0), (x, y, 60, 60))
    pygame.display.update()
    pygame.time.delay(10)