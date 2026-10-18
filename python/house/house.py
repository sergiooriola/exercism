"""Recite the nursery rhyme about the house that Jack built."""

# Each component is a character followed by what it did to the component before it.
VERSE_COMPONENTS: tuple[str, ...] = (
    "the house that Jack built.",
    "the malt that lay in",
    "the rat that ate",
    "the cat that killed",
    "the dog that worried",
    "the cow with the crumpled horn that tossed",
    "the maiden all forlorn that milked",
    "the man all tattered and torn that kissed",
    "the priest all shaven and shorn that married",
    "the rooster that crowed in the morn that woke",
    "the farmer sowing his corn that kept",
    "the horse and the hound and the horn that belonged to",
)


def _build_verse(verse_number: int) -> str:
    """Build one verse of the rhyme.

    Parameters:
        verse_number: The verse to build, from 1 to 12.

    Returns:
        The verse as a single line of text.

    Note:
        - A verse joins its components from the newest character back to the house.

    Examples:
        >>> _build_verse(2)
        'This is the malt that lay in the house that Jack built.'
    """
    included_components = VERSE_COMPONENTS[:verse_number]
    return f"This is {' '.join(included_components[::-1])}"


def recite(start_verse: int, end_verse: int) -> list[str]:
    """Recite a range of verses of the rhyme.

    Parameters:
        start_verse: The first verse to recite, from 1 to 12.
        end_verse: The last verse to recite, from start_verse to 12.

    Returns:
        The verses from start_verse to end_verse, both included, in order.

    Examples:
        >>> recite(1, 1)
        ['This is the house that Jack built.']
        >>> len(recite(4, 8))
        5
    """
    return [
        _build_verse(verse_number) for verse_number in range(start_verse, end_verse + 1)
    ]
