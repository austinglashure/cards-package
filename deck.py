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
        if len(self.deck) != 52:
            print("Error! Incorrect card count in the deck!")

    def shuffle_deck(self):
        random.shuffle(self.deck)
    
    def deal_card(self):
        return self.deck.pop(0)
    
    def retrieve_card(self, card):
        self.deck.append(card)