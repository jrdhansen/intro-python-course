# CS 1400, HOMEWORK 9, file 2
# DUE: Thursday, 03/22/2018 at 11:59 pm

# NAME:       Jared Hansen
# A-NUMBER:   A01439768
# SECTION:    CS-1400-002
# RECITATION: CS-1400-515




# Problem 7_8






'''
PROGRAM TITLE: "Stopwatch"


Design a class named StopWatch. The class contains:
    
-- The private data fields startTime and endTime with get methods.
-- A constructor that initializes startTime with the current time.
-- A method named start() that resets the startTime to the current time.
-- A method named stop() that sets the endTime to the current time.
-- A method named getElapsedTime() that returns the elapsed time for the stop watch in
   milliseconds.


Draw the UML diagram for the class, and then implement the class. Write a test program that
measures the execution time of adding numbers from 1 to 1,000,000.


'''






'''
HERE IS MY UML DIAGRAM

--------------------------------------------------------------------------------------------------------|
        StopWatch                                                            <-- CLASS NAME             |
--------------------------------------------------------------------------------------------------------|
startTime: float                                                              <-- DATA FIELDS           |
endTime: float                                                                <-/                       |
--------------------------------------------------------------------------------------------------------|
StopWatch()                                                                         <-- CONSTRUCTOR     |
getStartTime(): float                                                               <-- METHODS         |
getEndTime():float                                                                     <-/              |
start(): None                                                                         <-/               | 
stop(): None                                                                         <-/                |
getElapsedTime(): float                                                             <-/                 |
--------------------------------------------------------------------------------------------------------|
'''




# We'll need this module in order to get the start and stop times using the system's clock
import time



# Here is our definition of the StopWatch class.
class StopWatch:

    #       The code I initially wrote for the constructor was identical to the start() fctn, so I just
    # called the start fctn here to cut down on repetitive code.
    def __init__(self):
        self.start()

    # This fctn is simply used as an accessor for the (private) startTime data field.
    def getStartTime(self):
        return self.__startTime

    # This fctn is simply used as an accessor for the (private) endTime data field.
    def getEndTime(self):
        return self.__endTime

    # Upon call, this fctn sets the startTime variable equal to the number of seconds since the Unix Epoch.
    def start(self):
        self.__startTime = time.time()

    # Upon call, this fctn sets the endTime variable equal to the number of seconds since the Unix Epoch.
    def stop(self):
        self.__endTime = time.time()

    # This fctn just returns the difference between the endTime and startTime.
    def getElapsedTime(self):
        return (self.__endTime - self.__startTime)



# Write a test program that measures the execution time of adding numbers from 1 to 1,000,000.
def main():

    # Instantiate a StopWatch object, here called 'watch1'.
    watch1 = StopWatch()

    # Start the watch running.
    watch1.start()

    # Add the numbers 1 thru 1,000,000.
    sumOfOneThruOneMillion = 0
    for i in range(1, (1000000+1)):
        sumOfOneThruOneMillion += i
        
    # Stop the watch.
    watch1.stop()
    
    # Print the number of seconds that it took for the program to run.
    print("The total time it takes to add from 1 through 1,000,000 is:", watch1.getElapsedTime(), "seconds.")




# Call the main function
main()




input("\nPress any key to continue")