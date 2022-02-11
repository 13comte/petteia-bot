import pygame
from petteia.constants import WIDTH, HEIGHT, CELL_SIZE
from petteia.game import Game
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

FPS = 60

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('PETTEIA BOT v1.0')


def get_row_from_mouse(pos):
    x, y = pos
    row = y // CELL_SIZE
    col = x // CELL_SIZE
    return row, col


def main():
    run = True
    clock = pygame.time.Clock()
    game = Game(WIN)

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_row_from_mouse(pos)
                piece = game.board.get_piece(row, col)
                game.move(piece, 4, 3)
        game.update()

    pygame.quit()


main()
