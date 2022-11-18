# CS 1400, HOMEWORK 2
# DUE: Wednesday, 01/24/2018 at 11:59 pm

# NAME:       Jared Hansen
# A-NUMBER:   A01439768
# SECTION:    CS-1400-002
# RECITATION: CS-1400-515



'''
HOMEWORK DESCRIPTION

Write a Python program that takes as input 3 scores from the user, using the
input() function.  The scores will be homework points out of 150, exam points
out of 250, and recitation points out of 75.  

After storing the 3 scores, calculate the total points, and final percentage
and print these to the screen (see the sample output below).

Store the total possible points, 475, as a named constant (see section 2.7 in
the book).  Recall that named constants, by convention are given an ALL CAPS
name.  Store the 3 scores, homework, exams, recitation, with good variable
names.   

Code Style and Naming Conventions:
You need to follow the style and naming conventions used in class.  Name
variables with good descriptive names, and give proper spacing and indentation
to your code.  Add good comments to your code, that explain what your program
does.

Update 2018.01.17 - the hw file submitted should by named hw2.py, also I added
a requirement to make the variable name, for the named constant, in ALL CAPS
(see below).
 
Deliverables in Canvas: Upload your homework file hw2.py (and any other files)
into canvas.  If you have multiple files, like a README.txt, zip the files
together and upload a single zip file to canvas.

'''






# in ALL CAPS designate the named constant for the total number of points possible
POSS_TOTAL_PTS = 475


# get input from the user for homework points, exam points, and recitation points
homeworkPts = eval(input("Out of the 150 possible homework points, enter how many you earned: "))
examPts = eval(input("Out of the 250 possible exam points, enter how many you earned: "))
recitPts = eval(input("Out of the 75 possible recitation points, enter how many you earned: "))


# calculate how the user's total points and final percentage
earnedTotalPts = homeworkPts + examPts + recitPts
finalPctg = earnedTotalPts/POSS_TOTAL_PTS


# print the user's total points earned and final percentage
print("\nYou earned ", earnedTotalPts, "/", POSS_TOTAL_PTS, " total points.")
print("Your final percentage is: ", finalPctg*100, "%")