import pygame

from . constants import RED_PIECE, BLACK_TILE, SQUARE_SIZE, GREY, GOLD, CROWN

class Piece:
    PADDING = 15
    OUTLINE = 2

    def __init__(self,row,col,color): #need to pass what row and colum its in and the piece's color
        self.row = row
        self.col = col
        self.color = color
        self.king = False
        self.x = 0
        self.y = 0
        self.calc_pos()

        if self.color == RED_PIECE:
            self.direction = -1
        else:
            self.direction = 1

    def calc_pos(self):
        self.x = SQUARE_SIZE*self.col + SQUARE_SIZE // 2
        self.y = SQUARE_SIZE*self.row + SQUARE_SIZE // 2

    def make_king(self):
        self.king = True

    def draw(self, win):
        radius = SQUARE_SIZE//2 - self.PADDING
        pygame.draw.circle(win, GOLD, (self.x, self.y), radius + self.OUTLINE)
        pygame.draw.circle(win,self.color,(self.x, self.y),radius)
        if self.king:
            win.blit(CROWN, (self.x - CROWN.get_width()//2, self.y - CROWN.get_height()//2))

    def move(self, row, col):
        self.row = row
        self.col = col
        self.calc_pos()

    def __repr__(self):
        return str(self.color)

