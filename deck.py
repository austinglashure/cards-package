import random
SUITS = "SDCH"
FACES = "23456789TJQKA"

class Deck:
    def __init__(self):
        self.deck = []
        for foo in FACES:
            for bar in SUITS:
                self.card = [foo, bar]
                self.deck.append(self.card)

    def shuffle_deck(self):
        random.shuffle(self.deck)
    
    def deal_card(self):
        return self.deck.pop(0)
    
    def retrieve_card(self, card):
        self.deck.append(card)
    
    def get_card_value(self):
        return self.card[0]
    
    def get_card_suit(self):
        return self.card[1]