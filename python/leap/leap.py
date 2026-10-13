"""Functions for identifying leap years."""


def leap_year(year: int) -> bool:
    """Check whether a year is a leap year in the Gregorian calendar.

    Parameters:
        year: The year to check.

    Returns:
        True if the year is a leap year, False otherwise.

    Note:
        A year is a leap year if it is divisible by 4, unless it is also
        divisible by 100. Years divisible by 400 are leap years regardless.

    Examples:
        >>> leap_year(1996)
        True

        >>> leap_year(1900)
        False

        >>> leap_year(2000)
        True
    """
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0
