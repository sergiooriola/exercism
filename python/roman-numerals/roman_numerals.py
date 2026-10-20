"""Convert numbers to traditional Roman numerals."""

MIN_ROMAN_NUMBER = 1
MAX_ROMAN_NUMBER = 3999

# Symbols in descending order of value, with the subtractive pairs treated as
# symbols of their own, so each step can take the largest one that fits.
ARABIC_TO_ROMAN: tuple[tuple[int, str], ...] = (
    (1000, "M"),
    (900, "CM"),
    (500, "D"),
    (400, "CD"),
    (100, "C"),
    (90, "XC"),
    (50, "L"),
    (40, "XL"),
    (10, "X"),
    (9, "IX"),
    (5, "V"),
    (4, "IV"),
    (1, "I"),
)


def roman(number: int) -> str:
    """Return the Roman numeral of a number.

    Parameters:
        number: The number to convert, from 1 to 3999.

    Returns:
        The Roman numeral written with the traditional symbols.

    Raises:
        ValueError: If the number is outside 1 to 3999.

    Examples:
        >>> roman(4)
        'IV'
        >>> roman(1996)
        'MCMXCVI'
        >>> roman(4000)
        Traceback (most recent call last):
        ...
        ValueError: Number 4000 must be between 1 and 3999 inclusive.
    """
    if not MIN_ROMAN_NUMBER <= number <= MAX_ROMAN_NUMBER:
        raise ValueError(
            f"Number {number} must be between "
            f"{MIN_ROMAN_NUMBER} and {MAX_ROMAN_NUMBER} inclusive."
        )

    remaining_value = number
    roman_digits: list[str] = []
    for value, symbol in ARABIC_TO_ROMAN:
        while remaining_value >= value:
            roman_digits.append(symbol)
            remaining_value -= value

    return "".join(roman_digits)
