# CS 1400, HOMEWORK 13, file 2
# DUE: Thursday, 04/26/2018 at 11:59 pm

# NAME:       Jared Hansen
# A-NUMBER:   A01439768
# SECTION:    CS-1400-002
# RECITATION: CS-1400-515





# Problem 9_20






'''
PROGRAM TITLE: "Geometry: Inside a Circle?"

Write a program that draws a fixed circle centered at (100,60) with a radius of 50. Whenever the mouse
is moved while the left button is pressed, display the message indicating whether the mouse pointer is
inside the circle.

'''






# We need this library for the sqrt() function within the distance formula.
import math
# Import all definitions from tkinter
from tkinter import *


# Class we'll call to run the GUI.
class MouseInTheCircle:

    def __init__(self):

        # Given these values by the prompt, we'll be using them throughout the program.
        self.radius = 50
        self.centerX = 100
        self.centerY = 60
        self.text = ""

        # Make a window, give it a title.
        window = Tk()
        window.title("Inside the circle?")

        # Making a canvas for the circle.
        self.canvas = Canvas(window, bg = "white", width = 3*self.centerX, height = 2*self.centerY)
        self.canvas.pack()

        # Draw the circle.
        self.drawTheCircle()

        # Bind the left-click-hold-action to the 'processMouseEvent' function
        self.canvas.bind("<B1-Motion>", self.processMouseEvent)

        # Bind the release of the left-click button to the 'buttonRelease' function
        self.canvas.bind("<ButtonRelease-1>", self.buttonRelease)

        # Create an event loop.
        window.mainloop()


    # This function draws one of the sexiest circles you've ever seen.
    def drawTheCircle(self):
        self.canvas.create_oval(self.centerX-self.radius, self.centerY-self.radius, self.centerX+self.radius, self.centerY+self.radius)


    # This function contains the logic that displays whether or not the pointer is in the circle.
    def processMouseEvent(self, event):
        #print("clicked at", event.x, event.y)
        self.canvas.delete("text")

        if(math.sqrt((event.x-self.centerX)**2 + (event.y-self.centerY)**2) <= self.radius):
            self.canvas.create_text(event.x, event.y, text = "IN circle", tags = "text")

        else:
           self.canvas.create_text(event.x, event.y, text = "OUT of circle", tags = "text")


    # This function deletes the text once we let go of the left-click button.
    def buttonRelease(self, event):
        self.canvas.delete("text")



MouseInTheCircle()