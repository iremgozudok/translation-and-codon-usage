from structures import *
from DNAToolkit import *
import random

randDNASeq = ''.join([random.choice(Nucleotides)
                      for nuc in range(50)])

DNAStr = validateSeq(randDNASeq)

print(f"\nSequence: {DNAStr}\n")
print(f"Sequence Lenght: {len(DNAStr)}\n")
print(f"Amino acid sequence from DNA :{translate_seq(DNAStr, 0)}\n" )
print(f"Codon usage :{codon_usage(DNAStr, 'L')}\n" )