import pygame, os

class Spaceship:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Spaceship Game")
        self.WIDTH, self.HEIGHT = 900, 500
        self.SPACESHIP_WIDTH, self.SPACESHIP_HEIGHT = 55, 40
        self.FPS = 60
        self.VEL = 5
        self.BULLET_VEL = 15
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)
        self.RED = (255, 0, 0)
        self.YELLOW = (255, 255, 0)
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        yellow_img = pygame.image.load(os.path.join("assets", "spaceship_yellow.png"))
        self.YELLOW_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(yellow_img, (self.SPACESHIP_WIDTH, self.SPACESHIP_HEIGHT)), 90)
        red_img = pygame.image.load(os.path.join("assets", "spaceship_red.png"))
        self.RED_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(red_img, (self.SPACESHIP_WIDTH, self.SPACESHIP_HEIGHT)), 270)
        self.BORDER = pygame.Rect(self.WIDTH//2 - 5, 0, 10, self.HEIGHT)
        self.SPACE_IMG = pygame.transform.scale(pygame.image.load(os.path.join('assets', 'space.png')), (self.WIDTH, self.HEIGHT))

    def draw_window(self, red, yellow, red_bullets, yellow_bullets):
        #self.screen.fill(self.WHITE)
        self.screen.blit(self.SPACE_IMG, (0, 0))
        pygame.draw.rect(self.screen, self.BLACK, self.BORDER)
        self.screen.blit(self.YELLOW_SPACESHIP, (yellow.x, yellow.y))
        self.screen.blit(self.RED_SPACESHIP, (red.x, red.y))
        for b in red_bullets:
            pygame.draw.rect(self.screen, self.RED, b)
        for b in yellow_bullets:
            pygame.draw.rect(self.screen, self.YELLOW, b)
        pygame.display.update()

    def red_handle_movement(self, keys, red):
        if keys[pygame.K_LEFT] and red.x-self.VEL>self.BORDER.width+self.BORDER.x:
            red.x -= self.VEL
        if keys[pygame.K_RIGHT] and red.x+self.VEL+red.width<self.WIDTH:
            red.x += self.VEL
        if keys[pygame.K_UP] and red.y-self.VEL>0:
            red.y -= self.VEL
        if keys[pygame.K_DOWN] and red.y+self.VEL+red.height<self.HEIGHT-15:
            red.y += self.VEL

    def yellow_handle_movement(self, keys, yellow):
        if keys[pygame.K_a] and yellow.x-self.VEL>0:
            yellow.x -= self.VEL
        if keys[pygame.K_d] and yellow.x+self.VEL+yellow.width<self.BORDER.x:
            yellow.x += self.VEL
        if keys[pygame.K_w] and yellow.y-self.VEL>0:
            yellow.y -= self.VEL
        if keys[pygame.K_s] and yellow.y+self.VEL+yellow.height<self.HEIGHT-15:
            yellow.y += self.VEL

    def handle_bullets(self, red_bullets, yellow_bullets):
        for b in red_bullets:
            b.x -= self.BULLET_VEL
        for b in yellow_bullets:
            b.x += self.BULLET_VEL

    def main(self):
        red = pygame.Rect(700, 300, self.SPACESHIP_WIDTH, self.SPACESHIP_HEIGHT)
        yellow = pygame.Rect(100, 300, self.SPACESHIP_WIDTH, self.SPACESHIP_HEIGHT)
        red_bullets = []
        yellow_bullets = []

        clock = pygame.time.Clock()
        while not self.game_over():
            clock.tick(self.FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return self.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RSHIFT:
                        bullet = pygame.Rect(red.x-15, red.y+red.height//2+5, 10, 5)
                        red_bullets.append(bullet)
                    if event.key == pygame.K_LSHIFT:
                        bullet = pygame.Rect(yellow.x-15, yellow.y+yellow.height//2+3, 10, 5)
                        yellow_bullets.append(bullet)

            keys = pygame.key.get_pressed()
            self.red_handle_movement(keys, red)
            self.yellow_handle_movement(keys, yellow)
            self.handle_bullets(red_bullets, yellow_bullets)
            self.draw_window(red, yellow, red_bullets, yellow_bullets)

        self.quit()

    def quit(self):
        pygame.quit()

    def game_over(self):
        return False

app = Spaceship()
app.main()