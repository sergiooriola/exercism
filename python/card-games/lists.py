"""Functions for tracking rounds and card hands in the game of Black Joe."""

JACK = 11


def get_rounds(number: int) -> list[int]:
    """Create a list containing the current and next two round numbers.

    Parameters:
        number: The current round number.

    Returns:
        The current round number and the two that follow.

    Examples:
        >>> get_rounds(27)
        [27, 28, 29]
    """
    return [number, number + 1, number + 2]


def concatenate_rounds(rounds_1: list[int], rounds_2: list[int]) -> list[int]:
    """Concatenate two lists of round numbers.

    Parameters:
        rounds_1: The first rounds played.
        rounds_2: The second group of rounds played.

    Returns:
        All rounds played, in the order given.

    Examples:
        >>> concatenate_rounds([27, 28, 29], [35, 36])
        [27, 28, 29, 35, 36]
    """
    return rounds_1 + rounds_2


def list_contains_round(rounds: list[int], number: int) -> bool:
    """Check whether the list of rounds contains the given round number.

    Parameters:
        rounds: The rounds played.
        number: The round number to look for.

    Returns:
        True if the round was played, False otherwise.

    Examples:
        >>> list_contains_round([27, 28, 29, 35, 36], 29)
        True

        >>> list_contains_round([27, 28, 29, 35, 36], 30)
        False
    """
    return number in rounds


def card_average(hand: list[int]) -> float:
    """Calculate the average card value of the hand.

    Parameters:
        hand: The card values in the hand.

    Returns:
        The average value of the cards in the hand.

    Examples:
        >>> card_average([5, 6, 7])
        6.0
    """
    return sum(hand) / len(hand)


def approx_average_is_average(hand: list[int]) -> bool:
    """Check whether either approximate average equals the actual average.

    Parameters:
        hand: The card values in the hand, an odd number of them.

    Returns:
        True if the average of the first and last cards, or the value of
        the middle card, equals the actual average of the hand; False
        otherwise.

    Examples:
        >>> approx_average_is_average([1, 2, 3])
        True

        >>> approx_average_is_average([1, 2, 4, 5, 8])
        True

        >>> approx_average_is_average([1, 2, 3, 5, 9])
        False
    """
    actual_average = card_average(hand)
    first_last_average = (hand[0] + hand[-1]) / 2
    median = hand[len(hand) // 2]
    return actual_average in (first_last_average, median)


def average_even_is_average_odd(hand: list[int]) -> bool:
    """Check whether cards at even and odd indexes have the same average.

    Parameters:
        hand: The card values in the hand.

    Returns:
        True if the average of the cards at even indexes equals the average
        of the cards at odd indexes, False otherwise.

    Examples:
        >>> average_even_is_average_odd([1, 2, 3])
        True

        >>> average_even_is_average_odd([1, 2, 3, 4])
        False
    """
    even_index_cards = hand[::2]
    odd_index_cards = hand[1::2]
    return card_average(even_index_cards) == card_average(odd_index_cards)


def maybe_double_last(hand: list[int]) -> list[int]:
    """Double the value of the last card if it is a Jack.

    Parameters:
        hand: The card values in the hand.

    Returns:
        The same hand, with the last card doubled if it was a Jack.

    Note:
        The hand is modified in place, so the caller's list changes too.

    Examples:
        >>> maybe_double_last([5, 9, 11])
        [5, 9, 22]

        >>> maybe_double_last([5, 9, 10])
        [5, 9, 10]
    """
    if hand[-1] == JACK:
        hand[-1] *= 2
    return hand
