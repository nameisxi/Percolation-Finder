import numpy as np
import pygame
import random

from quickunionfind import QuickUnionFind
from percolation import Percolation


# Colors
BLACK = (102, 51, 0)
WHITE = (255, 255, 255)
BLUE = (110, 193, 248)
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

percolation = Percolation(rows) 
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
    screen.fill(BLACK)
    for row in range(rows):
        for column in range(columns):
            color = BLACK
            if grid[row][column] == 1:
                if row > 0 and column > 0 and percolation.is_full(row, column):
                    percolation.open_site(row, column)    
                    color = BLUE 
                elif row > 0 and column > 0:
                    percolation.open_site(row, column)     
                    color = WHITE         
                else:       
                    color = WHITE   

                #if percolation.percolates:
                #    color = GREEN         
            pygame.draw.rect(screen, color, [(MARGIN + WIDTH) * column + MARGIN, (MARGIN + HEIGHT) * row + MARGIN, WIDTH, HEIGHT])

    # FPS
    clock.tick(60)
    pygame.display.flip()

pygame.quit()
