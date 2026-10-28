"""Validate numbers with the Luhn formula."""


class Luhn:
    """A number to check with the Luhn formula, such as a credit card number.

    Attributes:
        card_num: The number with its spaces removed.

    Examples:
        >>> Luhn('4539 3195 0343 6467').valid()
        True
        >>> Luhn('066 123 478').valid()
        False
    """

    def __init__(self, card_num: str) -> None:
        """Store the number without its spaces.

        Parameters:
            card_num: The number to check. It may contain spaces.
        """
        self.card_num = card_num.replace(" ", "")

    def valid(self) -> bool:
        """Return whether the number passes the Luhn formula.

        Starting from the right, every second digit is doubled, and 9 is
        subtracted when the result is above 9. The number is valid if the sum
        of all the digits is divisible by 10.

        Returns:
            True if the number has at least two digits, no characters other
            than digits and spaces, and a sum divisible by 10; False
            otherwise.
        """
        if len(self.card_num) <= 1 or not self.card_num.isdecimal():
            return False

        digits = [int(digit) for digit in self.card_num]

        for index in range(len(digits) - 2, -1, -2):
            doubled = digits[index] * 2
            if doubled > 9:
                doubled -= 9
            digits[index] = doubled

        return sum(digits) % 10 == 0
