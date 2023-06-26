from .card import Card

class Pile:
    def __init__(self):
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def remove_card(self):
        if self.is_empty():
            return None
        return self.cards.pop()

    def is_empty(self):
        return len(self.cards) == 0

class TableauPile(Pile):
    def __init__(self):
        super().__init__()

    def can_add_card(self, card):
        if self.is_empty():
            return card.rank == 'King'
        top_card = self.cards[-1]
        return card.color != top_card.color and card.rank == str(int(top_card.rank) - 1)

class FoundationPile(Pile):
    def __init__(self, suit):
        super().__init__()
        self.suit = suit

    def can_add_card(self, card):
        if self.is_empty():
            return card.rank == 'Ace' and card.suit == self.suit
        top_card = self.cards[-1]
        return card.suit == self.suit and card.rank == str(int(top_card.rank) + 1)
