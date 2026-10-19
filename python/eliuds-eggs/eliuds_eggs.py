"""Count the eggs encoded in the display value of a chicken coop."""


def egg_count(display_value: int) -> int:
    """Return the number of eggs encoded in the display value.

    Parameters:
        display_value: The number shown on the coop display.

    Returns:
        The number of 1 bits in the binary representation of the display value.

    Raises:
        ValueError: If the display value is negative.

    Note:
        - Each 1 bit marks a spot with an egg.
        - The bits are read with % 2 and // 2, without a built-in bit count.

    Examples:
        >>> egg_count(89)
        4
        >>> egg_count(0)
        0
        >>> egg_count(-1)
        Traceback (most recent call last):
        ...
        ValueError: Display value -1 must be non-negative
    """
    if display_value < 0:
        raise ValueError(f"Display value {display_value} must be non-negative")

    total_eggs = 0
    remaining_value = display_value
    while remaining_value != 0:
        if remaining_value % 2 == 1:
            total_eggs += 1
        remaining_value //= 2
    return total_eggs
