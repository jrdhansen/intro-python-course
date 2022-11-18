# CS 1400, HOMEWORK 4, file 2
# DUE: Thursday, 02/08/2018 at 11:59 pm

# NAME:       Jared Hansen
# A-NUMBER:   A01439768
# SECTION:    CS-1400-002
# RECITATION: CS-1400-515


# Problem 3_14

'''
DESCRIPTION: "Turtle: Draw the Olpympic Symbol

Write a program that prompts the user to enter the radius of the rings and draw an
Olympic symbol of five rings of the same size with the colors blue, black, red,
yellow, and green, as shown in Figure 3.5c.


'''

######################
## Explanatory Note ##
######################
# There isn't necessarily a ton of rhyme or reason to the calcuations I made, especially certain ratios.
# I simply did a bunch of guess and check until I was able to get it to look almost exactly like the figure in the book.

# However, it should be noted that I purposely drew the yellow and green circles last, since in the book they
# appear to be lying on top of the blue, black, and red circles.




# import the turtle library, give it the alias "t" for less typing
import turtle as t


# get the radius from the user
radius = eval(input("Enter the radii of the circles: "))


# I'm just going to assume that the black circle has its bottom at (0,0).
# This seemed to be very close to where it was in the book's example, and a relatively logical choice.
# Also, I messed around with some different widths for the circles, and this one seemed to be pretty close to what
# the book did.
t.pensize(0.15*radius)
t.color("black")
t.circle(radius)


# Next we're going to draw the blue circle
# Although the real Olympic symbol has blue and black overlap, the one in the book doesn't; I'm going by the one in the book.
t.penup()
t.goto(0.0-((2*radius + (1/3)*radius)), 0.0)
t.pendown()
t.color("blue")
t.circle(radius)


# Next we're going to draw the red circle
# Although the real Olympic symbol has red and black overlap, the one in the book doesn't; I'm going by the one in the book.
t.penup()
t.goto(0.0+((2*radius + (1/3)*radius)), 0.0)
t.pendown()
t.color("red")
t.circle(radius)


# Now we're going to draw the yellow circle
t.penup()
t.goto(0.0-((2*radius + (1/3)*radius))/2, -(1.15*radius))
t.pendown()
t.color("yellow")
t.circle(radius)


# Finally, we're going to draw the green circle
t.penup()
t.goto(0.0+((2*radius + (1/3)*radius))/2, -(1.15*radius))
t.pendown()
t.color("green")
t.circle(radius)





# In the case of runnning this program in the console, I'm including this extra
# line so that the output can be seen before the program closes.
input("Press any key to continue")