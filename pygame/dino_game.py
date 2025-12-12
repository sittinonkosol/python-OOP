import pygame
import os

class Dino:
    BG = pygame.image.load(os.path.join('assets', 'bg.jpg'))
    P = pygame.image.load(os.path.join('assets', 'muslim-man.png'))

    PLAYER = pygame.transform.scale(P, (100,120))

    SCREEN_W = 800
    SCREEN_H = 600

    POSX = 350
    POSY = 400
    MOVE = 1

    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Dino game")
        self.screen = pygame.display.set_mode((self.SCREEN_W, self.SCREEN_H))

        ICON = pygame.image.load(os.path.join('assets', 'icon.png'))
        pygame.display.set_icon(ICON)

    def start(self):
        while not self.game_over():
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return self.quit
            keys = pygame.key.get_pressed()

            if keys[pygame.K_LEFT] and self.POSX > 0:
                self.POSX -= self.MOVE

            if keys[pygame.K_RIGHT] and self.POSX < self.SCREEN_W - 100:
                self.POSX += self.MOVE

            self.screen.blit(self.BG, (0,0))
            self.screen.blit(self.PLAYER, (self.POSX, self.POSY))

            pygame.display.update()
        
        self.quit()
    
    def quit():
        pygame.quit()

    def game_over(self):
        return False
    
app = Dino()
app.start()
