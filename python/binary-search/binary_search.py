"""Find a value in a sorted list using binary search."""


def find(search_list: list[int], value: int) -> int:
    """Find the position of a value in a sorted list.

    Parameters:
        search_list: The numbers to search, sorted from smallest to largest.
        value: The number to find.

    Returns:
        The index of the value in the list.

    Raises:
        ValueError: If the value is not in the list.

    Note:
        - Each step compares the value with the middle element and discards
          the half of the list where the value cannot be.

    Examples:
        >>> find([1, 3, 4, 6, 8, 9, 11], 6)
        3
        >>> find([1, 3, 4, 6, 8, 9, 11], 7)
        Traceback (most recent call last):
            ...
        ValueError: value not in array
    """
    left_index = 0
    right_index = len(search_list) - 1

    while left_index <= right_index:
        middle_index = (left_index + right_index) // 2
        middle_value = search_list[middle_index]
        if value == middle_value:
            return middle_index
        elif value < middle_value:
            right_index = middle_index - 1
        else:
            left_index = middle_index + 1

    raise ValueError("value not in array")
