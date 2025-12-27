import pygame
import random

CELL_SIZE = 20
GRID_SIZE = 20
SCREEN_RES = CELL_SIZE * GRID_SIZE

COLOR_BLACK = (0, 0, 0)
COLOR_GREEN = (0, 255, 0)
COLOR_RED   = (255, 0, 0)

class Snake:
    def __init__(self):
        self.body = [(10, 10), (10, 11), (10, 12)]
        self.direction = (0, 0)
        self.grow_pending = False

    def move(self):
        if self.direction == (0, 0):
            return
        head_x, head_y = self.body[0]
        new_head = (head_x + self.direction[0], head_y + self.direction[1])
        self.body.insert(0, new_head)
        if not self.grow_pending:
            self.body.pop()
        else:
            self.grow_pending = False

    def grow(self):
        self.grow_pending = True

    def draw(self, screen):
        for segment in self.body:
            rect = pygame.Rect(segment[0]*CELL_SIZE, segment[1]*CELL_SIZE, CELL_SIZE-1, CELL_SIZE-1)
            pygame.draw.rect(screen, COLOR_GREEN, rect)

class Food:
    def __init__(self):
        self.position = (0, 0)
        self.randomize_position()

    def randomize_position(self):
        self.position = (random.randint(0, GRID_SIZE-1), random.randint(0, GRID_SIZE-1))

    def draw(self, screen):
        rect = pygame.Rect(self.position[0]*CELL_SIZE, self.position[1]*CELL_SIZE, CELL_SIZE-1, CELL_SIZE-1)
        pygame.draw.rect(screen, COLOR_RED, rect)

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_RES, SCREEN_RES))
        self.clock = pygame.time.Clock()
        self.snake = Snake()
        self.food = Food()
        self.running = True

    def check_collision(self):
        head = self.snake.body[0]
        if not (0 <= head[0] < GRID_SIZE and 0 <= head[1] < GRID_SIZE):
            return True
        if head in self.snake.body[1:]:
            return True
        return False

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP and self.snake.direction != (0, 1):
                        self.snake.direction = (0, -1)
                    elif event.key == pygame.K_DOWN and self.snake.direction != (0, -1):
                        self.snake.direction = (0, 1)
                    elif event.key == pygame.K_LEFT and self.snake.direction != (1, 0):
                        self.snake.direction = (-1, 0)
                    elif event.key == pygame.K_RIGHT and self.snake.direction != (-1, 0):
                        self.snake.direction = (1, 0)

            self.snake.move()
            
            if self.snake.body[0] == self.food.position:
                self.snake.grow()
                self.food.randomize_position()

            if self.snake.direction != (0, 0) and self.check_collision():
                self.running = False

            self.screen.fill(COLOR_BLACK)
            self.food.draw(self.screen)
            self.snake.draw(self.screen)
            pygame.display.flip()
            self.clock.tick(10)

        pygame.quit()

if __name__ == "__main__":
    game = Game()
    game.run()