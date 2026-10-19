"""Functions to help Azara and Rui locate pirate treasure."""

# A coordinate split into its number and its letter, such as ('2', 'A').
type SplitCoordinate = tuple[str, str]
# A treasure and its coordinate, such as ('Brass Spyglass', '4B').
type AzaraRecord = tuple[str, str]
# A location, its split coordinate and its quadrant.
type RuiRecord = tuple[str, SplitCoordinate, str]
# An Azara record followed by a Rui record with the same coordinate.
type CombinedRecord = tuple[str, str, str, SplitCoordinate, str]
# A combined record without the coordinate from Azara.
type CleanedRecord = tuple[str, str, SplitCoordinate, str]


def get_coordinate(record: AzaraRecord) -> str:
    """Get the coordinate of a treasure from the list of Azara.

    Parameters:
        record: A treasure and its coordinate.

    Returns:
        The coordinate of the treasure.

    Examples:
        >>> get_coordinate(('Brass Spyglass', '4B'))
        '4B'
    """
    return record[1]


def convert_coordinate(coordinate: str) -> SplitCoordinate:
    """Split a coordinate into its number and its letter.

    Parameters:
        coordinate: A coordinate of one digit and one letter.

    Returns:
        The number and the letter of the coordinate.

    Examples:
        >>> convert_coordinate('2A')
        ('2', 'A')
    """
    return (coordinate[0], coordinate[1])


def compare_records(azara_record: AzaraRecord, rui_record: RuiRecord) -> bool:
    """Check whether a treasure and a location have the same coordinate.

    Parameters:
        azara_record: A treasure and its coordinate.
        rui_record: A location, its split coordinate and its quadrant.

    Returns:
        True if both records have the same coordinate, False otherwise.

    Note:
        - The coordinate from Azara is split first, because Rui writes it split.

    Examples:
        >>> azara_record = ('Crystal Crab', '6A')
        >>> rui_record = ('Old Schooner', ('6', 'A'), 'Purple')
        >>> compare_records(azara_record, rui_record)
        True
        >>> compare_records(('Brass Spyglass', '4B'), rui_record)
        False
    """
    return convert_coordinate(azara_record[1]) == rui_record[1]


def create_record(
    azara_record: AzaraRecord, rui_record: RuiRecord
) -> CombinedRecord | str:
    """Combine a treasure and a location that have the same coordinate.

    Parameters:
        azara_record: A treasure and its coordinate.
        rui_record: A location, its split coordinate and its quadrant.

    Returns:
        The Azara record followed by the Rui record, or 'not a match' if their
        coordinates are different.

    Examples:
        >>> azara_record = ('Crystal Crab', '6A')
        >>> rui_record = ('Old Schooner', ('6', 'A'), 'Purple')
        >>> create_record(azara_record, rui_record)
        ('Crystal Crab', '6A', 'Old Schooner', ('6', 'A'), 'Purple')
        >>> create_record(('Brass Spyglass', '4B'), rui_record)
        'not a match'
    """
    if compare_records(azara_record, rui_record):
        return azara_record + rui_record
    return "not a match"


def _clean_up_record(combined_record: CombinedRecord) -> CleanedRecord:
    """Remove the coordinate from Azara from a combined record.

    Parameters:
        combined_record: A treasure and a location with the same coordinate.

    Returns:
        The treasure, the location, the split coordinate and the quadrant.

    Examples:
        >>> _clean_up_record(
        ...     ('Crystal Crab', '6A', 'Old Schooner', ('6', 'A'), 'Purple')
        ... )
        ('Crystal Crab', 'Old Schooner', ('6', 'A'), 'Purple')
    """
    return (
        combined_record[0],
        combined_record[2],
        combined_record[3],
        combined_record[4],
    )


def clean_up(combined_record_group: tuple[CombinedRecord, ...]) -> str:
    """Build a report with one cleaned record on each line.

    Parameters:
        combined_record_group: The combined records to report, in order.

    Returns:
        The cleaned records, each on its own line.

    Note:
        - Every line ends in a newline, including the last one.

    Examples:
        >>> combined_record_group = (
        ...     ('Crystal Crab', '6A', 'Old Schooner', ('6', 'A'), 'Purple'),
        ...     ('Robot Parrot', '1C', 'Seaside Cottages', ('1', 'C'), 'Blue'),
        ... )
        >>> print(clean_up(combined_record_group), end='')
        ('Crystal Crab', 'Old Schooner', ('6', 'A'), 'Purple')
        ('Robot Parrot', 'Seaside Cottages', ('1', 'C'), 'Blue')
    """
    return "".join(
        f"{_clean_up_record(combined_record)}\n"
        for combined_record in combined_record_group
    )
