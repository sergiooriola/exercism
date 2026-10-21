"""Translate RNA sequences into proteins."""

CODON_TO_AMINO_ACID: dict[str, str] = {
    "AUG": "Methionine",
    "UUU": "Phenylalanine",
    "UUC": "Phenylalanine",
    "UUA": "Leucine",
    "UUG": "Leucine",
    "UCU": "Serine",
    "UCC": "Serine",
    "UCA": "Serine",
    "UCG": "Serine",
    "UAU": "Tyrosine",
    "UAC": "Tyrosine",
    "UGU": "Cysteine",
    "UGC": "Cysteine",
    "UGG": "Tryptophan",
    "UAA": "STOP",
    "UAG": "STOP",
    "UGA": "STOP",
}

CODON_LENGTH = 3


def proteins(strand: str) -> list[str]:
    """Return the amino acids that an RNA strand translates into.

    Parameters:
        strand: The RNA sequence, read three nucleotides (one codon) at a time.

    Returns:
        The amino acids in order, up to the first STOP codon.

    Raises:
        KeyError: If the strand contains an unknown or incomplete codon.

    Examples:
        >>> proteins('AUGUUUUCU')
        ['Methionine', 'Phenylalanine', 'Serine']
        >>> proteins('AUGUAAUUU')
        ['Methionine']
    """
    protein: list[str] = []
    for i in range(0, len(strand), CODON_LENGTH):
        amino_acid = CODON_TO_AMINO_ACID[strand[i : i + CODON_LENGTH]]
        if amino_acid == "STOP":
            break
        protein.append(amino_acid)
    return protein
