"""Say what you say when you share two cookies."""


def two_fer(name: str = "you") -> str:
    """Return the sentence for giving away the extra cookie.

    Parameters:
        name: The name of the person who gets the cookie. Use the default,
            'you', when the name is unknown.

    Returns:
        The sentence that shares the cookies with that person.

    Examples:
        >>> two_fer('Alice')
        'One for Alice, one for me.'
        >>> two_fer()
        'One for you, one for me.'
    """
    return f"One for {name}, one for me."
