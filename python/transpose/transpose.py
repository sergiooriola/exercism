"""Transpose a block of text, turning its rows into columns."""


def transpose(text: str) -> str:
    r"""Return the text with its rows and columns swapped.

    Shorter rows are padded with spaces on the left of the output, never on
    the right. Spaces that were already in the text are kept.

    Parameters:
        text: The rows of the text, separated by newlines.

    Returns:
        The transposed rows, separated by newlines, or an empty string if
        the text is empty.

    Examples:
        >>> transpose("ABC\nDEF")
        'AD\nBE\nCF'
        >>> transpose("AB\nDEF")
        'AD\nBE\n F'
        >>> transpose("ABC\nDE")
        'AD\nBE\nC'
    """
    if not text:
        return ""

    rows = text.split("\n")
    padded_rows = [
        row.ljust(max(len(remaining_row) for remaining_row in rows[i:]))
        for i, row in enumerate(rows)
    ]

    # Each row is padded to the longest row from it down, so the first row
    # is the longest and row lengths never grow from top to bottom.
    column_count = len(padded_rows[0])
    transposed_rows = [
        "".join(row[column] for row in padded_rows if column < len(row))
        for column in range(column_count)
    ]

    return "\n".join(transposed_rows)
