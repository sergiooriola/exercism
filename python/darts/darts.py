"""Functions for scoring a single toss in a game of darts."""

import math

RADIUS_OUTER_CIRCLE = 10
RADIUS_MIDDLE_CIRCLE = 5
RADIUS_INNER_CIRCLE = 1


def score(x: float, y: float) -> int:
    """Calculate the points earned by a dart landing at a given point.

    Parameters:
        x: Horizontal coordinate of the dart, in units from the centre.
        y: Vertical coordinate of the dart, in units from the centre.

    Returns:
        10 if the dart lands in the inner circle, 5 in the middle circle, 1
        in the outer circle, or 0 if it misses the target.

    Note:
        The circles are centred at (0, 0) and have radii of 1, 5 and 10
        units. A dart landing exactly on the edge of a circle counts as
        inside it.

    Examples:
        >>> score(0, 0)
        10

        >>> score(0, 10)
        1

        >>> score(-9, 9)
        0
    """
    distance = math.hypot(x, y)
    if distance > RADIUS_OUTER_CIRCLE:
        return 0
    elif distance > RADIUS_MIDDLE_CIRCLE:
        return 1
    elif distance > RADIUS_INNER_CIRCLE:
        return 5
    else:
        return 10
