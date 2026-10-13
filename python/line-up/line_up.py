"""Functions for telling customers their place in line."""


def _ordinal_suffix(number: int) -> str:
    """Determine the English ordinal suffix for a number.

    Parameters:
        number: The number to find the suffix for.

    Returns:
        'st', 'nd', 'rd' or 'th', so that the number followed by the suffix
        reads as an ordinal.

    Note:
        Numbers ending in 1, 2 or 3 take 'st', 'nd' and 'rd', except those
        ending in 11, 12 or 13, which take 'th' like all other numbers.

    Examples:
        >>> _ordinal_suffix(1)
        'st'

        >>> _ordinal_suffix(112)
        'th'
    """
    last_digit = number % 10
    last_two_digits = number % 100
    if 11 <= last_two_digits <= 13:
        return "th"
    elif last_digit == 1:
        return "st"
    elif last_digit == 2:
        return "nd"
    elif last_digit == 3:
        return "rd"
    else:
        return "th"


def line_up(name: str, number: int) -> str:
    """Build the sentence that tells a customer their place in line.

    Parameters:
        name: The name of the customer.
        number: The position of the customer among those served today.

    Returns:
        The sentence, with the number written as an ordinal numeral.

    Examples:
        >>> line_up('Mary', 1)
        'Mary, you are the 1st customer we serve today. Thank you!'

        >>> line_up('John', 12)
        'John, you are the 12th customer we serve today. Thank you!'
    """
    suffix = _ordinal_suffix(number)
    return f"{name}, you are the {number}{suffix} customer we serve today. Thank you!"
