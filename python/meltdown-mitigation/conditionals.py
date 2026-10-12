"""Functions to prevent a nuclear meltdown."""


def is_criticality_balanced(temperature: float, neutrons_emitted: float) -> bool:
    """Check whether the reactor is balanced in criticality.

    Parameters:
        temperature: The temperature value in kelvin.
        neutrons_emitted: The number of neutrons emitted per second.

    Returns:
        True if criticality is balanced, False otherwise.

    Note:
        A reactor is balanced in criticality if it satisfies all of these
        conditions:
            - The temperature is less than 800 K.
            - The number of neutrons emitted per second is greater than 500.
            - The product of temperature and neutrons emitted per second is
              less than 500000.
    """
    return (
        temperature < 800
        and neutrons_emitted > 500
        and temperature * neutrons_emitted < 500000
    )


def reactor_efficiency(
    voltage: float, current: float, theoretical_max_power: float
) -> str:
    """Assess reactor efficiency zone.

    Parameters:
        voltage: The voltage value.
        current: The current value.
        theoretical_max_power: The power level that corresponds to a 100%
            efficiency.

    Returns:
        One of 'green', 'orange', 'red' or 'black'.

    Note:
        Efficiency can be grouped into 4 bands:
            1. green -> efficiency of 80% or more,
            2. orange -> efficiency of less than 80% but at least 60%,
            3. red -> efficiency below 60%, but still 30% or more,
            4. black -> less than 30% efficient.

        The percentage value is calculated as
        (generated power / theoretical max power) * 100
        where generated power = voltage * current.
    """
    generated_power = voltage * current
    efficiency = (generated_power / theoretical_max_power) * 100
    if efficiency >= 80:
        return "green"
    elif efficiency >= 60:
        return "orange"
    elif efficiency >= 30:
        return "red"
    else:
        return "black"


def fail_safe(
    temperature: float, neutrons_produced_per_second: float, threshold: float
) -> str:
    """Assess and return status code for the reactor.

    Parameters:
        temperature: The value of the temperature in kelvin.
        neutrons_produced_per_second: The neutron flux.
        threshold: The threshold for the category.

    Returns:
        One of 'LOW', 'NORMAL' or 'DANGER'.

    Note:
        1. 'LOW' -> `temperature * neutrons per second` < 90% of `threshold`
        2. 'NORMAL' -> `temperature * neutrons per second` +/- 10% of `threshold`
        3. 'DANGER' -> `temperature * neutrons per second` is not in the
           above-stated ranges
    """
    criticality = temperature * neutrons_produced_per_second
    lower_limit = threshold * 0.9
    upper_limit = threshold * 1.1
    if criticality < lower_limit:
        return "LOW"
    elif criticality <= upper_limit:
        return "NORMAL"
    else:
        return "DANGER"
