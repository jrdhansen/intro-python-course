# CS 1400, HOMEWORK 12, file 1
# DUE: Thursday, 04/19/2018 at 11:59 pm

# NAME:       Jared Hansen
# A-NUMBER:   A01439768
# SECTION:    CS-1400-002
# RECITATION: CS-1400-515





# Problem 11_19






'''
PROGRAM TITLE: Pattern Recognition: four consecutive, equal numbers

Write the following function that tests whether a two-dimensional list has four consecutive numbers of the
same value, either horizontally, vertically, or diagonally:

def isConsecutiveFour(values):

Write a test program that prompts the user to enter the number of rows and columns of a two-dimensional list
and then the values in the list. The program displays 'True' if the list contains four consecutive numbers
with the same value, otherwise it displays 'False.' Here are some sample true cases:
=================   =================   ===========   =====================
| 0 0 0 0 0 0 0 |   | 0 5 0 0 0 0 0 |   | 4 0 0 0 |   | 0 0 0 0 0 0 0 0 7 |
| 0 0 0 0 0 0 0 |   | 0 5 0 0 0 0 0 |   | 0 4 0 0 |   | 0 0 0 0 0 0 0 7 0 |
| 0 0 0 0 0 0 0 |   | 0 5 0 0 0 0 0 |   | 0 0 4 0 |   | 0 0 0 0 0 0 7 0 0 |
| 0 0 0 0 0 0 0 |   | 0 5 0 0 0 0 0 |   | 0 0 0 4 |   | 0 0 0 0 0 7 0 0 0 |
| 0 0 0 0 0 0 0 |   | 0 5 0 0 0 0 0 |   ===========   =====================
| 3 3 3 3 0 0 0 |   | 0 5 0 0 0 0 0 |
=================   =================
'''














                            ########################
                            ########################
                            ### NOTE FOR GRADER ####
                            ########################
                            ########################
'''
After getting most of the way through this problem, I realized I could've taken a much simpler approach.
However, being as far in as I was, I just finished it out this way.


I did my best to make my code clear by commenting frequently/informatively, so hopefully it helps.
Also, I intentionally left a ton of space in between functions and blocks of code within functions.
I wrote 4 functions that are called by the isConsecutiveFour() function.
-- one to check the rows
-- one to check the columns
-- one to check the left-to-right-upward diagonals
-- one to check the left-to-right-downward diagonals.



The functions to check the rows and columns are pretty straightforward and brief, but the diagonal functions
are long and a bit messy. They're broken down as follows:
    
    
-- CHECK THE DIAGS FROM LEFT-TO-RIGHT-DOWNWARD (one of the diag-checking functions),
-- as well as CHECK THE DIAGS FROM LEFT-TO-RIGHT-UPWARD (the other diag-checking function)

    -- checks to see if the dimensions are such that there is even the possiblity of 4-long diagonals
    -- if so, check:
        -- is square array? If so:
            -- check the on/above main diagonal diagonals,
            -- then check the below diagonal diagonals.
        -- is squatty array? (cols > rows) If so:
            -- check the on/above main diagonal diagonals,
            -- check the middle diagonals (all the same length)
            -- check the below main diagonal diagonals.
        -- is tall/skinny array? (rows > cols) If so:
            -- check the on/below diagonal diagonals,
            -- check the middle diagonals (all the same length)
            -- check the above main diagonal diagonals.
        
'''













# We'll use the randint() function to generate random arrays (if user desires), so we'll need this library.
import random as rand










# This function checks the rows for runs of 4 consecutive, equal values, returns either 'True' or 'False.'
def checkRowsForConsecutive(valsArray, numRows, numCols):

    
    # A row cannot have 4 consective, equal values if the row isn't at least 4 elements long.
    if(numCols < 4):
        return False
    
    else:
        # This outer for loop will iterate through the number of rows (lists) in the array.
        for i in range(numRows):
            
            # Have to reset this value to 1 for each row (setting it to 0 doesn't work)
            countNumConsec = 1

            # This inner loop will compare indices within each row (num indices = numCols variable).
            for j in range(numCols-1):
                if(valsArray[i][j] != valsArray[i][j+1]):
                    countNumConsec = 1
                elif(valsArray[i][j] == valsArray[i][j+1]):
                    countNumConsec += 1
            # If a sequence contains at least 4 consecutive, equal values, then return 'True' and quit checking.
            if(countNumConsec >= 4):
                return True
        else:
            return False
        
        
        
        
        
        
        
        
        
        
