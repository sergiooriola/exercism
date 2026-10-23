import itertools


def encode(string: str) -> str:
    encoded_parts = []
    for character, group in itertools.groupby(string):
        count = len(list(group))
        count_str = str(count) if count > 1 else ""
        encoded_parts.append(f"{count_str}{character}")

    return "".join(encoded_parts)


def decode(string: str) -> str:
    decoded_parts = []
    digits = ""

    for character in string:
        if character.isdecimal():
            digits += character
        else:
            count = int(digits) if digits else 1
            decoded_parts.append(character * count)
            digits = ""

    return "".join(decoded_parts)
