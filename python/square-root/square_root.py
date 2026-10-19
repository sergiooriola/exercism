"""Calculate the integer square root of a perfect square."""


def square_root(number: int) -> int:
    """Return the square root of a perfect square using binary search.

    Parameters:
        number: The number to take the square root of.

    Returns:
        The non-negative integer whose square equals the number.

    Raises:
        ValueError: If the number is not a perfect square.

    Note:
        - Uses only multiplication, without the math module, ** or pow().

    Examples:
        >>> square_root(25)
        5
        >>> square_root(65025)
        255
        >>> square_root(0)
        0
        >>> square_root(2)
        Traceback (most recent call last):
        ...
        ValueError: Radicand 2 is not a perfect square.
    """
    lower_bound = 0
    upper_bound = number

    while lower_bound <= upper_bound:
        midpoint = (lower_bound + upper_bound) // 2
        squared_midpoint = midpoint * midpoint

        if number == squared_midpoint:
            return midpoint
        elif number > squared_midpoint:
            lower_bound = midpoint + 1
        else:
            upper_bound = midpoint - 1

    raise ValueError(f"Radicand {number} is not a perfect square.")
