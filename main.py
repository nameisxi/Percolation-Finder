import numpy as np
import pygame
import random

from pygame.locals import *
from quickunionfind import QuickUnionFind
from percolation import Percolation


# Colors
BLACK = (102, 51, 0)
WHITE = (255, 255, 255)
BLUE = (110, 193, 248)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Site dimensions
WIDTH = 6
HEIGHT = 6
MARGIN = 1

# Grid initialization
grid = []
rows = 80
columns = 80
for row in range(rows):
    grid.append([])
    for column in range(columns):
        grid[row].append(0)
random_rows = random.sample(range(0, rows), rows)
random_columns = random.sample(range(0, columns), columns)

# Pygame initialization
WINDOW_SIZE = [(columns * WIDTH + (MARGIN * columns) + MARGIN), (rows * HEIGHT + (MARGIN * rows) + MARGIN) + 20]
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Percolation Finder")
clock = pygame.time.Clock()
pygame.init()

percolation = Percolation(rows) 

# Does it percolate label initialization
does_it_percolate_text = pygame.font.SysFont("monospace", 12)
does_it_percolate_label = does_it_percolate_text.render("Percolates: False", 1, (255,255,255))
screen.blit(does_it_percolate_label, (50, 565))

# Number of open sites label initialization
number_of_open_sites_text = pygame.font.SysFont("monospace", 12)
number_of_open_sites_label = number_of_open_sites_text.render("Number of open sites: 0", 1, (255,255,255))
screen.blit(number_of_open_sites_label, (200, 565))

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
                if percolation.is_full(row, column):
                    percolation.open_site(row, column)    
                    color = BLUE 
                else:
                   percolation.open_site(row, column)     
                   color = WHITE           
       
            pygame.draw.rect(screen, color, [(MARGIN + WIDTH) * column + MARGIN, (MARGIN + HEIGHT) * row + MARGIN, WIDTH, HEIGHT])
    
    if percolation.percolates:
        does_it_percolate_label = does_it_percolate_text.render("Percolates: True", 1, (255,255,255))
        screen.blit(does_it_percolate_label, (50, 565))

    number_of_open_sites_label = number_of_open_sites_text.render("Number of open sites: " + str(percolation.get_number_of_open_site()), 1, (255,255,255))
    screen.blit(number_of_open_sites_label, (200, 565))    
    
    # FPS
    clock.tick(60)
    pygame.display.flip()

pygame.quit()
