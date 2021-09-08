from typing import List
from app.card import Card, Suite, Value


class Deck:
    def __init__(self, cards: List[Card]):
        self.cards = cards
        self.__validate_deck(cards)

    def __validate_deck(self, cards):
        pass

    def draw(self) -> Card:
        return Card(Suite.Clubs, Value.Ace)
