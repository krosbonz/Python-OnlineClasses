from random import shuffle

class Card:
    def __init__(self, suit, value):        
        self.suit = suit
        self.value = value

    def __repr__(self):
        return f"{self.value} of {self.suit}"

class Deck:
    def __init__(self):
        allow_suit = ['Spades', 'Diamonds', 'Clubs', 'Hearts']
        allow_value = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        self.cards = [Card(x, y) for x in allow_suit for y in allow_value]
        
    def __repr__(self):
        return f"Deck of {self.count()} cards"

    def count(self):
        return len(self.cards)

    def _deal(self, num):
        tot_cards = self.count()
        actual = min([tot_cards,num])
        if tot_cards == 0:
            raise ValueError("All cards have been dealt")
        hand = self.cards[-actual:]
        self.cards = self.cards[:-actual]
        return hand

    def deal_card(self):
        return self._deal(1)[0]

    def deal_hand(self, tot_hand):
        return self._deal(tot_hand)

    def shuffle(self):
        if self.count() < 52:
            raise ValueError("Only full decks can be shuffled")
        shuffle(self.cards)
        return self





