import pygame

from .piece import Piece
from .constants import BLACK, WHITE, ROWS, COLS, BG_GREY, CELL_SIZE


# Class to store the current state of the game/board
class Board:
    def __init__(self):
        self.board = []
        self.black_left = self.white_left = 9
        self.create_board()

    # This method handles drawing the
    def draw_squares(self, win):
        win.fill(BLACK)

        # Draw every other square with grey
        for row in range(ROWS):
            for col in range(row % 2, ROWS, 2):
                pygame.draw.rect(win, BG_GREY, (row*CELL_SIZE, col*CELL_SIZE, CELL_SIZE, CELL_SIZE))

    def move(self, piece, row, col):
        """
        Function to swap old piece coordinates with new
        Convoluted syntax, but it saves creating a temp variable

        :param piece: This is the piece which needs to be moved
        :param row: Row (

        """
        self.board[piece.row][piece.col], self.board[row][col] = self.board[row][col], self.board[piece.row][piece.col]
        piece.move(row, col)

    def get_piece(self, row, col):
        return self.board[row][col]

    def create_board(self):
        # Populate the board with the standard 9 piece starting position
        for row in range(ROWS):
            self.board.append([])
            for col in range(COLS):
                 if (row < 1) or (row == 1 and col == 4):
                    self.board[row].append(Piece(row, col, WHITE))
                 elif (row == 6 and col == 3) or (row > 6):
                    self.board[row].append(Piece(row, col, BLACK))
                 else:
                    self.board[row].append(0)

    # Calls the draw_squares method to draw the board bg and
    # then calls the piece.draw method to draw the player positions
    def draw(self, win):
        self.draw_squares(win)
        for row in range(ROWS):
            for col in range(COLS):
                piece = self.board[row][col]
                if piece != 0:
                    piece.draw(win)


    def find_vertical_obstacles(self, piece):
        pass
    def find_horizontal_obstacles(self, piece):
        pass
    def slide_vertical(self, piece, color):
        pass

    def slide_horizontal(self, piece, color):
        pass

    def get_valid_moves(self, piece):
        pass
