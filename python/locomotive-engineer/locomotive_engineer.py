"""Functions that help the locomotive engineer keep track of the train."""

from collections.abc import Mapping


def get_list_of_wagons(*wagon_ids: int) -> list[int]:
    """Return the wagon IDs as a list.

    Parameters:
        *wagon_ids: Any number of wagon IDs.

    Returns:
        A list with the wagon IDs in the order given.

    Examples:
        >>> get_list_of_wagons(3, 1, 2)
        [3, 1, 2]
        >>> get_list_of_wagons()
        []
    """
    return list(wagon_ids)


def fix_list_of_wagons(
    each_wagons_id: list[int], missing_wagons: list[int]
) -> list[int]:
    """Fix the order of the wagons and add the missing ones.

    The first two wagons were placed at the front by mistake and the
    locomotive (ID 1) is the third one.

    Parameters:
        each_wagons_id: The wagon IDs in their current, wrong order.
        missing_wagons: The IDs of the wagons that were left out.

    Returns:
        A list with the locomotive first, then the missing wagons, then the
        rest of the train, and the two wagons from the front at the end.

    Raises:
        ValueError: If each_wagons_id has fewer than three wagons.

    Examples:
        >>> fix_list_of_wagons([2, 5, 1, 7, 4], [3, 6])
        [1, 3, 6, 7, 4, 2, 5]
    """
    first_wagon, second_wagon, locomotive, *rest = each_wagons_id
    return [locomotive, *missing_wagons, *rest, first_wagon, second_wagon]


def add_missing_stops(
    route: dict[str, str], **stops: str
) -> dict[str, str | list[str]]:
    """Add the stops to the route information.

    Parameters:
        route: The route information, such as its origin and destination.
        **stops: The stops, as keyword arguments in the order they are made.

    Returns:
        A new dict with the route information and a 'stops' key that holds
        the stops in order, or an empty list if there are none.

    Examples:
        >>> add_missing_stops({'from': 'Berlin'}, stop_1='Leipzig', stop_2='Hanover')
        {'from': 'Berlin', 'stops': ['Leipzig', 'Hanover']}
        >>> add_missing_stops({'from': 'Berlin'})
        {'from': 'Berlin', 'stops': []}
    """
    return {**route, "stops": list(stops.values())}


def extend_route_information(
    route: Mapping[str, object], more_route_information: Mapping[str, object]
) -> dict[str, object]:
    """Combine the route information with more information.

    Parameters:
        route: The route information.
        more_route_information: More information to add to the route.

    Returns:
        A new dict with both. If a key is in both, the value from
        more_route_information wins.

    Examples:
        >>> extend_route_information({'from': 'Berlin'}, {'length': '100'})
        {'from': 'Berlin', 'length': '100'}
    """
    return {**route, **more_route_information}


def fix_wagon_depot(
    wagons_rows: list[list[tuple[int, str]]],
) -> list[list[tuple[int, str]]]:
    """Rearrange the depot so that each row has one wagon of each color.

    Each wagon is an (ID, color) tuple, and each row of the depot holds the
    wagons of a single color. The fix swaps rows and columns.

    Parameters:
        wagons_rows: The rows of the depot, one row per color.

    Returns:
        The new rows, where row n holds the n-th wagon of every color.

    Raises:
        ValueError: If the rows do not all have the same length.

    Examples:
        >>> fix_wagon_depot([[(2, 'red'), (4, 'red')], [(5, 'blue'), (9, 'blue')]])
        [[(2, 'red'), (5, 'blue')], [(4, 'red'), (9, 'blue')]]
    """
    return [list(row) for row in zip(*wagons_rows, strict=True)]
