"""Keep a player's list of high scores in the Frogger arcade game."""


class HighScores:
    """The scores of one player, in the order they were added.

    Attributes:
        scores: The scores, from the first to the latest. The methods do not
            change this list.

    Examples:
        >>> high_scores = HighScores([40, 20, 40, 30])
        >>> high_scores.personal_top_three()
        [40, 40, 30]
        >>> high_scores.latest()
        30
    """

    def __init__(self, scores: list[int]) -> None:
        """Store the scores of a player.

        Parameters:
            scores: The scores, from the first to the latest.
        """
        self.scores = scores

    def personal_best(self) -> int:
        """Return the highest score."""
        return max(self.scores)

    def latest(self) -> int:
        """Return the last score added."""
        return self.scores[-1]

    def personal_top_three(self) -> list[int]:
        """Return the three highest scores, from highest to lowest.

        If there are fewer than three scores, return all of them.
        """
        return sorted(self.scores, reverse=True)[0:3]
