"""Check that the brackets in a text are balanced and properly nested."""

CLOSING_TO_OPENING: dict[str, str] = {")": "(", "]": "[", "}": "{"}
OPENINGS = set(CLOSING_TO_OPENING.values())


def is_paired(input_string: str) -> bool:
    """Return whether every bracket in a text is closed in the right order.

    Only round brackets, square brackets and curly braces are checked; any other
    character is ignored.

    Parameters:
        input_string: The text to check.

    Returns:
        True if each bracket is closed by its matching pair and the pairs are
        properly nested, False otherwise.

    Examples:
        >>> is_paired('f(x) = [1, {2}]')
        True
        >>> is_paired('{[}]')
        False
        >>> is_paired('[[')
        False
    """
    # A closing bracket must match the latest opening one still unclosed, which
    # is the top of the stack. An empty stack is checked first so that pop()
    # never runs on it.
    stack = []
    for char in input_string:
        if char in OPENINGS:
            stack.append(char)
        elif char in CLOSING_TO_OPENING and (
            not stack or stack.pop() != CLOSING_TO_OPENING[char]
        ):
            return False

    return not stack
