from abc import ABC
from typing import List
from app.card import Card
from app.deck import Deck


class Hand:
    def __init__(self):
        self.cards = []

    def receive_card(self, card: Card):
        self.cards.append(card)


class Player(ABC):
    def draw_card(self, deck: Deck):
        self.hand.receive_card(deck.draw())


class HumanPlayer(Player):
    def __init__(self, name: str):
        self.hand = Hand()
        self.name = name


class DealerPlayer(Player):
    def __init__(self):
        self.hand = Hand()
        self.name = "Dealer"
