from structures import *
from collections import Counter

# DNA validation
def validateSeq(dna_seq):
    tmpseq = dna_seq.upper()
    for nuc in tmpseq:
        if nuc not in Nucleotides:
            return False
    return tmpseq


def translate_seq(seq, init_pos=0):
    return [DNA_Codons[seq[pos:pos + 3]] for pos in range(init_pos, len(seq) - 2,3)]

def codon_usage(seq, aminoacid):
    # provides the frequency of each codon encoding a giving aminoacid in a DNA sequence
    tmpList = []
    for i in range(0, len(seq) - 2, 3):
        if DNA_Codons[seq[i: i + 3]] == aminoacid:
            tmpList.append(seq[i: i + 3])
    
    freqDict = dict(Counter(tmpList))
    totalWight = sum(freqDict.values())
    for seq in freqDict:
        freqDict[seq] = round(freqDict[seq] / totalWight, 2)
    return freqDict