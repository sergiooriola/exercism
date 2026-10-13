"""Functions for creating, transforming, and adding prefixes to strings."""


def add_prefix_un(word: str) -> str:
    """Take the given word and add the 'un' prefix.

    Parameters:
        word: The root word.

    Returns:
        Root word prepended with 'un'.

    Examples:
        >>> add_prefix_un('happy')
        'unhappy'
    """
    return "un" + word


def make_word_groups(vocab_words: list[str]) -> str:
    """Transform a list containing a prefix and words.

    Parameters:
        vocab_words: Vocabulary words with prefix at first index.

    Returns:
        Prefix followed by vocabulary words with prefix applied, separated
        by ' :: '.

    Examples:
        >>> make_word_groups(['en', 'close', 'joy', 'lighten'])
        'en :: enclose :: enjoy :: enlighten'
    """
    prefix = vocab_words[0]
    prefixed_separator = " :: " + prefix
    return prefixed_separator.join(vocab_words)


def remove_suffix_ness(word: str) -> str:
    """Remove the 'ness' suffix from the word while keeping spelling in mind.

    Parameters:
        word: Word to remove suffix from.

    Returns:
        Word with suffix removed and spelling adjusted: a root ending in 'i'
        gets its original 'y' back.

    Examples:
        >>> remove_suffix_ness('heaviness')
        'heavy'

        >>> remove_suffix_ness('sadness')
        'sad'
    """
    suffix_length = len("ness")
    root = word[:-suffix_length]
    if root[-1] == "i":
        root = root[:-1] + "y"
    return root


def adjective_to_verb(sentence: str, index: int) -> str:
    """Change the adjective within the sentence to a verb.

    Parameters:
        sentence: The sentence containing the adjective.
        index: Position of the adjective among the words of the sentence.
            Negative values count from the end.

    Returns:
        The extracted adjective in verb form, i.e. with 'en' appended.

    Examples:
        >>> adjective_to_verb('It got dark as the sun set.', 2)
        'darken'

        >>> adjective_to_verb('The ink stains her fingers black.', -1)
        'blacken'
    """
    words = sentence.split()
    adjective = words[index].rstrip(".")
    return adjective + "en"
