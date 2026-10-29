"""Clean up North American phone numbers so they can receive SMS messages."""


class PhoneNumber:
    """A valid NANP phone number, stored as its ten digits.

    Attributes:
        number: The ten digits, without punctuation or country code.
        area_code: The first three digits.
        exchange_code: The next three digits.
        subscriber_number: The last four digits.

    Examples:
        >>> phone = PhoneNumber("+1 (223) 456-7890")
        >>> phone.number
        '2234567890'
        >>> phone.pretty()
        '(223)-456-7890'
    """

    def __init__(self, number: str) -> None:
        """Clean up the number and split it into its three parts.

        Parameters:
            number: The phone number as the user wrote it.

        Raises:
            ValueError: If the number is not a valid NANP phone number.
        """
        self.number = _clean_number(number)
        self.area_code = self.number[:3]
        self.exchange_code = self.number[3:6]
        self.subscriber_number = self.number[6:]

    def pretty(self) -> str:
        """Return the number in the (NXX)-NXX-XXXX format."""
        return f"({self.area_code})-{self.exchange_code}-{self.subscriber_number}"


def _clean_number(number: str) -> str:
    """Return the ten digits of a phone number, checking it is valid.

    Parameters:
        number: The phone number as the user wrote it.

    Returns:
        The ten digits, without punctuation or country code.

    Raises:
        ValueError: If the number has letters or symbols that are not
            separators, the wrong number of digits, a country code other
            than 1, or an area or exchange code that starts with 0 or 1.
    """
    clean_digits: list[str] = []

    # Separators are dropped, but any other symbol makes the number invalid.
    for character in number:
        if character.isdecimal():
            clean_digits.append(character)
        elif character in "() +-.":
            continue
        elif character.isalpha():
            raise ValueError("letters not permitted")
        else:
            raise ValueError("punctuations not permitted")

    clean_number = "".join(clean_digits)

    if len(clean_number) < 10:
        raise ValueError("must not be fewer than 10 digits")

    if len(clean_number) > 11:
        raise ValueError("must not be greater than 11 digits")

    if len(clean_number) == 11 and not clean_number.startswith("1"):
        raise ValueError("11 digits must start with 1")

    # Drop the country code, so the number always has ten digits from here.
    if len(clean_number) == 11:
        clean_number = clean_number[1:]

    if clean_number[3] == "0":
        raise ValueError("exchange code cannot start with zero")

    if clean_number[3] == "1":
        raise ValueError("exchange code cannot start with one")

    if clean_number[0] == "0":
        raise ValueError("area code cannot start with zero")

    if clean_number[0] == "1":
        raise ValueError("area code cannot start with one")

    return clean_number
