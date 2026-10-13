def _ordinal_suffix(number: int) -> str:
    last_digit = number % 10
    last_two_digits = number % 100
    if 11 <= last_two_digits <= 13:
        return "th"
    elif last_digit == 1:
        return "st"
    elif last_digit == 2:
        return "nd"
    elif last_digit == 3:
        return "rd"
    else:
        return "th"


def line_up(name: str, number: int) -> str:
    suffix = _ordinal_suffix(number)
    return f"{name}, you are the {number}{suffix} customer we serve today. Thank you!"
