# CS 1400, HOMEWORK 4, file 1
# DUE: Thursday, 02/08/2018 at 11:59 pm

# NAME:       Jared Hansen
# A-NUMBER:   A01439768
# SECTION:    CS-1400-002
# RECITATION: CS-1400-515


# Problem 3_9

'''
DESCRIPTION: "Financial Application: Payroll"

Write a program that reads in the following information and prints a payroll statement:
    Employee's name (e.g. Smith)
    Number of hours worked in a week (e.g., 10)
    Hourly pay rate (e.g., 9.75)
    Federal tax withholding rate (e.g., 20%)
    State tax withholding rate (e.g., 9%)
    
Here is a sample run:
    Enter employee's name: Smith
    Enter number of hours worked in a week: 10
    Enter hourly pay rate:
    Enter Federal tax withholding rate: 0.20
    Enter State withholding rate: 0.09
    
    (prints out)
    Employee Name: Smith
    Hours Worked: 10.0
    Pay Rate: $9.75
    Gross Pay: $97.50
    Deduction:
        Federal withholding (20.0%): $19.5
        State withholding (9.0%): $8.77
        Total deduction: $28.27
    Net Pay: $69.22


'''




############################
## OBTAIN AND STORE INPUT ##
############################

empName   = input("Enter the employee's last name: ")
numHours  = eval(input("Enter the number of hours worked this week: "))
payRate   = eval(input("Enter the hourly pay rate in the form dollars.cents: "))
fedRate   = eval(input("Enter the Federal tax rate in the\nform 0.__ (where 20% would be 0.2): "))
stateRate = eval(input("Enter the State tax rate in the\nform 0.__ (where 9% would be 0.09): "))
print("\n\n")





##########################
## CALCULATE QUANTITIES ##
##########################

grossPay   = numHours*payRate
fedTheft   = grossPay*fedRate
stateTheft = grossPay*stateRate
totalTheft = fedTheft+stateTheft
netPay     = grossPay-totalTheft






############################
## PRINT FORMATTED OUTPUT ##
############################
print("Employee name: ", empName)
print("Hours worked this week: ", numHours, sep = "")
print("Pay Rate: $", format(payRate, ".2f"), sep = "")
print("Gross Pay: $", format(grossPay, ".2f"), sep = "")
print("Deductions:")
print("\tFederal withholding (", format(fedRate, "2.1%"), "): $", format(fedTheft, "0.2f"), sep = "")
print("\tState withholding (", format(stateRate, "2.1%"), "): $", format(stateTheft, "0.2f"), sep = "")
print("\tTotal deduction: $", format(totalTheft, "0.2f"), sep = "")
print("Net Pay: $", format(netPay, "0.2f"), sep = "")



# In the case of runnning this program in the console, I'm including this extra
# line so that the output can be seen before the program closes.
input("Press any key to continue")
