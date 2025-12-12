import pygame

class Spaceship:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Spaceship Game")
        self.WIDTH, self.HEIGHT = 900, 500
        self.FPS = 60
        self.WHITE = (255, 255, 255)
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))

    def draw_window(self):
        self.screen.fill(self.WHITE)
        pygame.display.update()

    def main(self):
        clock = pygame.time.Clock()
        while not self.game_over():
            clock.tick(self.FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return self.quit()

            self.draw_window()

        self.quit()

    def quit(self):
        pygame.quit()

    def game_over(self):
        return False

app = Spaceship()
app.main()