# This function checks the columns for runs of 4 consecutive, equal values, returns either 'True' or 'False.'
def checkColsForConsecutive(valsArray, numRows, numCols):

    # A column cannot have 4 consective, equal values if the column isn't at least 4 elements long.
    if(numRows < 4):
        return False
    
    else:
                
        # This outer for loop will iterate through the number of rows (lists) in the array.
        for i in range(numCols):
            
            # Have to reset this value to 1 for each row (setting it to 0 doesn't work)
            countNumConsec = 1

            # This inner loop will compare indices within each row (num indices = numCols variable).
            for j in range(numRows-1):
                if(valsArray[j][i] != valsArray[j+1][i]):
                    countNumConsec = 1
                elif(valsArray[j][i] == valsArray[j+1][i]):
                    countNumConsec += 1
            # If a sequence contains at least 4 consecutive, equal values, then return 'True' and quit checking.
            if(countNumConsec >= 4):
                return True                
        else:
            return False
        
        
        
        
        
        
        
        
        
        
# This function checks all diagonals that are oriented from left-to-right and read upward from the left to 
# the right.
def checkLeftToRightUpwardDiagonals(valsArray, numRows, numCols):
    
    
    # There's no point in checking any diagonals if there aren't at least 4 rows and 4 columns, because
    # there can't be a diagonal at least 4 long is this is the case.
    if( (numRows < 4) or (numCols < 4) ):
        return False
    
    
    
    # The only way to enter the 'else' statement is if both (numRows >= 4) and (numCols >= 4), so we can 
    # rest assured that there's at least one l-to-r-upward diagonal to check.
    else:
        
        # For checking the diagonals of arrays from left-to-right and moving upward, we'll always start by
        # checking the sequence: [3][0], [2][1], [1][2], [0][3]
        firstRowIndex = 3
        firstColIndex = 0
        lastRowIndex = 0
        lastColIndex = 3
        # Initialize this value to 1 for all remaining checks of consecutive, equal values.
        countNumConsec = 1
        
        
        
        ###################################################################
        # TO CHECK ARRAYS THAT HAVE EQUAL DIMENSIONS (NUMROWS == NUMCOLS) #
        ###################################################################
        if (numRows == numCols):
            
            #==============================================================#
            # first, check diagonals that are 'above/on the main diagonal' #
            #==============================================================#
            while( (firstRowIndex < numRows) and (lastColIndex < numCols) ):
                
                # This is a temporary list that we'll use to hold the values in each of the diagonals on or
                # above the diagonal.
                listToHoldDiagVals = []
                
                # We have to use this placeholder variable because we use the firstRowIndex value in the
                # range function to control the for loop.
                placeholderRowIndex = firstRowIndex
                
                # This for loop will iterate through each diagonal, adding the value to the temporary list.
                for i in range(firstRowIndex+1):
                    listToHoldDiagVals.append(valsArray[placeholderRowIndex][i])
                    placeholderRowIndex -= 1
                                
                # See if the sequence has 4 consec and equal values.
                for i in range(len(listToHoldDiagVals)-1):
                    if(listToHoldDiagVals[i] == listToHoldDiagVals[i+1]):
                        countNumConsec += 1
                    elif(listToHoldDiagVals[i] != listToHoldDiagVals[i+1]):
                        countNumConsec = 1
                  # If a sequence contains at least 4 consecutive, equal values, then return 'True' and quit checking.
                if(countNumConsec >= 4):
                    return True
                firstRowIndex += 1
                lastColIndex += 1
            
    
    
            #==========================================================#
            # next, check diagonals that are 'below the main diagonal' #
            #==========================================================#

            firstRowIndex = (numRows-1)
            lastColIndex = (numCols-1)
            firstColIndex = 1
            lastRowIndex = 1
            numDiagsBelowMainDiag = numRows-4
            
            numElementsInDiagMinus1 = numRows-1
            while( (firstColIndex < (numDiagsBelowMainDiag+1)) and (lastRowIndex <  (numDiagsBelowMainDiag+1)) ):
                
                listToHoldDiagVals = []
                
                tempFirstColIndex = firstColIndex
                tempFirstRowIndex = firstRowIndex
                
                for i in range(numElementsInDiagMinus1):
                    listToHoldDiagVals.append(valsArray[tempFirstRowIndex][tempFirstColIndex])
                    tempFirstRowIndex -= 1
                    tempFirstColIndex += 1
                numElementsInDiagMinus1 -= 1
                                    
                # See if the sequence has 4 consec and equal values.
                for i in range(len(listToHoldDiagVals) - 1):
                    if (listToHoldDiagVals[i] == listToHoldDiagVals[i + 1]):
                        countNumConsec += 1
                    elif (listToHoldDiagVals[i] != listToHoldDiagVals[i + 1]):
                        countNumConsec = 1
                # If a sequence contains at least 4 consecutive, equal values, then return 'True' and quit checking.
                if (countNumConsec >= 4):
                    return True

                firstColIndex += 1
                lastRowIndex += 1
            
            
            
        ###################################################################################
        # TO CHECK ARRAYS THAT ARE WIDER THAN THEY ARE TALL "SQUATTY" (NUMROWS < NUMCOLS) #
        ###################################################################################
        elif (numRows < numCols):

            # For checking the diagonals of arrays from left-to-right and moving upward, we'll always start by
            # checking the sequence: [3][0], [2][1], [1][2], [0][3]
            firstRowIndex = 3
            firstColIndex = 0
            lastRowIndex = 0
            lastColIndex = 3
            # Initialize this value to 1 for all remaining checks of consecutive, equal values.
            countNumConsec = 1

            # Initially, the checks for squatty arrays is the same as for the 'on/above diagonal'
            # portion of a square matrix. This happens until the max row index is reached.

            #============================================================#
            # Checking diagonals while the row index is still increasing #
            #============================================================#
            while (firstRowIndex < numRows):

                # This is a temporary list that we'll use to hold the values in each of the diagonals on or
                # above the diagonal.
                listToHoldDiagVals = []

                # We have to use this placeholder variable because we use the firstRowIndex value in the
                # range function to control the for loop.
                placeholderRowIndex = firstRowIndex

                # This for loop will iterate through each diagonal, adding the value to the temporary list.
                for i in range(firstRowIndex + 1):
                    listToHoldDiagVals.append(valsArray[placeholderRowIndex][i])
                    placeholderRowIndex -= 1

                # See if the sequence has 4 consec and equal values.
                for i in range(len(listToHoldDiagVals) - 1):
                    if (listToHoldDiagVals[i] == listToHoldDiagVals[i + 1]):
                        countNumConsec += 1
                    elif (listToHoldDiagVals[i] != listToHoldDiagVals[i + 1]):
                        countNumConsec = 1
                # If a sequence contains at least 4 consecutive, equal values, then return 'True' and quit checking.
                if (countNumConsec >= 4):
                    return True
                firstRowIndex += 1
                lastColIndex += 1



            #==============================================================#
            # Checking the 'middle diagonals' that are all the same length #
            #==============================================================#
            # The 'middle diagonals' are the ones up until (and incl) when the max col index is reached.

            # We need to reset these values (they are each incremented 1 too high since coming out of the
            # loop(s) above.)
            firstRowIndex = (numRows-1)
            lastColIndex = (numRows-1)
            firstColIndex = 1


            # The number of elements in the diagonals will always be this quantity.
            numElementsInDiag = (numRows-1)

            while(lastColIndex < (numCols-1)):

                # This is a temporary list that we'll use to hold the values in each of the diagonals on or
                # above the diagonal.
                listToHoldDiagVals = []

                # We have to use this placeholder variable because we use the firstRowIndex value in the
                # range function to control the for loop.
                placeholderRowIndex = firstRowIndex

                # This for loop will iterate through each diagonal, adding the value to the temporary list.
                for i in range(firstColIndex, (firstColIndex+numElementsInDiag+1), 1):
                    listToHoldDiagVals.append(valsArray[placeholderRowIndex][i])
                    placeholderRowIndex -= 1

                # Need to reset this once out of the loop
                placeholderRowIndex = firstRowIndex


                for i in range(len(listToHoldDiagVals) - 1):
                    if (listToHoldDiagVals[i] == listToHoldDiagVals[i + 1]):
                        countNumConsec += 1
                    elif (listToHoldDiagVals[i] != listToHoldDiagVals[i + 1]):
                        countNumConsec = 1
                # If a sequence contains at least 4 consecutive, equal values, then return 'True' and quit checking.
                if (countNumConsec >= 4):
                    return True
                lastColIndex += 1
                firstColIndex += 1
                
                
                
            #=============================================================#
            # Checking the 'below digaonal' equivalent for squatty arrays #
            #=============================================================#

            # Set these values to what they'll be for all squatty arrays.
            firstRowIndex = (numRows - 1)
            lastColIndex = (numCols - 1)

            # This doesn't need to be reset. It's correct coming out of the loop(s) above.
            firstColIndex = firstColIndex

            # This value will always be 1 for squatty arrays.
            lastRowIndex = 1

            # We need this value for the logic below
            numDiagsBelowMainDiag = numRows - 4

            numElementsInDiagMinus1 = numRows - 1
            while ((firstColIndex < (numCols-3)) and (lastRowIndex < (numDiagsBelowMainDiag + 1))):

                listToHoldDiagVals = []

                tempFirstColIndex = firstColIndex
                tempFirstRowIndex = firstRowIndex

                for i in range(numElementsInDiagMinus1):
                    listToHoldDiagVals.append(valsArray[tempFirstRowIndex][tempFirstColIndex])
                    tempFirstRowIndex -= 1
                    tempFirstColIndex += 1
                numElementsInDiagMinus1 -= 1


                for i in range(len(listToHoldDiagVals) - 1):
                    if (listToHoldDiagVals[i] == listToHoldDiagVals[i + 1]):
                        countNumConsec += 1
                    elif (listToHoldDiagVals[i] != listToHoldDiagVals[i + 1]):
                        countNumConsec = 1
                # If a sequence contains at least 4 consecutive, equal values, then return 'True' and quit checking.
                if (countNumConsec >= 4):
                    return True

                firstColIndex += 1
                lastRowIndex += 1
                
                
                
        ########################################################################################
        # TO CHECK ARRAYS THAT ARE TALLER THAN THEY ARE WIDE "TALL/SKINNY" (NUMROWS > NUMCOLS) #
        ########################################################################################
        else:
            
            # For checking the diagonals of arrays from left-to-right and moving upward, we'll always start by
            # checking the sequence: [3][0], [2][1], [1][2], [0][3]
            firstRowIndex = 3
            firstColIndex = 0
            lastRowIndex = 0
            lastColIndex = 3
            # Initialize this value to 1 for all remaining checks of consecutive, equal values.
            countNumConsec = 1
            
            
            # Initially, the checks for tall/skinny arrays is the same as for the 'on/above diagonal'
            # portion of a square matrix. This happens until the max col index is reached.

            #============================================================#
            # Checking diagonals while the col index is still increasing #
            #============================================================#
            while (lastColIndex < numCols):

                # This is a temporary list that we'll use to hold the values in each of the diagonals on or
                # above the diagonal.
                listToHoldDiagVals = []

                # We have to use this placeholder variable because we use the firstRowIndex value in the
                # range function to control the for loop.
                placeholderRowIndex = firstRowIndex

                # This for loop will iterate through each diagonal, adding the value to the temporary list.
                for i in range(firstRowIndex + 1):
                    listToHoldDiagVals.append(valsArray[placeholderRowIndex][i])
                    placeholderRowIndex -= 1


                for i in range(len(listToHoldDiagVals) - 1):
                    if (listToHoldDiagVals[i] == listToHoldDiagVals[i + 1]):
                        countNumConsec += 1
                    elif (listToHoldDiagVals[i] != listToHoldDiagVals[i + 1]):
                        countNumConsec = 1
                # If a sequence contains at least 4 consecutive, equal values, then return 'True' and quit checking.
                if (countNumConsec >= 4):
                    return True
                firstRowIndex += 1
                lastColIndex += 1

            
            # We need to slightly modify some of the index vars (since they were altered by the loop)
            # firstRowIndex and firstColIndex come out correctly, but lastRowIndex comes out as 0, needs to
            # be a 1, and lastColIndex comes out as (numCols+1) which is outside of bounds. lastColIndex
            # will be equal to numCols for the remainder of checking this array.
            lastRowIndex = 1
            lastColIndex = numCols
            
            
            #==============================================================#
            # Checking the 'middle diagonals' that are all the same length #
            #==============================================================#
            # The 'middle diagonals' are the ones up until (and incl) when the max col index is reached.

            # We need to reset this values (incremented 1 too high since coming out of the loop(s) above.)
            lastColIndex = (numRows-1)


            # The number of elements in the diagonals will always be this quantity for tall/skinny arrays.
            numElementsInDiag = (numCols)

            while(firstRowIndex < numRows):

                # This is a temporary list that we'll use to hold the values in each of the diagonals on or
                # above the diagonal.
                listToHoldDiagVals = []

                # We have to use this placeholder variable because we use the firstRowIndex value in the
                # range function to control the for loop.
                placeholderRowIndex = firstRowIndex

                # This for loop will iterate through each diagonal, adding the value to the temporary list.
                for i in range(numElementsInDiag):
                    listToHoldDiagVals.append(valsArray[placeholderRowIndex][i])
                    placeholderRowIndex -= 1



                for i in range(len(listToHoldDiagVals) - 1):
                    if (listToHoldDiagVals[i] == listToHoldDiagVals[i + 1]):
                        countNumConsec += 1
                    elif (listToHoldDiagVals[i] != listToHoldDiagVals[i + 1]):
                        countNumConsec = 1
                # If a sequence contains at least 4 consecutive, equal values, then return 'True' and quit checking.
                if (countNumConsec >= 4):
                    return True
                lastRowIndex += 1
                firstRowIndex += 1
                
            
            
            #=================================================================#
            # Checking the 'below digaonal' equivalent for tall/skinny arrays #
            #=================================================================#
            
            # Set these values to what they'll be for all tall/skinny arrays.
            firstRowIndex = (numRows - 1)
            firstColIndex = 1
            lastColIndex = (numCols - 1)

            # We need this value for the logic below
            numDiagsBelowMainDiag = numCols - 4

            numElementsInDiagMinus1 = numCols - 1
            while ((firstColIndex < (numCols-3)) and (lastRowIndex < (numRows-3))):

                listToHoldDiagVals = []

                tempFirstColIndex = firstColIndex
                tempFirstRowIndex = firstRowIndex

                for i in range(numElementsInDiagMinus1):
                    listToHoldDiagVals.append(valsArray[tempFirstRowIndex][tempFirstColIndex])
                    tempFirstRowIndex -= 1
                    tempFirstColIndex += 1
                numElementsInDiagMinus1 -= 1


                for i in range(len(listToHoldDiagVals) - 1):
                    if (listToHoldDiagVals[i] == listToHoldDiagVals[i + 1]):
                        countNumConsec += 1
                    elif (listToHoldDiagVals[i] != listToHoldDiagVals[i + 1]):
                        countNumConsec = 1
                # If a sequence contains at least 4 consecutive, equal values, then return 'True' and quit checking.
                if (countNumConsec >= 4):
                    return True

                firstColIndex += 1
                lastRowIndex += 1
                
                
                
                
                
                
                
                
                
                
