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

