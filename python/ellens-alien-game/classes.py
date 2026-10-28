"""The aliens the player fights in Ellen's game."""


class Alien:
    """An alien with a position on the board and some health points.

    Attributes:
        total_aliens_created: The number of aliens created so far, shared by
            all of them.
        x_coordinate: The position of the alien on the x-axis.
        y_coordinate: The position of the alien on the y-axis.
        health: The health points the alien has left. It starts at 3.

    Examples:
        >>> alien = Alien(2, 0)
        >>> alien.hit()
        >>> alien.health, alien.is_alive()
        (2, True)
    """

    total_aliens_created = 0

    def __init__(self, x_coordinate: int, y_coordinate: int) -> None:
        """Create an alien at the given position, with full health.

        Parameters:
            x_coordinate: The starting position on the x-axis.
            y_coordinate: The starting position on the y-axis.
        """
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        self.health = 3
        Alien.total_aliens_created += 1

    def hit(self) -> None:
        """Take one health point away from the alien.

        Health can go below 0 if the alien keeps being hit.
        """
        self.health -= 1

    def is_alive(self) -> bool:
        """Return whether the alien has any health points left."""
        return self.health > 0

    def teleport(self, new_x_coordinate: int, new_y_coordinate: int) -> None:
        """Move the alien to a new position.

        Parameters:
            new_x_coordinate: The new position on the x-axis.
            new_y_coordinate: The new position on the y-axis.
        """
        self.x_coordinate = new_x_coordinate
        self.y_coordinate = new_y_coordinate

    def collision_detection(self, collidable_object: object) -> None:
        """Detect a collision with another object.

        Not implemented yet: Ellen will add the algorithm later.

        Parameters:
            collidable_object: The object the alien may have collided with.
        """


def new_aliens_collection(positions: list[tuple[int, int]]) -> list[Alien]:
    """Create one alien at each of the given positions.

    Parameters:
        positions: The starting (x, y) position of each alien.

    Returns:
        A list with the new aliens, in the same order as the positions.

    Examples:
        >>> aliens = new_aliens_collection([(4, 7), (-1, 0)])
        >>> [(alien.x_coordinate, alien.y_coordinate) for alien in aliens]
        [(4, 7), (-1, 0)]
    """
    return [
        Alien(x_coordinate, y_coordinate) for x_coordinate, y_coordinate in positions
    ]
