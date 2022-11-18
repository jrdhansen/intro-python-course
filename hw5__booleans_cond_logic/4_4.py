# CS 1400, HOMEWORK 5, file 1
# DUE: Thursday, 02/16/2018 at 11:59 pm

# NAME:       Jared Hansen
# A-NUMBER:   A01439768
# SECTION:    CS-1400-002
# RECITATION: CS-1400-515


# Problem 4_4

'''
DESCRIPTION: "Game: Learn Addition"

Write a program that generates two integers under 100 and prompts the user to
enter the sum of these two integers. The program then reports true if the
answer is correct, false otherwise.


'''


############  The instructions say "integers under 100." This technically could
### NOTE ###  be 100, 99, 98, ..... all the way to negative infinity, which
############  wouldn't make much sense. As such, I'm going to have the integers
############  for the program be in the inclusive interval [0,1,2,....99,100]


# In order to generate the two integers under 100 we need to have access to
# functions that will generate random numbers.
# As such, we'll import the "random" library and give it an alias.
import random as rand




# The randint(a,b) function will generate a random integer that is somewhere in
# the inclusive interval [a,....,b]
int1 = rand.randint(0,100)
int2 = rand.randint(0,100)
trueSum = int1 + int2




print("\nType your answer to the following question: ", end = "")
userSum = eval(input("{} + {} = ".format(int1, int2)))




# determine if the user is correct
    # display the veracity of their answer
if (userSum == trueSum):
    print("\nYour answer is true. Congratulations on being able to perform simple addition.\nThis skill will greatly enhance your life.")
else:
    print("\nYour answer is false. Please work on your addition skills.\nThe world is a cruel place, and will eat you alive.")
    
    
    
    
# If using Windows command line, this is to let the user see the output
input("Press any key to continue")