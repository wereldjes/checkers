import pygame

from .constants import WHITE, ACTUAL_BLACK, BLUE, SQUARE_SIZE
from game.board import Board

class Game:
    #Class constructor
    def __init__(self, win):
        self._init()
        self.win = win

    #Update window display
    def update(self):
        self.board.draw(self.win)
        self.draw_valid_moves(self.valid_moves)
        pygame.display.update()

    #Reusable part of constructor
    def _init(self):
        self.selected = None
        self.board = Board()
        self.turn = WHITE
        self.valid_moves = {}

    #Reset game to starting state
    def reset(self):
        self._init()

    #Select checker piece
    def select(self, row, col):
        if self.selected:
            result = self._move(row, col)
            if not result:
                self.selected = None
                self.select(row, col)
        
        piece = self.board.get_piece(row, col)
        if piece != 0 and piece.color == self.turn:
            self.selected = piece
            self.valid_moves = self.board.get_valid_moves(piece)
            return True

        return False

    #Move the actual checkerpiece on the board
    def _move(self, row, col):
        piece = self.board.get_piece(row, col)
        if self.selected and piece == 0 and (row, col) in self.valid_moves:
            self.board.move(self.selected, row, col)
            skipped = self.valid_moves[(row, col)]
            if skipped:
                self.board.remove(skipped)
            self.change_turn()
        else:
            return False

        return True

    def change_turn(self):
        """Change player turn."""
        self.valid_moves = {}
        if self.turn == WHITE:
            self.turn = ACTUAL_BLACK
        else:
            self.turn = WHITE

    def draw_valid_moves(self, moves):
        """Draw blue dot on the board to see where a checker piece can move."""
        for move in moves:
            row, col = move
            pygame.draw.circle(self.win, BLUE, (col * SQUARE_SIZE + SQUARE_SIZE//2, row * SQUARE_SIZE + SQUARE_SIZE//2), 15)

    def winner(self):
        """Declare a winner."""
        return self.board.winner()

    def get_board(self):
        """Get board object."""
        return self.board

    def ai_move(self, board):
        """Update board object with new board."""
        self.board = board
        self.change_turn()