"""Functions for calculating steps in exchanging currency."""


def exchange_money(budget: float, exchange_rate: float) -> float:
    """Calculate estimated value after exchange.

    Parameters:
        budget: The amount of money you are planning to exchange.
        exchange_rate: The unit value of the foreign currency.

    Returns:
        The exchanged value of the foreign currency you can receive.

    Examples:
        >>> exchange_money(127.5, 1.2)
        106.25
    """
    return budget / exchange_rate


def get_change(budget: float, exchanging_value: float) -> float:
    """Calculate currency left after an exchange.

    Parameters:
        budget: The amount of money you own.
        exchanging_value: The amount of your money you want to exchange now.

    Returns:
        The amount left of your starting currency after the exchange.

    Examples:
        >>> get_change(127.5, 120.0)
        7.5

        >>> get_change(300.75, 150.25)
        150.5
    """
    return budget - exchanging_value


def get_value_of_bills(denomination: int, number_of_bills: int) -> int:
    """Calculate the total value of currency at current denomination.

    Parameters:
        denomination: The value of a single unit (bill).
        number_of_bills: The total number of units (bills).

    Returns:
        The calculated value of the units (bills).

    Examples:
        >>> get_value_of_bills(5, 128)
        640
    """
    return denomination * number_of_bills


def get_number_of_bills(amount: float, denomination: int) -> int:
    """Calculate the number of currency units (bills) within the amount.

    Parameters:
        amount: The total starting value.
        denomination: The value of a single unit (bill).

    Returns:
        The number of whole units (bills) that can be obtained from the amount.

    Examples:
        >>> get_number_of_bills(127.5, 5)
        25

        >>> get_number_of_bills(35.16, 10)
        3
    """
    return int(amount // denomination)


def get_leftover_of_bills(amount: float, denomination: int) -> float:
    """Calculate leftover amount after exchanging into bills.

    Parameters:
        amount: The total starting value.
        denomination: The value of a single unit (bill).

    Returns:
        The amount that is "leftover", given the current denomination.

    Examples:
        >>> get_leftover_of_bills(127.5, 20)
        7.5
    """
    return amount % denomination


def exchangeable_value(
    budget: float, exchange_rate: float, spread: int, denomination: int
) -> int:
    """Calculate the maximum value of the new currency.

    Parameters:
        budget: The amount of your money you are planning to exchange.
        exchange_rate: The unit value of the foreign currency.
        spread: The percentage that is taken as an exchange fee.
        denomination: The value of a single unit (bill).

    Returns:
        The maximum value you can get in the new currency, in whole bills.

    Examples:
        >>> exchangeable_value(127.25, 1.20, 10, 20)
        80

        >>> exchangeable_value(127.25, 1.20, 10, 5)
        95
    """
    final_exchange_rate = exchange_rate + exchange_rate * (spread / 100)
    money_exchanged = exchange_money(budget, final_exchange_rate)
    number_of_bills = get_number_of_bills(money_exchanged, denomination)
    return get_value_of_bills(denomination, number_of_bills)
