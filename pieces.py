# chess/pieces.py
from abc import ABC, abstractmethod
from movement import BoardMovement

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
    def move(self, direction=None, squares=1):
        movement = BoardMovement.forward(self.position, self.color, squares)
        self.board.squares[self.position] = None
        self.position = movement
        self.board.squares[self.position] = self

class Rook(BaseChessPiece):
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

        self.board.squares[self.position] = None
        self.position = movement
        self.board.squares[self.position] = self

class Bishop(BaseChessPiece):
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

        self.board.squares[self.position] = None
        self.position = movement
        self.board.squares[self.position] = self

class Knight(BaseChessPiece):
    def move(self, direction, squares=1):
        column = self.position[0]
        row = int(self.position[1])

        if direction == 'forward_left':
            new_row = row + (1 if self.color == 'WHITE' else -1) * 2
            new_column = chr(ord(column) - 1)
        elif direction == 'forward_right':
            new_row = row + (1 if self.color == 'WHITE' else -1) * 2
            new_column = chr(ord(column) + 1)
        elif direction == 'left_forward':
            new_row = row + (1 if self.color == 'WHITE' else -1) * 1
            new_column = chr(ord(column) - 2)
        elif direction == 'left_backward':
            new_row = row + (-1 if self.color == 'WHITE' else 1) * 1
            new_column = chr(ord(column) - 2)
        elif direction == 'right_forward':
            new_row = row + (1 if self.color == 'WHITE' else -1) * 1
            new_column = chr(ord(column) + 2)
        elif direction == 'right_backward':
            new_row = row + (-1 if self.color == 'WHITE' else 1) * 1
            new_column = chr(ord(column) + 2)
        else:
            return

        if 1 <= new_row <= 8 and 'a' <= new_column <= 'h':
            self.board.squares[self.position] = None
            self.position = f"{new_column}{new_row}"
            self.board.squares[self.position] = self

class King(BaseChessPiece):
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

        self.board.squares[self.position] = None
        self.position = movement
        self.board.squares[self.position] = self

class Queen(BaseChessPiece):
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

        self.board.squares[self.position] = None
        self.position = movement
        self.board.squares[self.position] = self
