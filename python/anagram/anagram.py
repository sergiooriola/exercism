"""Find the anagrams of a word among a list of candidate words."""


def find_anagrams(word: str, candidates: list[str]) -> list[str]:
    """Find the candidates that are anagrams of a word.

    Parameters:
        word: The word to find anagrams of.
        candidates: The words to check.

    Returns:
        The candidates that are anagrams of the word, in their original order.

    Note:
        - Uppercase and lowercase letters are treated as the same letter.
        - A word is not an anagram of itself.
        - The anagrams keep their original uppercase and lowercase letters.

    Examples:
        >>> find_anagrams('stone', ['stone', 'tones', 'banana', 'notes', 'Seton'])
        ['tones', 'notes', 'Seton']
        >>> find_anagrams('Listen', ['enlists', 'Silent', 'LISTEN'])
        ['Silent']
    """
    lowercase_word = word.lower()
    sorted_lowercase_letters = sorted(lowercase_word)
    return [
        candidate
        for candidate in candidates
        if candidate.lower() != lowercase_word
        and sorted_lowercase_letters == sorted(candidate.lower())
    ]
