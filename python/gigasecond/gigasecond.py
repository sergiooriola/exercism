"""Find the moment one gigasecond after a given moment."""

import datetime

# One thousand million seconds.
GIGASECOND = datetime.timedelta(seconds=1_000_000_000)


def add(moment: datetime.datetime) -> datetime.datetime:
    """Return the moment one gigasecond after the given one.

    Parameters:
        moment: The starting date and time.

    Returns:
        The date and time one gigasecond (10**9 seconds) later.

    Examples:
        >>> add(datetime.datetime(2015, 1, 24, 22, 0))
        datetime.datetime(2046, 10, 2, 23, 46, 40)
    """
    return moment + GIGASECOND
