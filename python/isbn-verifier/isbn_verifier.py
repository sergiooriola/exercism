"""Validate ISBN-10 book identification numbers."""

import string


def is_valid(isbn: str) -> bool:
    """Check whether a string is a valid ISBN-10.

    Parameters:
        isbn: The ISBN-10 to check, with or without hyphens.

    Returns:
        True if the ISBN-10 is valid, False otherwise.

    Note:
        - An ISBN-10 has 9 digits (0 to 9) followed by a check character.
        - The check character is a digit or "X", which represents 10.
        - Each value is multiplied by its weight, from 10 down to 1, and the
          sum must be divisible by 11.

    Examples:
        >>> is_valid('3-598-21508-8')
        True
        >>> is_valid('3-598-21507-X')
        True
        >>> is_valid('3-598-21508-9')
        False
    """
    characters = isbn.replace("-", "")

    if len(characters) != 10:
        return False

    if not all(character in string.digits for character in characters[:9]):
        return False

    check_character = characters[-1]
    if check_character == "X":
        check_value = 10
    elif check_character in string.digits:
        check_value = int(check_character)
    else:
        return False

    values = [int(character) for character in characters[:9]] + [check_value]

    total = sum(value * (10 - index) for index, value in enumerate(values))

    return total % 11 == 0
