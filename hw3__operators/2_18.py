# CS 1400, HOMEWORK 3, file 1
# DUE: Wednesday, 01/31/2018 at 11:59 pm

# NAME:       Jared Hansen
# A-NUMBER:   A01439768
# SECTION:    CS-1400-002
# RECITATION: CS-1400-515


# Problem 2_18

'''
DESCRIPTION: "Current Time"

Listing 2.7, ShowcurrentTime.py, gives a program that displays the current time in GMT. Revise the program so that it prompts the user to enter the time zone in hours away from (offset to) GMT and displays the time in the spcified time zone. Here is a sample run:
    
    Enter the time zone offset to GMT (any integer in the set {-12, 12}): -5
    The current time is 4:50:34


'''

# Imports the time library so we can utilize the time function
import time


# Get input from the user; how many time zones are they offset from GMT?
zonesAway = int(input("Enter the time zone offset to GMT (any integer in the set [-12, 11,..., 12]): "))


# Gets the current time
currentTime = time.time()


# Modifies the current time relative to the offset the user entered
# Since the user's difference is in hours, we simply multiply the number they
#       enter by 3600 (seconds in an hour) and add that number to currentTime.
#       Becuase they can enter a negative number, that is already factored into
#       the calculation, so simple addition is all that is needed.
currentTime += (zonesAway*3600)


# Gets the total seconds since the UNIX epoch
#       We only want to deal with whole seconds, so use the int() function to
#       convert the value given by the time() function.
totalSeconds = int(currentTime)


# Gets the current second.
currentSecond = totalSeconds%60


# Gets the total minutes since UNIX epoch
totalMinutes = totalSeconds//60


# Gets the current minute in the hour
currentMinute = totalMinutes%60


# Obtains the total hours since UNIX epoch
totalHours = totalMinutes//60


# Gets the current hour
currentHour = totalHours%24


# Print the results
print("Current time (hour:minute:second) is ", currentHour, ":", currentMinute, ":", currentSecond)


# In the case of runnning this program in the console, I'm including this extra
# line so that the output can be seen before the program closes.
input("Press any key to continue")