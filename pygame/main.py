import pygame

class Mygame:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((400,300))
        self.screen.fill((200,100,155))
        pygame.display.set_caption("Hello Pygame")
    
    def start(self):
        while not self.game_over():
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return self.quit
        
            pygame.display.update()
        
        self.quit()
    
    def quit():
        pygame.quit()

    def game_over(self):
        return False
    
app = Mygame()
app.start()
