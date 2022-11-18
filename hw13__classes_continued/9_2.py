# CS 1400, HOMEWORK 13, file 1
# DUE: Thursday, 04/26/2018 at 11:59 pm

# NAME:       Jared Hansen
# A-NUMBER:   A01439768
# SECTION:    CS-1400-002
# RECITATION: CS-1400-515





# Problem 9_2






'''
PROGRAM TITLE: Create an Investment-Value Calculator


Write a program that calculates the future value of an investment at a given interest rate for a specified
number of years. The formula for the calculation is as follows:
    
futureValue = investmentAmount * (1 + annualInterestRatePercentage/100) ** years
note: if the interest rate is entered as a percentage, like 3.25, you'll need to convert it to a decimal by dividing by 100. 
So the math in the example would be:
FV = 1000 * (1 + .0325)**3


Use text fields for users to enter the investment amount, years, and interest rate. Display the future amount in a text
field when the user click the 'Calculate' button.

'''




# Import all definitions from tkinter
from tkinter import *





# Our class for future value calculations
class FutureValueCalculator:
    
    
    
    def __init__(self):
        
        # Create a window
        window = Tk()
        # Desired title
        window.title("Investment Calculator") 


        # Get user input for principal amount, place it in the GUI
        Label(window, text = "Investment Amount:").grid(row = 1, column = 1)
        self.principal = StringVar()
        Entry(window, textvariable=self.principal).grid(row = 1, column = 2, padx=5 , pady = 5)
        
        
        # Get user input for number of years, place it in the GUI
        Label(window, text = "Years:").grid(row = 2, column = 1)
        self.years = StringVar()
        Entry(window, textvariable=self.years).grid(row = 2, column = 2)
        
        
        # Get user input for the annual interest rate, place it in the GUI
        Label(window, text = "Annual Interest Rate:").grid(row = 3, column = 1)
        self.annualRate = StringVar()
        Entry(window, textvariable=self.annualRate).grid(row = 3, column = 2)
        
        
        # Creat the button to calculate the FV based on user inputs
        Button(window, text = "Calculate", command=self.calculate).grid(row = 5, padx = 5, pady = 5, column = 2, sticky = E)
    
    
        # Display the calculated FV in a nice format.
        Label(window, text = "Future Value:").grid(row = 4, column = 1)
        self.calculatedValue=StringVar()
        Label(window, textvariable = self.calculatedValue).grid(row = 4, column = 2)
        
        
        # Create an event loop
        window.mainloop()
        
        
    # This function does the math and the formatting of the value we calculate.
    def calculate(self):
        futureValue = '${:,.2f}'.format((float(self.principal.get())) * ((1 + (float(self.annualRate.get()))/100) ** (float(self.years.get()))))
        #print(futureValue)
        self.calculatedValue.set(futureValue)
        
        
        
        
        
        
 # Create GUI  
FutureValueCalculator()

























