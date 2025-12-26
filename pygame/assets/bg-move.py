import pygame
import os

class Game:
    SCREEN_W = 800
    SCREEN_H = 600
    SCREEN_SIZE = (SCREEN_W,SCREEN_H)

    PLAYER_W = 24 * 2
    PLAYER_H = 47 * 2
    PLAYER_SIZE = (PLAYER_W,PLAYER_H)
    PLAYER_X = 387
    PLAYER_Y = 414
    move = 3

    clock = pygame.time.Clock()
    FPS = 60

    def __init__(self):
        pygame.display.set_caption("OH I CAN MOVE")
        self.screen = pygame.display.set_mode((self.SCREEN_W,self.SCREEN_H))

        player_img = pygame.image.load(os.path.join('pygame', 'assets', 'img', 'player.png'))
        self.player = pygame.transform.scale(player_img, self.PLAYER_SIZE)

        background_img = pygame.image.load(os.path.join('pygame', 'assets', 'img', 'pixel-background.png'))
        self.background = pygame.transform.scale(background_img, self.SCREEN_SIZE)
    
    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.screen.blit(self.background, (0,0))

            self.player_draw()
            self.player_move()
            
            pygame.display.update()
            self.clock.tick(self.FPS)
    
    def player_draw(self):
        self.screen.blit(self.player, (self.PLAYER_X,self.PLAYER_Y))
    def player_move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] and self.PLAYER_X >= 0:
            self.PLAYER_X -= self.move
        if keys[pygame.K_RIGHT] and self.PLAYER_X <= self.PLAYER_X + self.PLAYER_W:
            self.PLAYER_X += self.move
        if keys[pygame.K_UP] and self.PLAYER_Y >= 0:
            self.PLAYER_Y -= self.move
        if keys[pygame.K_DOWN] and self.PLAYER_Y <= self.PLAYER_Y + self.PLAYER_H:
            self.PLAYER_Y += self.move

if __name__ == "__main__":
    app = Game()
    app.run()