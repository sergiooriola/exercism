"""Find prime numbers with the Sieve of Eratosthenes."""


def primes(limit: int) -> list[int]:
    """Return the prime numbers up to a limit.

    Parameters:
        limit: The largest number to check. It is included.

    Returns:
        The prime numbers from 2 to the limit, in ascending order, or an empty
        list if the limit is below 2.

    Examples:
        >>> primes(13)
        [2, 3, 5, 7, 11, 13]
        >>> primes(1)
        []
    """
    prime_list: list[int] = []
    marked_numbers: set[int] = set()

    for number in range(2, limit + 1):
        if number not in marked_numbers:
            prime_list.append(number)
            # Start at the square: every smaller multiple of number has a
            # smaller prime factor, so it has already been marked.
            marked_numbers = marked_numbers.union(range(number**2, limit + 1, number))

    return prime_list
