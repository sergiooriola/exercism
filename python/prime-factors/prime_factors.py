"""Compute the prime factors of a natural number."""


def factors(value: int) -> list[int]:
    """Return the prime factors of a natural number in ascending order.

    Parameters:
        value: The natural number to factorize.

    Returns:
        The prime factors, repeated as many times as they divide the value.

    Raises:
        ValueError: If the value is not a natural number.

    Examples:
        >>> factors(60)
        [2, 2, 3, 5]
        >>> factors(1)
        []
        >>> factors(0)
        Traceback (most recent call last):
        ...
        ValueError: Value 0 must be a natural number.
    """
    if value <= 0:
        raise ValueError(f"Value {value} must be a natural number.")

    prime_factors: list[int] = []
    possible_factor = 2
    remaining_value = value

    # Once the square of possible_factor exceeds remaining_value, no smaller factor
    # is left, so remaining_value is either 1 or prime.
    while possible_factor * possible_factor <= remaining_value:
        if remaining_value % possible_factor == 0:
            prime_factors.append(possible_factor)
            remaining_value //= possible_factor
        else:
            possible_factor += 1

    # A remaining value above 1 is the largest prime factor.
    if remaining_value > 1:
        prime_factors.append(remaining_value)

    return prime_factors
