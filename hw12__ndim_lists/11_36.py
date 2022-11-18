# CS 1400, HOMEWORK 12, file 2
# DUE: Thursday, 04/19/2018 at 11:59 pm

# NAME:       Jared Hansen
# A-NUMBER:   A01439768
# SECTION:    CS-1400-002
# RECITATION: CS-1400-515




# Problem 11_36





'''
PROGRAM TITLE: "Simulation using Turtle: self-avoiding random walk"

A self-avoiding walk in a lattice is a path from one point to another that does not visit the same point twice. Self-avoiding
walks have applications in pysics, chemistry, and mathematics. They can be used to model chain-like entities such as solvents
and polymners.

Write a turtle program that displays a random path that starts from the center and ends:
    -- at a point on the boundary
    -- or at a dead-end point (avoiding self-intersection, surrounded by four points that have already been visited)
Assume the size of the lattice is 16x16.
'''






# We're definitely gonna need the old turtle library, so let's import it. 
import turtle
# We'll also need this library to randomly increment/decrement the turtle's coordinates.
import random as rand



# This function draw the path that the turtle will take. Uses the coordinates generated in the random
# walk algorithm.
def drawRandomWalk(coordsList):
    turtle.speed(1)
    turtle.color("red")
    turtle.pensize(4)
    turtle.pendown()
    print("len(coordsList):", len(coordsList))
    for i in range(len(coordsList)):
        turtle.goto(25*(coordsList[i][0]), 25*(coordsList[i][1]))



# This function prints the lattice on which we'll show the walk of the turtle.
# https://stackoverflow.com/questions/40186594/how-can-i-draw-a-grid-of-squares
def printLattice():
    loadWindow = turtle.Screen()
    turtle.penup()
    turtle.setpos(-85,220)
    turtle.pendown()
    turtle.write("See console for the coordinate list")
    turtle.speed(20)
    turtle.colormode(255)
    turtle.pensize(1)

    
    # The for loop below doesn't draw the bottom line so we have to do it manually
    turtle.penup()
    turtle.setpos(-200,-200)
    turtle.pendown()
    turtle.setpos(200,-200)
    
    # The for loop below doesn't draw the vertical right edge so we have to do it manually
    turtle.penup()
    turtle.setpos(200,-200)
    turtle.pendown()
    turtle.setpos(200,200)
    
    STEP = 25
    LENGTH = 400
    for i in range(0, LENGTH, STEP):
       turtle.penup()
       turtle.setpos(-LENGTH/2, LENGTH/2 - i)
       turtle.pendown()
       turtle.setpos(LENGTH/2, LENGTH/2 - i)
       turtle.penup()
       turtle.setpos(-LENGTH/2 + i, LENGTH/2)
       turtle.pendown()
       turtle.setpos(-LENGTH/2 + i, -LENGTH/2)
       
    # Have to move the turtle back to the center to start the random walk.
    turtle.penup()
    turtle.setpos(0,0)
    turtle.pendown()
       
       
      



# This function takes the current coordinate, moves 1 to the left, and appends the new coordinate to
# the coordinates list. Returns the coordinate list.
def moveLeft(currentCoord, coordsList):
    newCoord = [currentCoord[0]-1, currentCoord[1]]
    coordsList.append(newCoord)
    return coordsList
    

# This function takes the current coordinate, moves 1 above, and appends the new coordinate to the
# coordinate list. Returns the coordinate list.
def moveAbove(currentCoord, coordsList):
    newCoord = [currentCoord[0], currentCoord[1]+1]
    coordsList.append(newCoord)
    return coordsList
    

# This function takes the current coordinate, moves 1 to the right, and appends the new coordinate to
# the coordinates list. Returns the coordinate list.
def moveRight(currentCoord, coordsList):
    newCoord = [currentCoord[0]+1, currentCoord[1]]
    coordsList.append(newCoord)
    return coordsList


# This function takes the current coordinate, moves 1 below, and appends the new coordinate to the
# coordinate list. Return the coordinate list.
def moveBelow(currentCoord, coordsList):
    newCoord = [currentCoord[0], currentCoord[1]-1]
    coordsList.append(newCoord)
    return coordsList







