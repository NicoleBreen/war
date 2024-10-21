import random
# needs to be title case atm
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}

class Card:
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
    
    def __str__(self):
        return self.rank + " of " + self.suit

# game logic
two_hearts = Card("Hearts","Two")
three_of_clubs = Card("Clubs","Three")

# is the two of hearts the same value as three of clubs?
result = two_hearts.value == three_of_clubs.value
print(result) # False

class Deck:

    def __init__(self):
        self.all_cards = []
        for suit in suits:
            for rank in ranks:
                self.all_cards.append(Card(suit,rank))

    def shuffle(self):
        random.shuffle(self.all_cards)
    # permanently removes one card
    # can remove two or split etc
    def deal_one(self):
        return self.all_cards.pop()

# test
new_deck = Deck()
first_card = new_deck.all_cards[0]
last_card = new_deck.all_cards[-1]
print(first_card)
print(last_card)

for card_object in new_deck.all_cards:
    print(card_object)

# shuffle creates a new deck
new_deck.shuffle()
for card_object in new_deck.all_cards:
    print(card_object)