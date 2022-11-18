# CS 1400, HOMEWORK 6, file 1
# DUE: Thursday, 02/23/2018 at 11:59 pm

# NAME:       Jared Hansen
# A-NUMBER:   A01439768
# SECTION:    CS-1400-002
# RECITATION: CS-1400-515


# Problem 5_34

'''
DESCRIPTION: "Game: Lottery"

Revise Listing 4.10, lottery.py, to generate a lottery of a two-digit number. The two digits
in the number are distinct. (Hint: generate the first digit. Use a loop to continuously
generate the second digit until it is different from the first digit.)

Note: You need to add logic to lottery.py to make sure the lottery number digits are not the
same.  For example, you cannot generate 44 as a lottery number because both digits are the
same.  Notice the hint above: (Hint: Generate the first digit.  Use a loop to continuously
generate the second digit until it is different from the first digit.)


'''


# we'll be randomly generating numbers, so we'll need this library
import random


# generate digits of the numbers; if we're dealing with only two-digit numbers,
#       then we need a number between 1 and 9 (instead of 0 and 9 like the ones digit)
lottoTensDigit = random.randint(1,9)
lottoOnesDigit = random.randint(0,9)


# check to see if the ones digit and the tens digit have the same value; if so, then we
# keep generating new ones digits until we get one that is not-equal to the tens digit.
while (lottoOnesDigit == lottoTensDigit):
    digitOnes = random.randint(0, 9)


# Since we only have the tens digit, multiply it by 10 and then add the ones digit to get
#   the final two-unequal-digits lottery number
finalNum = (lottoTensDigit*10) + (lottoOnesDigit)


########## To test the program manually, just un-comment the line of code below so you can see the
## NOTE ## randomly-picked lottery number and can test the logic of the if-elif-else block.
##########
# print("The final lottery number is:", finalNum)


# Prompt the user to enter a guess
userGuess = eval(input("Enter your lottery pick (two digits): "))


# Turn the user's guess into a "tens digit value" and a "ones digit value"
userTensDigit = userGuess//10
userOnesDigit = userGuess%10


print("The final lottery number is:", finalNum)


# Check the guess, and reward them accordingly
if (userGuess == finalNum):
    print("Exact match: you win $10,000!!")
elif( (userTensDigit == lottoOnesDigit) and (userOnesDigit == lottoTensDigit) ):
    print("You matched both digits, but not an exact match. You win $3,000!")
elif( (lottoOnesDigit == userOnesDigit) or
      (lottoOnesDigit == userTensDigit) or
      (lottoTensDigit == userOnesDigit) or
      (lottoTensDigit == userTensDigit)):
    print("You matched one digit. You win $1,000!")
else:
    print("You had no matches whatsoever. Quit gambling before you're a broke, homeless bum.")



input("Press any key to continue")