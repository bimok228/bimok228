import pygame

pygame.init()

width, height = 500, 500
s = 1
win = pygame.display.set_mode((width, height))
class Button(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("button.webp")
        self.image = pygame.transform.scale(self.image, (150, 150))
        self.rect = self.image.get_rect()
        self.rect.centerx = width / 2
        self.rect.centery = height / 2

startButton = Button()
menu_sprites = pygame.sprite.Group()
menu_sprites.add(startButton)

FPS = 60
clock = pygame.time.Clock()
startGame = False
startSurface = pygame.Surface((width, height))
startSurface.fill((255, 255, 255))
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                mouse_pos = pygame.mouse.get_pos()
                x = mouse_pos[0]
                y = mouse_pos[1]
                if x >= startButton.rect.left and \
                        x <= startButton.rect.right and \
                        y >= startButton.rect.top and \
                        y <= startButton.rect.bottom and \
                    startGame == False:
                    s += 1
                    print(s)
                    startGame = True
    win.fill((255, 255, 255))
    if startGame == False:
        win.blit(startSurface, (0, 0))
    menu_sprites.draw(startSurface)
    menu_sprites.update()
    pygame.display.update()
    clock.tick(FPS)