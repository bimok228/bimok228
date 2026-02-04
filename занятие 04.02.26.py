import random

import pygame
pygame.init()
width = 500
height = 500
win = pygame.display.set_mode((width, height))
x = 490
y = 250
rad = 35
class Circle:
    def __init__(self, color, x, y, rad,):
        self.color = color
        self.x = x
        self.y = y
        self.rad = rad
        self.dir = 1
    def draw(self):
        pygame.draw.circle(win, self.color, (self.x, self.y,), self.rad)
    def move_by_keys(self):
        if self.x > width:
            self.dir = -1
        if self.x < 0:
            self.dir = 1
        self.x += self.dir

FPS = 60
clock = pygame.time.Clock()

list_circles = []
for i in range(100):
    list_circles.append(Circle(random.choices(range(256), k=3), i * 10, i * 10, 35))
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    win.fill((255, 255, 255))

    for i in range(100):
        list_circles[i].draw()
        list_circles[i].move_by_keys()
    pygame.display.update()
    clock.tick(FPS)
    print(clock.get_fps())
