from abc import ABC
from typing import List
from app.card import Card


class Hand:
    def __init__(self):
        List[Card]: self.cards = []

    def receive_card(self, card: Card):
        pass


class Player(ABC):
    pass


class HumanPlayer(Player):
    def __init__(self, name: str):
        # This may very well be overengineering at this point but in standard BlackJack rules
        # a player can hold more than one hand through splitting a pair and if I was setting
        # up a code interview, this is something that I would ask to implement in that interview
        List[Hand]: self.hands = []
        self.name = name


class DealerPlayer(Player):
    pass
