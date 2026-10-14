"""Functions for predicting how Bob, a lackadaisical teenager, replies."""

RESPONSE_QUESTION = "Sure."
RESPONSE_YELL = "Whoa, chill out!"
RESPONSE_YELL_QUESTION = "Calm down, I know what I'm doing!"
RESPONSE_SILENCE = "Fine. Be that way!"
RESPONSE_ANYTHING_ELSE = "Whatever."


def response(hey_bob: str) -> str:
    """Determine what Bob replies to a remark.

    Parameters:
        hey_bob: What someone says to Bob.

    Returns:
        Bob's reply: one of the five fixed responses.

    Note:
        Whitespace at either end of the remark is ignored. A remark with
        nothing else is silence, one ending in a question mark is a
        question, and one whose letters are all uppercase is yelling.

    Examples:
        >>> response('How are you?')
        'Sure.'

        >>> response('WATCH OUT!')
        'Whoa, chill out!'

        >>> response('WHAT IS GOING ON?')
        "Calm down, I know what I'm doing!"

        >>> response('   ')
        'Fine. Be that way!'

        >>> response('Tom-ay-to, tom-aaaah-to.')
        'Whatever.'
    """
    clean_text = hey_bob.strip()
    is_question = clean_text.endswith("?")
    is_yelling = clean_text.isupper()
    if not clean_text:
        return RESPONSE_SILENCE
    elif is_question and is_yelling:
        return RESPONSE_YELL_QUESTION
    elif is_question:
        return RESPONSE_QUESTION
    elif is_yelling:
        return RESPONSE_YELL
    else:
        return RESPONSE_ANYTHING_ELSE
