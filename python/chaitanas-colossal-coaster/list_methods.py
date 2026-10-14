"""Functions for managing the queues at Chaitana's roller coaster."""

EXPRESS_TICKET = 1
NORMAL_TICKET = 0


def add_me_to_the_queue(
    express_queue: list[str],
    normal_queue: list[str],
    ticket_type: int,
    person_name: str,
) -> list[str]:
    """Add a person to the express or the normal queue, based on their ticket.

    Parameters:
        express_queue: The names in the express (fast-track) queue.
        normal_queue: The names in the normal queue.
        ticket_type: EXPRESS_TICKET for the express queue; any other value,
            such as NORMAL_TICKET, for the normal queue.
        person_name: The name of the person to add.

    Returns:
        The queue the name was added to, modified in place.

    Examples:
        >>> add_me_to_the_queue(['Tony'], ['WW'], EXPRESS_TICKET, 'RichieRich')
        ['Tony', 'RichieRich']

        >>> add_me_to_the_queue(['Tony'], ['WW'], NORMAL_TICKET, 'HawkEye')
        ['WW', 'HawkEye']
    """
    target_queue = express_queue if ticket_type == EXPRESS_TICKET else normal_queue
    target_queue.append(person_name)
    return target_queue


def find_my_friend(queue: list[str], friend_name: str) -> int:
    """Find the position of a friend in the queue.

    Parameters:
        queue: The names in the queue.
        friend_name: The name of the friend to find.

    Returns:
        The index of the first occurrence of the name.

    Raises:
        ValueError: If the name is not in the queue.

    Examples:
        >>> find_my_friend(['Natasha', 'Steve', 'Wanda'], 'Steve')
        1
    """
    return queue.index(friend_name)


def add_me_with_my_friends(queue: list[str], index: int, person_name: str) -> list[str]:
    """Insert a late arrival's name at a specific position of the queue.

    Parameters:
        queue: The names in the queue.
        index: The position at which to add the new name.
        person_name: The name to add.

    Returns:
        The same queue with the name inserted, modified in place.

    Examples:
        >>> add_me_with_my_friends(['Natasha', 'Steve'], 1, 'Bucky')
        ['Natasha', 'Bucky', 'Steve']
    """
    queue.insert(index, person_name)
    return queue


def remove_the_mean_person(queue: list[str], person_name: str) -> list[str]:
    """Remove the mean person from the queue.

    Parameters:
        queue: The names in the queue.
        person_name: The name of the mean person.

    Returns:
        The same queue without the first occurrence of the name, modified
        in place.

    Raises:
        ValueError: If the name is not in the queue.

    Examples:
        >>> remove_the_mean_person(['Natasha', 'Eltran', 'Wanda'], 'Eltran')
        ['Natasha', 'Wanda']
    """
    queue.remove(person_name)
    return queue


def how_many_namefellows(queue: list[str], person_name: str) -> int:
    """Count how many times a name appears in the queue.

    Parameters:
        queue: The names in the queue.
        person_name: The name to count.

    Returns:
        The number of times the name appears in the queue.

    Examples:
        >>> how_many_namefellows(['Natasha', 'Steve', 'Natasha'], 'Natasha')
        2
    """
    return queue.count(person_name)


def remove_the_last_person(queue: list[str]) -> str:
    """Remove the last person from the queue.

    Parameters:
        queue: The names in the queue, modified in place.

    Returns:
        The name that was removed from the end of the queue.

    Raises:
        IndexError: If the queue is empty.

    Examples:
        >>> remove_the_last_person(['Natasha', 'Steve', 'Rocket'])
        'Rocket'
    """
    return queue.pop()


def sorted_names(queue: list[str]) -> list[str]:
    """Sort the names in the queue alphabetically.

    Parameters:
        queue: The names in the queue, which is left unchanged.

    Returns:
        A new list with the names in alphabetical order.

    Examples:
        >>> sorted_names(['Steve', 'Natasha', 'Rocket'])
        ['Natasha', 'Rocket', 'Steve']
    """
    return sorted(queue)
