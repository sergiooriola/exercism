"""Find the nth prime number."""


def _is_prime(number: int) -> bool:
    """Return whether a number is prime, testing divisors up to its square root.

    Parameters:
        number: The number to test.

    Returns:
        True if no divisor from 2 up to the square root divides the number.

    Note:
        - The number must be at least 2: for 0 and 1 the result is wrongly True.
    """
    divisor = 2
    while divisor * divisor <= number:
        if number % divisor == 0:
            return False
        divisor += 1
    return True


def prime(number: int) -> int:
    """Return the prime at the given position, counting 2 as the first.

    Parameters:
        number: The position of the prime, starting at 1.

    Returns:
        The prime at that position.

    Raises:
        ValueError: If the position is less than 1.

    Examples:
        >>> prime(1)
        2
        >>> prime(6)
        13
        >>> prime(0)
        Traceback (most recent call last):
        ...
        ValueError: there is no zeroth prime
    """
    if number < 1:
        raise ValueError("there is no zeroth prime")

    primes_count = 0
    candidate = 2
    last_prime = 2

    while primes_count < number:
        if _is_prime(candidate):
            primes_count += 1
            last_prime = candidate
        candidate += 1

    return last_prime
