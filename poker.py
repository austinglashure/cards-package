import cards_package.deck as deck
import copy

HAND_LIST = ["High Card", "Two of a Kind", "Two Pair", "Three of a Kind", "Straight", "Flush", "Full House",
             "Four of a Kind", "Straight Flush"]
VALUES = deck.FACES
SUITS = deck.SUITS


def get_value(card):
    return card[0]


def get_suit(card):
    return card[1]


class Evaluator:
    def __init__(self):
        self.cards_pool = []

    def load_card(self, card):
        self.cards_pool.append(card)
    
    def reset_pool(self):
        self.cards_pool = []
        self.sorted_cards_pool = []
    
    def sort_cards(self):
        self.sorted_cards_pool = copy.deepcopy(self.cards_pool)
        for i in range(len(self.sorted_cards_pool)-1):
            for j in range(len(self.sorted_cards_pool)-1):
                if VALUES.index(self.sorted_cards_pool[j][0]) < VALUES.index(self.sorted_cards_pool[j + 1][0]):
                    foo = self.sorted_cards_pool[j]
                    self.sorted_cards_pool[j] = self.sorted_cards_pool[j + 1]
                    self.sorted_cards_pool[j + 1] = foo
    
    def check_flush(self):  # 1 / 520 for five card stud
        self.sort_cards()
        for suit in SUITS:
            self.flush = []
            for card in self.sorted_cards_pool:
                if get_suit(card) == suit:
                    self.flush.append(card)
                if len(self.flush) == 5:
                    return True
            if len(self.flush) < 5:
                self.flush = []
        if len(self.flush) < 5:
            self.flush = None
            return False
    
    def check_straight(self):
        self.sort_cards()
        self.span_string = "AKQJT98765432A"
        self.poss_straight = ""
        for i in self.sorted_cards_pool:
            self.poss_straight += get_value(i)
        if self.poss_straight in self.span_string:
            self.straight = copy.deepcopy(self.sorted_cards_pool)
            return True
        else:
            self.straight = None
            return False
                
    def check_straight_flush(self):
        if self.check_straight():
            if self.check_flush():
                self.straight_flush = copy.deepcopy(self.sorted_cards_pool)
                return True
            else:
                self.straight_flush = None
                return False
        else:
            self.straight_flush = None
            return False
    
    def check_royal_flush(self):
        temp = get_value(self.sorted_cards_pool[0])
        if self.check_straight_flush():
            if temp in "A":
                self.royal_flush = copy.deepcopy(self.sorted_cards_pool)
                return True
            else:
                return False
        else:
            self.royal_flush = None
            return False

    def check_four_of_kind(self):
        for face in deck.FACES:
            self.four_kind = []
            for card in self.sorted_cards_pool:
                if get_value(card) == face:
                    self.four_kind.append(card)
            if len(self.four_kind) == 4: 
                return True
        if len(self.four_kind) != 4:
            return False

    def check_three_of_kind(self):
        if not self.check_four_of_kind():
            for face in deck.FACES:
                self.three_kind = []
                for card in self.sorted_cards_pool:
                    if get_value(card) == face:
                        self.three_kind.append(card)
                if len(self.three_kind) == 3: 
                    return True
            if len(self.three_kind) != 3:
                return False