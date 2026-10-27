"""Find the Pythagorean triplets whose numbers add up to a given sum."""


def triplets_with_sum(number: int) -> list[list[int]]:
    """Return the Pythagorean triplets [a, b, c] with a + b + c equal to number.

    A Pythagorean triplet has a² + b² = c² and a < b < c.

    Parameters:
        number: The sum the three numbers must add up to.

    Returns:
        A list with each triplet as [a, b, c], in no particular order, or an
        empty list if there are none.

    Examples:
        >>> triplets_with_sum(12)
        [[3, 4, 5]]
        >>> triplets_with_sum(1001)
        []
    """
    triplets: list[list[int]] = []
    # Since b > a and c > b, number is at least a + (a + 1) + (a + 2), so a
    # is below number // 3.
    max_value_a = number // 3
    for a in range(1, max_value_a):
        # Replacing c with number - a - b in a² + b² = c² and solving for b
        # leaves a single possible b for each a.
        numerator = number**2 - 2 * number * a
        denominator = 2 * number - 2 * a
        if numerator % denominator == 0:
            b = numerator // denominator
            c = number - a - b
            if a < b < c:
                triplets.append([a, b, c])
    return triplets
