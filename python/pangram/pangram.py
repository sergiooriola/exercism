"""Functions for identifying pangrams."""

import string


def is_pangram(sentence: str) -> bool:
    """Check whether a sentence uses every letter of the English alphabet.

    Parameters:
        sentence: The sentence to check.

    Returns:
        True if every letter from a to z appears at least once, False
        otherwise. Letter case is ignored.

    Examples:
        >>> is_pangram('The quick brown fox jumps over the lazy dog')
        True

        >>> is_pangram('The quick brown fox jumps over the lazy cat')
        False
    """
    lowercase_sentence = sentence.lower()
    return all(letter in lowercase_sentence for letter in string.ascii_lowercase)
