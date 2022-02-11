from .constants import WHITE, BLACK, CELL_SIZE, HYPER_YELLOW
import pygame

class Piece:
    PADDING = 20
    STROKE = 3

    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.direction = 1

        self.x = 0
        self.y = 0
        self.calc_pos()

    # Find middle of the square to draw the piece
    def calc_pos(self):
        self.x = self.col * CELL_SIZE + CELL_SIZE // 2
        self.y = self.row * CELL_SIZE + CELL_SIZE // 2

    # Function to draw circle
    def draw(self, win):
        radius = CELL_SIZE//2 - self.PADDING
        # Draw larger circle behind first to create outline
        pygame.draw.circle(win, WHITE, (self.x, self.y), radius + self.STROKE)
        # Fill with smaller circle
        pygame.draw.circle(win, self.color, (self.x, self.y), radius)

    def move(self, row, col):
        self.row = row
        self.col = col
        self.calc_pos()

    def __rep__(self):
        return str(self.color)
