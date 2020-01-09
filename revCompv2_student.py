import sys

# The script will print reverse complement of a sequence provided when run.  The objective is to use our knowledge of loops to "loop through" the nucleotide letters in a sequence and build a new sequence where each entry is the complement of the corresponding entry in the original sequence.  So, if the third nucleotide in our test sequence is an "A", then the new sequence should have a "T" in its place.  Finally, the sequence needs to be reversed in its orderdering.  Some suggested steps are provided below.

# Note that the major difference this time is that we will be saving our reverse complement nucleotides as list elements and using list methods to perform the task within our loop.

# define temporary sequence variable for input value from command line/terminal (remember to use the sys.argv[] command).


# define empty list that will be populated with reverse complement of each nucleotide in seq



# write a for loop to iterate through all of the nucleotides in seq






# Once your loop is complete, use the join method to join elements of list into one string with empty brackets preceding to indicate no spaces or characters are to be placed between elements.  This part is done since it is a wholly new method we have not yet seen.

rc_seq = ''.join(rc_seq)

# finally, print your rc_seq to the console.
