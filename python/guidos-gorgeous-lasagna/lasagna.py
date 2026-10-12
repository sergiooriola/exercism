"""Functions used in preparing Guido's gorgeous lasagna."""

EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2


def bake_time_remaining(elapsed_bake_time: int) -> int:
    """Calculate the bake time remaining.

    Parameters:
        elapsed_bake_time: The baking time already elapsed, in minutes.

    Returns:
        The remaining bake time in minutes, derived from `EXPECTED_BAKE_TIME`.
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time


def preparation_time_in_minutes(number_of_layers: int) -> int:
    """Calculate the preparation time.

    Parameters:
        number_of_layers: The number of layers in the lasagna.

    Returns:
        The preparation time in minutes.
    """
    return PREPARATION_TIME * number_of_layers


def elapsed_time_in_minutes(number_of_layers: int, elapsed_bake_time: int) -> int:
    """Calculate the total elapsed cooking time.

    Parameters:
        number_of_layers: The number of layers in the lasagna.
        elapsed_bake_time: The baking time already elapsed, in minutes.

    Returns:
        The total time spent preparing and baking, in minutes.
    """
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time
