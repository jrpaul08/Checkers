import pygame
WIDTH = 800
HEIGHT = 800

ROWS, COLS = 8, 8

SQUARE_SIZE = WIDTH//COLS

#RGB
RED_PIECE = (255, 0, 0)
RED_TILE = (205, 0, 0)
WHITE = (255, 255, 255)
BLACK_TILE = (0, 0, 0)
BLUE = (0, 0, 255)
WOOD = (205,170,125)
GREY = (128, 128, 128)
BLACK_PIECE = (25, 25, 25)
GOLD = (255,193,37)

CROWN = pygame.transform.scale(pygame.image.load('assets/crown.png'), (44, 25))