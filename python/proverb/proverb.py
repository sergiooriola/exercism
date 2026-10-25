"""Build the 'For want of a nail' proverb from a chain of words."""

import itertools


def proverb(*words: str, qualifier: str | None = None) -> list[str]:
    """Return the lines of the proverb for the given words.

    Each pair of consecutive words gives one line, and the last line goes
    back to the first word.

    Parameters:
        *words: The chain of things that were lost, in order.
        qualifier: A word to put before the first word in the last line.
            None or an empty string adds nothing.

    Returns:
        The lines of the proverb, or an empty list if there are no words.

    Examples:
        >>> proverb("nail", "shoe")
        ['For want of a nail the shoe was lost.', 'And all for the want of a nail.']
        >>> proverb("nail", qualifier="horseshoe")
        ['And all for the want of a horseshoe nail.']
        >>> proverb()
        []
    """
    if not words:
        return []

    lines = [
        f"For want of a {want} the {lost} was lost."
        for want, lost in itertools.pairwise(words)
    ]

    initial_item = f"{qualifier} {words[0]}" if qualifier else words[0]
    lines.append(f"And all for the want of a {initial_item}.")

    return lines
