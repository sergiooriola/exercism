"""Functions for classifying triangles by their side lengths."""


def _is_triangle(sides: list[float]) -> bool:
    """Check whether three side lengths can form a triangle.

    Parameters:
        sides: The lengths of the three sides.

    Returns:
        True if the sides form a triangle, False otherwise.

    Note:
        Every side must be longer than 0, and the sum of any two sides must
        be greater than or equal to the third. Degenerate triangles, where
        that sum is equal to the third side, are accepted.

    Examples:
        >>> _is_triangle([3, 4, 5])
        True

        >>> _is_triangle([1, 1, 3])
        False
    """
    a, b, c = sorted(sides)
    return a > 0 and a + b >= c


def equilateral(sides: list[float]) -> bool:
    """Check whether a triangle is equilateral.

    Parameters:
        sides: The lengths of the three sides.

    Returns:
        True if the sides form a triangle with all three sides the same
        length, False otherwise.

    Examples:
        >>> equilateral([2, 2, 2])
        True

        >>> equilateral([2, 3, 2])
        False
    """
    return _is_triangle(sides) and len(set(sides)) == 1


def isosceles(sides: list[float]) -> bool:
    """Check whether a triangle is isosceles.

    Parameters:
        sides: The lengths of the three sides.

    Returns:
        True if the sides form a triangle with at least two sides the same
        length, False otherwise.

    Note:
        An equilateral triangle is therefore also isosceles.

    Examples:
        >>> isosceles([3, 4, 4])
        True

        >>> isosceles([1, 1, 3])
        False
    """
    return _is_triangle(sides) and len(set(sides)) <= 2


def scalene(sides: list[float]) -> bool:
    """Check whether a triangle is scalene.

    Parameters:
        sides: The lengths of the three sides.

    Returns:
        True if the sides form a triangle with all three sides of different
        lengths, False otherwise.

    Examples:
        >>> scalene([5, 4, 6])
        True

        >>> scalene([4, 4, 3])
        False
    """
    return _is_triangle(sides) and len(set(sides)) == 3
