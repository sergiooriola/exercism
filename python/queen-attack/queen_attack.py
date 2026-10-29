"""Tell whether two queens on a chessboard can attack each other."""


class Queen:
    """A queen on an 8 by 8 chessboard, with rows and columns from 0 to 7.

    Attributes:
        row: The row of the queen.
        column: The column of the queen.

    Examples:
        >>> Queen(2, 2).can_attack(Queen(0, 4))
        True
        >>> Queen(4, 1).can_attack(Queen(2, 5))
        False
    """

    def __init__(self, row: int, column: int) -> None:
        """Place a queen on the board.

        Parameters:
            row: The row of the queen, from 0 to 7.
            column: The column of the queen, from 0 to 7.

        Raises:
            ValueError: If the row or the column is not on the board.
        """
        if row < 0:
            raise ValueError("row not positive")
        if row > 7:
            raise ValueError("row not on board")
        if column < 0:
            raise ValueError("column not positive")
        if column > 7:
            raise ValueError("column not on board")

        self.row = row
        self.column = column

    def can_attack(self, another_queen: "Queen") -> bool:
        """Return whether this queen and another one can attack each other.

        Parameters:
            another_queen: The other queen on the board.

        Returns:
            True if both queens share a row, a column or a diagonal.

        Raises:
            ValueError: If both queens are on the same square.
        """
        if self.row == another_queen.row and self.column == another_queen.column:
            raise ValueError("Invalid queen position: both queens in the same square")

        # On a diagonal, the rows and the columns change by the same amount.
        return (
            self.row == another_queen.row
            or self.column == another_queen.column
            or abs(self.row - another_queen.row)
            == abs(self.column - another_queen.column)
        )
