import random

class Deck():

    def __init__(self):      
        self.deck = []

    def getDeck(self):
        return self.deck
    
    def loadDeck(self):
        #load all 52 cards into the deck.
        #should not be allowed to be called by the player
        #will represent the cards as a 4 digit string encoded as example: 0000
        # 0000 = two of hearts as Card.getSuit(0) == Hearts, Card.getRank(0) == 2
        # 0105 = seven of Clubs as Card.getSuit(1) == Clubs, Card.getRank(5) == 7
        for x in range(0,4):
            for y in range(0,13):
                if y < 10:
                    self.deck.append('0'+str(x)+'0'+str(y))
                else:
                    self.deck.append('0'+str(x)+str(y))
    
    def shuffleDeck(self):
        #after loading cards into the deck, randomizes the order of the cards
        #run the randomizer a few times.
        for x in range(0,7):
            random.shuffle(self.deck)
            #print(self.deck)
    
    def resetDeck(self):
        #not for use in player class
        self.deck = []
        self.loadDeck()

    def dealCard(self):
        #esures deck has a card before attempting to pop
        if self.deck:
            return self.deck.pop()

# if __name__ == "__main__":
#     d = Deck()
#     d.loadDeck()
#     print(d.deck)
#     d.shuffleDeck()

#     while d.deck:
#         print(d.dealCard())

#     d.resetDeck()
#     print(d.deck)

    

    


    
