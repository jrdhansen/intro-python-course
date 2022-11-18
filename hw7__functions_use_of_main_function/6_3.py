# CS 1400, HOMEWORK 7, file 1
# DUE: Thursday, 03/02/2018 at 11:59 pm

# NAME:       Jared Hansen
# A-NUMBER:   A01439768
# SECTION:    CS-1400-002
# RECITATION: CS-1400-515


# Problem 6_3

'''
DESCRIPTION: "Palindrome Integer"

Write the functions with the following headers:

# Return the reversal of an integer, e.g reverse(456) returns 654
def reverse(number)

# Return true if number is a palindrome
def isPalindrome(number)

Use the reverse function to implement isPalindrome. A number is a palindrome if its reversal
is the same as itself. Write a test program that prompts the user to enter an integer and
reports whether the integer is a palindrome.

'''






# The logic to come up with the reversal of a number is kind of tricky. Basically, we're
# using integer division and the modulus operator to turn the number around using a while
# loop, adding to the "reversal" number, and integer-dividing the "number" term.

# This function will return the reversal of any integer, positive or negative
def reverse(number):
    reversal = 0

    # This "if" is used to handle positive ints
    if (number > 0):
        while(number > 0):
            reversal = (reversal*10) + (number%10)
            number //= 10
    # This "else" will handle negative ints, as well as 0
    else:
        number *= (-1)
        while (number > 0):
            reversal = (reversal * 10) + (number % 10)
            number //= 10
        reversal *= (-1)

    return reversal



# Here, we employ the reverse() function to flip a number around, and comparing the flipped-
# around number to the original. If they're equivalent then we return True, else we return
# false.
def isPalindrome(number):
    if (number == reverse(number)):
        return True
    else:
        return False



# Our main function is where we'll get user input, and employ the functions written above to
# test whether the integer they enter is a palindrome.
def main():

    # Obtain and validate user input (make sure it's an integer).
    userNum = eval(input("Enter an integer: "))
    while (userNum % 1 != 0):
        print("The number you entered is not an integer.")
        userNum = eval(input("Enter an integer: "))

    # check to see whether the number they entered is a palindrome or not
    if(isPalindrome(userNum)):
        print("The reversal of", userNum, "is", reverse(userNum), ". This number is a palindrome.")
    else:
        print("The reversal of", userNum, "is", reverse(userNum), ". This number is not a palindrome.")


# call the main function
main()



input("Press any key to continue")