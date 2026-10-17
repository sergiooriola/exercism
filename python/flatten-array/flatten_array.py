"""Flatten a nested list of numbers into a single flat list."""

type NestedList = list[int | None | NestedList]


def flatten(iterable: NestedList) -> list[int]:
    """Flatten a nested list of any depth into a list of numbers.

    Parameters:
        iterable: A list whose elements are numbers, None or other such lists.

    Returns:
        All the numbers in the nested list, in their original order.

    Note:
        - None values are left out of the result.

    Examples:
        >>> flatten([1, [2, 6, None], [[None, [4]], 5]])
        [1, 2, 6, 4, 5]
        >>> flatten([[[]]])
        []
    """
    flat_list: list[int] = []
    for element in iterable:
        if isinstance(element, list):
            flat_list.extend(flatten(element))
        elif element is not None:
            flat_list.append(element)
    return flat_list
