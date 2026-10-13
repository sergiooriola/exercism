"""Functions for reversing strings."""


def reverse(text: str) -> str:
    """Reverse the given text.

    Parameters:
        text: The text to reverse.

    Returns:
        The characters of the text in reverse order.

    Examples:
        >>> reverse('stressed')
        'desserts'

        >>> reverse('')
        ''
    """
    return text[::-1]
