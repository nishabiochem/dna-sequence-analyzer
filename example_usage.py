# example_usage.py
# This file shows how to use the functions from dna_tools.py

from dna_tools import count_bases, calculate_gc, reverse_complement, translate_dna

# Test DNA sequence
dna = "ATGCGATCGATCGTAA"

print("Original DNA:", dna)
print()

print("1. Base counts:")
print(count_bases(dna))
print()

print("2. GC content:")
print(calculate_gc(dna), "%")
print()

print("3. Reverse complement:")
print(reverse_complement(dna))
print()

print("4. Translated protein:")
print(translate_dna(dna))
