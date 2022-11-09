import pygame
from Checkers.constants import WIDTH, HEIGHT, SQUARE_SIZE, RED_PIECE
from Checkers.board import Board
from Checkers.game import Game

FPS = 60

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Checkers')


def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col




def main():
    run = True
    clock = pygame.time.Clock()
    game = Game(WIN)




    while run:
        clock.tick(FPS)                #Makes game run at a specifc frames per second so it is the same on different systems


        if game.winner() != None:
            print(game.winner())
        for event in pygame.event.get():      #checks to see if any event has happened at a given time
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                game.select(row, col)

        game.update()
    pygame.quit()


main()