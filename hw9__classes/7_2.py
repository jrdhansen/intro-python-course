# CS 1400, HOMEWORK 9, file 1
# DUE: Thursday, 03/22/2018 at 11:59 pm

# NAME:       Jared Hansen
# A-NUMBER:   A01439768
# SECTION:    CS-1400-002
# RECITATION: CS-1400-515





# Problem 7_2





'''
PROGRAM TITLE: Stock Info (The Stock Class)

Design a class named Stock to represent a company's stock that contains:

-- A private string data field named 'symbol' for the stock's symbol.
-- A private string data field named 'name' for the stock's name.
-- A private float data field named 'previousClosingPrice' that stores the stock price for
   the previous day.
-- A private float data field named 'currentPrice' that stores the stock price for the
   current time.
-- A constructor that creates a stock with the specified symbol, name, previous price, and
   current price.
-- A get method for returning the stock name.
-- A get method for returning the stock symbol.
-- Get and set methods for getting/setting the stock's previous price.
-- Get and set methods for getting/setting the stock's current price.
-- A method named 'getChangePercent()' that returns the percentage changed from
   'previousClosingPrice' to 'currentPrice.'
   
   
Draw the UML diagram for the class, and then implement the class. Write a test program that
creates a Stock object with the stock symbol INTC, the name Intel Corporation, the previous
closing price 20.5, and the new current price of 20.35, and display the price-change
percentage.
'''







'''
HERE IS MY UML DIAGRAM

--------------------------------------------------------------------------------------------------------|
        Stock                                                                <-- CLASS NAME             |
--------------------------------------------------------------------------------------------------------|
symbol:string                                                                 <-- DATA FIELDS           |
name: string                                                                           <-/              |
previousClosingPrice: float                                                           <-/               |
currentPrice: float                                                                  <-/                |
--------------------------------------------------------------------------------------------------------|
Stock(symbol:string, name:string, previousClosingPrice:float, currentPrice:float)   <-- CONSTRUCTOR     |
getStockName(): string                                                              <-- METHODS         |
getSymbol(): string                                                                   <-/               |
getPrevClosingPrice(): float                                                         <-/                |
setPrevClosingPrice(previousClosingPrice:float): None                               <-/                 |
getStockCurrPrice(): float                                                         <-/                  |
setStockCurrPrice(currentPrice:float): None                                       <-/                   |
getChangePercent(): float                                                        <-/                    |
--------------------------------------------------------------------------------------------------------|
'''





# Here is our definition of the Stock class.
class Stock:

    # Constructor function, with 4 private data fields.
    def __init__(self, symbol, name, previousClosingPrice, currentPrice):
        self.__symbol = symbol
        self.__name = name
        self.__previousClosingPrice = previousClosingPrice
        self.__currentPrice = currentPrice

    # Accessor (getter) function for the stock's name.
    def getStockName(self):
        return self.__name

    # Accessor (getter) function for the stock's symbol.
    def getSymbol(self):
        return self.__symbol

    # Accessor (getter) function for the stock's previous closing price.
    def getPrevClosingPrice(self):
        return self.__previousClosingPrice

    # Mutator (setter) function for the stock's previous closing price.
    def setPrevClosingPrice(self, prevClsPrc):
        self.previousClosingPrice = prevClsPrc

    # Accessor(getter) function for the stock's current price.
    def getStockCurrPrice(self):
        return self.__currentPrice

    # Mutator (setter) function for the stock's current price.
    def setStockCurrPrice(currentPrice):
        self.currentPrice = currentPrice

    # Function that calculates the percent change between currentPrice and previousClosingPrice.
    def getChangePercent(self):
        return (((self.__currentPrice - self.__previousClosingPrice)/(self.__previousClosingPrice))*100)
        
        



#       Per the books' instructions: "Write a test program that creates a Stock object with the stock
# symbol INTC, the name Intel Corporation, the previous closing price 20.5, and the new current price of
# 20.35, and display the price-change percentage.
def main():

    # Creating a Stock object (called intelStock) that has the desired arguments.
    intelStock = Stock("INTC", "Intel Corporation", 20.5, 20.35)

    # Print the price-change percentage. Didn't specify how to format the percentage, so I left it as is.
    print("The price-change percentage is: ", intelStock.getChangePercent(), "%", sep = '')





# call the main function
main()





input("Press any key to continue")