# chess/main.py
from board import Board

# Create a board
board = Board()

# Test moving a pawn
pawn = board.get_piece('a2')
pawn.move()

# Test moving a rook
rook = board.get_piece('a1')
rook.move('forward', 1)

# Test moving a bishop
bishop = board.get_piece('c1')
bishop.move('forward_right', 2)

# Test moving a knight
knight = board.get_piece('b1')
knight.move('forward_left')

# Test moving a king
king = board.get_piece('e1')
king.move('forward')

# Test moving a queen
queen = board.get_piece('d1')
queen.move('forward_right', 3)
