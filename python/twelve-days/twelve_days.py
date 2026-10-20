"""Recite the lyrics of the cumulative song The Twelve Days of Christmas."""

ORDINALS: tuple[str, ...] = (
    "first",
    "second",
    "third",
    "fourth",
    "fifth",
    "sixth",
    "seventh",
    "eighth",
    "ninth",
    "tenth",
    "eleventh",
    "twelfth",
)

GIFTS: tuple[str, ...] = (
    "a Partridge in a Pear Tree",
    "two Turtle Doves",
    "three French Hens",
    "four Calling Birds",
    "five Gold Rings",
    "six Geese-a-Laying",
    "seven Swans-a-Swimming",
    "eight Maids-a-Milking",
    "nine Ladies Dancing",
    "ten Lords-a-Leaping",
    "eleven Pipers Piping",
    "twelve Drummers Drumming",
)


def _build_verse(verse: int) -> str:
    """Return the lyrics of one verse of the song.

    Parameters:
        verse: The number of the verse, from 1 to 12.

    Returns:
        The verse, listing the gifts from the latest day back to the first.

    Examples:
        >>> _build_verse(1).split(': ')[1]
        'a Partridge in a Pear Tree.'
        >>> header, gifts = _build_verse(3).split(': ')
        >>> header
        'On the third day of Christmas my true love gave to me'
        >>> gifts
        'three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.'
    """
    day_ordinal = ORDINALS[verse - 1]
    header = f"On the {day_ordinal} day of Christmas my true love gave to me: "
    if verse == 1:
        gifts = GIFTS[0]
    else:
        # Walk backwards from the gift of the day, stopping before the partridge.
        preceding_gifts = ", ".join(GIFTS[verse - 1 : 0 : -1])
        gifts = f"{preceding_gifts}, and {GIFTS[0]}"
    return f"{header}{gifts}."


def recite(start_verse: int, end_verse: int) -> list[str]:
    """Return the lyrics of a range of verses of the song.

    Parameters:
        start_verse: The number of the first verse to recite, from 1 to 12.
        end_verse: The number of the last verse to recite, from 1 to 12.

    Returns:
        One string per verse, from the start verse to the end verse inclusive.

    Raises:
        ValueError: If a verse number is outside 1 to 12, or the start verse is
            greater than the end verse.

    Examples:
        >>> verses = recite(1, 3)
        >>> len(verses)
        3
        >>> verses[1].split(': ')[1]
        'two Turtle Doves, and a Partridge in a Pear Tree.'
        >>> recite(3, 2)
        Traceback (most recent call last):
        ...
        ValueError: start_verse (3) cannot be greater than end_verse (2).
    """
    if not (1 <= start_verse <= len(GIFTS)):
        raise ValueError(
            f"start_verse must be between 1 and {len(GIFTS)}, got {start_verse}."
        )
    if not (1 <= end_verse <= len(GIFTS)):
        raise ValueError(
            f"end_verse must be between 1 and {len(GIFTS)}, got {end_verse}."
        )
    if start_verse > end_verse:
        raise ValueError(
            f"start_verse ({start_verse}) cannot be "
            f"greater than end_verse ({end_verse})."
        )

    return [_build_verse(verse) for verse in range(start_verse, end_verse + 1)]
