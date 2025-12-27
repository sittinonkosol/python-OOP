import pygame

pygame.display.set_mode((800,600))
pygame.display.set_caption("Hello World")

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False