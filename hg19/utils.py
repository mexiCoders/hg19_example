from Bio import pairwise2
from Bio.SubsMat import MatrixInfo as matlist

def local_alignment(base, seq):
    matrix = matlist.blosum62
    gap_open = -10
    gap_extend = -0.5
    alns = pairwise2.align.localds(base, seq, matrix, gap_open, gap_extend)
    return alns