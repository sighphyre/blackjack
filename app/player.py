from abc import ABC
from typing import List
from app.card import Card, Deck, Hand
from app.gamerules import HandEvaluator

HIT_THRESHOLD = 17


class Player(ABC):
    def __init__(self, name: str, hand_evaluator: HandEvaluator):
        self.hand_evaluator = hand_evaluator
        self.hand = Hand()

    def take_card(self, deck: Deck):
        self.hand.receive_card(deck.draw())

    def play_round(self, deck: Deck) -> int:
        while self.hand_evaluator.calculate_hand_value(self.hand) <= HIT_THRESHOLD:
            self.hand.receive_card(deck.draw())
        return self.hand_evaluator.calculate_hand_value(self.hand)


class HumanPlayer(Player):
    def __init__(self, name: str, hand_evaluator: HandEvaluator):
        super().__init__(name, hand_evaluator)


class DealerPlayer(Player):
    def __init__(self, hand_evaluator: HandEvaluator):
        super().__init__("Dealer", hand_evaluator)
