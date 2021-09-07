from typing import List
from app.player import Player
from app.deck import Deck


class Game:
    def __init__(self, players: List[Player], deck: Deck):
        self.players = players
        self.deck = deck
