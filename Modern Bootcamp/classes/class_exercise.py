# Create two classes (Card and Deck) > Exercise 249
from random import shuffle

class Card:
    def __init__(self, suit, value):        
        self.suit = suit
        self.value = value

    def __repr__(self):
        return f"{self.value} of {self.suit}"

card1 = Card('Spades', 'J')
print(card1)
# Output
J of Spades

class Deck:
    def __init__(self):
        allow_suit = ['Spades', 'Diamonds', 'Clubs', 'Hearts']
        allow_value = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        self.cards = [Card(x, y) for x in allow_suit for y in allow_value]
# Or 
        # self.cards = []
        # for x in allow_suit:
        #     for y in allow_value:
        #         self.cards.append(Card(x, y))
        print(self.cards)

Deck()
# Output from "Deck()"
[A of Spades, 2 of Spades, 3 of Spades, 4 of Spades, 5 of Spades, 6 of Spades, 7 of Spades, 8 of Spades, 9 of Spades, 10 of Spades, J of Spades, Q of Spades, K of Spades, A of Diamonds, 2 of Diamonds, 3 of Diamonds, 4 of Diamonds, 5 of Diamonds, 6 of Diamonds, 7 of Diamonds, 8 of Diamonds, 9 of Diamonds, 10 of Diamonds, J of Diamonds, Q of Diamonds, K of Diamonds, A of Clubs, 2 of 
Clubs, 3 of Clubs, 4 of Clubs, 5 of Clubs, 6 of Clubs, 7 of Clubs, 8 of Clubs, 9 of Clubs, 10 of Clubs, J of Clubs, Q of Clubs, K of Clubs, A of Hearts, 2 of Hearts, 3 of Hearts, 4 of Hearts, 
5 of Hearts, 6 of Hearts, 7 of Hearts, 8 of Hearts, 9 of Hearts, 10 of Hearts, J of Hearts, Q of Hearts, K of Hearts]
        
    def __repr__(self):
        return f"Deck of {self.count()} cards"
# This calls the "count" instance method
    def count(self):
        return len(self.cards)
# This, by default, will be "52"

    def _deal(self, num):
        tot_cards = self.count()
        actual = min([tot_cards,num])
# "min" will take the lesser of two values, In this case the lesser of the number of cards remaining
# or the number to be taken (num)
        if tot_cards == 0:
            raise ValueError("All cards have been dealt")
        hand = self.cards[-actual:]
# "hand" represents a list consisting of the cards taken which is basd on the var "actual".
# Use a slice to count from the end of the list of cards 
        self.cards = self.cards[:-actual]
# At the same time the list of cards in self.cards needs to be updated to only include
# the cards remaining after the hand was dealt
        return hand

d = Deck()
print(d._deal(3))
print(d.count())
print(d._deal(52))

# Output
[J of Hearts, Q of Hearts, K of Hearts]
49
ValueError: All cards have been dealt


    # def shuffle(self):
    #     return random.shuffle

    def deal_card(self):
        return self._deal(1)[0]
# Returns a single card
# The use of "[0]" returns just the card NOT in a list, so;
# "K of Hearts" instead of "[K of Hearts]"

    def deal_hand(self, tot_hand):
        return self._deal(tot_hand)
# Returns however many cards requested in a list

    def shuffle(self):
        if self.count() < 52:
            raise ValueError("Only full decks can be shuffled")
        shuffle(self.cards)
        return self
# Import "shuffle" from random was added to the top of the code
# The "return self" is just good Python, it doesn't mean anything



