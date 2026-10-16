"""Functions for comparing DNA strands."""


def distance(strand_a: str, strand_b: str) -> int:
    """Calculate the Hamming distance between two DNA strands.

    Parameters:
        strand_a: The first DNA strand.
        strand_b: The second DNA strand, as long as the first.

    Returns:
        The number of positions where the two strands have different
        nucleotides.

    Raises:
        ValueError: If the strands have different lengths.

    Examples:
        >>> distance('GAGCCTACTAACGGGAT', 'CATCGTAATGACGGCCT')
        7

        >>> distance('GGACG', 'GGACG')
        0
    """
    if len(strand_a) != len(strand_b):
        raise ValueError("Strands must be of equal length.")
    return sum(
        nucleotide_a != nucleotide_b
        for nucleotide_a, nucleotide_b in zip(strand_a, strand_b, strict=True)
    )
