"""Give factory robots random names that no other robot has."""

import random
import string
from typing import ClassVar


class Robot:
    """A robot with a unique random name, such as RX837.

    Attributes:
        robot_names: Every name given so far, shared by all the robots. Old
            names stay in it after a reset, so they are never given again.
        name: The current name of the robot.

    Examples:
        >>> robot = Robot()
        >>> old_name = robot.name
        >>> robot.reset()
        >>> robot.name != old_name
        True
    """

    robot_names: ClassVar[set[str]] = set()

    def __init__(self) -> None:
        """Create a robot with a new name."""
        self.reset()

    def reset(self) -> None:
        """Give the robot a new name that no robot has had before."""
        robot_name = _generate_name()
        while robot_name in Robot.robot_names:
            robot_name = _generate_name()

        self.name = robot_name
        Robot.robot_names.add(self.name)


def _generate_name() -> str:
    """Return a random name: two capital letters and three digits.

    The name may already be in use. Robot.reset checks that.
    """
    return "".join(
        [
            random.choice(string.ascii_uppercase),
            random.choice(string.ascii_uppercase),
            random.choice(string.digits),
            random.choice(string.digits),
            random.choice(string.digits),
        ]
    )
