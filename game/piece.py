import pygame

from .constants import RED, WHITE, SQUARE_SIZE, GREY, CROWN

class Piece:
    """Class Creates checkerpiece and if its a king or not."""
    PADDING = 10
    OUTLINE = 2

    def __init__(self, row, col, color):
        """Class constructor."""
        self.row = row
        self.col = col
        self.color = color
        self.king = False
        self.x = 0
        self.y = 0
        self.calc_pos()

    def calc_pos(self):
        """calculate the position of the checkerpiece."""
        self.x = SQUARE_SIZE * self.col + SQUARE_SIZE // 2
        self.y = SQUARE_SIZE * self.row + SQUARE_SIZE // 2

    def make_king(self):
        """make the checkerpiece a king."""
        self.king = True

    def draw(self, win):
        """draw the pieces on the board."""
        radius = SQUARE_SIZE//2 - self.PADDING
        pygame.draw.circle(win, GREY, (self.x, self.y), radius + self.OUTLINE)
        pygame.draw.circle(win, self.color, (self.x, self.y), radius)
        if self.king:
            win.blit(CROWN, (self.x - CROWN.get_width()//2, self.y - CROWN.get_height()//2))

    def move(self, row, col):
        """Get checker move."""
        self.row = row
        self.col = col
        self.calc_pos()
