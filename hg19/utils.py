from Bio import pairwise2
from Bio.SubsMat import MatrixInfo as matlist

import swalign

def pairwise2_local_alignment(base, seq):
    matrix = matlist.blosum62
    gap_open = -10
    gap_extend = -0.5
    alns = pairwise2.align.localds(base, seq, matrix, gap_open, gap_extend)
    return alns


def swalign_local_alignment(base, seq):
    #match = 2
    #mismatch = -1
    scoring = swalign.NucleotideScoringMatrix()
    sw = swalign.LocalAlignment(scoring)
    a = sw.align(seq, base)
    return {'q_pos': a.q_pos,
            'q_end': a.q_end,
            'r_end': a.r_end,
            'r_offset': a.r_offset,
            'r_pos': a.r_pos,
            'rc': a.rc,
            'ref': a.ref,
            'score': a.score,
           }
    #print alignment.matches, alignment.mismatches, alignment.orig_query, alignment.orig_ref, alignment.q_end, alignment.q_name, alignment.q_pos, alignment.query, alignment.r_end, alignment.r_name, alignment.r_offset, alignment.r_pos, alignment.r_region, alignment.rc, alignment.ref, alignment.score
    #print alignment.q_pos, alignment.matches, alignment.mismatches, alignment.r_offset, alignment.r_pos, alignment.r_region, alignment.rc, alignment.ref, alignment.score