"""Functions for decoding the color bands of a resistor."""

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


def color_code(color: str) -> int:
    """Look up the numeric value of a color band.

    Parameters:
        color: Name of the band color, in any letter case.

    Returns:
        The value of the color, from 0 for black to 9 for white.

    Raises:
        ValueError: If the color is not a resistor band color.

    Examples:
        >>> color_code('orange')
        3

        >>> color_code('White')
        9
    """
    return COLORS.index(color.lower())


def colors() -> list[str]:
    """List the band colors in order of value.

    Returns:
        A new list with the color names, so that each color's index is
        its value.

    Examples:
        >>> colors()[:3]
        ['black', 'brown', 'red']
    """
    return list(COLORS)
