"""Basic list operations built from loops instead of built-in functions."""

from collections.abc import Callable


def append[T](list1: list[T], list2: list[T]) -> list[T]:
    """Join two lists into a new one.

    Parameters:
        list1: The list whose items come first.
        list2: The list whose items come after those of list1.

    Returns:
        A new list with the items of list1 followed by the items of list2.

    Examples:
        >>> append([1, 2], [3, 4])
        [1, 2, 3, 4]
    """
    combined_items: list[T] = []
    for item in list1:
        combined_items.append(item)
    for item in list2:
        combined_items.append(item)
    return combined_items


def concat[T](lists: list[list[T]]) -> list[T]:
    """Join a series of lists into a single list.

    Parameters:
        lists: The lists to join, in order.

    Returns:
        A new list with the items of every list, in order.

    Note:
        - Only one level of nesting is removed: lists inside the lists are kept.

    Examples:
        >>> concat([[1, 2], [3], [4, 5]])
        [1, 2, 3, 4, 5]
        >>> concat([[[1], [2]], [[3]]])
        [[1], [2], [3]]
    """
    concatenated_items: list[T] = []
    for sublist in lists:
        concatenated_items = append(concatenated_items, sublist)
    return concatenated_items


def filter[T](function: Callable[[T], bool], items: list[T]) -> list[T]:
    """Keep only the items that satisfy a condition.

    Parameters:
        function: The condition; it receives one item and returns whether to keep it.
        items: The items to check.

    Returns:
        A new list with the items for which function returns True, in order.

    Examples:
        >>> filter(lambda number: number % 2 == 1, [1, 2, 3, 5])
        [1, 3, 5]
    """
    filtered_items: list[T] = []
    for item in items:
        if function(item):
            filtered_items.append(item)
    return filtered_items


def length[T](items: list[T]) -> int:
    """Count the items in a list.

    Parameters:
        items: The items to count.

    Returns:
        The number of items.

    Examples:
        >>> length([1, 2, 3, 4])
        4
    """
    item_count = 0
    for _ in items:
        item_count += 1
    return item_count


def map[T, U](function: Callable[[T], U], items: list[T]) -> list[U]:
    """Apply a function to every item of a list.

    Parameters:
        function: The function to apply; it receives one item.
        items: The items to transform.

    Returns:
        A new list with the result of function for each item, in order.

    Examples:
        >>> map(lambda number: number + 1, [1, 3, 5, 7])
        [2, 4, 6, 8]
    """
    mapped_items: list[U] = []
    for item in items:
        mapped_items.append(function(item))
    return mapped_items


def foldl[T, U](function: Callable[[U, T], U], items: list[T], initial: U) -> U:
    """Reduce a list to a single value, from the first item to the last.

    Parameters:
        function: Combines the accumulator with one item into the new accumulator.
        items: The items to combine.
        initial: The starting value of the accumulator.

    Returns:
        The accumulator after combining every item, or initial if items is empty.

    Note:
        - function receives the accumulator first and the item second.

    Examples:
        >>> foldl(lambda text, letter: text + letter, ['a', 'b', 'c'], '')
        'abc'
    """
    accumulator = initial
    for item in items:
        accumulator = function(accumulator, item)
    return accumulator


def foldr[T, U](function: Callable[[U, T], U], items: list[T], initial: U) -> U:
    """Reduce a list to a single value, from the last item to the first.

    Parameters:
        function: Combines the accumulator with one item into the new accumulator.
        items: The items to combine.
        initial: The starting value of the accumulator.

    Returns:
        The accumulator after combining every item, or initial if items is empty.

    Note:
        - function receives the accumulator first and the item second, as in foldl.

    Examples:
        >>> foldr(lambda text, letter: text + letter, ['a', 'b', 'c'], '')
        'cba'
    """
    return foldl(function, reverse(items), initial)


def reverse[T](items: list[T]) -> list[T]:
    """Reverse the order of the items in a list.

    Parameters:
        items: The items to reverse.

    Returns:
        A new list with the same items in reverse order.

    Note:
        - Only the top level is reversed: lists inside the list keep their order.

    Examples:
        >>> reverse([1, 2, 3])
        [3, 2, 1]
        >>> reverse([[1, 2], [3]])
        [[3], [1, 2]]
    """
    reversed_items: list[T] = []
    for index in range(length(items) - 1, -1, -1):
        reversed_items.append(items[index])
    return reversed_items
