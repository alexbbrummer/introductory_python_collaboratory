# This is the main text of our script.

# We are going to make a tip calculating script that will calculate the cost of a meal with tax and tip included.

# To pass arguments from outside script (command line/terminal) to inside of script add a call to import the 'sys' module (or library) and assign variable names to the numerical values for meal and tip with sys.argv[1] and sys.argv[2].  The argv list refers to the variables associated with this file to be read when we run the script.

import sys

# Define our meal, tax and tip variables.

# Add the float function to coerce the sys.argv[] values into floats.
meal = WHAT GOES HERE
tax = 0.075
tip = WHAT GOSE HERE

# Now calculate the cost of the meal including tax, and the cost of the meal including tip.




# Now, use the print function to print the final total into the command line/terminal.  But, our calculation might result in a value that has more than three decimal places.  So we use a special variation on the print function.   Using the % and f tells Python to insert a variable float into a printed string.  Placing '0.2' between the % and f tells Python to round to two decimal places.  An example is below

#print('Dinner plus tax and tip costs $%0.2f' % total)

# Finally, save the script file and execute as before.