# This function checks all diagonals that are oriented from left-to-right and read downward from the left to 
# the right.
def checkLeftToRightDownwardDiagonals(valsArray, numRows, numCols):
    
    
    # There's no point in checking any diagonals if there aren't at least 4 rows and 4 columns, because
    # there can't be a diagonal at least 4 long is this is the case.
    if( (numRows < 4) or (numCols < 4) ):
        return False
    

    # The only way to enter the 'else' statement is if both (numRows >= 4) and (numCols >= 4), so we can 
    # rest assured that there's at least one l-to-r-upward diagonal to check.
    else:
        
        # For checking the diagonals of arrays from left-to-right and moving upward, we'll always start by
        # checking the sequence: [numRows-4][0], [numRows-3][1], [numRows-2][2], [numRows-1][3]
        firstRowIndex = (numRows-4)
        firstColIndex = 0
        lastRowIndex = (numRows-1)
        lastColIndex = 3
        # Initialize this value to 1 for all remaining checks of consecutive, equal values.
        countNumConsec = 1          
        
        

        ###################################################################
        # TO CHECK ARRAYS THAT HAVE EQUAL DIMENSIONS (NUMROWS == NUMCOLS) #
        ###################################################################
        if (numRows == numCols):
            
            #==============================================================#
            # first, check diagonals that are 'below/on the main diagonal' #
            #==============================================================#
            while((firstRowIndex >= 0) and (lastColIndex < numCols)):
                
                # This is a temporary list that we'll use to hold the values in each of the diagonals on or
                # above the diagonal.
                listToHoldDiagVals = []
                
                # We have to use this placeholder variable because we use the firstRowIndex value in the
                # range function to control the for loop.
                placeholderRowIndex = firstRowIndex
                
                # This for loop will iterate through each diagonal, adding the value to the temporary list.
                for i in range(lastColIndex+1):
                    listToHoldDiagVals.append(valsArray[placeholderRowIndex][i])
                    placeholderRowIndex += 1
                                
                
                for i in range(len(listToHoldDiagVals)-1):
                    if(listToHoldDiagVals[i] == listToHoldDiagVals[i+1]):
                        countNumConsec += 1
                    elif(listToHoldDiagVals[i] != listToHoldDiagVals[i+1]):
                        countNumConsec = 1
                  # If a sequence contains at least 4 consecutive, equal values, then return 'True' and quit checking.
                if(countNumConsec >= 4):
                    return True
                firstRowIndex -= 1
                lastColIndex += 1
              
            
            #==========================================================#
            # next, check diagonals that are 'above the main diagonal' #
            #==========================================================#

            
            # Need to reset some values that came out of the above loop and are incorrect as is.
            # Also create some variables that will control logic for the code below.
            firstRowIndex = 0
            firstColIndex = 1
            lastColIndex = (numCols-1)
            numDiagsAboveMainDiag = numRows-4
            numElementsInDiagMinus1 = numRows-1
            
            while( (firstColIndex < (numDiagsAboveMainDiag+1)) and (lastRowIndex >  (numDiagsAboveMainDiag)) ):
                
                listToHoldDiagVals = []
                
                tempFirstColIndex = firstColIndex
                tempFirstRowIndex = firstRowIndex
                
                for i in range(numElementsInDiagMinus1):
                    listToHoldDiagVals.append(valsArray[tempFirstRowIndex][tempFirstColIndex])
                    tempFirstColIndex += 1
                    tempFirstRowIndex += 1
                numElementsInDiagMinus1 -= 1
                                    
                    
                for i in range(len(listToHoldDiagVals) - 1):
                    if (listToHoldDiagVals[i] == listToHoldDiagVals[i + 1]):
                        countNumConsec += 1
                    elif (listToHoldDiagVals[i] != listToHoldDiagVals[i + 1]):
                        countNumConsec = 1
                # If a sequence contains at least 4 consecutive, equal values, then return 'True' and quit checking.
                if (countNumConsec >= 4):
                    return True

                firstColIndex += 1
                lastRowIndex -= 1
            
            

        ###################################################################################
        # TO CHECK ARRAYS THAT ARE WIDER THAN THEY ARE TALL "SQUATTY" (NUMROWS < NUMCOLS) #
        ###################################################################################
        elif (numRows < numCols):
            
            
            # For checking the diagonals of arrays from left-to-right and moving upward, we'll always start by
            # checking the sequence: [numRows-4][0], [numRows-3][1], [numRows-2][2], [numRows-1][3]
            firstRowIndex = (numRows-4)
            firstColIndex = 0
            lastRowIndex = (numRows-1)
            lastColIndex = 3
            # Initialize this value to 1 for all remaining checks of consecutive, equal values.
            countNumConsec = 1         


            # Initially, the checks for squatty arrays is the same as for the 'on/below diagonal'
            # portion of a square array. This happens until the min firstRowIndex is reached.

            #==============================================================#
            # first, check diagonals that are 'below/on the main diagonal' #
            #==============================================================#
            while(firstRowIndex >= 0):
                
                # This is a temporary list that we'll use to hold the values in each of the diagonals on or
                # above the diagonal.
                listToHoldDiagVals = []
                
                # We have to use this placeholder variable because we use the firstRowIndex value in the
                # range function to control the for loop.
                placeholderRowIndex = firstRowIndex
                
                # This for loop will iterate through each diagonal, adding the value to the temporary list.
                for i in range(lastColIndex+1):
                    listToHoldDiagVals.append(valsArray[placeholderRowIndex][i])
                    placeholderRowIndex += 1
                                
                
                for i in range(len(listToHoldDiagVals)-1):
                    if(listToHoldDiagVals[i] == listToHoldDiagVals[i+1]):
                        countNumConsec += 1
                    elif(listToHoldDiagVals[i] != listToHoldDiagVals[i+1]):
                        countNumConsec = 1
                  # If a sequence contains at least 4 consecutive, equal values, then return 'True' and quit checking.
                if(countNumConsec >= 4):
                    return True
                firstRowIndex -= 1
                lastColIndex += 1
            

            #==============================================================#
            # Checking the 'middle diagonals' that are all the same length #
            #==============================================================#
            # The 'middle diagonals' are the ones up until (and incl) when the max col index is reached.

            # We need to reset these values.
            firstRowIndex = 0
            firstColIndex = 1


            # The number of elements in the diagonals will always be this quantity.
            numElementsInDiag = numRows

            while(lastColIndex < numCols):

                # This is a temporary list that we'll use to hold the values in each of the diagonals on or
                # above the diagonal.
                listToHoldDiagVals = []

                # We have to use this placeholder variable because we use the firstRowIndex value in the
                # range function to control the for loop.
                placeholderRowIndex = firstRowIndex

                # This for loop will iterate through each diagonal, adding the value to the temporary list.
                for i in range(firstColIndex, (firstColIndex+numElementsInDiag), 1):
                    listToHoldDiagVals.append(valsArray[placeholderRowIndex][i])
                    placeholderRowIndex += 1
                    

                # Need to reset this once out of the loop
                placeholderRowIndex = firstRowIndex


                for i in range(len(listToHoldDiagVals) - 1):
                    if (listToHoldDiagVals[i] == listToHoldDiagVals[i + 1]):
                        countNumConsec += 1
                    elif (listToHoldDiagVals[i] != listToHoldDiagVals[i + 1]):
                        countNumConsec = 1
                # If a row contains at least 4 consecutive, equal values, then return 'True' and quit checking.
                if (countNumConsec >= 4):
                    return True
                lastColIndex += 1
                firstColIndex += 1
                

    
            #==========================================================#
            # next, check diagonals that are 'above the main diagonal' #
            #==========================================================#

            # Need to reset some values that came out of the above loop and are incorrect as is.
            # Also create some variables that will control logic for the code below.
            lastColIndex -= 1
            lastRowIndex -= 1
            numDiagsAboveMainDiag = numRows-4
            numElementsInDiagMinus1 = numRows-1
            
            while(firstColIndex < (numCols-3)):
                
                listToHoldDiagVals = []
                
                tempFirstColIndex = firstColIndex
                tempFirstRowIndex = firstRowIndex
                
                for i in range(numElementsInDiagMinus1):
                    listToHoldDiagVals.append(valsArray[tempFirstRowIndex][tempFirstColIndex])
                    tempFirstColIndex += 1
                    tempFirstRowIndex += 1
                numElementsInDiagMinus1 -= 1
                                    
                for i in range(len(listToHoldDiagVals) - 1):
                    if (listToHoldDiagVals[i] == listToHoldDiagVals[i + 1]):
                        countNumConsec += 1
                    elif (listToHoldDiagVals[i] != listToHoldDiagVals[i + 1]):
                        countNumConsec = 1
                # If a sequence contains at least 4 consecutive, equal values, then return 'True' and quit checking.
                if (countNumConsec >= 4):
                    return True

                firstColIndex += 1
                lastRowIndex -= 1
     

       
        ########################################################################################
        # TO CHECK ARRAYS THAT ARE TALLER THAN THEY ARE WIDE "TALL/SKINNY" (NUMROWS > NUMCOLS) #
        ########################################################################################
        else:
            
            # For checking the diagonals of arrays from left-to-right and moving upward, we'll always start by
            # checking the sequence: [numRows-4][0], [numRows-3][1], [numRows-2][2], [numRows-1][3]
            firstRowIndex = (numRows-4)
            firstColIndex = 0
            lastRowIndex = (numRows-1)
            lastColIndex = 3
            # Initialize this value to 1 for all remaining checks of consecutive, equal values.
            countNumConsec = 1     
            
            
            # Initially, the checks for tall/skinny arrays is the same as for the 'on/below diagonal'
            # portion of a square array. This happens until the max lastColIndex is reached.

            #==============================================================#
            # first, check diagonals that are 'below/on the main diagonal' #
            #==============================================================#
            while(lastColIndex < numCols):
                
                # This is a temporary list that we'll use to hold the values in each of the diagonals on or
                # above the diagonal.
                listToHoldDiagVals = []
                
                # We have to use this placeholder variable because we use the firstRowIndex value in the
                # range function to control the for loop.
                placeholderRowIndex = firstRowIndex
                
                # This for loop will iterate through each diagonal, adding the value to the temporary list.
                for i in range(lastColIndex+1):
                    listToHoldDiagVals.append(valsArray[placeholderRowIndex][i])
                    placeholderRowIndex += 1
                                
                
                for i in range(len(listToHoldDiagVals)-1):
                    if(listToHoldDiagVals[i] == listToHoldDiagVals[i+1]):
                        countNumConsec += 1
                    elif(listToHoldDiagVals[i] != listToHoldDiagVals[i+1]):
                        countNumConsec = 1
                  # If a sequence contains at least 4 consecutive, equal values, then return 'True' and quit checking.
                if(countNumConsec >= 4):
                    return True
                firstRowIndex -= 1
                lastColIndex += 1

            
            #==============================================================#
            # Checking the 'middle diagonals' that are all the same length #
            #==============================================================#
            # The 'middle diagonals' are the ones up until (and incl) when the max col index is reached.

            # We need to reset these values.
            lastColIndex = (numCols-1)
            lastRowIndex = (numRows-2)


            # The number of elements in the diagonals will always be this quantity.
            numElementsInDiag = numCols

            while(firstRowIndex >= 0):

                # This is a temporary list that we'll use to hold the values in each of the diagonals on or
                # above the diagonal.
                listToHoldDiagVals = []

                # We have to use this placeholder variable because we use the firstRowIndex value in the
                # range function to control the for loop.
                placeholderRowIndex = firstRowIndex

                # This for loop will iterate through each diagonal, adding the value to the temporary list.
                for i in range(firstColIndex, (firstColIndex+numElementsInDiag), 1):
                    listToHoldDiagVals.append(valsArray[placeholderRowIndex][i])
                    placeholderRowIndex += 1
                    

                # Need to reset this once out of the loop
                placeholderRowIndex = firstRowIndex


                for i in range(len(listToHoldDiagVals) - 1):
                    if (listToHoldDiagVals[i] == listToHoldDiagVals[i + 1]):
                        countNumConsec += 1
                    elif (listToHoldDiagVals[i] != listToHoldDiagVals[i + 1]):
                        countNumConsec = 1
                # If a sequence contains at least 4 consecutive, equal values, then return 'True' and quit checking.
                if (countNumConsec >= 4):
                    return True
                firstRowIndex -= 1
                lastRowIndex -= 1
                
            
            #==========================================================#
            # next, check diagonals that are 'above the main diagonal' #
            #==========================================================#

            # Need to reset some values that came out of the above loop and are incorrect as is.
            # Also create some variables that will control logic for the code below.
            firstRowIndex = 0
            firstColIndex = 1

            numDiagsAboveMainDiag = numCols-4
            numElementsInDiag = numCols-1
            
            while(firstColIndex < (numCols-3)):
                
                listToHoldDiagVals = []
                
                tempFirstColIndex = firstColIndex
                tempFirstRowIndex = firstRowIndex
                
                for i in range(numElementsInDiag):
                    listToHoldDiagVals.append(valsArray[tempFirstRowIndex][tempFirstColIndex])
                    tempFirstColIndex += 1
                    tempFirstRowIndex += 1
                numElementsInDiag -= 1
                                    
                for i in range(len(listToHoldDiagVals) - 1):
                    if (listToHoldDiagVals[i] == listToHoldDiagVals[i + 1]):
                        countNumConsec += 1
                    elif (listToHoldDiagVals[i] != listToHoldDiagVals[i + 1]):
                        countNumConsec = 1
                # If a sequence contains at least 4 consecutive, equal values, then return 'True' and quit checking.
                if (countNumConsec >= 4):
                    return True

                firstColIndex += 1
                lastRowIndex -= 1
                
                
                
                
                
                
                
                
                
