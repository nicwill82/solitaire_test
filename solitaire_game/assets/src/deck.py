import random
from .card import Card

class Deck:
    def __init__(self):
        self.cards = []

        # Create the deck of cards
        self.create_deck()

    def create_deck(self):
        # Create the deck of cards with suits and ranks
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        ranks = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']

        for suit in suits:
            for rank in ranks:
                card = Card(suit, rank)
                self.cards.append(card)

    def shuffle(self):
        # Shuffle the deck of cards
        random.shuffle(self.cards)

    def deal_cards(self, num_cards, piles):
        # Deal the specified number of cards to the tableau piles
        for _ in range(num_cards):
            for pile in piles:
                card = self.cards.pop()
                pile.add_card(card)
