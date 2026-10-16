"""Translate English text into Pig Latin."""

VOWELS = ("a", "e", "i", "o", "u")


def _find_split_index(word: str) -> int:
    """Find the position where a word is split before moving its start to the end.

    Parameters:
        word: A single lowercase word.

    Returns:
        The index of the first letter that stays at the front of the word.
        Zero means nothing is moved.

    Note:
        - Words starting with a vowel, "xr" or "yt" are not split.
        - A "u" right after a "q" is moved together with the "q".
        - A "y" counts as a vowel unless it is the first letter.
        - Words without vowels or "y" are not split.

    Examples:
        >>> _find_split_index('apple')
        0
        >>> _find_split_index('square')
        3
        >>> _find_split_index('rhythm')
        2
    """
    if word.startswith(("xr", "yt")) or word.startswith(VOWELS):
        return 0
    for index, letter in enumerate(word):
        if index > 0 and letter == "y":
            return index
        if letter in VOWELS:
            if index > 0 and letter == "u" and word[index - 1] == "q":
                return index + 1
            return index
    return 0


def _translate_word(word: str) -> str:
    """Translate a single word into Pig Latin.

    Parameters:
        word: A single English word.

    Returns:
        The word with its leading consonant sound moved to the end, followed
        by "ay".

    Examples:
        >>> _translate_word('pig')
        'igpay'
        >>> _translate_word('queen')
        'eenquay'
    """
    split_index = _find_split_index(word.lower())
    return f"{word[split_index:]}{word[:split_index]}ay"


def translate(text: str) -> str:
    """Translate a text into Pig Latin word by word.

    Parameters:
        text: English words separated by whitespace.

    Returns:
        The translated words joined by single spaces.

    Examples:
        >>> translate('quick fast run')
        'ickquay astfay unray'
    """
    return " ".join(_translate_word(word) for word in text.split())
