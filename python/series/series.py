"""Extract the contiguous series of a given length from a string of digits."""


def slices(series: str, length: int) -> list[str]:
    """Return every contiguous series of the given length, in order of appearance.

    Parameters:
        series: The string of digits to slice.
        length: The number of digits in each series.

    Returns:
        The series of the given length, from left to right.

    Raises:
        ValueError: If the series is empty, or the length is zero, negative or
            greater than the length of the series.

    Examples:
        >>> slices('49142', 3)
        ['491', '914', '142']
        >>> slices('49142', 5)
        ['49142']
        >>> slices('12345', 6)
        Traceback (most recent call last):
        ...
        ValueError: slice length cannot be greater than series length
    """
    if not series:
        raise ValueError("series cannot be empty")
    if length == 0:
        raise ValueError("slice length cannot be zero")
    if length < 0:
        raise ValueError("slice length cannot be negative")
    if length > len(series):
        raise ValueError("slice length cannot be greater than series length")

    return [
        series[start_index : start_index + length]
        for start_index in range(len(series) - length + 1)
    ]
