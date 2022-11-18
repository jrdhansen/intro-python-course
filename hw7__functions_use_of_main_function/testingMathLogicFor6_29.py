

number = 4388576018402626



number = 12345




# Return the number of digits in d
def getSize(d):
    digits = 1
    while (d > 10):
        d = (d - d%10)//(10)
        digits += 1
    return digits
    







'''
def sumOfDoubleEvenPlace(number):
    
    counter = 2
    num = 0
    sumOfDoubleEvens = 0
    while(getSize(number) >= counter):
        num = str(number)
        digit = num[getSize(number) - (counter)]
        digit = int(digit)
        sumOfDoubleEvens += getDigit(digit)
        counter += 2
        print("sumOfDoubleEvens:", sumOfDoubleEvens)

        
    return sumOfDoubleEvens
'''
    
    
'''
def sumOfDoubleEvenPlace(number):
    sumOfDoubleEvens = 0
    while(number > 0):
        lengthOfNumber = getSize(number)
        number = str(number)
        digit = number[lengthOfNumber - 2]
        print("Digit is:", digit)
        sumOfDoubleEvens += getDigit(digit)
        print("sumOfDoubleEvens:", sumOfDoubleEvens)
        
'''


def sumOfDoubleEvenPlace(number):
    sumOfDoubleEvens = 0
    digit = 0
    while(number > 0):
        digit = (number - ((((number//100)*100)) + ((number - (number//10)*10)))) / 10
        print("stripped out digit is:", digit)
        digit = getDigit(digit)
        print("getDigit(digit) is:", digit)
        sumOfDoubleEvens += digit
        number = (number//100)

    return sumOfDoubleEvens




    
    
    
# Returns the number if it is a single digit, otherwise, return the sum of the two digits.
def getDigit(number):
    if (number*2 < 10):
        return (2*number) 
    else:
        num1 = (number*2)//10
        num2 = (number*2)%10
        number = (num1 + num2)
        return number
     
    
    
    
    
def sumOfOddPlace(number):
    sumOfOdds = 0
    while(number > 0):
        sumOfOdds += number - ((number//10)*10)
        print("SumOfOdds:", sumOfOdds)
        number = (number//100)
        print("Number:", number)
    return sumOfOdds
    
    
    
    
    





print(sumOfDoubleEvenPlace(number))
print(sumOfOddPlace(number))

