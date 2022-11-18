# CS 1400, HOMEWORK 10, file 2
# DUE: Thursday, 04/12/2018 at 11:59 pm

# NAME:       Jared Hansen
# A-NUMBER:   A01439768
# SECTION:    CS-1400-002
# RECITATION: CS-1400-515




# Problem 10_22





'''
PROGRAM TITLE: "Simulation: coupon collector's problem"

Coupon Collector is a classic statistics problem with many practical applications. The problem is to pick objects from a set
of objects repeatedly and find out how many picks are needed for all the objects to be picked at least once. A variation of 
the problem is to pick cards from a shuffled deck of 52 cards repeatedly and find out how many picks are needed before you
see one of each suit. Assume a picked card is placed back in the deck before picking another. Write a program to simulate the
number of picks needed to get four cards, one from each suit, and display the 4 cards picked (it is possible a card may be
picked twice). Here is a sample run of the program:
    
    -- Queen of Spades
    -- 5 of Clubs
    -- Queen of Hearts
    -- 4 of Diamonds
    -- Number of picks: 12
    
'''




# We'll need the 'random' library to shuffle the deck and draw cards, so let's import it.
import random as rand




# This function 'draws a card' by returning a random integer x, such that 0 <= x <= 51
# (The integer returned is used to take the xth element of the deck list as a draw.)
def drawCard():
    return rand.randint(0,51)




# This function is simply used to shuffle the deck list.
def shuffleDeck(cardsList):
    return rand.shuffle(cardsList)










# main function definition.
def main():
    
    # Lists with strings used to create the deck list.
    suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
    faceValues = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
    
    
    # Initialize an empty list 'deck' to store the names of the cards in.
    deck = []
    
    
    # Populate the deck.
    for i in suits:
        for j in faceValues:
            deck.append(j + " of " + i)
            
                
    # Shuffle the deck.
    shuffleDeck(deck)
    
    
    # Initialize counter variables to 0.
    numCardsDrawn = 0
    numHeartsDrawn = 0
    numDiamondsDrawn = 0
    numClubsDrawn = 0
    numSpadesDrawn = 0
    
    
    # Initalize an empty list to keep track of drawn cards.
    cardsDrawn = []
    
    
    # Initialize an empty list to keep track of the first cards drawn from each suit.
    firstCardFromEachSuit = []
    
    
    
    # Draw cards until we have one from each suit. Add each draw to the appropriate list(s).
    while( (numHeartsDrawn == 0) or (numDiamondsDrawn == 0) or (numClubsDrawn == 0) or (numSpadesDrawn == 0) ):
        
        # Append the drawn card to the list of (other) drawn cards)
        cardsDrawn.append(deck[drawCard()])
        
        # Check to see the suit of each draw, and increment the appropriate counter variable. Also, if it's the first draw
        # of a given suit, add that draw to the 'firstCardFromEachSuit' list.
        if("Hearts" in cardsDrawn[numCardsDrawn]):
            if(numHeartsDrawn == 0):
                firstCardFromEachSuit.append(cardsDrawn[numCardsDrawn])
            numHeartsDrawn += 1
        elif("Diamonds" in cardsDrawn[numCardsDrawn]):
            if(numDiamondsDrawn == 0):
                firstCardFromEachSuit.append(cardsDrawn[numCardsDrawn])
            numDiamondsDrawn += 1
        elif("Clubs" in cardsDrawn[numCardsDrawn]):
            if(numClubsDrawn == 0):
                firstCardFromEachSuit.append(cardsDrawn[numCardsDrawn])
            numClubsDrawn += 1
        else:
            if(numSpadesDrawn == 0):
                firstCardFromEachSuit.append(cardsDrawn[numCardsDrawn])
            numSpadesDrawn += 1
        
        # Increment the counter variable keeping track of how many cards have been drawn.
        numCardsDrawn += 1





    # Print the desired output: the first card drawn from each suit, and the number of draws it took to get at least one
    # card from each suit.
    print()
    print("The first card from each suit was:")
    print("\t", firstCardFromEachSuit[0])
    print("\t", firstCardFromEachSuit[1])
    print("\t", firstCardFromEachSuit[2])
    print("\t", firstCardFromEachSuit[3])
    print("The number of cards drawn to get at least one of each suit was:", numCardsDrawn)







# Call the main function
main()