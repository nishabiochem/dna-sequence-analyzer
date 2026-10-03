# DNA Sequence Analyzer

Simple Python tools to analyze DNA sequences.

This project provides basic functions to:
- Count the number of A, T, C, and G bases
- Calculate GC content
- Generate the reverse complement of a DNA sequence
- Translate a DNA sequence into a protein sequence (using the standard genetic code)
- Create simple visualizations of base composition

Built with pure Python (no external bioinformatics libraries in the first version).

---

## Features

- `count_bases(dna)` → Returns a dictionary with base counts
- `calculate_gc(dna)` → Returns GC content as a percentage
- `reverse_complement(dna)` → Returns the reverse complement
- `translate_dna(dna)` → Translates DNA to protein (stops at first stop codon)
- Simple bar chart visualization of base counts

---

## Requirements

- Python 3.8 or higher
- matplotlib (only needed for visualization)

Install matplotlib if you don't have it:

```bash
pip install matplotlib
