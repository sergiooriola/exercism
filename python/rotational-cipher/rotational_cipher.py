"""Encode text with a rotational (Caesar) cipher."""

import string

LOWERCASE_ENGLISH_ALPHABET = string.ascii_lowercase
UPPERCASE_ENGLISH_ALPHABET = string.ascii_uppercase
ALPHABET_LENGTH = len(LOWERCASE_ENGLISH_ALPHABET)


def _rotate_character(character: str, key: int) -> str:
    """Shift a single character forward in the English alphabet.

    Parameters:
        character: A single character.
        key: The number of positions to shift.

    Returns:
        The shifted letter with its case preserved, or the character unchanged
        if it is not an English letter.

    Note:
        - The shift wraps around from "z" back to "a".

    Examples:
        >>> _rotate_character('a', 1)
        'b'
        >>> _rotate_character('Z', 1)
        'A'
        >>> _rotate_character('!', 1)
        '!'
    """
    if character in LOWERCASE_ENGLISH_ALPHABET:
        alphabet = LOWERCASE_ENGLISH_ALPHABET
    elif character in UPPERCASE_ENGLISH_ALPHABET:
        alphabet = UPPERCASE_ENGLISH_ALPHABET
    else:
        return character
    index = alphabet.index(character)
    return alphabet[(index + key) % ALPHABET_LENGTH]


def rotate(text: str, key: int) -> str:
    """Encode a text by shifting each of its letters by the same key.

    Parameters:
        text: The text to encode.
        key: The number of positions to shift each letter.

    Returns:
        The encoded text, with non-letters left unchanged.

    Examples:
        >>> rotate('omg', 5)
        'trl'
        >>> rotate('Testing 1 2 3 testing', 4)
        'Xiwxmrk 1 2 3 xiwxmrk'
    """
    return "".join(_rotate_character(character, key) for character in text)
