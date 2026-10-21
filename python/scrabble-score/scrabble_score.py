"""Compute the Scrabble score of a word."""

LETTER_VALUES: dict[str, int] = {
    "a": 1,
    "b": 3,
    "c": 3,
    "d": 2,
    "e": 1,
    "f": 4,
    "g": 2,
    "h": 4,
    "i": 1,
    "j": 8,
    "k": 5,
    "l": 1,
    "m": 3,
    "n": 1,
    "o": 1,
    "p": 3,
    "q": 10,
    "r": 1,
    "s": 1,
    "t": 1,
    "u": 1,
    "v": 4,
    "w": 4,
    "x": 8,
    "y": 4,
    "z": 10,
}


def score(word: str) -> int:
    """Return the Scrabble score of a word, the sum of its letter values.

    Parameters:
        word: The word to score, in any letter case.

    Returns:
        The total value of the letters in the word.

    Raises:
        KeyError: If the word contains a character that is not a letter.

    Examples:
        >>> score('cabbage')
        14
        >>> score('')
        0
    """
    return sum(LETTER_VALUES[letter] for letter in word.lower())
