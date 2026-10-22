"""Manage the shopping carts and store inventory of the Mecha Munch app."""

from collections.abc import Iterable

# Each item mapped to its quantity (or 'Out of Stock'), its aisle and whether it
# needs refrigeration, such as {'Milk': [2, 'Aisle 2', True]}.
type StoreItems = dict[str, list[int | str | bool]]


def add_item(
    current_cart: dict[str, int], items_to_add: Iterable[str]
) -> dict[str, int]:
    """Add items to a shopping cart, in place.

    Parameters:
        current_cart: The cart, mapping each item to its quantity.
        items_to_add: The items to add, one unit per appearance.

    Returns:
        The same cart, with new items added at a quantity of 1.

    Examples:
        >>> add_item({'Apple': 1}, ['Apple', 'Kiwi', 'Apple'])
        {'Apple': 3, 'Kiwi': 1}
    """
    for item in items_to_add:
        current_cart[item] = current_cart.setdefault(item, 0) + 1
    return current_cart


def read_notes(notes: Iterable[str]) -> dict[str, int]:
    """Create a shopping cart from the items in the user's notes.

    Parameters:
        notes: The items written in the notes.

    Returns:
        A new cart with a quantity of 1 for each item, even if it is repeated.

    Examples:
        >>> read_notes(['Apple', 'Kiwi'])
        {'Apple': 1, 'Kiwi': 1}
    """
    return dict.fromkeys(notes, 1)


def update_recipes(
    ideas: dict[str, dict[str, int]],
    recipe_updates: Iterable[tuple[str, dict[str, int]]],
) -> dict[str, dict[str, int]]:
    """Add or replace recipes in the recipe ideas, in place.

    Parameters:
        ideas: The recipes, mapping each name to its ingredients and quantities.
        recipe_updates: Pairs of a recipe name and its ingredients. An existing
            recipe is replaced whole; a new one is added.

    Returns:
        The same recipe ideas, updated.

    Examples:
        >>> ideas = {'Toast': {'Bread': 1}}
        >>> update_recipes(ideas, [('Toast', {'Bread': 2, 'Butter': 1})])
        {'Toast': {'Bread': 2, 'Butter': 1}}
    """
    ideas.update(recipe_updates)
    return ideas


def sort_entries(cart: dict[str, int]) -> dict[str, int]:
    """Return a copy of a shopping cart sorted alphabetically by item.

    Parameters:
        cart: The cart, mapping each item to its quantity.

    Returns:
        A new cart with the same items in alphabetical order.

    Note:
        - The sort is case-sensitive: every uppercase letter comes before any
          lowercase one, so 'Zucchini' comes before 'apple'.

    Examples:
        >>> sort_entries({'Kiwi': 2, 'Apple': 1})
        {'Apple': 1, 'Kiwi': 2}
    """
    return dict(sorted(cart.items()))


def send_to_store(
    cart: dict[str, int], aisle_mapping: dict[str, list[str | bool]]
) -> StoreItems:
    """Build the fulfillment cart the store needs to prepare an order.

    Parameters:
        cart: The user's cart, mapping each item to its quantity.
        aisle_mapping: Each item mapped to its aisle and whether it needs
            refrigeration.

    Returns:
        A new dict mapping each item in the cart to its quantity, aisle and
        refrigeration flag, in reverse alphabetical order.

    Raises:
        KeyError: If an item in the cart is missing from the aisle mapping.

    Examples:
        >>> aisles = {'Apple': ['Aisle 4', False], 'Milk': ['Aisle 2', True]}
        >>> send_to_store({'Apple': 2, 'Milk': 1}, aisles)
        {'Milk': [1, 'Aisle 2', True], 'Apple': [2, 'Aisle 4', False]}
    """
    fulfillment_cart: StoreItems = {}
    for item in sorted(cart, reverse=True):
        fulfillment_cart[item] = [
            cart[item],
            aisle_mapping[item][0],
            aisle_mapping[item][1],
        ]

    return fulfillment_cart


def update_store_inventory(
    fulfillment_cart: StoreItems,
    store_inventory: StoreItems,
) -> StoreItems:
    """Subtract an order from the store inventory, in place.

    Parameters:
        fulfillment_cart: The order, as built by send_to_store().
        store_inventory: The stock of each item, in the same layout as the order.

    Returns:
        The same inventory, with 'Out of Stock' where an item runs out.

    Raises:
        KeyError: If an ordered item is missing from the store inventory.

    Note:
        - Ordering more units than the store has also leaves the item as
          'Out of Stock', with no warning about the missing units.
        - An item that is already 'Out of Stock' is left unchanged.

    Examples:
        >>> order = {'Milk': [2, 'Aisle 2', True]}
        >>> update_store_inventory(order, {'Milk': [5, 'Aisle 2', True]})
        {'Milk': [3, 'Aisle 2', True]}
        >>> update_store_inventory(order, {'Milk': [2, 'Aisle 2', True]})
        {'Milk': ['Out of Stock', 'Aisle 2', True]}
    """
    for item, order_details in fulfillment_cart.items():
        ordered_quantity = order_details[0]
        current_stock = store_inventory[item][0]

        if isinstance(ordered_quantity, int) and isinstance(current_stock, int):
            remaining = current_stock - ordered_quantity
            store_inventory[item][0] = remaining if remaining > 0 else "Out of Stock"

    return store_inventory
