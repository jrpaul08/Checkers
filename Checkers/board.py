import pygame

from .constants import WHITE, RED_PIECE, BLACK_TILE, ROWS, SQUARE_SIZE, WOOD, COLS, BLACK_PIECE, RED_TILE
from .piece import Piece


class Board:
    def __init__(self):
        self.board = []
        self.red_left = 12
        self.black_left = 12
        self.red_kings = 0
        self.black_kings = 0
        self.create_board()

    def draw_squares(self, win):
        win.fill(BLACK_TILE)
        for row in range(ROWS):
            for col in range(row % 2, COLS, 2):
                pygame.draw.rect(win, RED_TILE, (row * SQUARE_SIZE, col * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

    def move(self, piece, row, col):
        self.board[piece.row][piece.col], self.board[row][col] = self.board[row][col], self.board[piece.row][piece.col]
        piece.move(row, col)

        if row == ROWS - 1 or row == 0:
            piece.make_king()
            if piece.color == BLACK_PIECE:
                self.black_kings += 1
            else:
                self.red_kings += 1

    def get_piece(self, row, col):
        return self.board[row][col]

    def create_board(self):
        for row in range(ROWS):
            self.board.append([])
            for col in range(COLS):
                if col % 2 == ((row + 1) % 2):
                    if row < 3:
                        self.board[row].append(Piece(row, col, BLACK_PIECE))
                    elif row > 4:
                        self.board[row].append(Piece(row, col, RED_PIECE))
                    else:
                        self.board[row].append(0)
                else:
                    self.board[row].append(0)

    def draw(self, win):
        self.draw_squares(win)
        for row in range(ROWS):
            for col in range(COLS):
                piece = self.board[row][col]
                if piece != 0:
                    piece.draw(win)


    def remove(self, pieces):
        for piece in pieces:
            self.board[piece.row][piece.col] = 0
            if piece != 0:
                if piece.color == RED_PIECE:
                    self.red_left -= 1
                else:
                    self.black_left -= 1

    def winner(self):
        if self.red_left <= 0:
            return BLACK_PIECE
        elif self.black_left <= 0:
            return RED_PIECE

        return None


    def get_valid_moves(self, piece):
        moves = {}
        left = piece.col - 1
        right = piece.col + 1
        row = piece.row

        if piece.color == RED_PIECE or piece.king:
            moves.update(self._traverse_left(row-1, max(row-3, -1), -1, piece.color, left)) #looks at the 2 rows above and sees possible move to traverse left
            moves.update(self._traverse_right(row-1, max(row-3, -1), -1, piece.color, right))

        if piece.color == BLACK_PIECE or piece.king:
            moves.update(self._traverse_left(row + 1, min(row + 3, ROWS), 1, piece.color, left))  # looks at the 2 rows above and sees possible move to traverse left
            moves.update(self._traverse_right(row + 1, min(row + 3, ROWS), 1, piece.color, right))
        return moves

    def _traverse_left(self, start, stop, step, color, left, skipped=[]):
        moves = {}
        last = []
        for r in range(start, stop, step):
            if left < 0:
                break

            current = self.board[r][left]
            if current == 0:                            #we have found an empty square
                if skipped and not last:               #if we have skipped a piece and last which is a piece we'd skipped is not defined than do action
                    break
                elif skipped:
                    moves[(r,left)] = last + skipped   #scenario where we found valid move, skipped over soemthing and now we are double jumping something or so on...
                else:
                    moves[(r, left)] = last           #if its 0 and last existed that means we can jump to it

                if last:                              #at this point we have skipped over something and do the following to know where to go to double or triple jump
                    if step == -1:
                        row = max(r-3,0)
                    else:
                        row = min(r+3, ROWS)
                    moves.update(self._traverse_left(r+step, row, step, color, left-1, last))        #make recursive calls if we can actually double jumpr or triple jump
                    moves.update(self._traverse_right(r + step, row, step, color, left + 1, last))
                break
            elif current.color == color:              #if the spot is the same colored piece as the one making the move, we want to break as it is invalid option
                break

            else:
                last = [current]                     #the spot contains opposite piece, in which case we want to check if the spots diagonal from that piece are valid to jump over to it
            left -= 1

        return moves




    def _traverse_right(self, start, stop, step, color, right, skipped = []):
        moves = {}
        last = []
        for r in range(start, stop, step):
            if right >= COLS:
                break

            current = self.board[r][right]
            if current == 0:  # we have found an empty square
                if skipped and not last:  # if we have skipped a piece and last which is a piece we'd skipped is not defined than do action
                    break
                elif skipped:
                    moves[(r,right)] = last + skipped  # scenario where we found valid move, skipped over soemthing and now we are double jumping something or so on...
                else:
                    moves[(r, right)] = last  # if its 0 and last existed that means we can jump to it

                if last:  # at this point we have skipped over something and do the following to know where to go to double or triple jump
                    if step == -1:
                        row = max(r - 3, 0)
                    else:
                        row = min(r + 3, ROWS)
                    moves.update(self._traverse_left(r + step, row, step, color, right - 1, last))  # make recursive calls if we can actually double jumpr or triple jump
                    moves.update(self._traverse_right(r + step, row, step, color, right + 1, last))
                break
            elif current.color == color:  # if the spot is the same colored piece as the one making the move, we want to break as it is invalid option
                break

            else:
                last = [current]  # the spot contains opposite piece, in which case we want to check if the spots diagonal from that piece are valid to jump over to it
            right += 1

        return moves


