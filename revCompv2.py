import sys

# print reverse complement of a sequence provided.

# define temporary sequence variable for input value from command line/terminal
seq = sys.argv[1]

# define empty list that will be populated with reverse complement of each nucleotide in seq

rc_seq = []

# write a for loop to iterate through all of the nucleotides in seq

for nuc in seq:
    if nuc == 'A':
        # use append method to add new elements to list
        rc_seq.append('T')
    elif nuc == 'T':
        rc_seq.append('A')
    elif nuc == 'G':
        rc_seq.append('C')
    elif nuc == 'C':
        rc_seq.append('G')
        
# use reverse method to reverse list
rc_seq.reverse()

# use join function to join elements of list into one string with empty brackets preceding to indicate no spaces or characters are to be placed between elements.
rc_seq = ''.join(rc_seq)
print('%s' % rc_seq)