# This function calls the other 4 functions that I've written above to check: rows, cols, lTOrUP diags, and lTOrDOWN diags.             
def isConsecutiveFour(valsArray, numRows, numCols):
    
    # Setting up some boolean variables to control logic of the function.
    rowsBool = checkRowsForConsecutive(valsArray, numRows, numCols)
    colsBool = checkColsForConsecutive(valsArray, numRows, numCols)
    lTOrUPdiagsBool = checkLeftToRightUpwardDiagonals(valsArray, numRows, numCols)
    lTOrDOWNdiagsBool = checkLeftToRightDownwardDiagonals(valsArray, numRows, numCols)
    
    # If any of the 4 fctns find a sequence of 4 equal values the user will get a message.
    if(checkRowsForConsecutive(valsArray, numRows, numCols)):
        print("There is (at least) one sequence of four, consecutive, equal values in one of the rows.")
    if(checkColsForConsecutive(valsArray, numRows, numCols)):
        print("There is (at least) one sequence of four, consecutive, equal values in one of the columns.")
    if(checkLeftToRightUpwardDiagonals(valsArray, numRows, numCols)):
        print("There is (at least) one sequence of four, consecutive equal values in one of the L-to-R-up diagonals.")
    if(checkLeftToRightDownwardDiagonals(valsArray, numRows, numCols)):
        print("There is (at least) one sequence of four, consecutive equal values in one of the L-to-R-down diagonals.")
    
    
    # The function either returns 'True' if one of the 4 nested fctns called returns True, or 'False' otherwise.
    if(rowsBool or colsBool or lTOrUPdiagsBool or lTOrDOWNdiagsBool):
        return True
    else:
        print("There are no sequences of four, consecutive equal values.")
        return False
    
    
    
    
    
    
    
    
    
    
