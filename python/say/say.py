"""Spell out numbers from 0 to 999,999,999,999 in English words."""

ONES = (
    "zero",
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
    "ten",
    "eleven",
    "twelve",
    "thirteen",
    "fourteen",
    "fifteen",
    "sixteen",
    "seventeen",
    "eighteen",
    "nineteen",
)

# Indexed by the tens digit. The first two entries are empty because numbers
# below 20 take their words from ONES.
TENS = (
    "",
    "",
    "twenty",
    "thirty",
    "forty",
    "fifty",
    "sixty",
    "seventy",
    "eighty",
    "ninety",
)

# Indexed by the position of a group of three digits, counting from the right.
# The rightmost group has no scale word.
SCALES = (
    "",
    "thousand",
    "million",
    "billion",
)

MAX_NUMBER = 999_999_999_999


def _say_under_1000(number: int) -> str:
    """Return the English words for a number from 0 to 999.

    Parameters:
        number: The number to spell out, from 0 to 999.

    Returns:
        The words, with a hyphen between tens and units, as in 'forty-two'.
    """
    if number < 20:
        return ONES[number]

    if number < 100:
        tens, units = divmod(number, 10)
        if units == 0:
            return TENS[tens]
        return f"{TENS[tens]}-{ONES[units]}"

    hundreds, remainder = divmod(number, 100)
    if remainder == 0:
        return f"{ONES[hundreds]} hundred"
    return f"{ONES[hundreds]} hundred {_say_under_1000(remainder)}"


def say(number: int) -> str:
    """Return the English words for a number, as it would be said out loud.

    Parameters:
        number: The number to spell out, from 0 to 999,999,999,999.

    Returns:
        The words, with each group of three digits followed by its scale.

    Raises:
        ValueError: If the number is outside 0 to 999,999,999,999.

    Note:
        - A billion is a thousand million, and no 'and' follows 'hundred'.

    Examples:
        >>> say(0)
        'zero'
        >>> say(1002345)
        'one million two thousand three hundred forty-five'
        >>> say(-1)
        Traceback (most recent call last):
        ...
        ValueError: input out of range
    """
    if not 0 <= number <= MAX_NUMBER:
        raise ValueError("input out of range")

    if number == 0:
        return "zero"

    parts = []
    scale_index = 0

    while number > 0:
        number, group = divmod(number, 1000)
        if group > 0:
            group_words = _say_under_1000(group)
            if SCALES[scale_index]:
                parts.append(f"{group_words} {SCALES[scale_index]}")
            else:
                parts.append(group_words)
        scale_index += 1

    return " ".join(reversed(parts))
