# Decompose Single Strand DNA into 3 reading frames

"""
In genetics a reading frame is a way to divide a sequence of nucleotides (DNA bases) into a set of consecutive non-overlapping triplets (also called codon). Each of this triplets is translated into an amino-acid during a translation process to create proteins.

Input
In a single strand of DNA you find 3 Reading frames, take for example the following input sequence:

AGGTGACACCGCAAGCCTTATATTAGC
Output
For the output we are going to take the combinations and show them in the following manner:

Frame 1: AGG TGA CAC CGC AAG CCT TAT ATT AGC
Frame 2: A GGT GAC ACC GCA AGC CTT ATA TTA GC
Frame 3: AG GTG ACA CCG CAA GCC TTA TAT TAG C

"""

# My Solution

def decompose_single_strand(single_strand):
    frame1 = ' '.join([single_strand[i:i+3] for i in range(0, len(single_strand), 3)])
    frame2 = single_strand[0] + ' ' + ' '.join([single_strand[i:i+3] for i in range(1, len(single_strand), 3)])
    frame3 = single_strand[:2] + ' ' + ' '.join([single_strand[i:i+3] for i in range(2, len(single_strand), 3)])
    return f'Frame 1: {frame1}\nFrame 2: {frame2}\nFrame 3: {frame3}'

# Other Solution

def decompose_single_strand(dna):        
    return '\n'.join('Frame {}: {}'.format(k+1, frame(dna, k)) for k in range(3))
    
def frame(s, k):
    return ' '.join(([s[:k]] if k else []) + [s[i:i+3] for i in range(k, len(s), 3)])    


