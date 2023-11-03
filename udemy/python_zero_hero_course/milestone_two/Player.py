import random

class Player():

    def __init__(self):
        self.player_cards = []
        self.drawn_card = ""
        self.war_hand = []

    def draw_card(self):
        self.drawn_card = self.player_cards.pop()
    
    def get_drawn_card(self):
        return self.drawn_card

    def ready_player_for_war(self):

        self.war_hand.append(self.drawn_card)

        if self.player_deck_count() < 4:
            for x in range(0,self.player_deck_count()):
                self.war_hand.append(self.player_cards.pop())
        else:
            for x in range(0,3):
                self.war_hand.append(self.player_cards.pop())         

    def after_war_shuffle(self):
        random.shuffle(self.player_cards)
    
    def reset_drawn_card(self):
        self.drawn_card = ""
    
    def reset_war_hand(self):
        self.war_hand = []
    
    def hand_won(self, card):
        self.player_cards.append(card)
    
    def war_won(self, war_hand):
        self.player_cards.extend(war_hand)
    
    def player_deck_count(self):
        return len(self.player_cards)



