"""Convert letter scores from the legacy format to one score per letter."""


def transform(legacy_data: dict[int, list[str]]) -> dict[str, int]:
    """Return the score of each letter from scores grouped by point value.

    Parameters:
        legacy_data: The uppercase letters grouped under their point value.

    Returns:
        Each lowercase letter mapped to its point value.

    Examples:
        >>> transform({1: ['A', 'E'], 2: ['D']})
        {'a': 1, 'e': 1, 'd': 2}
    """
    letter_scores: dict[str, int] = {}
    for point, letters in legacy_data.items():
        for letter in letters:
            letter_scores[letter.lower()] = point
    return letter_scores
