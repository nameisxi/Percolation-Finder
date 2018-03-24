import numpy as np
import pygame
import random

from quickunionfind import QuickUnionFind

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Site dimensions
WIDTH = 15
HEIGHT = 15
MARGIN = 1

# Grid initialization
grid = []
rows = 50
columns = 50
for row in range(rows):
    grid.append([])
    for column in range(columns):
        grid[row].append(0)
random_rows = random.sample(range(0, rows), rows)
random_columns = random.sample(range(0, columns), columns)

# Pygame initialization
WINDOW_SIZE = [(columns * WIDTH + (MARGIN * columns) + MARGIN), (rows * HEIGHT + (MARGIN * rows) + MARGIN)]
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Percolation Threshold Checker")
clock = pygame.time.Clock()
pygame.init()

union_find = QuickUnionFind()
done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # Fills new square
    while True:
        random_row = random.randint(0, rows) - 1
        random_column = random.randint(0, columns) - 1
        if grid[random_row][random_column] == 0:
            grid[random_row][random_column] = 1
            break

    # Drawing
    screen.fill(WHITE)
    for row in range(rows):
        for column in range(columns):
            color = BLACK
            if grid[row][column] == 1:
                color = WHITE
            pygame.draw.rect(screen, color, [(MARGIN + WIDTH) * column + MARGIN, (MARGIN + HEIGHT) * row + MARGIN, WIDTH, HEIGHT])

    # FPS
    clock.tick(60)
    pygame.display.flip()

pygame.quit()
