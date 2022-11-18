# CS 1400, HOMEWORK 3, file 2
# DUE: Wednesday, 01/31/2018 at 11:59 pm

# NAME:       Jared Hansen
# A-NUMBER:   A01439768
# SECTION:    CS-1400-002
# RECITATION: CS-1400-515


# Problem 2_25



'''
DESCRIPTION: "Turtle: Draw a Rectangle"

Write a program that prompts the user to enter the center of a rectangle, width,
and height, and displays the rectangle as shown in Figure 2.4c.


'''



# Imports the turtle library
import turtle


# Shows the turtle initially, allows us to see what it's doing, although this
# didn't exactly work for me....but I put it in anyway, so hopefully it works
# for whomever is grading this ¯\_(ツ)_/¯
turtle.showturtle


# Obtain user input: where do they want the rectangle to be centered?
#       Get both the x-coordinate and the y-coordinate
centerX = eval(input("Enter what you would like the x-coordinate to be for the center of the rectangle: "))
centerY = eval(input("Enter what you would like the y-coordinate to be for the center of the rectangle: "))


# Obtain user input: what dimensions do they want for the rectangle?
#       Get both the width and the height dimensions.
width = eval(input("Enter what you would like the width of the rectangle to be: "))
height = eval(input("Enter what you would like the height of the rectangle to be: "))


# I'm going to (arbitrarily) start drawing the rectangle at the bottom left
# corner, moving around in a clockwise direction.
#       Calculate the starting coordinate of the rectangle.
startX = centerX - (width/2.0)
startY = centerY - (height/2.0)


# Move the turtle to the starting (x,y) coordinate
# Must pick the turtle up before moving in order to avoid lines being drawn,
#       then put the pen back down
turtle.penup()
turtle.goto(startX, startY)
turtle.pendown()


# I'm assuming that the turtle is always starting oriented facing right
# (oriented horizontally, facing from smaller x-values to larger x-values)
# Now we must orient the turtle 90 degrees to the left so that it's facing
#       upward and ready to draw the left side.
turtle.left(90)


# Now move the turtle "forward" for the given height, drawing the left side
turtle.forward(height)


# Now turn the turtle 90 degrees to the right so that it's facing to the right
#       and ready to draw the top side.
turtle.right(90)


# Now move the turtle "forward" for the given width to draw the top side.
turtle.forward(width)


# Now turn the turtle 90 degrees to the right in preparation to draw the right
#       side.
turtle.right(90)


# Move the turtle "forward" for the given height, drawing the right side.
turtle.forward(height)


# Turn the turtle 90 degrees to the right in preparation do draw the bottom side
turtle.right(90)


# Move the turtle "forward" for the given width to complete the rectangle,
#       drawing the bottom side.
turtle.forward(width)


# In the case of runnning this program in the console, I'm including this extra
# line so that the output can be seen before the program closes.
input("Press any key to continue")