# CS 1400, HOMEWORK 6, file 3
# DUE: Thursday, 02/23/2018 at 11:59 pm

# NAME:       Jared Hansen
# A-NUMBER:   A01439768
# SECTION:    CS-1400-002
# RECITATION: CS-1400-515


# Problem 5_40

'''
DESCRIPTION: "Simulation: Heads or Tails"

Write a program that simulates flipping a coin one million times and displays
the numer of heads and tails.

'''


# We'll be using the randint() function to generate "flips", so we need to 
#   import the "random" library
import random


# Initialize the count of the number of heads and tails to 0
countHeads = 0
countTails = 0


# Use a for loop to generate 1,000,000 "flips." I'm letting 0's represent heads
#   and 1's represent tails
for i in range(1000000):
    
    flip = random.randint(0,1)
    
    if (flip == 0):
        countHeads += 1
    else:
        countTails += 1


# Print the results of the simulation
print("The number of heads is:", countHeads)
print("The number of tails is:", countTails)


input("Press any key to continue")