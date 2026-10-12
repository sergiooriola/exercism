"""Functions for implementing the rules of the classic arcade game Pac-Man."""


def eat_ghost(power_pellet_active: bool, touching_ghost: bool) -> bool:
    """Check whether Pac-Man can eat a ghost.

    Parameters:
        power_pellet_active: Whether the player has an active power pellet.
        touching_ghost: Whether the player is touching a ghost.

    Returns:
        True if the player can eat the ghost, False otherwise.
    """
    return power_pellet_active and touching_ghost


def score(touching_power_pellet: bool, touching_dot: bool) -> bool:
    """Check whether Pac-Man scores by eating a power pellet or a dot.

    Parameters:
        touching_power_pellet: Whether the player is touching a power pellet.
        touching_dot: Whether the player is touching a dot.

    Returns:
        True if the player has scored, False otherwise.
    """
    return touching_power_pellet or touching_dot


def lose(power_pellet_active: bool, touching_ghost: bool) -> bool:
    """Check whether Pac-Man loses by touching a ghost without a power pellet.

    Parameters:
        power_pellet_active: Whether the player has an active power pellet.
        touching_ghost: Whether the player is touching a ghost.

    Returns:
        True if the player has lost the game, False otherwise.
    """
    return touching_ghost and not power_pellet_active


def win(
    has_eaten_all_dots: bool, power_pellet_active: bool, touching_ghost: bool
) -> bool:
    """Check whether Pac-Man wins by eating all the dots without losing.

    Parameters:
        has_eaten_all_dots: Whether the player has eaten all the dots.
        power_pellet_active: Whether the player has an active power pellet.
        touching_ghost: Whether the player is touching a ghost.

    Returns:
        True if the player has won the game, False otherwise.
    """
    return has_eaten_all_dots and not lose(power_pellet_active, touching_ghost)
