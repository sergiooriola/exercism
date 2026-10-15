"""Functions for labelling one-, four- and five-band resistors."""

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

TOLERANCES: dict[str, str] = {
    "grey": "±0.05%",
    "violet": "±0.1%",
    "blue": "±0.25%",
    "green": "±0.5%",
    "brown": "±1%",
    "red": "±2%",
    "gold": "±5%",
    "silver": "±10%",
}


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
    """Calculate the resistance in ohms shown by a four- or five-band resistor.

    Parameters:
        colors: Band colors in order. Any list that does not have four bands
            is read as a five-band resistor.

    Returns:
        The number formed by the digit bands (all but the last two),
        followed by as many zeros as the value of the multiplier band (the
        second to last).

    Raises:
        ValueError: If a digit or multiplier color is not a band color.

    Examples:
        >>> _value(['orange', 'orange', 'brown', 'green'])
        330

        >>> _value(['orange', 'orange', 'orange', 'black', 'green'])
        333
    """
    multiplier: int = 10 ** _color_code(colors[-2])
    if len(colors) == 4:
        base_1 = _color_code(colors[0]) * 10
        base_2 = _color_code(colors[1])
        base = base_1 + base_2
    else:
        base_1 = _color_code(colors[0]) * 100
        base_2 = _color_code(colors[1]) * 10
        base_3 = _color_code(colors[2])
        base = base_1 + base_2 + base_3
    return base * multiplier


def _scale_value(value: int) -> tuple[float, str]:
    """Express a resistance with the metric prefix for its magnitude.

    Parameters:
        value: The resistance in ohms.

    Returns:
        The resistance divided by 1000 once for every full group of three
        digits after the leading one, and the metric prefix for that
        magnitude ('' if none).

    Examples:
        >>> _scale_value(680)
        (680.0, '')

        >>> _scale_value(2540000)
        (2.54, 'mega')
    """
    num_digits = len(str(value))
    prefix_index = (num_digits - 1) // 3
    prefix = PREFIXES[prefix_index]

    divisor: int = 1000**prefix_index
    scaled_value = value / divisor
    return scaled_value, prefix


def _tolerance(colors: list[str]) -> str:
    """Look up the tolerance shown by the last band.

    Parameters:
        colors: Band colors in order, the last one being the tolerance band.

    Returns:
        The tolerance as text, such as '±0.5%'.

    Raises:
        KeyError: If the last color is not a tolerance band color.

    Examples:
        >>> _tolerance(['orange', 'orange', 'brown', 'green'])
        '±0.5%'
    """
    return TOLERANCES[colors[-1]]


def resistor_label(colors: list[str]) -> str:
    """Create the label for a resistor's color bands.

    Parameters:
        colors: Band colors in order: a single black band, or four or five
            bands ending with the multiplier and tolerance bands.

    Returns:
        The resistance with its metric prefix, if any, followed by 'ohms'
        and the tolerance. A one-band resistor has no tolerance.

    Raises:
        ValueError: If a digit or multiplier color is not a band color.
        KeyError: If the last color is not a tolerance band color.

    Examples:
        >>> resistor_label(['black'])
        '0 ohms'

        >>> resistor_label(['orange', 'orange', 'black', 'red'])
        '33 ohms ±2%'

        >>> resistor_label(['violet', 'orange', 'red', 'grey'])
        '7.3 kiloohms ±0.05%'

        >>> resistor_label(['red', 'green', 'yellow', 'yellow', 'brown'])
        '2.54 megaohms ±1%'
    """
    if len(colors) == 1:
        return "0 ohms"
    scaled_value, prefix = _scale_value(_value(colors))
    return f"{scaled_value:g} {prefix}ohms {_tolerance(colors)}"
