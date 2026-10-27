"""Calculate the energy points a player earns for completing a level."""


def sum_of_multiples(limit: int, base_values: list[int]) -> int:
    """Return the sum of the unique multiples of the base values below a limit.

    Parameters:
        limit: The level the player completed. Only multiples below it count.
        base_values: The base value of each magical item the player found.

    Returns:
        The sum of every number below the limit that is a multiple of at
        least one base value, each number counted once.

    Examples:
        >>> sum_of_multiples(20, [3, 5])
        78
        >>> sum_of_multiples(4, [3, 0])
        3
    """
    unique_multiples: set[int] = set()
    for base_value in base_values:
        # The only multiple of 0 is 0, which adds nothing to the sum, and
        # range() does not accept a step of 0.
        if base_value == 0:
            continue
        unique_multiples = unique_multiples.union(range(base_value, limit, base_value))

    return sum(unique_multiples)
