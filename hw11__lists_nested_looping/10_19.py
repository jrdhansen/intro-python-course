# CS 1400, HOMEWORK 11, file 1
# DUE: Thursday, 04/12/2018 at 11:59 pm

# NAME:       Jared Hansen
# A-NUMBER:   A01439768
# SECTION:    CS-1400-002
# RECITATION: CS-1400-515





# Problem 10_19






'''
PROGRAM TITLE: "Game: bean machine"

The bean machine, also known as a quincunx or the Galton Box, is a device for statistics experiments named after English
scientist Sir Francis Galton. It consists of an upright board with evenly spaced nails (or pegs) in a triangular pattern.

Balls are dropped from the opening of the board. Every time a ball hits a nail, it has a 50% chance of falling to the left or
to the right. The piles of balls are accumulated in the slots at the bottom of the board.



Write a program that simulates the bean machine. Your program should prompt the user to enter the number of balls and the 
number of slots in the machine. Simulate the falling of each ball by printing its path. For example, LLRRLLR could represent
the path of a ball that took 7 steps to get to the bottom. Display the final buildup of the balls in the slots in a histogram.

Here is a sample run of the program:
    -- Enter the number of balls to drop: 5
    -- Enter the number of slots in the bean machine: 7
    
    LRLRLRR
    RRLLLRR
    LLRLLRR
    RRLLLLL
    LRLRRLR
    
    
      O
      O
    OOO

'''
















#=================#
#=================#
# NOTE FOR GRADER #
#=================#
#=================#
'''
#       The diagram from the prompt and the sample output from the prompt conflict with each other.
#       Per the diagram, if there are 8 slots then it should take a ball 7 moves to get into one slot.
# In that case, when the user specifies n slots then it should take a ball (n-1) moves to get into a slot.
#       However, per the sample output, the user specifies 7 slots and it shows the balls taking 7 moves
# to get into a slot.
#       Because the diagram is right there in front of my eyes and makes more sense, I'm going to go that
# route. I am assuming that if a user specifies n slots then it takes (n-1) moves for a ball to reach a
# slot.


Here is an example
# If the user inputs that there be 6=n slots at the bottom, it takes each ball 5=(n-1) moves to make it into
one slot.
# In this example there are 11 balls that were dropped through the pegboard.


     | |
    / . \
   / . . \
  / . . . \
 / . . . . \ 
/ . . . . . \
| | | |o| | |
| | | |o| | |
| |o| |o|o| |
|o|o|o|o|o|o|

'''





















# We'll use this library to generate random ints to simulate an 'L' move and an 'R' move at each peg.
import random as rand




# This function just returns either a 0 or a 1 to simulate movement at a peg.
def moveAtPeg():
    return rand.randint(0,1)




# Gives graphical output based on the user's input (I also included the pegboard as well as the histogram
# part. I wanted to print it for fun, so I figured I might as well include it.)
def printResults(listOfNumBallsPerSlot, numSlots):

    # This chunk of code prints the top of the pegboard machine.
    print(" "*(numSlots-2), "| |")
    for i in range(1, numSlots):
        print(" "*(numSlots-(i+1)), "/", " ."*i, " \\", sep = "")

    # This chunk of code prints the "histogram" part, showing where the balls ended up.
    for i in range(max(listOfNumBallsPerSlot), 0, -1):
        for j in range(len(listOfNumBallsPerSlot)):
            if ((listOfNumBallsPerSlot[j] >= i) and ((j+1) == len(listOfNumBallsPerSlot))):
                print("|O|", sep = "", end = "")
            elif (listOfNumBallsPerSlot[j] >= i):
                print("|O", sep = "", end = "")
            elif ((listOfNumBallsPerSlot[j]) < i and ((j+1) == len(listOfNumBallsPerSlot))):
                print("| |", sep = "", end = "")
            else:
                print("| ", sep = "", end = "")
        print()










# main function definition
def main():


    # Initialize these variables to 0 to avoid any problems when using them later.
    numBallsToDrop = 0
    numSlots = 0


    # Make sure the user is entering valid values for the number of balls and the number of slots.
    while ((numBallsToDrop <= 0) or (numBallsToDrop%1 != 0) or (numSlots <= 0) or (numSlots%1 != 0)):
        numBallsToDrop = eval(input("Enter the number of balls to drop: "))
        numSlots = eval(input("Enter the number of slots in the machine: "))


    # Initialize some important variables that will be used throughout the program.
    numMovesTotal = ((numBallsToDrop)*(numSlots-1))
    allMovesMade = [None]*numMovesTotal 


    # Each of these ballPath lists will contain the path of one ball going through the machine.
    # (We create as many lists as there are balls to be dropped.)
    ballPath = []
    for i in range(numBallsToDrop):
        ballPath.append([])


    # This list will keep track of the number of balls in each slot of the machine.
    ballsInSlot = [0]*(numSlots)


    # Determine what the list 'numMovesTotal' is in terms of "L" and "R" instead of 0's and 1's.
    for i in range(0, numMovesTotal):
        if(moveAtPeg() == 0):
            allMovesMade[i] = "L"
        else:
            allMovesMade[i] = "R"


    # This chunk of code does the following:
    #   -- breaks the list of 'allMovesMade' into separate lists for the path of each ball.
    #   -- prints the path for each individual ball.
    #   -- determines the number of balls that end up in each slot at the bottom.
    for i in range(len(ballPath)):
        startIndex = (i*(numSlots-1))
        endIndex = (startIndex+(numSlots-1))
        ballPath[i] = allMovesMade[startIndex:endIndex]
        print("---".join(ballPath[i]))

        lateralMovesToTheRight = 0
        for j in range(numSlots-1):
            if (ballPath[i][j] == "R"):
                lateralMovesToTheRight += 1
        ballsInSlot[lateralMovesToTheRight] += 1
    print()


    # Call this function to get graphical representation of the simulation.
    printResults(ballsInSlot, numSlots)







# call the main function
main()