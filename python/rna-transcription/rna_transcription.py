"""Functions for transcribing DNA strands into RNA."""

DNA_TO_RNA: dict[str, str] = {"G": "C", "C": "G", "T": "A", "A": "U"}


def to_rna(dna_strand: str) -> str:
    """Transcribe a DNA strand into its complementary RNA strand.

    Parameters:
        dna_strand: The DNA nucleotides, written with G, C, T and A.

    Returns:
        The RNA strand, with every nucleotide replaced by its complement:
        G by C, C by G, T by A and A by U.

    Raises:
        KeyError: If the strand contains a letter that is not a DNA
            nucleotide.

    Examples:
        >>> to_rna('ACGTGGTCTTAA')
        'UGCACCAGAAUU'

        >>> to_rna('')
        ''
    """
    return "".join(DNA_TO_RNA[nucleotide] for nucleotide in dna_strand)