# main() fctn definition. This is where the magic happens.
def main():
    
    
    # Empty list that will contain the coordinates directing the turtle's movement.
    coordsList = []
    
    # Start the turtle right in the middle at (0,0)
    currentCoord = [0,0]
    
    # Start the coordsList with (0,0)
    coordsList.append(currentCoord)
    
    # This variable starts out at 0 when we are just at the beginning point (0,0)
    numSidesSurrounded = 0


    # So long as we haven't reached an edge (anytime abs(x-coord)==8 or abs(y-coord)==8) and we aren't completely
    # surrounded we keep moving.
    while( (abs(currentCoord[0]) < 8) and (abs(currentCoord[1]) < 8) ):
        
        
        # Rest this variable each time through the loop. It is another indicator of whether or not the walk will come
        # to an end (when == 4), and we increment it down in the for loop immediately below.
        numSidesSurrounded = 0
        
        # Reset these bools each time through the loop; they'll change once we've made another move.
        ptToLeftTakenBool = False
        ptToAboveTakenBool = False
        ptToRightTakenBool = False
        ptToBelowTakenBool = False
        
        # Reset this each time through the loop, since each time we'll have appended a most-recent coordinate.
        currentCoord = coordsList[-1]
        
        # We want to compare the current coordinate to each existing coordinate in the list to know where to make the 
        # next move in the walk. We must check each side, hence no if/elif block, just if's instead.
        for i in range((len(coordsList))):
            
            if( [currentCoord[0]+1, currentCoord[1]] == coordsList[i] ):
                ptToRightTakenBool = True
                numSidesSurrounded += 1
            if( [currentCoord[0]-1, currentCoord[1]] == coordsList[i] ):
                ptToLeftTakenBool = True
                numSidesSurrounded += 1
            if( [currentCoord[0], currentCoord[1]+1] == coordsList[i] ):
                ptToAboveTakenBool = True
                numSidesSurrounded += 1
            if( [currentCoord[0], currentCoord[1]-1] == coordsList[i] ):
                ptToBelowTakenBool = True
                numSidesSurrounded += 1
            
            
            
        #=============================================#
        # Next move for a point surrounded on 4 sides #
        #=============================================#            
            
        # If all 4 points surrounding the current point are taken then it's the end of the road.
        if(numSidesSurrounded == 4):
            break

        
        
        #=============================================#
        # Next move for a point surrounded on 3 sides #
        #=============================================#
        
        elif(numSidesSurrounded == 3):
            
            # If the point is surrounded on all side except to the left, then we must move to the left,
            if(ptToAboveTakenBool and ptToRightTakenBool and ptToBelowTakenBool):
                moveLeft(currentCoord, coordsList)
                
            # If the point is surrounded on all sides except above, then we must move above.
            elif(ptToRightTakenBool and ptToBelowTakenBool and ptToLeftTakenBool):
                moveAbove(currentCoord, coordsList)
                
            # If the point is surrounded on all sides except to the right, then we must move to the right,
            elif(ptToBelowTakenBool and ptToLeftTakenBool and ptToAboveTakenBool):
                moveRight(currentCoord, coordsList)
                
            # If the point is surrounded on all sides except below then we must move below.
            else:
                moveBelow(currentCoord, coordsList)
        
        
        #=============================================#
        # Next move for a point surrounded on 2 sides #
        #=============================================#
        
        elif(numSidesSurrounded == 2):
        
            # Make the next move, returning either 0,1 to control which move randomly gets made.
            nextMove = rand.randint(0,1)
            
            # Surrounded: left,above --> possible moves: right,below
            if(ptToLeftTakenBool and ptToAboveTakenBool):
                if(nextMove): moveRight(currentCoord, coordsList)
                else: moveBelow(currentCoord, coordsList)
                
            # Surrounded: above, right --> possible moves: below,left
            elif(ptToAboveTakenBool and ptToRightTakenBool):
                if(nextMove): moveBelow(currentCoord, coordsList)
                else: moveLeft(currentCoord, coordsList)
            
            # Surrounded: right,below --> possible moves: left,above
            elif(ptToRightTakenBool and ptToBelowTakenBool):
                if(nextMove): moveLeft(currentCoord, coordsList)
                else: moveAbove(currentCoord, coordsList)
                
            # Surrounded: below, left --> possible moves: above,right
            elif(ptToBelowTakenBool and ptToLeftTakenBool):
                if(nextMove): moveAbove(currentCoord, coordsList)
                else: moveRight(currentCoord, coordsList)
            
            # Surrounded: above,below --> possible moves: left,right
            elif(ptToAboveTakenBool and ptToBelowTakenBool):
                if(nextMove): moveLeft(currentCoord, coordsList)
                else: moveRight(currentCoord, coordsList)
                
            # Surrounded: left,right --> possible moves: above,below
            else:
                if(nextMove): moveAbove(currentCoord, coordsList)
                else: moveBelow(currentCoord, coordsList)
    
        
        #============================================#
        # Next move for a point surrounded on 1 side #
        #============================================#
        
        # (numSidesSurrounded == 1) is the only option left, so we can just code it as an 'else'    
        else:
            
            # Make the next move, returning either 0,1,2 to control which move randomly gets made.
            nextMove = rand.randint(0,2)

            # Surrounded: left --> possible moves: above,right,below
            if(ptToLeftTakenBool):
                if(nextMove == 0): moveAbove(currentCoord, coordsList)
                elif(nextMove == 1): moveRight(currentCoord, coordsList)
                else: moveBelow(currentCoord, coordsList)
                
            # Surrounded: above --> possible moves: right,below,left
            elif(ptToAboveTakenBool):
                if(nextMove == 0): moveRight(currentCoord, coordsList)
                elif(nextMove == 1): moveBelow(currentCoord, coordsList)
                else: moveLeft(currentCoord, coordsList)
                
            # Surrounded: right --> possible moves: below,left,above
            elif(ptToRightTakenBool):
                if(nextMove == 0): moveBelow(currentCoord, coordsList)
                elif(nextMove == 1): moveLeft(currentCoord, coordsList)
                else: moveAbove(currentCoord, coordsList)
                
            # Surrounded: below --> possible moves: left,above,right
            else:
                if(nextMove == 0): moveLeft(currentCoord, coordsList)
                elif(nextMove == 1): moveAbove(currentCoord, coordsList)
                else: moveRight(currentCoord, coordsList)                    
        


        # Assign the current coordinate so that the loop has accurate info on whether or not to keep going.
        currentCoord = coordsList[-1]

            
            
    print("Here is the list of coordinates")
    print(coordsList)
    
    printLattice()
    drawRandomWalk(coordsList)
    
    
    
main()