"""Functions for identifying isograms."""


def is_isogram(phrase: str) -> bool:
    """Check whether a phrase is an isogram.

    Parameters:
        phrase: The word or phrase to check.

    Returns:
        True if no letter appears more than once, False otherwise. Letter
        case is ignored, and spaces and hyphens may appear any number of
        times.

    Examples:
        >>> is_isogram('lumberjacks')
        True

        >>> is_isogram('Alphabet')
        False

        >>> is_isogram('six-year-old')
        True
    """
    seen_letters = []
    for character in phrase.lower():
        if not character.isalpha():
            continue
        if character in seen_letters:
            return False
        seen_letters.append(character)
    return True
