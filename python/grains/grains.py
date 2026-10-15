"""Functions for counting the grains of wheat on a chessboard."""

TOTAL_SQUARES = 64


def square(number: int) -> int:
    """Count the grains of wheat on one square of the chessboard.

    Parameters:
        number: The square number, from 1 to 64.

    Returns:
        The grains on that square. The first square has one grain and each
        following square has twice as many as the one before.

    Raises:
        ValueError: If the square number is not between 1 and 64.

    Examples:
        >>> square(1)
        1

        >>> square(3)
        4
    """
    if not 1 <= number <= TOTAL_SQUARES:
        raise ValueError(f"square must be between 1 and {TOTAL_SQUARES}")
    grains: int = 2 ** (number - 1)
    return grains


def total() -> int:
    """Count the grains of wheat on the whole chessboard.

    Returns:
        The sum of the grains on all 64 squares.

    Examples:
        >>> total()
        18446744073709551615
    """
    grains_count = 0
    for square_number in range(1, TOTAL_SQUARES + 1):
        grains_count += square(square_number)
    return grains_count
