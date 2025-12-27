import pygame

class Game:
    SCREEN_W = 800
    SCREEN_H = 600

    clock = pygame.time.Clock()

    def __init__(self):
        pygame.display.set_caption("Hello Pyagame IN OOP!!")
        self.screen = pygame.display.set_mode((self.SCREEN_W,self.SCREEN_H))
    
    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.clock.tick(60)

if __name__ == "__main__":
    app = Game()
    app.run()