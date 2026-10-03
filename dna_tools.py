# dna_tools.py
# Basic DNA sequence analysis functions
# Written in pure Python (no Biopython)

def count_bases(dna):
    """
    Count the number of A, T, C, G bases in a DNA sequence.
    Returns a dictionary.
    """
    dna = dna.upper()  # Make sure all letters are uppercase
    counts = {
        "A": dna.count("A"),
        "T": dna.count("T"),
        "C": dna.count("C"),
        "G": dna.count("G")
    }
    return counts


def calculate_gc(dna):
    """
    Calculate GC content of a DNA sequence.
    Returns the percentage (float).
    """
    dna = dna.upper()
    total_bases = len(dna)
    
    if total_bases == 0:
        return 0.0
    
    g_count = dna.count("G")
    c_count = dna.count("C")
    
    gc_content = ((g_count + c_count) / total_bases) * 100
    return round(gc_content, 2)


def reverse_complement(dna):
    """
    Return the reverse complement of a DNA sequence.
    """
    dna = dna.upper()
    
    complement = {
        "A": "T",
        "T": "A",
        "C": "G",
        "G": "C"
    }
    
    # Create complement
    comp = ""
    for base in dna:
        if base in complement:
            comp += complement[base]
        else:
            comp += "N"  # For unknown bases
    
    # Reverse it
    reverse_comp = comp[::-1]
    return reverse_comp


def translate_dna(dna):
    """
    Translate a DNA sequence into a protein sequence.
    Uses the standard genetic code.
    Stops at the first stop codon.
    """
    dna = dna.upper()
    
    # Standard genetic code
    codon_table = {
        "ATA":"I", "ATC":"I", "ATT":"I", "ATG":"M",
        "ACA":"T", "ACC":"T", "ACG":"T", "ACT":"T",
        "AAC":"N", "AAT":"N", "AAA":"K", "AAG":"K",
        "AGC":"S", "AGT":"S", "AGA":"R", "AGG":"R",
        "CTA":"L", "CTC":"L", "CTG":"L", "CTT":"L",
        "CCA":"P", "CCC":"P", "CCG":"P", "CCT":"P",
        "CAC":"H", "CAT":"H", "CAA":"Q", "CAG":"Q",
        "CGA":"R", "CGC":"R", "CGG":"R", "CGT":"R",
        "GTA":"V", "GTC":"V", "GTG":"V", "GTT":"V",
        "GCA":"A", "GCC":"A", "GCG":"A", "GCT":"A",
        "GAC":"D", "GAT":"D", "GAA":"E", "GAG":"E",
        "GGA":"G", "GGC":"G", "GGG":"G", "GGT":"G",
        "TCA":"S", "TCC":"S", "TCG":"S", "TCT":"S",
        "TTC":"F", "TTT":"F", "TTA":"L", "TTG":"L",
        "TAC":"Y", "TAT":"Y", "TAA":"*", "TAG":"*",
        "TGC":"C", "TGT":"C", "TGA":"*", "TGG":"W",
    }
    
    protein = ""
    
    # Read DNA in steps of 3 (codons)
    for i in range(0, len(dna) - 2, 3):
        codon = dna[i:i+3]
        
        if codon in codon_table:
            amino_acid = codon_table[codon]
            
            if amino_acid == "*":  # Stop codon
                break
            
            protein += amino_acid
        else:
            protein += "X"  # Unknown codon
    
    return protein


# Simple test (this runs only if you run the file directly)
if __name__ == "__main__":
    test_dna = "ATGCGATCGATCGTAA"
    
    print("DNA Sequence:", test_dna)
    print("Base counts:", count_bases(test_dna))
    print("GC content:", calculate_gc(test_dna), "%")
    print("Reverse complement:", reverse_complement(test_dna))
    print("Protein:", translate_dna(test_dna))
