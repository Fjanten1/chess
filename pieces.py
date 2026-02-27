# chess/pieces.py
from abc import ABC, abstractmethod

class BaseChessPiece(ABC):
    def __init__(self, color: str, identifier: int):
        self.color = color
        self.identifier = identifier
        self.is_alive = True
        self.position = None
        self.name = self.__class__.__name__

        # Define symbols for each piece type
        self.symbol = {
            'Pawn': '-',
            'Rook': 'R',
            'Bishop': 'B',
            'Knight': 'N',
            'King': 'K',
            'Queen': 'Q'
        }.get(self.name, '?')

    @abstractmethod
    def move(self, movement: str):
        pass

    def die(self):
        self.is_alive = False

    def __str__(self):
        return f"{self.color} {self.name} {self.identifier}"

    def __repr__(self):
        return self.__str__()

# chess/pieces.py
class Pawn(BaseChessPiece):
    def move(self):
        movement = "Pawn moves forward 1 position"
        super().move(movement)
        print(movement)

class Rook(BaseChessPiece):
    def move(self):
        movement = "Rook moves in a straight line"
        super().move(movement)

class Bishop(BaseChessPiece):
    def move(self):
        movement = "Bishop moves diagonally"
        super().move(movement)

class Knight(BaseChessPiece):
    def move(self):
        movement = "Knight moves in an L shape"
        super().move(movement)

class King(BaseChessPiece):
    def move(self):
        movement = "King moves one position in any direction"
        super().move(movement)

class Queen(BaseChessPiece):
    def move(self):
        movement = "Queen moves in any direction"
        super().move(movement)