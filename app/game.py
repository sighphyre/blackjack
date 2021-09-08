from typing import List
from app.player import DealerPlayer, HumanPlayer, Hand
from app.deck import Deck
from app.card import Value


class HandEvaluator:

    value_mapping = {
        Value.Two: 2,
        Value.Three: 3,
        Value.Four: 4,
        Value.Five: 5,
        Value.Six: 6,
        Value.Seven: 7,
        Value.Eight: 8,
        Value.Nine: 9,
        Value.Ten: 10,
        Value.Jack: 10,
        Value.Queen: 10,
        Value.King: 10,
        Value.Ace: 11,
    }

    def calculate_hand_value(self, hand: Hand) -> int:
        for card in hand.cards:
            print(self.value_mapping[card.value])


class Game:
    def __init__(
        self,
        dealer: DealerPlayer,
        players: List[HumanPlayer],
        deck: Deck,
        hand_evaluator: HandEvaluator,
    ):
        self.players = players
        self.deck = deck
        self.dealer = dealer
        self.hand_evaluator = hand_evaluator

    def first_round(self):
        for player in self.players:
            player.draw_card(self.deck)
            player.draw_card(self.deck)

        self.dealer.draw_card(self.deck)
        self.dealer.draw_card(self.deck)

        self.hand_evaluator.calculate_hand_value(self.dealer.hand)
