"""Encode and decode text with the Atbash cipher."""

import string

# Each letter mapped to the one in the same position of the reversed alphabet.
ATBASH_CIPHER = dict(
    zip(string.ascii_lowercase, string.ascii_lowercase[::-1], strict=True)
)

# Encoded text is written in groups of this size to hide the word boundaries.
GROUP_SIZE = 5


def _cipher(text: str) -> str:
    """Swap each letter for its Atbash pair, keep numbers and drop the rest.

    Parameters:
        text: The text to transform, in any letter case.

    Returns:
        The transformed text in lowercase, without spaces or punctuation.

    Raises:
        KeyError: If the text contains a letter outside the English alphabet.
    """
    ciphered_characters = []
    for character in text.lower():
        if character.isalpha():
            ciphered_characters.append(ATBASH_CIPHER[character])
        elif character.isnumeric():
            ciphered_characters.append(character)
    return "".join(ciphered_characters)


def encode(plain_text: str) -> str:
    """Encode a text with the Atbash cipher.

    Parameters:
        plain_text: The text to encode, in any letter case.

    Returns:
        The encoded text in lowercase, in groups of 5 characters separated by
        spaces. Numbers are kept; spaces and punctuation are dropped.

    Raises:
        KeyError: If the text contains a letter outside the English alphabet.

    Examples:
        >>> encode('Testing, 1 2 3.')
        'gvhgr mt123'
    """
    encoded_text = _cipher(plain_text)

    return " ".join(
        encoded_text[i : i + GROUP_SIZE]
        for i in range(0, len(encoded_text), GROUP_SIZE)
    )


def decode(ciphered_text: str) -> str:
    """Decode a text encoded with the Atbash cipher.

    Parameters:
        ciphered_text: The encoded text; its spaces are ignored.

    Returns:
        The decoded text in lowercase, without spaces.

    Raises:
        KeyError: If the text contains a letter outside the English alphabet.

    Examples:
        >>> decode('gvhgr mt123')
        'testing123'
    """
    return _cipher(ciphered_text)
