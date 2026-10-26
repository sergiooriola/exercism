"""Functions for compiling dishes and ingredients for a catering company."""

from collections.abc import Iterable

from sets_categories_data import (
    ALCOHOLS,
    KETO,
    OMNIVORE,
    PALEO,
    SPECIAL_INGREDIENTS,
    VEGAN,
    VEGETARIAN,
)


def clean_ingredients(
    dish_name: str, dish_ingredients: list[str]
) -> tuple[str, set[str]]:
    """Remove the duplicated ingredients of a dish.

    Parameters:
        dish_name: The name of the dish.
        dish_ingredients: The ingredients of the dish, possibly repeated.

    Returns:
        A tuple with the name of the dish and the set of its ingredients.

    Examples:
        >>> clean_ingredients('Punch', ['lime', 'lime'])
        ('Punch', {'lime'})
    """
    return (dish_name, set(dish_ingredients))


def check_drinks(drink_name: str, drink_ingredients: list[str]) -> str:
    """Label a drink as a cocktail or a mocktail.

    Parameters:
        drink_name: The name of the drink.
        drink_ingredients: The ingredients of the drink.

    Returns:
        The name of the drink followed by 'Cocktail' if any ingredient is an
        alcohol, or by 'Mocktail' otherwise.

    Examples:
        >>> check_drinks('Mojito', ['rum', 'mint'])
        'Mojito Cocktail'
        >>> check_drinks('Lemonade', ['lemon', 'water'])
        'Lemonade Mocktail'
    """
    drink_type = "Mocktail" if ALCOHOLS.isdisjoint(drink_ingredients) else "Cocktail"
    return f"{drink_name} {drink_type}"


def categorize_dish(dish_name: str, dish_ingredients: set[str]) -> str:
    """Find the meal category of a dish.

    The categories are checked in this order, and a dish that fits several
    gets the first one: VEGAN, VEGETARIAN, PALEO, KETO and OMNIVORE.

    Parameters:
        dish_name: The name of the dish.
        dish_ingredients: The ingredients of the dish.

    Returns:
        The name of the dish followed by ': ' and its category.

    Raises:
        ValueError: If the dish does not fit any category.

    Examples:
        >>> categorize_dish('Tofu Bowl', {'tofu'})
        'Tofu Bowl: VEGAN'
    """
    if dish_ingredients.issubset(VEGAN):
        dish_category = "VEGAN"
    elif dish_ingredients.issubset(VEGETARIAN):
        dish_category = "VEGETARIAN"
    elif dish_ingredients.issubset(PALEO):
        dish_category = "PALEO"
    elif dish_ingredients.issubset(KETO):
        dish_category = "KETO"
    elif dish_ingredients.issubset(OMNIVORE):
        dish_category = "OMNIVORE"
    else:
        raise ValueError(f"Dish does not fit any category: {dish_name!r}")

    return f"{dish_name}: {dish_category}"


def tag_special_ingredients(
    dish: tuple[str, Iterable[str]],
) -> tuple[str, set[str]]:
    """Find the ingredients of a dish that need a special note.

    Parameters:
        dish: A tuple with the name of the dish and its ingredients.

    Returns:
        A tuple with the name of the dish and the set of its ingredients that
        are in SPECIAL_INGREDIENTS, such as allergens.

    Examples:
        >>> tag_special_ingredients(('Satay', ['peanuts', 'rice']))
        ('Satay', {'peanuts'})
    """
    return (dish[0], SPECIAL_INGREDIENTS.intersection(dish[1]))


def compile_ingredients(dishes: list[set[str]]) -> set[str]:
    """Combine the ingredients of all the dishes.

    Parameters:
        dishes: The set of ingredients of each dish.

    Returns:
        A set with every ingredient that appears in any dish.

    Examples:
        >>> sorted(compile_ingredients([{'rice', 'salt'}, {'salt', 'tofu'}]))
        ['rice', 'salt', 'tofu']
    """
    master_list: set[str] = set()
    for dish in dishes:
        master_list = master_list.union(dish)
    return master_list


def separate_appetizers(dishes: list[str], appetizers: list[str]) -> list[str]:
    """Remove the appetizers from a list of dishes.

    Either list may contain duplicates.

    Parameters:
        dishes: The names of the dishes.
        appetizers: The names of the appetizers.

    Returns:
        A list, in no particular order, of the dish names that are not
        appetizers, each one once.

    Examples:
        >>> separate_appetizers(['Soup', 'Soup', 'Fries'], ['Fries'])
        ['Soup']
    """
    return list(set(dishes).difference(appetizers))


def singleton_ingredients(dishes: list[set[str]], intersection: set[str]) -> set[str]:
    """Find the ingredients that appear in only one dish.

    Parameters:
        dishes: The set of ingredients of each dish in a category.
        intersection: The ingredients that appear in more than one dish of
            that category, such as VEGAN_INTERSECTIONS.

    Returns:
        A set with the ingredients that appear in a single dish.

    Examples:
        >>> dishes = [{'rice', 'salt'}, {'salt', 'tofu'}, {'lime', 'salt', 'tofu'}]
        >>> sorted(singleton_ingredients(dishes, {'salt', 'tofu'}))
        ['lime', 'rice']
    """
    return compile_ingredients(dishes).difference(intersection)
