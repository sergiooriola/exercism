"""Functions to help play and score a game of blackjack.

How to play blackjack:    https://bicyclecards.com/how-to-play/blackjack/
"Standard" playing cards: https://en.wikipedia.org/wiki/Standard_52-card_deck
"""

FACE_CARDS = {"J", "Q", "K"}
TEN_CARDS = {"10", "J", "Q", "K"}


def value_of_card(card: str) -> int:
    """Determine the scoring value of a card.

    Parameters:
        card: The given card: '2' to '10', 'J', 'Q', 'K' or 'A'.

    Returns:
        The value of the given card.

    Note:
        1. 'J', 'Q' or 'K' (otherwise known as "face cards") = 10
        2. 'A' (ace card) = 1
        3. '2' - '10' = numerical value
    """
    if card in FACE_CARDS:
        return 10
    elif card == "A":
        return 1
    else:
        return int(card)


def higher_card(card_one: str, card_two: str) -> str | tuple[str, str]:
    """Determine which card has a higher value in the hand.

    Parameters:
        card_one: First card dealt in the hand.
        card_two: Second card dealt in the hand.

    Returns:
        The card with the higher value, or a tuple containing both cards if
        they are of equal value.

    Note:
        Cards are scored as in `value_of_card`, so an ace counts as 1.
    """
    value_of_card_one = value_of_card(card_one)
    value_of_card_two = value_of_card(card_two)
    if value_of_card_one > value_of_card_two:
        return card_one
    elif value_of_card_one < value_of_card_two:
        return card_two
    else:
        return card_one, card_two


def value_of_ace(card_one: str, card_two: str) -> int:
    """Calculate the most advantageous value for an upcoming ace card.

    Parameters:
        card_one: First card dealt in the hand.
        card_two: Second card dealt in the hand.

    Returns:
        Either 1 or 11, which is the value of the upcoming ace card.

    Note:
        An ace already in the hand counts as 11, so the upcoming ace is
        worth 1. Otherwise it is worth 11, unless that would take the hand
        over 21.
    """
    if card_one == "A" or card_two == "A":
        return 1
    accumulated_value = value_of_card(card_one) + value_of_card(card_two)
    if accumulated_value + 11 > 21:
        return 1
    else:
        return 11


def is_blackjack(card_one: str, card_two: str) -> bool:
    """Determine if the hand is a 'natural' or 'blackjack'.

    Parameters:
        card_one: First card dealt in the hand.
        card_two: Second card dealt in the hand.

    Returns:
        True if the hand is a blackjack (an ace and a ten-card: '10', 'J',
        'Q' or 'K'), False otherwise.
    """
    return (card_one == "A" and card_two in TEN_CARDS) or (
        card_one in TEN_CARDS and card_two == "A"
    )


def can_split_pairs(card_one: str, card_two: str) -> bool:
    """Determine if a player can split their hand into two hands.

    Parameters:
        card_one: First card in the hand.
        card_two: Second card in the hand.

    Returns:
        True if the hand can be split into two hands (i.e. both cards are of
        the same value), False otherwise.
    """
    return value_of_card(card_one) == value_of_card(card_two)


def can_double_down(card_one: str, card_two: str) -> bool:
    """Determine if a blackjack player can place a double down bet.

    Parameters:
        card_one: First card in the hand.
        card_two: Second card in the hand.

    Returns:
        True if the hand can be doubled down (i.e. totals 9, 10 or 11
        points), False otherwise.
    """
    hand_total = value_of_card(card_one) + value_of_card(card_two)
    return 9 <= hand_total <= 11
