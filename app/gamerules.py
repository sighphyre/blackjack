from dataclasses import dataclass
from typing import List
from enum import Enum, unique
from app.card import Value, Hand, Card
from copy import deepcopy

BLACKJACK_SCORE = 21


CARD_VALUES = {
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


@unique
class BustState(Enum):
    Bust = 1
    Viable = 2


@unique
class GameState(Enum):
    Active = 1
    DealerWin = 2
    PlayerWin = 3


@dataclass
class HandState:
    bust_state: BustState
    value: int
    cards: List[Card]


def calculate_hand_value(hand: Hand) -> int:
    return sum(CARD_VALUES[card.value] for card in hand.cards)


class HandEvaluator:
    def calculate_hand_value(self, hand: Hand) -> HandState:
        hand_value = calculate_hand_value(hand)

        if hand_value > BLACKJACK_SCORE:
            bust_state = BustState.Bust
        else:
            bust_state = BustState.Viable

        return HandState(bust_state, hand_value, deepcopy(hand.cards))
