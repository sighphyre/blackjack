from abc import ABC
from typing import List, Optional
from app.card import Card, Deck, Hand
from app.gamerules import HandEvaluator, HandState

PLAYER_HIT_THRESHOLD = 17


class HitStrategy:
    def __init__(self, target_value):
        self.target_value = target_value

    def should_hit(self, hand_state: HandState) -> bool:
        return hand_state.value < self.target_value

    @classmethod
    def default_player_hit_strategy(cls):
        return cls(PLAYER_HIT_THRESHOLD)


class Player(ABC):
    def __init__(self, name: str, hand_evaluator: HandEvaluator):
        self.name = name
        self.hand_evaluator = hand_evaluator
        self.hand = Hand()

    def take_card(self, deck: Deck):
        self.hand.receive_card(deck.draw())

    def play_round(
        self, deck: Deck, hit_strategy: Optional[HitStrategy] = None
    ) -> HandState:
        if not hit_strategy:
            hit_strategy = self.hit_strategy
        while hit_strategy.should_hit(
            self.hand_evaluator.calculate_hand_value(self.hand)
        ):
            self.hand.receive_card(deck.draw())
        return self.hand_evaluator.calculate_hand_value(self.hand)


# The human player has a fixed hitting strategy so we can set that in the constructor,
# whereas the dealer will only decide based on the players' actions
class HumanPlayer(Player):
    def __init__(
        self, name: str, hand_evaluator: HandEvaluator, hit_strategy: HitStrategy
    ):
        super().__init__(name, hand_evaluator)
        self.hit_strategy = hit_strategy


class DealerPlayer(Player):
    def __init__(self, hand_evaluator: HandEvaluator):
        super().__init__("Dealer", hand_evaluator)
