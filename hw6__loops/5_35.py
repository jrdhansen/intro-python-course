# CS 1400, HOMEWORK 6, file 2
# DUE: Thursday, 02/23/2018 at 11:59 pm

# NAME:       Jared Hansen
# A-NUMBER:   A01439768
# SECTION:    CS-1400-002
# RECITATION: CS-1400-515


# Problem 5_35

'''
DESCRIPTION: "Perfect Number"

A positive integer is called a perfect number if it is equal to the sum of all of its positive
divisors, excluding itself. For example, 6 is the first perfect number because 6 = 1 + 2 + 3.
The next is 28 = 14 + 7 + 4 + 2 + 1. There are four perfect numbers less than 10,000. Write a
program to find these four numbers.

'''



# We're going to test out all integers between 1 and 10,000. Based on the information given in
#   the problem description, we know that we could simply start the loop at 6, but I'm going to
#   start it at 1 for the sake of thoroughness.
for testNum in range(1, 10000, 1):
    
# Initialize the sum of the divisors to 0 for the given test number.
    sumOfDivisors = 0
    
# Try dividing each test number by all integers less than it.
# If the number divides into the test number evenly, add it to the running total of the sum of
#   the divisors for that test number.
    for divisor in range(1,testNum,1):
        if ((testNum%divisor) == 0):
            sumOfDivisors += divisor
            
# If the sum of the divisors for that number is equal to the number itself, then we have found
#   a perfect number. As such, print something to let the user know that we've found a perfect
#   number. No need for an else, since any number that doesn't fit this criterion is
#   inconsequential to us.
    if (sumOfDivisors == testNum):
        print("A perfect number is:", testNum)
        
        
        
input("Press any key to continue")