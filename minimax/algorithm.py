from copy import deepcopy
import pygame
from game.constants import WHITE, ACTUAL_BLACK


def minimax(board, depth, max_player):
    """
    AI algorithm to check which is the best move.

    :param board: an object of the board
    :param depth: the depth of the tree. a higher number means a better AI but also a longer wait time
    :param max_player: check if the player is maximizing his score or not
    """
    if depth == 0:
        return board.evaluate(), board

    if max_player:
        value = float("-inf")
        best_move = None
        for move in get_all_moves(board, WHITE):
            evaluation = minimax(move, depth -1, False)[0]
            value = max(value, evaluation)
            if value == evaluation:
                best_move = move
        return value, best_move
    else:
        value = float("inf")
        best_move = None
        for move in get_all_moves(board, ACTUAL_BLACK):
            evaluation = minimax(move, depth -1, True)[0]
            value = min(value, evaluation)
            if value == evaluation:
                best_move = move
        return value, best_move

def get_all_moves(board, color):
    """Get all possible moves for a certain color."""
    moves = []

    for piece in board.get_all_pieces(color):
        valid_moves = board.get_valid_moves(piece)

        for move, skip in valid_moves.items():
            temp_board = deepcopy(board)
            temp_piece = temp_board.get_piece(piece.row, piece.col)
            new_board = simulate_move(temp_piece, move, temp_board, skip)
            moves.append(new_board)

    return moves

def simulate_move(piece, move, board, skip):
    board.move(piece, move[0], move[1])

    if skip:
        board.remove(skip)

    return board
