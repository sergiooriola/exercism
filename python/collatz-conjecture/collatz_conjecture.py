"""Functions for exploring the Collatz Conjecture."""


def steps(number: int) -> int:
    """Count the steps needed to reach 1 following the Collatz rules.

    Parameters:
        number: The starting number, a positive integer.

    Returns:
        How many steps it takes to reach 1, where each step halves an even
        number or turns an odd number n into 3n + 1.

    Raises:
        ValueError: If the number is zero or negative.

    Examples:
        >>> steps(1)
        0

        >>> steps(16)
        4

        >>> steps(12)
        9
    """
    if number <= 0:
        raise ValueError("Only positive integers are allowed")
    step_count = 0
    while number != 1:
        if number % 2 == 0:
            number //= 2
        else:
            number = 3 * number + 1
        step_count += 1
    return step_count
