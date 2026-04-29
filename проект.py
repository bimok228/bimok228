import pygame
pygame.init()
width = 1200
height = 800

win = pygame.display.set_mode((width, height))
background_image = pygame.image.load("555e71fc3786f4d133fc2d77a1c81d1d (1).jpg").convert()
background_scaled = pygame.transform.scale(background_image, (width, height))
def load_image(name):
    img = pygame.image.load("555e71fc3786f4d133fc2d77a1c81d1d (1).jpg")
    img = img.convert()  # Конвертирует в нужный формат
    colorkey = img.get_at((0, 0))
    img.set_colorkey(colorkey)
    return img
class Circle:
    def __init__(self, color, x, y, rad):
        self.color = color
        self.x = 100
        self.y = 300
        self.rad = rad
        self.isJump = False
        self.jumpCount = 10


    def draw(self):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.rad)

    def move_by_keys(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            self.isJump = True
        if self.isJump:
            if self.jumpCount >= -10:
                if self.jumpCount < 0:
                    self.y += (self.jumpCount ** 2) // 2
                else:
                    self.y -= (self.jumpCount ** 2) // 2
                self.jumpCount -= 1
            else:
                self.jumpCount = 10
                self.isJump = False

FPS = 60
clock = pygame.time.Clock()

krug = Circle((255, 0, 0), width / 2, height / 2, 30)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    krug.draw()
    krug.move_by_keys()
    pygame.display.update()
    clock.tick(FPS)
    win.blit(background_scaled, (0, 0))