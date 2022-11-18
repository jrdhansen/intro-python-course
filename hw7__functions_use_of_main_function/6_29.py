# CS 1400, HOMEWORK 7, file 2
# DUE: Thursday, 03/02/2018 at 11:59 pm

# NAME:       Jared Hansen
# A-NUMBER:   A01439768
# SECTION:    CS-1400-002
# RECITATION: CS-1400-515


# Problem 6_29

'''
DESCRIPTION: "Financial: Credit Card Number Validation"

Credit cards follow certain patterns. It must have between 13 and 16 digits, and the number
must start with:
-- 4 for Visa cards
-- 5 for MasterCard credit cards
-- 37 for AmericanExpress cards
-- 6 for Discover cards
In 1954, Hans Luhn of IBM proposed an algorithm for validating credit card numbers. The
algorithm is useful to determine whether a card number is entered correctly or whether a
credit card is scanned correctly by a scanner. Credit card numbers are generated following
this validity check, commonly known as the "Luhn Check" or the "Mod 10 Check", which can be
decsribed as follows. For illustration, consider the card number 4388576018402626:
1.  Double every second digit from right to left. If doubling of a digit results in a
    two-digit number, add up the two digits to get a single digit number.
    (2*2 = 4), (2*2 = 4), (4*2 = 8), (1*2 = 2), (6*2 = 12 --> 1+2 = 3), (5*2 = 10 --> 1+0=1),
    (8*2= 16 --> 1+6=7), (4*2 = 8)
2.  Now add all single-digit numbers from Step 1
    4 + 4 + 8 + 2 + 3 + 1 + 7 + 8  =  37
3.  Add all digits in the odd places from right to left in the card number
    6 + 6 + 0 + 8 + 0 + 7 + 8 + 3  =  38
4.  Sum the results from Steps 2 and 3.
    37 + 38= 75
5.  If the result from Step 4 is divisible by 10, the card number is valid, otherwise it is
    invalid. For example, this card number is invalid, since 75%10 != 0.
A valid number is 4388576018410707


Write a program that prompts the user to enter a credit card number as an integer. Display
whether the number is valid or invalid. Design your program to use the following functions:

# Return True if the card number is valid
def isValid(number):

# Get the result from Step 2
def sumOfDoubleEvenPlace(number):

# Return this number if it is a single digit, otherwise, return the sum of the two digits
def getDigit(number):

# Return sum of odd place digits in number
def sumOfOddPlace(number):

# Return True if the digit d is a prefix for number
def prefixMatched(number, d):

# Return the number of digits in d
def getSize(d):

# Return the first k number of digits from number. If the number of digits in number is less
# than k, return number.
def getPrefix(number, k):


'''












#########******************
### NOTE ***** 
#########******************
#########***** 
#########******************
'''
    One of my functions (getPrefix) is slightly different from how the book said to write it.
I simply couldn't figure out how they wanted me to use it, so I adjusted to make it fit the
needs of the program. I got really tired of trying to guess how they wanted me to use it, so
I got it similar to what they wanted and used it. Basically, it only has one argument instead
of 2 (I couldn't figure out where it wanted the "k" arg to come from), but it does the exact
same thing from what I can tell.
    You'll find that my program works as it should, checking for valid prefixes and the mod10
check. Hopefully this slight difference in one function is an acceptable departure from how the
book instructed to make the program since its' nearly identical.
'''




















# Returns "True" if the card number is valid, "False" otherwise.
# In order to be true, the total of the sum functions must be evenly divisible by 10,
#   the number must have a valid prefix, and the number must have 13-16 digits.
def isValid(number):
    total = 0
    total = (sumOfDoubleEvenPlace(number) + sumOfOddPlace(number))
    if ((total%10 == 0) and (prefixMatched(number, getPrefix(number))) and (13 <= getSize(number) <= 16)):
        return True
    else:
        return False
    
    
    
    
    
# Return the number of digits in d
def getSize(d):
    digits = 1
    while (d > 10):
        d = (d - d%10)//(10)
        digits += 1
    return digits
    
    
    
    
    
# Get the result from Step 2
def sumOfDoubleEvenPlace(number):
    sumOfDoubleEvens = 0
    digit = 0
    while(number > 0):
        digit = (number - ((((number//100)*100)) + ((number - (number//10)*10)))) / 10
        digit = getDigit(digit)
        sumOfDoubleEvens += digit
        number = (number//100)

    return sumOfDoubleEvens
    
    
    
    
    
    
    
# Returns the number if it is a single digit, otherwise, return the sum of the two digits.
def getDigit(number):
    if (number*2 < 10):
        return (number*2)
    else:
        num1 = (number*2)//10
        num2 = (number*2)%10
        number = (num1 + num2)
        return number
     
    
    
    
    
    
# Return sum of odd place digits in number    
def sumOfOddPlace(number):
    sumOfOdds = 0
    while(number > 0):
        sumOfOdds += number - ((number//10)*10)
        number = (number//100)
    
    return sumOfOdds
    

    


# Return True if the digit d is a prefix for number
def prefixMatched(number, d):
    
    if(getSize(d) == 1):
        if (getPrefix(number) == d):
            return True
    elif(getSize(d) == 2):
        if (getPrefix(number) == d):
            return True
    else:
        return False
    





# (I did this one slightly different from how the book said to)
# This function returns the prefix (first 1 or 2 numbers of the credit card)
# if the card number begins with a valid prefix, otherwise it returns the card number
def getPrefix(number):
    numDigits = getSize(number)
    
    prefixNum = number//(10**(numDigits-1))
    # This covers prefixes 4,5,6, which are all valid.
    if (prefixNum == 4):
        return 4
    elif (prefixNum == 5):
        return 5
    elif (prefixNum == 6):
        return 6
    
    # This covers prefix 37, which is valid.
    prefixNum = number//(10**(numDigits-2))
    if ((prefixNum == 37)):
        return 37
    
    # If the prefix wasn't 4,5,6,37 we return the number since it's not a valid prefix.
    else:
        return number 
    
    
    
    
    









# Write a program that prompts the user to enter a credit card number as an integer. Display
# whether the number is valid or invalid.

def main():
    userNum = eval(input("Enter a credit card number as a positive integer with no spaces in it: "))
    
    # User input validation: make sure it's an integer and >= 0
    while(((userNum%1) != 0) or (userNum <= 0)):
        print("That is not a valid number. Please try again.")
        userNum = eval(input("Enter a credit card number as a positive integer with no spaces in it: "))


    if (isValid(userNum)):
        print("This is a valid credit card number.")
    else:
        print("This is not a valid credit card number.")
        
        
        
main()















input("Press any key to continue")

