# CS 1400, HOMEWORK 10, file 1
# DUE: Thursday, 03/29/2018 at 11:59 pm

# NAME:       Jared Hansen
# A-NUMBER:   A01439768
# SECTION:    CS-1400-002
# RECITATION: CS-1400-515





# Problem 8_3





'''
PROGRAM TITLE: "Check Password"

Some websites impose certain rules for passwords. Write a function that checks whether
a string  is a valid password. Suppose the password rules are as follows:
    -- a password must have at least eight characters.
    -- a password must consist of only letters and digits.
    -- a password must contain at least two digits.
    
Write a program that prompts the user to enter a password and displays "valid password"
if the rules are followed or "invalid password" otherwise.
'''





# Function to check whether a string is a valid password or not.
def checkPassword(password):
    
    
    # Set up these two strings to use as reference to check whether or not the value
    # of a certain index is valid. (For any given index of the user-inputted password,
    # the value must be the same as one of the indices in these two strings.)
    letterValues = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    digits = "0123456789"
    
    
    # Checks to make sure that the password is at least 8 characters long.
    if(len(password) >= 8):
        
        numDigits = 0
        for i in range(0, len(password)):
          
            # This elif block checks to make sure that all indices of the password
            # are valid values (either a letter or a digit).
            if(password[i] in digits):
                numDigits += 1
            elif(password[i] in letterValues):
                continue
            else:
                return False        
                   
        # Checks to make sure that the password has at least 2 digits.    
        if(numDigits >= 2):
            return True
                    

    # The logic above is set up such that a failure to meet any of the given
    # requirements kicks down to here, returning a false.
    else:
        return False










# This is the 'test program' that prompts the user to enter a password and displays "valid password"
# if the rules are followed or "invalid password" otherwise.
def main():
    
    
    # Give the user instructions regarding qualities the passoword must possess.
    print("Please enter a password with the following characteristics:")
    print("-- has at least 8 characters")
    print("-- consists only of letters and digits")
    print("-- contains at least two digits\n")

    # Prompt the user to enter a password
    userPassword = input("Enter the password now: ")
    
    # Since the checkPassword function returns a boolean value, we simply use an if statement:
    # if the checkPassword function returns true, then the print statement within the if gets 
    # run, otherwise, the else gets run (which we know means that it's an invalid password).
    if(checkPassword(userPassword)):
        print("valid password")
    else:
        print("invalid password")

   





# call the main function
main()