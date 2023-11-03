class Cards():

    #No need for parameter as Cards will only ever have
    #4 suits
    #13 ranks
    #deck will use cards to build out the deck.
    #because the cards are never added to/reassigned only get methods required
    def __init__(self):
        self.suit = ['Hearts','Clubs','Spades','Diamonds']
        self.rank = ['2','3','4','5','6','7','8','9','10','Jack','Queen','King','Ace']

    def getSuit(self, check):
        return self.suit[check]
    
    def getRank(self, check):
        return self.rank[check]
    
    def getRankAsInt(self,player_card):
        rank = player_card[2:4]

        if rank[0] == '0':
            rank = rank[1:]
        return int(rank)


    def getCardString(self, player_card):
        suit = player_card[1]
        rank = player_card[2:4]

        if rank[0] == '0':
            rank = rank[1:]

        return self.getRank(int(rank)) + ' of ' + self.getSuit(int(suit))



