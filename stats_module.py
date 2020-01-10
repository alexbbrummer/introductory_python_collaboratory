# This file will be our homemade statistics module.  As with stand alone functions and scripts, always be sure you add comments to your code so that you and your colleagues will know what the code did.

# We are going to write a series of functions in this .py file that will later be read into Python as a module.  The first function we will write is a function that will print all the numbers in our list of data.

def printNums(numbers):
    for num in numbers:
        print(num)


# Next we will write a function that adds all the values in your list together.
        
def sumNums(numbers):
    # first initialize the total variable 
    total = 0
    for num in numbers:
    # now reassign total variable to itself plus each value from numbers
        total += num
    return total

# Now we will write a function that returns the mean average of a list of numbers, and it will call on our previous function to do so.
    
def averageNums(numbers):
    # use sumNums() to calculate sum
    sumOfNums = sumNums(numbers)
    # divide by length of numbers
    average = sumOfNums/len(numbers)
    return average

# Next we will write a function that returns the variance of a list of numbers, and it will call on our previous function to do so.
    
def varianceNums(numbers):
    # initialize variance list
    variance = [0]*len(numbers)
    # calculate average of list
    average = averageNums(numbers)
    for i in range(0,len(numbers)):
        # loop through initialized variance list and replace values with corresponding numbers list value - average squared.
        variance[i] = (numbers[i]-average)**2
    # calculate average of variance list
    variance = averageNums(variance)
    return(variance)
    
# Finally, we will write a function to calculate the standard deviation of a list of numbers, again calling on our previous function.
    
def stdDevNums(numbers):
    variance = varianceNums(numbers)
    return variance**0.5

