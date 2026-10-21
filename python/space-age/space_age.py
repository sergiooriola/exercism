"""Calculate how old someone is on each planet of the Solar System."""

# One Earth year of 365.25 days, the length the exercise defines.
EARTH_YEAR_SECONDS: int = 31_557_600

# Time each planet takes to orbit the Sun, in Earth years.
ORBITAL_PERIODS: dict[str, float] = {
    "mercury": 0.2408467,
    "venus": 0.61519726,
    "earth": 1.0,
    "mars": 1.8808158,
    "jupiter": 11.862615,
    "saturn": 29.447498,
    "uranus": 84.016846,
    "neptune": 164.79132,
}


class SpaceAge:
    """An age in seconds, expressed in the years of each planet.

    Attributes:
        seconds: The age in seconds.

    Examples:
        >>> age = SpaceAge(1_000_000_000)
        >>> age.on_earth()
        31.69
        >>> age.on_mercury()
        131.57
    """

    def __init__(self, seconds: int) -> None:
        """Store the age in seconds.

        Parameters:
            seconds: The age in seconds.
        """
        self.seconds = seconds

    def _calculate_age(self, planet: str) -> float:
        """Return the age in years of the given planet.

        Parameters:
            planet: The lowercase name of the planet.

        Returns:
            The age in years of that planet, rounded to two decimals.
        """
        earth_years = self.seconds / EARTH_YEAR_SECONDS
        return round(earth_years / ORBITAL_PERIODS[planet], 2)

    def on_mercury(self) -> float:
        """Return the age in Mercury years, rounded to two decimals."""
        return self._calculate_age("mercury")

    def on_venus(self) -> float:
        """Return the age in Venus years, rounded to two decimals."""
        return self._calculate_age("venus")

    def on_earth(self) -> float:
        """Return the age in Earth years, rounded to two decimals."""
        return self._calculate_age("earth")

    def on_mars(self) -> float:
        """Return the age in Mars years, rounded to two decimals."""
        return self._calculate_age("mars")

    def on_jupiter(self) -> float:
        """Return the age in Jupiter years, rounded to two decimals."""
        return self._calculate_age("jupiter")

    def on_saturn(self) -> float:
        """Return the age in Saturn years, rounded to two decimals."""
        return self._calculate_age("saturn")

    def on_uranus(self) -> float:
        """Return the age in Uranus years, rounded to two decimals."""
        return self._calculate_age("uranus")

    def on_neptune(self) -> float:
        """Return the age in Neptune years, rounded to two decimals."""
        return self._calculate_age("neptune")
