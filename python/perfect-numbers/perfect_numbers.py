"""Functions for classifying numbers by the sum of their factors."""

import math

PERFECT = "perfect"
ABUNDANT = "abundant"
DEFICIENT = "deficient"


def classify(number: int) -> str:
    """Classify a number by comparing it with its aliquot sum.

    Parameters:
        number: The number to classify, a positive integer.

    Returns:
        'perfect' if the number equals its aliquot sum (the sum of its
        factors, not including the number itself), 'abundant' if it is
        smaller and 'deficient' if it is larger.

    Raises:
        ValueError: If the number is zero or negative.

    Examples:
        >>> classify(6)
        'perfect'

        >>> classify(12)
        'abundant'

        >>> classify(8)
        'deficient'
    """
    if number < 1:
        raise ValueError("Classification is only possible for positive integers.")
    if number == 1:
        return DEFICIENT
    aliquot_sum = 1
    for factor in range(2, math.isqrt(number) + 1):
        if number % factor == 0:
            complement = number // factor
            aliquot_sum += factor
            if factor != complement:
                aliquot_sum += complement
    if number == aliquot_sum:
        return PERFECT
    elif number < aliquot_sum:
        return ABUNDANT
    else:
        return DEFICIENT
