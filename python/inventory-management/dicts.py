"""Functions to track and update an inventory of items."""


def create_inventory(items: list[str]) -> dict[str, int]:
    """Return an inventory with the number of times each item appears.

    Parameters:
        items: The items to count.

    Returns:
        A new inventory that maps each item to its count.

    Examples:
        >>> create_inventory(['coal', 'wood', 'wood'])
        {'coal': 1, 'wood': 2}
    """
    return add_items({}, items)


def add_items(inventory: dict[str, int], items: list[str]) -> dict[str, int]:
    """Add one to the count of each item in the list, in place.

    Parameters:
        inventory: The inventory to update.
        items: The items to add, once per appearance.

    Returns:
        The same inventory, with new items added at a count of 1.

    Examples:
        >>> add_items({'coal': 1}, ['wood', 'coal'])
        {'coal': 2, 'wood': 1}
    """
    for item in items:
        inventory[item] = inventory.get(item, 0) + 1
    return inventory


def decrement_items(inventory: dict[str, int], items: list[str]) -> dict[str, int]:
    """Subtract one from the count of each item in the list, in place.

    Parameters:
        inventory: The inventory to update.
        items: The items to subtract, once per appearance.

    Returns:
        The same inventory, with the counts decremented.

    Note:
        - Counts never drop below 0.
        - Items that are not in the inventory are ignored.

    Examples:
        >>> decrement_items({'coal': 1, 'iron': 2}, ['coal', 'coal', 'gold'])
        {'coal': 0, 'iron': 2}
    """
    for item in items:
        if inventory.get(item, 0) > 0:
            inventory[item] -= 1
    return inventory


def remove_item(inventory: dict[str, int], item: str) -> dict[str, int]:
    """Remove an item and its count from the inventory, in place.

    Parameters:
        inventory: The inventory to update.
        item: The item to remove.

    Returns:
        The same inventory, unchanged if the item was not in it.

    Examples:
        >>> remove_item({'coal': 2, 'wood': 1}, 'coal')
        {'wood': 1}
        >>> remove_item({'wood': 1}, 'gold')
        {'wood': 1}
    """
    inventory.pop(item, "Unknown")
    return inventory


def list_inventory(inventory: dict[str, int]) -> list[tuple[str, int]]:
    """Return the items that are available, with their counts.

    Parameters:
        inventory: The inventory to list.

    Returns:
        A list of (item, count) pairs whose count is greater than 0.

    Examples:
        >>> list_inventory({'coal': 7, 'silver': 0, 'wood': 11})
        [('coal', 7), ('wood', 11)]
    """
    return [(item, count) for item, count in inventory.items() if count > 0]
