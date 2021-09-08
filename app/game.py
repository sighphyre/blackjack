from typing import List
from app.player import DealerPlayer, HumanPlayer
from app.card import Value, Hand, Deck
from app.gamerules import HandEvaluator


class Game:
    def __init__(
        self,
        dealer: DealerPlayer,
        player: HumanPlayer,
        deck: Deck,
        hand_evaluator: HandEvaluator,
    ):
        self.player = player
        self.deck = deck
        self.dealer = dealer
        self.hand_evaluator = hand_evaluator

    def play_first_round(self):
        self.player.take_card(self.deck)
        self.player.take_card(self.deck)

        self.dealer.take_card(self.deck)
        self.dealer.take_card(self.deck)

        hand_value = self.hand_evaluator.calculate_hand_value(self.dealer.hand)
        print(hand_value)

    def play_second_round(self):
        self.player.play_round(self.deck)
