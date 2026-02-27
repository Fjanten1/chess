# chess/movement.py
class BoardMovement:
    @staticmethod
    def forward(position: str, color: str, squares: int = 1):
        """Move the piece forward on the board."""
        column = position[0]
        row = int(position[1])
        new_row = row + (1 if color == 'WHITE' else -1) * squares
        if 1 <= new_row <= 8:
            return f"{column}{new_row}"
        return position

    @staticmethod
    def backward(position: str, color: str, squares: int = 1):
        """Move the piece backward on the board."""
        column = position[0]
        row = int(position[1])
        new_row = row + (-1 if color == 'WHITE' else 1) * squares
        if 1 <= new_row <= 8:
            return f"{column}{new_row}"
        return position

    @staticmethod
    def left(position: str, squares: int = 1):
        """Move the piece left on the board."""
        column = position[0]
        row = int(position[1])
        new_column = chr(ord(column) - squares)
        if 'a' <= new_column <= 'h':
            return f"{new_column}{row}"
        return position

    @staticmethod
    def right(position: str, squares: int = 1):
        """Move the piece right on the board."""
        column = position[0]
        row = int(position[1])
        new_column = chr(ord(column) + squares)
        if 'a' <= new_column <= 'h':
            return f"{new_column}{row}"
        return position

    @staticmethod
    def diagonally_forward_left(position: str, color: str, squares: int = 1):
        """Move the piece diagonally forward left on the board."""
        column = position[0]
        row = int(position[1])
        new_row = row + (1 if color == 'WHITE' else -1) * squares
        new_column = chr(ord(column) - squares)
        if 1 <= new_row <= 8 and 'a' <= new_column <= 'h':
            return f"{new_column}{new_row}"
        return position

    @staticmethod
    def diagonally_forward_right(position: str, color: str, squares: int = 1):
        """Move the piece diagonally forward right on the board."""
        column = position[0]
        row = int(position[1])
        new_row = row + (1 if color == 'WHITE' else -1) * squares
        new_column = chr(ord(column) + squares)
        if 1 <= new_row <= 8 and 'a' <= new_column <= 'h':
            return f"{new_column}{new_row}"
        return position

    @staticmethod
    def diagonally_backward_left(position: str, color: str, squares: int = 1):
        """Move the piece diagonally backward left on the board."""
        column = position[0]
        row = int(position[1])
        new_row = row + (-1 if color == 'WHITE' else 1) * squares
        new_column = chr(ord(column) - squares)
        if 1 <= new_row <= 8 and 'a' <= new_column <= 'h':
            return f"{new_column}{new_row}"
        return position

    @staticmethod
    def diagonally_backward_right(position: str, color: str, squares: int = 1):
        """Move the piece diagonally backward right on the board."""
        column = position[0]
        row = int(position[1])
        new_row = row + (-1 if color == 'WHITE' else 1) * squares
        new_column = chr(ord(column) + squares)
        if 1 <= new_row <= 8 and 'a' <= new_column <= 'h':
            return f"{new_column}{new_row}"
        return position
