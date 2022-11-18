# CS 1400, HOMEWORK 8, file 1
# DUE: Thursday, 03/15/2018 at 11:59 pm

# NAME:       Jared Hansen
# A-NUMBER:   A01439768
# SECTION:    CS-1400-002
# RECITATION: CS-1400-515


# Problem 6_14

'''
PROGRAM TITLE: Estimate Pi


Pi can be computed (approximated) using the following series:
m(i) = 4(1 - 1/3 + 1/5 - 1/7 + 1/9 - 1/11 + .... + ((-1)^(i+1))/(2i-1))

Write a function that returns m(i) for a given i and write a test program that
displays the following table:

i          m(i)
1          4.0000
101        3.1515
201        3.1466
301        3.1449
401        3.1441
501        3.1436
601        3.1433
701        3.1430
801        3.1428
901        3.1427

'''




# function that returns the estimate of pi for a given index i
def calculateEstimate(index):
    estimate = 0
    parenthTerm = 0
    while(index > 0):
        parenthTerm += (((-1)**(index + 1)) / (2*index - 1))
        index -= 1

    estimate = 4 * parenthTerm
    return format(estimate, "1.4f")




# function that prints the index "i", the neccesary whitespace, and the estimate of pi "m(i)"
def printIandMI(i):
    print(i, "             ", calculateEstimate(i))




# main function will display the table. I tried to get it as close as possible to the
# spacing and everything that the book example had, but it may be just a tad off.
def main():
    print("\ni                  m(i)\n")
    print("1                ", calculateEstimate(1))
#       In order to get the formatting that the book wanted, I had to do the printing of
# i=1 and m(1) without the function printIandMI since all the other i's have three digits
# and i=1 only has one digit.
#       However, since 101, 201, ..., 901 all needed the same thing, I just wrote a function
# that would print the i value and the corresponding m(i).
    printIandMI(101)
    printIandMI(201)
    printIandMI(301)
    printIandMI(401)
    printIandMI(501)
    printIandMI(601)
    printIandMI(701)
    printIandMI(801)
    printIandMI(901)




# call the main function
main()




input("Press any key to continue")