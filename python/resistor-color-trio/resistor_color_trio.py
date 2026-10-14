"""Functions for labelling the resistance shown by three resistor color bands."""

COLORS = (
    "black",
    "brown",
    "red",
    "orange",
    "yellow",
    "green",
    "blue",
    "violet",
    "grey",
    "white",
)

PREFIXES = ("", "kilo", "mega", "giga")


def _color_code(color: str) -> int:
    """Look up the numeric value of a color band.

    Parameters:
        color: Name of the band color, in any letter case.

    Returns:
        The value of the color, from 0 for black to 9 for white.

    Raises:
        ValueError: If the color is not a resistor band color.

    Examples:
        >>> _color_code('orange')
        3
    """
    return COLORS.index(color.lower())


def _value(colors: list[str]) -> int:
    """Calculate the resistance in ohms shown by the first three bands.

    Parameters:
        colors: Band colors in order; any after the third are ignored.

    Returns:
        The two-digit value of the first two bands, followed by as many
        zeros as the value of the third band.

    Raises:
        ValueError: If one of the first three colors is not a band color.

    Examples:
        >>> _value(['orange', 'orange', 'red'])
        3300
    """
    base = _color_code(colors[0]) * 10 + _color_code(colors[1])
    multiplier: int = 10 ** _color_code(colors[2])
    return base * multiplier


def _scale_value(value: int) -> tuple[int, str]:
    """Express a resistance with the largest metric prefix that fits exactly.

    Parameters:
        value: The resistance in ohms.

    Returns:
        The resistance divided by 1000 once for every group of three
        trailing zeros, and the metric prefix for that magnitude ('' if
        none).

    Examples:
        >>> _scale_value(680)
        (680, '')

        >>> _scale_value(2000)
        (2, 'kilo')
    """
    digits = str(value)
    trailing_zeros = len(digits) - len(digits.rstrip("0"))
    prefix_index = trailing_zeros // 3
    prefix = PREFIXES[prefix_index]
    divisor: int = 1000**prefix_index
    scaled_value = value // divisor
    return scaled_value, prefix


def label(colors: list[str]) -> str:
    """Create the resistance label for a resistor's color bands.

    Parameters:
        colors: Band colors in order; any after the third are ignored.

    Returns:
        The resistance followed by its metric prefix, if any, and 'ohms'.

    Raises:
        ValueError: If one of the first three colors is not a band color.

    Examples:
        >>> label(['orange', 'orange', 'black'])
        '33 ohms'

        >>> label(['red', 'black', 'red'])
        '2 kiloohms'

        >>> label(['white', 'white', 'white'])
        '99 gigaohms'
    """
    scaled_value, prefix = _scale_value(_value(colors))
    return f"{scaled_value} {prefix}ohms"
