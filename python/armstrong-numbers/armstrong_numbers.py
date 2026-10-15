"""Functions for identifying Armstrong numbers."""


def is_armstrong_number(number: int) -> bool:
    """Check whether a number is an Armstrong number.

    Parameters:
        number: The number to check, zero or positive.

    Returns:
        True if the number equals the sum of its digits, each raised to the
        power of the number of digits, False otherwise.

    Raises:
        ValueError: If the number is negative.

    Examples:
        >>> is_armstrong_number(153)
        True

        >>> is_armstrong_number(10)
        False
    """
    digits = str(number)
    digit_count = len(digits)
    powered_digits_sum = 0
    for digit in digits:
        powered_digits_sum += int(digit) ** digit_count
    return number == powered_digits_sum
