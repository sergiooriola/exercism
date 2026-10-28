"""Generate random characters for a game of Dungeons & Dragons."""

import random


class Character:
    """A character with six random abilities and its hitpoints.

    Attributes:
        strength: The strength score, from 3 to 18.
        dexterity: The dexterity score, from 3 to 18.
        constitution: The constitution score, from 3 to 18.
        intelligence: The intelligence score, from 3 to 18.
        wisdom: The wisdom score, from 3 to 18.
        charisma: The charisma score, from 3 to 18.
        hitpoints: 10 plus the constitution modifier.
    """

    def __init__(self) -> None:
        """Roll the six abilities once and work out the hitpoints."""
        self.strength = self.ability()
        self.dexterity = self.ability()
        self.constitution = self.ability()
        self.intelligence = self.ability()
        self.wisdom = self.ability()
        self.charisma = self.ability()
        self.hitpoints = 10 + modifier(self.constitution)

    def ability(self) -> int:
        """Return a new ability score: four 6-sided dice, without the lowest.

        Returns:
            The sum of the three highest dice, from 3 to 18.
        """
        return sum(
            sorted(
                [random.randint(1, 6) for _ in range(4)],
                reverse=True,
            )[0:-1]
        )


def modifier(value: int) -> int:
    """Return the modifier of an ability score.

    Parameters:
        value: The ability score.

    Returns:
        The score minus 10, divided by 2 and rounded down.

    Examples:
        >>> modifier(3)
        -4
        >>> modifier(18)
        4
    """
    return (value - 10) // 2
