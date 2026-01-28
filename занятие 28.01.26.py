import pygame

pygame.init()
width = 500
height = 500
win = pygame.display.set_mode((width, height))
x = 250
y = 250
rad = 35
jump = x

class Circle:
    def __init__(self, color, x, y, rad, jump):
        self.color = color
        self.x = x
        self.y = y
        self.rad = rad
        self.jump = jump
        self.isjump = False
    def draw(self):
        pygame.draw.circle(win, self.color, (self.x, self.y,), self.rad)

    def move_by_keys(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.x -= 3
        elif keys[pygame.K_d]:
            self.x += 3
        elif keys[pygame.K_w]:
            self.y -= 3
        elif keys[pygame.K_s]:
            self.y += 3
        elif keys[pygame.K_SPACE]:
            self.isjump = True
            self.Sta
        if self.isjump

krug = Circle((255, 255, 0), 250, 250, 35)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    win.fill((255, 255, 255))
    krug.jump()
    krug.draw()
    krug.move_by_keys()
    pygame.display.update()
    pygame.display.update()
    pygame.time.delay(6)
