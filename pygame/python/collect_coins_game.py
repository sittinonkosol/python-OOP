import pygame
import random
import sys

# -----------------------------
# ตั้งค่าพื้นฐาน
# -----------------------------
WIDTH, HEIGHT = 800, 600
BG_COLOR = (20, 20, 20)
PLAYER_COLOR = (0, 255, 0)
COIN_COLOR = (255, 255, 0)


class Player:
    def __init__(self, x, y, size, speed):
        self.size = size
        self.speed = speed
        self.rect = pygame.Rect(x, y, size, size)

    def handle_input(self):
        keys = pygame.key.get_pressed()
        dx, dy = 0, 0
        if keys[pygame.K_LEFT]:
            dx -= self.speed
        if keys[pygame.K_RIGHT]:
            dx += self.speed
        if keys[pygame.K_UP]:
            dy -= self.speed
        if keys[pygame.K_DOWN]:
            dy += self.speed
        self.rect.x += dx
        self.rect.y += dy

    def keep_inside(self, width, height):
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > width:
            self.rect.right = width
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > height:
            self.rect.bottom = height

    def update(self, width, height):
        self.handle_input()
        self.keep_inside(width, height)

    def draw(self, surface):
        pygame.draw.rect(surface, PLAYER_COLOR, self.rect)


class Coin:
    def __init__(self, radius):
        self.radius = radius
        self.x = 0
        self.y = 0
        self.randomize_position()

    def randomize_position(self):
        # สุ่มให้เหรียญอยู่ในจอ
        self.x = random.randint(self.radius, WIDTH - self.radius)
        self.y = random.randint(self.radius, HEIGHT - self.radius)

    def draw(self, surface):
        pygame.draw.circle(surface, COIN_COLOR, (self.x, self.y), self.radius)

    def is_collected_by(self, player_rect):
        # ตรวจชนแบบง่าย: เหรียญอยู่ในกรอบ player
        return player_rect.collidepoint(self.x, self.y)


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Collect Coins - OOP Version")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("consolas", 24)

        self.player = Player(WIDTH // 2, HEIGHT // 2, size=40, speed=5)
        self.coin = Coin(radius=15)
        self.score = 0
        self.running = True

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self):
        self.player.update(WIDTH, HEIGHT)

        # ชนเหรียญ
        if self.coin.is_collected_by(self.player.rect):
            self.score += 1
            self.coin.randomize_position()

    def draw(self):
        self.screen.fill(BG_COLOR)
        self.player.draw(self.screen)
        self.coin.draw(self.screen)
        score_surf = self.font.render(f"Score: {self.score}", True, (255, 255, 255))
        self.screen.blit(score_surf, (10, 10))
        pygame.display.flip()

    def run(self):
        while self.running:
            self.clock.tick(60)  # FPS
            self.handle_events()
            self.update()
            self.draw()

        pygame.quit()
        sys.exit()


if __name__ == "__main__":
    game = Game()
    game.run()
