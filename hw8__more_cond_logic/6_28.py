# CS 1400, HOMEWORK 8, file 2
# DUE: Thursday, 03/15/2018 at 11:59 pm

# NAME:       Jared Hansen
# A-NUMBER:   A01439768
# SECTION:    CS-1400-002
# RECITATION: CS-1400-515


# Problem 6_28



'''
PROGRAM TITLE: Craps Game

Craps is a popular dice game played in casinos. Write a program to play a variation of the
game as follows:

-- Roll two dice. (Each die has 6 faces with numbers 1,2,3,4,5,6.)
-- Check the sum of the two dice.
    -- If the sum is 2, 3, or 12 (called "craps") then you lose.
    -- If the sum is 7 or 11 (called "natural") then you win.
    -- If the sum is another value (4,5,6,8,9,10) a "point" is established.
-- Continue to roll the dice until either a 7 or the same point value is rolled.
    -- If 7 is rolled then you lose.
    -- Otherwise you win.


'''




# We'll need the random library to use the randint() function to generate our die rolls.
import random as rand




#       My initial thought was to have a separate function for the initial roll, the
# "point roll", and any other subsequent rolls, but this didn't make any sense. Since all
# the rolls are simply returning the sum of the roll of two dice it just makes sense to have
# one function to generate an individual die roll.
def roll():
    num = 0
    num = rand.randint(1,6)
    return num




# I just use this function to print the roll of the two dice and their sum.
def printRoll(rollA, rollB):
    total = rollA + rollB
    print("You rolled ", rollA, " + ", rollB, " = ", total, sep = "")




#       The main function contains all the logic of the game. I didn't think there was really
# a better place to put it (i.e. some other function) so I just put it here.
#       Also, the logic is self-explanatory, so I won't make the code look all messy by
# commenting what's happening within this function.
def main():

    rollOneA = roll()
    rollOneB = roll()
    rollOneTotal = rollOneA + rollOneB

    printRoll(rollOneA, rollOneB)
    if ( (rollOneTotal == 7) or (rollOneTotal == 11) ):
        print("Congrats, you win!")
    elif ( (rollOneTotal == 2) or (rollOneTotal == 3) or (rollOneTotal == 12) ):
        print("Sorry, you lose.")
    else:
        currentRoll = 0
        while ( (currentRoll != rollOneTotal) and (currentRoll != 7) ):
            print("You neither won nor lost. Keep rolling until you either match", rollOneTotal, "or roll a 7.")
            rollNum1 = roll()
            rollNum2 = roll()
            currentRoll = (rollNum1 + rollNum2)
            printRoll(rollNum1, rollNum2)

        if(currentRoll == rollOneTotal):
            print("Congrats, you rolled", rollOneTotal, "again. You win!")
        else:
            print("Sorry. You rolled a 7, so you lose.")




# Call the main function
main()




input("\nPress any key to continue")