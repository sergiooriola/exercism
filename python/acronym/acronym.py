"""Convert a phrase to its acronym."""


def _clean_phrase(phrase: str) -> str:
    """Return the phrase with hyphens as spaces and other punctuation removed.

    Parameters:
        phrase: The phrase to clean.

    Returns:
        The phrase containing only letters and whitespace.

    Note:
        - Letters and whitespace are kept.
        - Hyphens become spaces, because they separate words.
        - Any other character is removed.

    Examples:
        >>> _clean_phrase('Liquid-crystal display!')
        'Liquid crystal display'
        >>> _clean_phrase('Rock & Roll')
        'Rock  Roll'
    """
    cleaned_characters = []
    for character in phrase:
        if character.isalpha() or character.isspace():
            cleaned_characters.append(character)
        elif character == "-":
            cleaned_characters.append(" ")
    return "".join(cleaned_characters)


def abbreviate(words: str) -> str:
    """Return the acronym of a phrase.

    Parameters:
        words: The phrase to abbreviate.

    Returns:
        The uppercase first letter of each word in the phrase.

    Examples:
        >>> abbreviate('Portable Network Graphics')
        'PNG'
        >>> abbreviate('Complementary metal-oxide semiconductor')
        'CMOS'
        >>> abbreviate('The Road _Not_ Taken')
        'TRNT'
    """
    cleaned_phrase = _clean_phrase(words)
    return "".join(word[0].upper() for word in cleaned_phrase.split())
