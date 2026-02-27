# chess/pieces.py
from abc import ABC, abstractmethod
from movement import BoardMovement
import functools

def print_board(func):
    @functools.wraps(func)
    def wrapper(self, *args, **kwargs):
        func(self, *args, **kwargs)
        if self.board:
            self.board.print_board()
    return wrapper

class BaseChessPiece(ABC):
    def __init__(self, color: str, identifier: int):
        self.color = color
        self.identifier = identifier
        self.is_alive = True
        self.position = None
        self.name = self.__class__.__name__
        self.board = None

        self.symbol = {
            'Pawn': '-',
            'Rook': 'R',
            'Bishop': 'B',
            'Knight': 'N',
            'King': 'K',
            'Queen': 'Q'
        }.get(self.name, '?')

    @abstractmethod
    def move(self, direction=None, squares=1):
        pass

    def die(self):
        self.is_alive = False

    def set_initial_position(self, position):
        self.position = position

    def define_board(self, board):
        self.board = board

    def __str__(self):
        return f"{self.color} {self.name} {self.identifier}"

    def __repr__(self):
        return self.__str__()

class Pawn(BaseChessPiece):
    @print_board
    def move(self, direction=None, squares=1):
        # Pawns can only move forward, ignore direction parameter
        movement = BoardMovement.forward(self.position, self.color, squares)
        if self.board:
            self.board.squares[self.position] = None
            self.position = movement
            self.board.squares[self.position] = self

class Rook(BaseChessPiece):
    @print_board
    def move(self, direction, squares=1):
        if direction == 'forward':
            movement = BoardMovement.forward(self.position, self.color, squares)
        elif direction == 'backward':
            movement = BoardMovement.backward(self.position, self.color, squares)
        elif direction == 'left':
            movement = BoardMovement.left(self.position, squares)
        elif direction == 'right':
            movement = BoardMovement.right(self.position, squares)
        else:
            return

        if self.board:
            self.board.squares[self.position] = None
            self.position = movement
            self.board.squares[self.position] = self

class Bishop(BaseChessPiece):
    @print_board
    def move(self, direction, squares=1):
        if direction == 'forward_left':
            movement = BoardMovement.diagonally_forward_left(self.position, self.color, squares)
        elif direction == 'forward_right':
            movement = BoardMovement.diagonally_forward_right(self.position, self.color, squares)
        elif direction == 'backward_left':
            movement = BoardMovement.diagonally_backward_left(self.position, self.color, squares)
        elif direction == 'backward_right':
            movement = BoardMovement.diagonally_backward_right(self.position, self.color, squares)
        else:
            return

        if self.board:
            self.board.squares[self.position] = None
            self.position = movement
            self.board.squares[self.position] = self

class Knight(BaseChessPiece):
    @print_board
    def move(self, direction, squares=1):
        # Knight moves in L-shape: 2 squares in one direction and 1 square perpendicular
        column = self.position[0]
        row = int(self.position[1])
        new_row, new_column = row, column

        # Define knight movement patterns
        move_patterns = {
            'forward_left': (2, -1),
            'forward_right': (2, 1),
            'left_forward': (1, -2),
            'left_backward': (-1, -2),
            'right_forward': (1, 2),
            'right_backward': (-1, 2)
        }

        if direction in move_patterns:
            row_change, col_change = move_patterns[direction]
            # Adjust row change based on color (white moves up, black moves down)
            if self.color == 'WHITE':
                new_row = row + row_change
            else:
                new_row = row - row_change
            new_column = chr(ord(column) + col_change)
        else:
            return

        if 1 <= new_row <= 8 and 'a' <= new_column <= 'h':
            if self.board:
                self.board.squares[self.position] = None
                self.position = f"{new_column}{new_row}"
                self.board.squares[self.position] = self

class King(BaseChessPiece):
    @print_board
    def move(self, direction, squares=1):
        if direction == 'forward':
            movement = BoardMovement.forward(self.position, self.color, squares)
        elif direction == 'backward':
            movement = BoardMovement.backward(self.position, self.color, squares)
        elif direction == 'left':
            movement = BoardMovement.left(self.position, squares)
        elif direction == 'right':
            movement = BoardMovement.right(self.position, squares)
        elif direction == 'forward_left':
            movement = BoardMovement.diagonally_forward_left(self.position, self.color, squares)
        elif direction == 'forward_right':
            movement = BoardMovement.diagonally_forward_right(self.position, self.color, squares)
        elif direction == 'backward_left':
            movement = BoardMovement.diagonally_backward_left(self.position, self.color, squares)
        elif direction == 'backward_right':
            movement = BoardMovement.diagonally_backward_right(self.position, self.color, squares)
        else:
            return

        if self.board:
            self.board.squares[self.position] = None
            self.position = movement
            self.board.squares[self.position] = self

class Queen(BaseChessPiece):
    @print_board
    def move(self, direction, squares=1):
        if direction in ['forward', 'backward', 'left', 'right']:
            if direction == 'forward':
                movement = BoardMovement.forward(self.position, self.color, squares)
            elif direction == 'backward':
                movement = BoardMovement.backward(self.position, self.color, squares)
            elif direction == 'left':
                movement = BoardMovement.left(self.position, squares)
            elif direction == 'right':
                movement = BoardMovement.right(self.position, squares)
        elif direction in ['forward_left', 'forward_right', 'backward_left', 'backward_right']:
            if direction == 'forward_left':
                movement = BoardMovement.diagonally_forward_left(self.position, self.color, squares)
            elif direction == 'forward_right':
                movement = BoardMovement.diagonally_forward_right(self.position, self.color, squares)
            elif direction == 'backward_left':
                movement = BoardMovement.diagonally_backward_left(self.position, self.color, squares)
            elif direction == 'backward_right':
                movement = BoardMovement.diagonally_backward_right(self.position, self.color, squares)
        else:
            return

        if self.board:
            self.board.squares[self.position] = None
            self.position = movement
            self.board.squares[self.position] = self
