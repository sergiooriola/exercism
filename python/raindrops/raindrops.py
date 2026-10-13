"""Functions for converting a number into raindrop sounds."""


def convert(number: int) -> str:
    """Convert a number into its corresponding raindrop sounds.

    Parameters:
        number: The number to convert.

    Returns:
        The sounds for the factors of the number ('Pling' for 3, 'Plang' for
        5, 'Plong' for 7), joined in that order, or the number itself as a
        string if it has none of those factors.

    Examples:
        >>> convert(30)
        'PlingPlang'

        >>> convert(34)
        '34'
    """
    result = ""
    if number % 3 == 0:
        result += "Pling"
    if number % 5 == 0:
        result += "Plang"
    if number % 7 == 0:
        result += "Plong"

    return result or str(number)
