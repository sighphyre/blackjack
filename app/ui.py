from typing import List
from app.gamerules import HandState
from app.player import Player
from app.card import Suit, Hand, Card
from app.cardparse import INVERSE_VALUE_MAPPING


def _represent_cards(cards: List[Card]) -> str:
    return ",".join(map(_represent_card, cards))


def _represent_card(card) -> str:
    return _represent_suit(card.suit) + INVERSE_VALUE_MAPPING[card.value]


def _represent_suit(suit: Suit) -> str:
    if suit == Suit.Hearts:
        return "H"
    elif suit == Suit.Spades:
        return "S"
    elif suit == Suit.Diamonds:
        return "D"
    elif suit == Suit.Clubs:
        return "C"
    raise Exception("Invalid Suit")


class Tui:
    def take_win_condition(
        self,
        winner: Player,
        player_name: str,
        dealer_name: str,
        dealer_hand_state: HandState,
        player_hand_state: HandState,
    ):
        player_cards = player_hand_state.cards
        dealer_cards = dealer_hand_state.cards
        print("Winner:", winner.name)
        print("")
        print(
            dealer_name,
            "|",
            dealer_hand_state.value,
            "|",
            _represent_cards(dealer_cards),
        )

        print(
            player_name,
            "|",
            player_hand_state.value,
            "|",
            _represent_cards(player_cards),
        )
