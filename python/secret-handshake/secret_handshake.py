"""Convert binary codes into secret handshake actions."""

ACTIONS = ("wink", "double blink", "close your eyes", "jump")


def commands(binary_str: str) -> list[str]:
    """Convert a binary code into the actions of a secret handshake.

    Parameters:
        binary_str: A number from 1 to 31 written in binary.

    Returns:
        The handshake actions in the order they are performed.

    Note:
        - The digits are read from right to left.
        - Each of the four rightmost digits adds one action when it is 1.
        - A 1 in the fifth digit reverses the order of the actions.

    Examples:
        >>> commands('00011')
        ['wink', 'double blink']
        >>> commands('10011')
        ['double blink', 'wink']
    """
    actions: list[str] = []
    reversed_digits = binary_str[::-1]
    for index, digit in enumerate(reversed_digits):
        if index == len(ACTIONS) and digit == "1":
            actions.reverse()
            return actions
        if digit == "1":
            actions.append(ACTIONS[index])
    return actions
