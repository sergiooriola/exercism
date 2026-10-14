"""Functions for editing essay homework with string methods."""


def capitalize_title(title: str) -> str:
    """Capitalize the first letter of each word in the title.

    Parameters:
        title: Essay title that needs title casing.

    Returns:
        The title with every word starting in uppercase and the rest of
        each word in lowercase.

    Examples:
        >>> capitalize_title('canis familiaris')
        'Canis Familiaris'
    """
    return title.title()


def check_sentence_ending(sentence: str) -> bool:
    """Check whether the sentence ends with a period.

    Parameters:
        sentence: A sentence to check.

    Returns:
        True if the last character of the sentence is a period, False
        otherwise.

    Examples:
        >>> check_sentence_ending('Snails can sleep for 3 years.')
        True

        >>> check_sentence_ending('Snails can sleep for 3 years')
        False
    """
    return sentence.endswith(".")


def clean_up_spacing(sentence: str) -> str:
    """Remove leading and trailing whitespace from the sentence.

    Parameters:
        sentence: A sentence to clean up.

    Returns:
        The sentence without whitespace at either end.

    Examples:
        >>> clean_up_spacing('  Octopuses have three hearts.  ')
        'Octopuses have three hearts.'
    """
    return sentence.strip()


def replace_word_choice(sentence: str, old_word: str, new_word: str) -> str:
    """Replace a word in the sentence with a new one.

    Parameters:
        sentence: A sentence to replace words in.
        old_word: The word to replace.
        new_word: The replacement word.

    Returns:
        The sentence with every occurrence of the old word replaced by the
        new word.

    Examples:
        >>> replace_word_choice('Animals are cool.', 'cool', 'awesome')
        'Animals are awesome.'
    """
    return sentence.replace(old_word, new_word)
