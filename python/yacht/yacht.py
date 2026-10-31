"""Score a throw of five dice in one category of the Yacht dice game."""

# Score categories. Any distinct values work, because the tests only use
# these names.
YACHT = "yacht"
ONES = "ones"
TWOS = "twos"
THREES = "threes"
FOURS = "fours"
FIVES = "fives"
SIXES = "sixes"
FULL_HOUSE = "full_house"
FOUR_OF_A_KIND = "four_of_a_kind"
LITTLE_STRAIGHT = "little_straight"
BIG_STRAIGHT = "big_straight"
CHOICE = "choice"

# The face that each number category counts.
FACE_BY_CATEGORY: dict[str, int] = {
    ONES: 1,
    TWOS: 2,
    THREES: 3,
    FOURS: 4,
    FIVES: 5,
    SIXES: 6,
}


def score(dice: list[int], category: str) -> int:
    """Return the score of the dice in the category.

    Parameters:
        dice: The five dice, each from 1 to 6, in any order.
        category: One of the category constants, such as YACHT or ONES.

    Returns:
        The score, or 0 if the dice do not fit the category.

    Examples:
        >>> score([3, 3, 3, 5, 5], FULL_HOUSE)
        19
        >>> score([1, 4, 4, 4, 4], FULL_HOUSE)
        0
        >>> score([3, 3, 3, 3, 3], FOUR_OF_A_KIND)
        12
    """
    total_score = 0

    if category in FACE_BY_CATEGORY:
        amount = dice.count(FACE_BY_CATEGORY[category])
        total_score = FACE_BY_CATEGORY[category] * amount

    # With only two faces, the counts are either 1 and 4 or 2 and 3, so the
    # count of the first die tells which case it is.
    if category == FULL_HOUSE and len(set(dice)) == 2 and dice.count(dice[0]) in (2, 3):
        total_score = sum(dice)

    if category == FOUR_OF_A_KIND:
        for die in set(dice):
            if dice.count(die) >= 4:
                total_score = 4 * die

    if category == LITTLE_STRAIGHT and sorted(dice) == [1, 2, 3, 4, 5]:
        total_score = 30

    if category == BIG_STRAIGHT and sorted(dice) == [2, 3, 4, 5, 6]:
        total_score = 30

    if category == CHOICE:
        total_score = sum(dice)

    if category == YACHT and len(set(dice)) == 1:
        total_score = 50

    return total_score
