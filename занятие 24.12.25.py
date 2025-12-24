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
    pygame.display.update()
