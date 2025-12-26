import pygame
import os

class Game:
    SCREEN_W = 800
    SCREEN_H = 600
    SCREEN_SIZE = (SCREEN_W,SCREEN_H)

    PLAYER_W = 24
    PLAYER_H = 47
    PLAYER_SIZE = (PLAYER_W,PLAYER_H)
    PLAYER_X = 0
    PLAYER_Y = 0

    clock = pygame.time.Clock()

    def __init__(self):
        pygame.display.set_caption("OH I CAN MOVE")
        self.screen = pygame.display.set_move((self.SCREEN_W,self.SCREEN_H))

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
            
            self.player()
    
    def player_move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP] and self.PLAYER_Y >= 0:
            