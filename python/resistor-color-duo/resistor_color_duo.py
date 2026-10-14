"""Functions for reading the value of the first two bands of a resistor."""

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


def value(colors: list[str]) -> int:
    """Calculate the two-digit value shown by the first two color bands.

    Parameters:
        colors: Band colors in order; any after the second are ignored.

    Returns:
        The first band's value as the tens digit followed by the second
        band's value as the units digit.

    Raises:
        ValueError: If one of the first two colors is not a band color.

    Examples:
        >>> value(['brown', 'green'])
        15

        >>> value(['brown', 'green', 'violet'])
        15

        >>> value(['black', 'brown'])
        1
    """
    return _color_code(colors[0]) * 10 + _color_code(colors[1])
