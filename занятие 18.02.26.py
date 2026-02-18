import pygame as pg
BLACK = (0,) * 3
GRAY = (100,) * 3
WHITE = (255,) * 3
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
LIGHTGREEN = (0, 200, 200)

CROSS = "#046582"
CIRCLE = "#e4bad4"

pg.init()
W, H = 600, 600
screen = pg.display.set_mode((W, H))
class Board:
    def __init__(self, W, H, size):
        self.W, self.H = W, H
        self.size = size
        self.board = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
        ]
        self.move = 1

    def click(self, mouse_pos):
        x = mouse_pos[0] // self.size
        y = mouse_pos[1] // self.size
        self.board[y][x] = self.move
        self.move = -self.move
    def render(self, screen):
        pg.draw.line(screen, GRAY, (0, 200), (self.W, 200))
        pg.draw.line(screen, GRAY, (0, 400), (self.W, 400))
        pg.draw.line(screen, GRAY, (200, 0), (200, self.H))
        pg.draw.line(screen, GRAY, (400, 0), (400, self.H))
        for y in range(3):
            for x in range(3):
                if self.board[y][x] == 1:
                    draw_cross(screen, x, y, self.size)
                elif self.board[y][x] == -1:
                    draw_circle(screen, x, y, self.size)
def draw_circle(sc, x, y, size):
    x = (x + .5) * size
    y = (y + .5) * size
    pg.draw.circle(sc, CIRCLE, (x, y), (size - 3) // 2, 3)

def draw_cross(sc, x, y, size):
    x = x * size + 3
    y = y * size + 3
    pg.draw.line(sc, CROSS, (x, y), (x + size - 3, y + size - 3), 3)
    pg.draw.line(sc, CROSS, (x + size - 3, y - 3), (x, y + size - 3), 3)

board = Board(W, H, 200)
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()
        if event.type == pg.MOUSEBUTTONDOWN:
            board.click(event.pos)

    screen.fill(WHITE)
    board.render(screen)
    pg.display.update()

    keys = pg.key.get_pressed()
    if keys[pg.K_ESCAPE]:
        pg.quit()
        exit()
