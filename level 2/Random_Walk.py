import pygame
import random

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Random Walk')
clock = pygame.time.Clock()

x, y = 400, 300
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.set_at((x, y), (255, 255, 255))
    x += random.choice([-1, 1])
    y += random.choice([-1, 1])
    x = max(0, min(x, 799))
    y = max(0, min(y, 599))

    pygame.display.update()
    clock.tick(120)

pygame.quit()
