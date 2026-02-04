import pygame

pygame.init()

win = pygame.display.set_mode((500, 500))
x = 250
y = 250
j = 1
s = 1
f = 1
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    win.fill((255, 255, 255))
    keys = pygame.key.get_pressed()
    if keys[pygame.k_]:
        y -= 1
    elif keys[pygame.K_s]:
        y += 1
    if keys[pygame.K_a]:
        x -= 1
    if keys[pygame.K_d]:
        x += 1
    if x >= 251:
        x -= 0.5
    if y >= 251:
        y -= 0.5
    if x <= 251:
        x += 0.5
    if y <= 251:
        y += 0.5


    pygame.draw.circle(win, (j, s, f), (x, y), 25)
    pygame.display.update()
    pygame.time.delay(2)
