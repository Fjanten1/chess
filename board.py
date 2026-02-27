# chess/board.py
from pieces import Rook, Knight, Bishop, Queen, King, Pawn
import json

class Board:
    def __init__(self):
        self.squares = {
            f"{chr(col)}{row}": None
            for col in range(ord('a'), ord('i'))
            for row in range(1, 9)
        }
        self.setup_board()

    def setup_board(self):
        """Add all the pieces to the board."""
        # White pieces (bottom row)
        self.squares['a1'] = Rook('WHITE', 1)
        self.squares['b1'] = Knight('WHITE', 1)
        self.squares['c1'] = Bishop('WHITE', 1)
        self.squares['d1'] = Queen('WHITE', 1)
        self.squares['e1'] = King('WHITE', 1)
        self.squares['f1'] = Bishop('WHITE', 2)
        self.squares['g1'] = Knight('WHITE', 2)
        self.squares['h1'] = Rook('WHITE', 2)

        # White pawns (second row)
        white_pawns = {
            f"{chr(col)}2": Pawn('WHITE', col - ord('a') + 1)
            for col in range(ord('a'), ord('i'))
        }
        self.squares.update(white_pawns)

        # Black pieces (top row)
        self.squares['a8'] = Rook('BLACK', 1)
        self.squares['b8'] = Knight('BLACK', 1)
        self.squares['c8'] = Bishop('BLACK', 1)
        self.squares['d8'] = Queen('BLACK', 1)
        self.squares['e8'] = King('BLACK', 1)
        self.squares['f8'] = Bishop('BLACK', 2)
        self.squares['g8'] = Knight('BLACK', 2)
        self.squares['h8'] = Rook('BLACK', 2)

        # Black pawns (second from top row)
        black_pawns = {
            f"{chr(col)}7": Pawn('BLACK', col - ord('a') + 1)
            for col in range(ord('a'), ord('i'))
        }
        self.squares.update(black_pawns)

        # Set initial positions and boards
        for square, piece in self.squares.items():
            if piece:
                piece.set_initial_position(square)
                piece.define_board(self)

    def print_board(self):
        """Print the board in a row-first way."""
        for row in range(8, 0, -1):
            row_pieces = []
            for col in range(ord('a'), ord('i')):
                square = f"{chr(col)}{row}"
                piece = self.squares[square]
                row_pieces.append(str(piece) if piece else "None")
            print(row_pieces)

    def find_piece(self, symbol: str, identifier: int, color: str):
        """Find a piece on the board by its symbol, identifier, and color."""
        return [
            piece for piece in self.squares.values()
            if piece and piece.symbol == symbol and piece.identifier == identifier and piece.color == color
        ]

    def get_piece(self, square: str):
        """Return the piece on a specific square."""
        return self.squares[square]

    def is_square_empty(self, square: str):
        """Return True if the square is empty, False otherwise."""
        return self.get_piece(square) is None

    def kill_piece(self, square: str):
        """Kill the piece on a specific square."""
        piece = self.get_piece(square)
        if piece:
            piece.die()
            self.squares[square] = None

    def save_board_state(self, filename='board_states.txt'):
        """Save the current state of the board to a file."""
        board_state = {
            square: piece.to_dict() if piece else None
            for square, piece in self.squares.items()
        }
        with open(filename, 'a') as file:
            file.write(json.dumps(board_state) + '\n')
    
    @staticmethod
    def load_board_states(filename='board_states.txt'):
        """Load board states from a file using a generator."""
        with open(filename, 'r') as file:
            for line in file:
                yield json.loads(line)
