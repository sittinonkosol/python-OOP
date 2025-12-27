import pygame
import os
import sys

yellow_controls = {
    "LEFT": pygame.K_a,
    "RIGHT": pygame.K_d,
    "UP": pygame.K_w,
    "DOWN": pygame.K_s
}

red_controls = {
    "LEFT": pygame.K_LEFT,
    "RIGHT": pygame.K_RIGHT,
    "UP": pygame.K_UP,
    "DOWN": pygame.K_DOWN
}

min_x = 0
max_x = 450
height = 500
border_x = 450

class Ship:
    def __init__(self, x, y, image, health=10, side="left"):
        self.start_pos = (x, y)
        self.rect = pygame.Rect(x, y, 55, 40)
        self.image = image
        self.vel = 3
        self.health = health
        self.side = side

    def reset(self, health=10):
        self.rect.topleft = self.start_pos
        self.health = health

    def move(self, controls):
        keys = pygame.key.get_pressed()
        
        if self.side == "left":
            min_bound, max_bound = min_x, border_x
        else:
            min_bound, max_bound = border_x, 900

        if keys[controls["LEFT"]] and self.rect.x - self.vel > min_bound:
            self.rect.x -= self.vel
        if keys[controls["RIGHT"]] and self.rect.x + self.vel + self.rect.width < max_bound:
            self.rect.x += self.vel
        if keys[controls["UP"]] and self.rect.y - self.vel > 0:
            self.rect.y -= self.vel
        if keys[controls["DOWN"]] and self.rect.y + self.vel + self.rect.height < height:
            self.rect.y += self.vel

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))

class Game:
    PLAYING = "PLAYING"
    ROUND_OVER = "ROUND_OVER"

    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        pygame.font.init()
        self.WIDTH, self.HEIGHT = 900, 500
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption('Spaceship Game')

        self.clock = pygame.time.Clock()
        self.FPS = 60

        self.WHITE = (255,255,255)
        self.BLACK = (0,0,0)
        self.RED = (255,0,0)
        self.YELLOW = (255,255,0)

        self.MAX_BULLETS = 3
        self.BULLET_VEL = 7
        self.red_bullets = []
        self.yellow_bullets = []

        self.border = pygame.Rect(self.WIDTH // 2 - 5, 0, 10, self.HEIGHT)
        yellow_img = pygame.image.load(os.path.join('pygame', 'assets', 'img', 'spaceship_yellow.png'))
        red_img = pygame.image.load(os.path.join('pygame', 'assets', 'img','spaceship_red.png'))
        self.YELLOW_SHIP_IMAGE = pygame.transform.rotate(pygame.transform.scale(yellow_img, (55,40)), 90)
        self.RED_SHIP_IMAGE = pygame.transform.rotate(pygame.transform.scale(red_img, (55,40)), 270)

        self.yellow = Ship(100, 300, self.YELLOW_SHIP_IMAGE, health=10, side="left")
        self.red = Ship(self.WIDTH - 155, 300, self.RED_SHIP_IMAGE, health=10, side="right")

        self.FIRE_SOUND = pygame.mixer.Sound(os.path.join('pygame', 'assets', 'sound', 'Assets_Gun+Silencer.mp3'))
        self.HIT_SOUND = pygame.mixer.Sound(os.path.join('pygame', 'assets', 'sound', 'Assets_Grenade+1.mp3'))

        self.BG = pygame.transform.scale(
            pygame.image.load(os.path.join("pygame", "assets", "img", "space.png")),
            (self.WIDTH, self.HEIGHT)
        )

        self.font = pygame.font.SysFont("comicsans", 40)
        self.winner_font = pygame.font.SysFont("comicsans", 80)
        
        self.state = self.PLAYING
        self.winner_text = ""

    def restart_round(self):
        self.yellow.reset(health=10)
        self.red.reset(health=10)
        self.yellow_bullets.clear()
        self.red_bullets.clear()
        self.state = self.PLAYING
        self.winner_text = ""

    def damage(self, ship, amount=1):
        ship.health = max(0, ship.health - amount)

    def handle_bullets(self):
        for b in self.red_bullets[:]:
            b.x -= self.BULLET_VEL
            if self.yellow.rect.colliderect(b):
                self.damage(self.yellow, 1)
                self.HIT_SOUND.play()
                self.red_bullets.remove(b)
            elif b.x < 0:
                self.red_bullets.remove(b)
        for b in self.yellow_bullets[:]:
            b.x += self.BULLET_VEL
            if self.red.rect.colliderect(b):
                self.damage(self.red, 1)
                self.HIT_SOUND.play()
                self.yellow_bullets.remove(b)
            elif b.x > self.WIDTH:
                self.yellow_bullets.remove(b)

    def check_winner(self):
        if self.red.health <= 0:
            self.state = self.ROUND_OVER
            self.winner_text = "Yellow Wins!"
        elif self.yellow.health <= 0:
            self.state = self.ROUND_OVER
            self.winner_text = "Red Wins!"

    def draw_hud(self):
        red_text = self.font.render(f"Health: {self.red.health}", True, self.WHITE)
        yellow_text = self.font.render(f"Health: {self.yellow.health}", True, self.WHITE)
        self.screen.blit(red_text, (self.WIDTH - red_text.get_width() - 10, 10))
        self.screen.blit(yellow_text, (10, 10))

    def draw_winner_overlay(self):
        overlay = pygame.Surface((self.WIDTH, self.HEIGHT))
        overlay.set_alpha(180)
        overlay.fill(self.BLACK)
        self.screen.blit(overlay, (0, 0))

        msg = self.winner_font.render(self.winner_text, True, self.WHITE)
        tip = self.font.render("Press any key to restart...", True, self.WHITE)
        self.screen.blit(msg, (self.WIDTH // 2 - msg.get_width() // 2, self.HEIGHT // 2 - 80))
        self.screen.blit(tip, (self.WIDTH // 2 - tip.get_width() // 2, self.HEIGHT // 2 + 10))

    def draw(self):
        self.screen.blit(self.BG, (0, 0))
        pygame.draw.rect(self.screen, self.BLACK, self.border)
        self.draw_hud()
        self.yellow.draw(self.screen)
        self.red.draw(self.screen)

        for b in self.red_bullets:
            pygame.draw.rect(self.screen, self.RED, b)
        for b in self.yellow_bullets:
            pygame.draw.rect(self.screen, self.YELLOW, b)

        if self.state == self.ROUND_OVER:
            self.draw_winner_overlay()

        pygame.display.update()
    
    def run(self):
        running = True
        while running:
            self.clock.tick(self.FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if self.state == self.ROUND_OVER:
                    if event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                        self.restart_round()
                    continue

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RSHIFT and len(self.red_bullets) < self.MAX_BULLETS:
                        bullet = pygame.Rect(self.red.rect.x - 10, self.red.rect.y + 20, 10, 5)
                        self.red_bullets.append(bullet)
                        self.FIRE_SOUND.play()
                    elif event.key == pygame.K_LSHIFT and len(self.yellow_bullets) < self.MAX_BULLETS:
                        bullet = pygame.Rect(self.yellow.rect.x + self.yellow.rect.width, self.yellow.rect.y + 20, 10, 5)
                        self.yellow_bullets.append(bullet)
                        self.FIRE_SOUND.play()

            if self.state == self.PLAYING:
                self.yellow.move(yellow_controls)
                self.red.move(red_controls)
                self.handle_bullets()
                self.check_winner()

            self.draw()
        
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    Game().run()