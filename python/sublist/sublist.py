"""Classify how one list relates to another: equal, sublist, superlist or unequal."""

from enum import Enum, auto


class SublistRelation(Enum):
    """The possible relations of a first list to a second list.

    Attributes:
        EQUAL: Both lists have the same values in the same order.
        SUBLIST: The first list appears, contiguous and in order, in the second.
        SUPERLIST: The second list appears, contiguous and in order, in the first.
        UNEQUAL: None of the relations above holds.
    """

    EQUAL = auto()
    SUBLIST = auto()
    SUPERLIST = auto()
    UNEQUAL = auto()


# Module-level names for each relation, which the Exercism tests import directly.
EQUAL = SublistRelation.EQUAL
SUBLIST = SublistRelation.SUBLIST
SUPERLIST = SublistRelation.SUPERLIST
UNEQUAL = SublistRelation.UNEQUAL


def _is_sublist[T](target: list[T], source: list[T]) -> bool:
    """Return whether the target appears, contiguous and in order, in the source.

    Parameters:
        target: The list to look for.
        source: The list to look in.

    Returns:
        True if some slice of the source equals the target, False otherwise.

    Examples:
        >>> _is_sublist([2, 3], [1, 2, 3])
        True
        >>> _is_sublist([1, 3], [1, 2, 3])
        False
        >>> _is_sublist([], [1, 2, 3])
        True
    """
    target_length = len(target)
    source_length = len(source)

    # A target longer than the source gives a negative count, so range() is empty
    # and any() returns False without a special case.
    window_count = source_length - target_length + 1
    return any(source[i : i + target_length] == target for i in range(window_count))


def sublist[T](list_one: list[T], list_two: list[T]) -> SublistRelation:
    """Return how the first list relates to the second.

    Parameters:
        list_one: The list to classify.
        list_two: The list to compare it with.

    Returns:
        The relation of the first list to the second.

    Examples:
        >>> sublist([1, 2, 3], [1, 2, 3])
        <SublistRelation.EQUAL: 1>
        >>> sublist([2, 3], [1, 2, 3, 4])
        <SublistRelation.SUBLIST: 2>
        >>> sublist([1, 2, 3, 4], [2, 3])
        <SublistRelation.SUPERLIST: 3>
        >>> sublist([1, 3], [1, 2, 3])
        <SublistRelation.UNEQUAL: 4>
    """
    if list_one == list_two:
        return EQUAL

    if _is_sublist(list_one, list_two):
        return SUBLIST

    if _is_sublist(list_two, list_one):
        return SUPERLIST

    return UNEQUAL
