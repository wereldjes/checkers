"""
Constants for the game files
"""
import pygame

#board size
WIDTH, HEIGHT = 800, 800
ROWS, COLS = 8, 8
SQUARE_SIZE =  WIDTH//COLS

#colors red=lightbrown black=darkbrown
RED = (188, 158, 130)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (101, 67, 33)
ACTUAL_BLACK = (0, 0, 0)
GREY = (128, 128, 128)

CROWN = pygame.transform.scale(pygame.image.load('assets/crown.png'), (55, 50))
