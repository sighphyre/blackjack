from enum import Enum, unique
from dataclasses import dataclass
from typing import List


@unique
class Suit(Enum):
    Spades = 1
    Hearts = 2
    Clubs = 3
    Diamonds = 4


@unique
class Value(Enum):
    Ace = 1
    Two = 2
    Three = 3
    Four = 4
    Five = 5
    Six = 6
    Seven = 7
    Eight = 8
    Nine = 9
    Ten = 10
    Jack = 11
    Queen = 12
    King = 13


@dataclass
class Card:
    suit: Suit
    value: Value


class Deck:
    def __init__(self, cards: List[Card]):
        self.cards = cards
        self.__validate_deck(cards)

    def __validate_deck(self, cards):
        pass

    def draw(self) -> Card:
        return self.cards.pop(0)


class Hand:
    def __init__(self):
        self.cards = []

    def receive_card(self, card: Card):
        self.cards.append(card)
