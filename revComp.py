import sys

# print reverse complement of a sequence provided.

# define temporary sequence variable for input value from command line/terminal
seq = sys.argv[1]

# define empty string that will be populated with reverse complement of each nucleotide in seq

rc_seq = ''

# write a for loop to iterate through all of the nucleotides in seq

for nuc in seq:
    if nuc == 'A':
        rc_seq = 'T' + rc_seq
    elif nuc == 'T':
        rc_seq = 'A' + rc_seq
    elif nuc == 'G':
        rc_seq = 'C' + rc_seq
    elif nuc == 'C':
        rc_seq = 'G' + rc_seq

print('%s' % rc_seq)