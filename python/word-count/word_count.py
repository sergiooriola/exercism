"""Count how many times each word occurs in a subtitle."""


def count_words(sentence: str) -> dict[str, int]:
    """Return how many times each word occurs in the sentence.

    Parameters:
        sentence: The subtitle text to count.

    Returns:
        Each lowercase word mapped to the number of times it occurs.

    Note:
        - Words are made of letters and numbers, and are case insensitive.
        - An apostrophe inside a word is part of a contraction, such as can't.
        - Any other character separates words.

    Examples:
        >>> count_words('go Go GO stop')
        {'go': 3, 'stop': 1}
        >>> count_words("Joe can't tell 'large' from large.")
        {'joe': 1, "can't": 1, 'tell': 1, 'large': 2, 'from': 1}
    """
    clean_characters: list[str] = []
    for character in sentence.lower():
        if character.isalnum() or character == "'":
            clean_characters.append(character)
        else:
            clean_characters.append(" ")
    clean_sentence = "".join(clean_characters)

    # Apostrophes at the edges of a word are quotation marks, not part of a
    # contraction. A word made only of them is left empty, and is skipped below.
    words = [word.strip("'") for word in clean_sentence.split()]

    words_count: dict[str, int] = {}
    for word in words:
        if word:
            words_count[word] = words_count.get(word, 0) + 1

    return words_count