# main function definition
def main():

    
    ###=================================###
    ### USER INPUT RE: ARRAY DIMENSIONS ###
    ###=================================###
    
    # Initialize these values to something that will force entry into the while loop below.
    userNumRows = userNumCols = 0.5

    # Make sure the user puts in valid info:
    #   -- can't possibly have four consecutive, equal values if both rows and columns are < 4
    #   -- the values for numRows and numCols must be integers
    while( ((userNumRows < 4) and (userNumCols < 4)) or
           ((userNumRows%1) != 0) or
           ((userNumCols%1) != 0)):

        userNumRows = eval(input("Enter the number of rows you want to have: "))
        userNumCols = eval(input("Enter the number of columns you want to have: "))



    ###=====================###
    ### OBTAINING THE ARRAY ###
    ###=====================###
    
    # Give this variable a value that will force the program into the while loop.
    generateArrayRandomly = "q"

    while( (generateArrayRandomly != "y") and (generateArrayRandomly != "n") ):
        print("\nWould you like the values of the array to be generated randomly?")
        generateArrayRandomly = input("Please enter either 'y' or 'n': ")
        print()


    # initalize an empty array
    arrayToCheck = [[]]*userNumRows
    # Initialize an empty list to initially store all the values (we'll break it down, put in the array.)
    listOfValsInArray = []
    # Create this constant for ease of use in programming further logic.
    totalElementsInArray = (userNumRows * userNumCols)


    # If the user wants values randomly generated, enter this 'if' statement.
    if (generateArrayRandomly == "y"):

        # This for loop randomly generates all the values in the array (but in a single 1-d list)
        for i in range(totalElementsInArray):
            listOfValsInArray.append(rand.randint(0, 9))

        # This for loop breaks the 1-d list into the 'row lists' in the array.
        for i in range(userNumRows):
            arrayToCheck[i] = listOfValsInArray[(i*userNumCols):(i*userNumCols+userNumCols)]
            
            
    # if the user doesn't want the values generated randomly        
    else:
        # I'm going to assume that all values entered are valid. I tried to code input validation conditions,
        # but it was a giant pain in the butt, and I don't think that it was at all specified for the asmt.
        while((len(listOfValsInArray) != totalElementsInArray)):
            print("Please enter all values (0-9) in the array with commas in between them. Hit enter when finished.")
            print("For example, for a 4x4 array with same values in each row enter: 1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4")
            listOfValsInArray = eval(input("Enter the values here: "))
 
        # This for loop breaks the 1-d list into the 'row lists' in the array.
        for i in range(userNumRows):
            arrayToCheck[i] = listOfValsInArray[(i*userNumCols):(i*userNumCols+userNumCols)]
        
    print()
    print("\n\nBelow is the 2-dimensional list to be checked:")
    for i in range(userNumRows):
        print(arrayToCheck[i])
    


    ###===========================================###
    ### CHECKING THE ARRAY FOR CONSECUTIVE VALUES ###
    ###===========================================###
    print("\nRESULTS")
    isConsecutiveFour(arrayToCheck, userNumRows, userNumCols)
    







# call the main function
main()