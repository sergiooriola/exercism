"""Draw a diamond of letters from 'A' up to a given letter."""

import string


def _build_row(current_index: int, max_index: int) -> str:
    """Return one row of the diamond, padded to the full width.

    Parameters:
        current_index: The position in the alphabet of the row's letter.
        max_index: The position in the alphabet of the widest row's letter.

    Returns:
        The row, with its letter once for 'A' and twice for any other letter.
    """
    letter = string.ascii_uppercase[current_index]
    outer_spaces = " " * (max_index - current_index)

    if current_index == 0:
        return f"{outer_spaces}{letter}{outer_spaces}"

    inner_spaces = " " * (2 * current_index - 1)
    return f"{outer_spaces}{letter}{inner_spaces}{letter}{outer_spaces}"


def rows(letter: str) -> list[str]:
    """Return the rows of a diamond with the given letter at its widest point.

    Parameters:
        letter: The letter of the widest row, in any letter case.

    Returns:
        The rows from top to bottom, all as wide as the diamond is tall.

    Raises:
        ValueError: If the input is not a single letter from A to Z.

    Examples:
        >>> rows('C')
        ['  A  ', ' B B ', 'C   C', ' B B ', '  A  ']
        >>> rows('AB')
        Traceback (most recent call last):
        ...
        ValueError: Not a single letter from A to Z: 'AB'
    """
    if len(letter) != 1 or letter.upper() not in string.ascii_uppercase:
        raise ValueError(f"Not a single letter from A to Z: {letter!r}")

    target_letter = letter.upper()
    max_index = string.ascii_uppercase.index(target_letter)

    # The bottom half mirrors the top half without repeating the widest row.
    ascending_indices = list(range(max_index + 1))
    descending_indices = list(reversed(range(max_index)))
    index_sequence = ascending_indices + descending_indices

    return [_build_row(index, max_index) for index in index_sequence]
