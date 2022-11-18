# CS 1400, HOMEWORK 5, file 2
# DUE: Thursday, 02/16/2018 at 11:59 pm

# NAME:       Jared Hansen
# A-NUMBER:   A01439768
# SECTION:    CS-1400-002
# RECITATION: CS-1400-515


# Problem 4_17

'''
DESCRIPTION: "Game: Rock-Paper-Scissors"

Write a program that plays rock paper scissors. (Rock smashes scissors,
scissors cut paper, paper wraps rock.)
The program randomly generates a number 0, 1, or 2 representing scissor, rock,
and paper. The program prompts the user to enter a number 0, 1, or 2, and
displays a message indicating whether the user or the computer wins, losses or
draws.

Example:
    scissors(0), rock(1), paper(2): user enters their choice
    The computer is scissor. You are rock. You won.

'''




# In order to get the computer's choice, we'll need to be able to randomly
# generate integers. As such, we'll need to import the "random" library.
import random as rand




# Define the three choices as integers
scissors = 0
rock = 1
paper = 2




# Generate the computer's choice
computerChoice = rand.randint(0,2)




# Get the user's choice of move
userChoice = eval(input("Enter 0 for scissors, 1 for rock, or 2 for paper: "))




# Figure out who wins, and what to display
# There's probably a more efficient way to get the desired result than how I
# did it, but hard-coding everything seemed to be the best way to go.

# User chooses scissors
if (userChoice == 0):
    if (computerChoice == 0):
        print("You chose scissors and the computer chose scissors. The result is a draw.")
    elif (computerChoice == 1):
        print("You chose scissors and the computer chose rock. The computer wins; the dominance of AI is imminent!")
    else:
        print("You chose scissors and the computer chose paper. You win.")
        
# User chooses rock
elif (userChoice == 1):
    if (computerChoice == 0):
        print("You chose rock and the computer chose scissors. You win.")
    elif (computerChoice == 1):
        print("You chose rock and the computer chose rock. The result is a draw.")
    else:
        print("You chose rock and the computer chose paper. The computer wins; the dominance of AI is imminent!")
        
# User chooses paper
else:
    if (computerChoice == 0):
        print("You chose paper and the computer chose scissors. The computer wins; the dominance of AI is imminent!")
    elif (computerChoice == 1):
        print("You chose paper and the computer chose rock. You win.")
    else:
        print("You chose paper and the computer chose paper. The result is a draw.")




# If using Windows command line, this is to let the user see the output
input("Press any key to continue")