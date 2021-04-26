import cards_package.deck as deck
import copy

HAND_LIST = ["High Card", "Two of a Kind", "Two Pair", "Three of a Kind", "Straight", "Flush", "Full House",
             "Four of a Kind", "Straight Flush"]


def get_value(card):
    return card[0]


def get_suit(card):
    return card[1]


class Evaluator:
    def __init__(self):
        self.cards_pool = []

    def load_card(self, card):
        self.cards_pool.append(card)
    
    def sort_cards(self):
        self.sorted_cards_pool = copy.deepcopy(self.cards_pool)
        for i in range(len(self.sorted_cards_pool)-1):
            for j in range(len(self.sorted_cards_pool)-1):
                if deck.FACES.index(self.sorted_cards_pool[j][0]) > deck.FACES.index(self.sorted_cards_pool[j + 1][0]):
                    foo = self.sorted_cards_pool[j]
                    self.sorted_cards_pool[j] = self.sorted_cards_pool[j + 1]
                    self.sorted_cards_pool[j + 1] = foo
        print(self.cards_pool)
        print(self.sorted_cards_pool)