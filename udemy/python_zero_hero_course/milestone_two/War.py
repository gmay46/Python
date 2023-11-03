from Cards import Cards
from Deck import Deck
from Player import Player

class War():
    def __init__(self):
        self.deck = Deck()
        self.cards = Cards()
        self.player1 = Player()
        self.player2 = Player()
    
    def setup(self):
        self.deck.loadDeck()
        self.deck.shuffleDeck()
        while self.deck.getDeck():
            self.player1.hand_won(self.deck.dealCard())
            self.player2.hand_won(self.deck.dealCard())
    

    def reset_winning_hands(self):
            self.player1.war_hand = []
            self.player2.war_hand = []


    def play_hand(self):
        self.player1.draw_card()
        self.player2.draw_card()

        p1_card = self.player1.get_drawn_card()
        p2_card = self.player2.get_drawn_card()

        print(p1_card + " " + p2_card)
        print("Player One: ")
        print(self.cards.getCardString(p1_card))
        print("war hand: ")
        print(self.player1.war_hand)
        print("-------------")
        print("Player Two:")
        print(self.cards.getCardString(p2_card))
        print("war hand: ")
        print(self.player2.war_hand)
        print("-------------")

        p1_card_rank = self.cards.getRankAsInt(p1_card)
        p2_card_rank = self.cards.getRankAsInt(p2_card)


        if p1_card_rank == p2_card_rank:
            #war logic here
            print("Time for a WAR!")
            print("WWWWWWWWAAAAAAAGGGGGGGGGGGGGGGGGHHHHHHHHHHHHHHHH!")
            self.player1.ready_player_for_war()
            self.player2.ready_player_for_war()
        elif p1_card_rank > p2_card_rank:
            print("Player 1 takes the hand!")
            self.player1.hand_won(self.player2.get_drawn_card())
            self.player1.hand_won(self.player1.get_drawn_card())
            self.player1.war_won(self.player2.war_hand)
            self.player1.war_won(self.player1.war_hand)
            self.reset_winning_hands()
        elif p1_card_rank < p2_card_rank:
            print("Player 2 takes the hand!")
            self.player2.hand_won(self.player1.get_drawn_card())
            self.player2.hand_won(self.player2.get_drawn_card())
            self.player2.war_won(self.player1.war_hand)
            self.player2.war_won(self.player2.war_hand)
            self.reset_winning_hands()

        print("---------------")
        print("Player1 Card Count: " + str(self.player1.player_deck_count()))
        print("Player2 Card Count: " + str(self.player2.player_deck_count()))


if __name__ == "__main__":
    w = War()
    w.setup()

    while w.player1.player_deck_count() > 0 and w.player2.player_deck_count() >0:
        w.play_hand()

    if w.player1.player_deck_count() == 0:
        print("player 2 Wins!")
    else:
        print("player 1 wins!")


