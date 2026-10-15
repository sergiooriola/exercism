"""Functions for comparing the square of a sum with the sum of squares."""


def square_of_sum(number: int) -> int:
    """Square the sum of the first natural numbers.

    Parameters:
        number: How many natural numbers to add, starting from 1.

    Returns:
        The sum of the numbers from 1 to the given number, squared.

    Examples:
        >>> square_of_sum(10)
        3025
    """
    return sum(range(1, number + 1)) ** 2


def sum_of_squares(number: int) -> int:
    """Add up the squares of the first natural numbers.

    Parameters:
        number: How many natural numbers to square, starting from 1.

    Returns:
        The sum of the squares of the numbers from 1 to the given number.

    Examples:
        >>> sum_of_squares(10)
        385
    """
    squared_values = []
    for value in range(1, number + 1):
        squared_values.append(value**2)
    return sum(squared_values)


def difference_of_squares(number: int) -> int:
    """Subtract the sum of squares from the square of the sum.

    Parameters:
        number: How many natural numbers to use, starting from 1.

    Returns:
        The square of the sum minus the sum of the squares of the numbers
        from 1 to the given number.

    Examples:
        >>> difference_of_squares(10)
        2640
    """
    return square_of_sum(number) - sum_of_squares(number)
