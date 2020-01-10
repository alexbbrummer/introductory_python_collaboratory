# This is the main text of our first script.

# To pass arguments from outside script (command line/terminal) to inside of script add a call to import the 'sys' module (or library).

import sys

# Next, we need to replace the temporary parameter "seq" with sys.argv[1].  The argv list refers to the variables associated with this file to be read when we run the script.

seq = sys.argv[1]

if seq.startswith("ATC"):
    print(seq.count('T')/len(seq))
elif seq.startswith("AGC"):
    gcount = seq.count("G") - seq.count("AG")
    print('Starting with AGC', gcount)
else:
    print("Starting with neither ATC or AGC")
