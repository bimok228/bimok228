import pygame
import sys


class DinosaurGame:
    def __init__(self):
        pygame.init()

        self.WIDTH, self.HEIGHT = 1280, 720
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption('Dinosaur Game')

        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)

        self.load_assets()

        self.reset_game()

        self.clock = pygame.time.Clock()

    def load_assets(self):
        self.background = pygame.image.load('desert.jpg')
        self.background = pygame.transform.scale(self.background, (self.WIDTH, self.HEIGHT))

        self.dinosaur = pygame.image.load('dino.png')
        self.dinosaur = pygame.transform.scale(self.dinosaur, (75, 100))
        self.dinosaur_rect = self.dinosaur.get_rect()
        self.dinosaur_rect.x = 50
        self.dinosaur_rect.y = 355

        self.cactus = pygame.image.load('kactus.jpg')
        self.cactus = pygame.transform.scale(self.cactus, (50, 75))
        self.cactus_rect = self.cactus.get_rect()
        self.cactus_rect.x = self.WIDTH
        self.cactus_rect.y = 389

        self.font = pygame.font.Font(None, 64)

    def reset_game(self):
        self.speed = 6.0
        self.y_speed = 0
        self.is_jumping = False
        self.game_over = False
        self.score = 0

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and not self.is_jumping and not self.game_over:
                    self.is_jumping = True
                    self.y_speed = -25

    def update_game(self):
        if not self.game_over:
            self.cactus_rect.x -= self.speed

            if self.cactus_rect.right < 0:
                self.cactus_rect.x = self.WIDTH
                self.speed += 0.3
                self.score += 10

            if self.is_jumping:
                self.dinosaur_rect.y += self.y_speed
                self.y_speed += 1

                if self.dinosaur_rect.y >= 355:
                    self.dinosaur_rect.y = 355
                    self.is_jumping = False
                    self.y_speed = 0

            if self.dinosaur_rect.colliderect(self.cactus_rect):
                self.game_over = True

    def draw(self):
        self.screen.blit(self.background, (0, 0))

        if not self.game_over:
            self.screen.blit(self.dinosaur, self.dinosaur_rect)
            self.screen.blit(self.cactus, self.cactus_rect)

            score_text = self.font.render(f'Score: {int(self.score)}', True, self.BLACK)
            self.screen.blit(score_text, (10, 10))
        else:
            game_over_text = self.font.render('GAME OVER', True, self.BLACK)
            restart_text = self.font.render('Press R to restart', True, self.BLACK)
            self.screen.blit(game_over_text, (self.WIDTH // 2 - 150, self.HEIGHT // 2 - 50))
            self.screen.blit(restart_text, (self.WIDTH // 2 - 120, self.HEIGHT // 2 + 20))

    def check_restart(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_r] and self.game_over:
            self.reset_game()
            self.cactus_rect.x = self.WIDTH

    def run(self):
        while True:
            self.handle_events()
            self.update_game()
            self.draw()
            self.check_restart()
            pygame.display.update()
            self.clock.tick(60)  # 60 FPS


if __name__ == '__main__':
    game = DinosaurGame()
    game.run()