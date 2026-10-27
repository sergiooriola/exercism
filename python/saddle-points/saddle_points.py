"""Find the saddle points of a matrix: the best spots for a tree house."""


def saddle_points(matrix: list[list[int]]) -> list[dict[str, int]]:
    """Return the points that are largest in their row and smallest in their column.

    Parameters:
        matrix: The rows of the matrix, all of the same length.

    Returns:
        A list with one dict per saddle point, with its 'row' and 'column'
        counted from 1, or an empty list if there are none.

    Raises:
        ValueError: If the rows do not all have the same length.

    Examples:
        >>> saddle_points([[9, 8, 7], [5, 3, 2], [6, 6, 7]])
        [{'row': 2, 'column': 1}]
        >>> saddle_points([[1, 2], [3]])
        Traceback (most recent call last):
        ...
        ValueError: irregular matrix
    """
    if not matrix:
        return []

    row_lengths = {len(row) for row in matrix}

    if len(row_lengths) > 1:
        raise ValueError("irregular matrix")

    # A matrix with no columns has no points, and max() would fail on its
    # empty rows.
    if row_lengths == {0}:
        return []

    points: list[dict[str, int]] = []

    transposed_matrix = list(zip(*matrix, strict=True))

    max_values_per_row = [max(row) for row in matrix]
    min_values_per_column = [min(column) for column in transposed_matrix]

    for row_index, row in enumerate(matrix):
        for column_index, value in enumerate(row):
            if (
                value == max_values_per_row[row_index]
                and value == min_values_per_column[column_index]
            ):
                points.append({"row": row_index + 1, "column": column_index + 1})

    return points
