"""
import pygame
pygame.init()
win = pygame.display.set_mode((600, 400))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    color = (255, 0, 0)
    win.fill((255, 255, 255))
    pygame.draw.rect(win, (255, 255, 0), (100, 150, 60, 80))
    pygame.draw.circle(win, (0, 255, 255), (50, 40,), 10)
    pygame.draw.polygon(win, (0, 0, 0), [(0, 100), (100, 50), (100, 150),])
    pygame.draw.line(win, (0, 255, 255), (0, 0), (100, 100), 5)
    pygame.draw.lines(win, (0, 0, 0), True, ((200, 200), (300, 150), (300, 250)), 10)
    pygame.display.update()


import pygame
x = int(input("введите ширину окна: "))
t = int(input("введите высоту окна: "))
pygame.init()
win = pygame.display.set_mode((x, t))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    color = (255, 0, 0)
    win.fill((0, 0, 0))
    pygame.draw.line(win, (255, 255, 255), (0, 0), (x, t), 5)
    pygame.draw.line(win, (255, 255, 255), (0, t), (x, 0), 5)
    pygame.display.update()
"""
import pygame
pygame.init()
win = pygame.display.set_mode((500, 500))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    color = (255, 0, 0)
    win.fill((255, 255, 255))
    pygame.draw.rect(win, (0, 0, 0), (0, 0, 100, 100))
    pygame.draw.rect(win, (0, 0, 0), (200, 0, 100, 100))
    pygame.draw.rect(win, (0, 0, 0), (400, 0, 100, 100))
    pygame.draw.rect(win, (0, 0, 0), (100, 100, 100, 100))
    pygame.draw.rect(win, (0, 0, 0), (200, 200, 100, 100))
    pygame.draw.rect(win, (0, 0, 0), (300, 100, 100, 100))
    pygame.draw.rect(win, (0, 0, 0), (400, 400, 100, 100))
    pygame.draw.rect(win, (0, 0, 0), (300, 300, 100, 100))
    pygame.draw.rect(win, (0, 0, 0), (400, 200, 100, 100))
    pygame.draw.rect(win, (0, 0, 0), (0, 0, 100, 100))
    pygame.draw.rect(win, (0, 0, 0), (0, 200, 100, 100))
    pygame.draw.rect(win, (0, 0, 0), (0, 400, 100, 100))
    pygame.draw.rect(win, (0, 0, 0), (100, 300, 100, 100))
    pygame.draw.rect(win, (0, 0, 0), (200, 400, 100, 100))
    pygame.display.update()