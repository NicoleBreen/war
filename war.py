'''
War Card Game

This code simulates the card game "War" between two players. The game consists of two players drawing cards from 
their decks, comparing their values, and the player with the higher value wins the round. In the case of a tie ("war"), 
each player draws five additional cards, and the process repeats until one player wins the round or runs out of cards.

This code was developed as part of a learning project from Udemy.

Author: Nicole Breen, 2024

'''
import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}

# represents a single playing card with a suit and rank
class Card:
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
    
    def __str__(self):
        return self.rank + " of " + self.suit

# Represents a deck of 52 cards that can be shuffled and dealt.
class Deck:
    def __init__(self):
        self.all_cards = []
        for suit in suits:
            for rank in ranks:
                self.all_cards.append(Card(suit,rank))

    # Shuffle the deck using random.shuffle()
    def shuffle(self):
        random.shuffle(self.all_cards)

    # permanently removes and resturns one card from deck
    def deal_one(self):
        return self.all_cards.pop()

# Represents a player who holds cards and can add or remove cards 
class Player:    
    def __init__(self,name):
        self.name = name
        self.all_cards = []

    # Removed one card from the player's hand (the top card, index 0)
    def remove_one(self):
        return self.all_cards.pop(0)
    
    # Adds one or more cards to the player's hand
    def add_cards(self,new_cards):
        if type(new_cards) == type([]):
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)

    # String representation of the player and the number of cards they have.
    def __str__(self):
        return f'Player {self.name} has {len(self.all_cards)} cards.'

# Game setup
player_one = Player("One")
player_two = Player("Two")
new_deck = Deck()
new_deck.shuffle()

# Deals 26 (half the deck) cards to each player
for x in range(26):
    player_one.add_cards(new_deck.deal_one())
    player_two.add_cards(new_deck.deal_one())

# Game loop to continue until one player runs out of cards
game_on = True

round_num = 0
while game_on:
    round_num += 1
    print(f"Round {round_num}")

    if len(player_one.all_cards) == 0:
        print('Player One, out of cards! Player Two wins!')
        game_on = False
        break
    if len(player_two.all_cards) == 0:
        print('Player Two, out of cards! Player One wins!')
        game_on = False
        break
    
    # each player plays top card
    player_one_cards = []
    player_one_cards.append(player_one.remove_one())

    player_two_cards = []
    player_two_cards.append(player_two.remove_one())

    at_war = True
    # Continue while "war" is happening (i.e., the top cards are tied)
    while at_war:
        # Compare values at the top cards
        if player_one_cards[-1].value > player_two_cards[-1].value:
            player_one.add_cards(player_one_cards)
            player_one.add_cards(player_two_cards)
            at_war = False
        elif player_one_cards[-1].value < player_two_cards[-1].value:
            player_two.add_cards(player_one_cards)
            player_two.add_cards(player_two_cards)
            at_war = False
        else:
            # WAR scenario
            print('WAR!')

            # Check if player can declare war (have at least 5 cards)
            if len(player_one.all_cards) < 5:
                print("Player One unable to declare war")
                print("PLAYER TWO WINS!")
                game_on = False
                break

            elif len(player_two.all_cards) < 5:
                print("Player Two unable to declare war")
                print("PLAYER ONE WINS!")
                game_on = False
                break

            else:
                # Each player draws five additional cards (for the 'war')
                for num in range(5):
                    player_one_cards.append(player_one.remove_one())
                    player_two_cards.append(player_two.remove_one())