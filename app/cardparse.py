import json
from typing import List
from types import SimpleNamespace
from app.card import Value, Suit, Card

VALUE_MAPPING = {
    "2": Value.Two,
    "3": Value.Three,
    "4": Value.Four,
    "5": Value.Five,
    "6": Value.Six,
    "7": Value.Seven,
    "8": Value.Eight,
    "9": Value.Nine,
    "10": Value.Ten,
    "J": Value.Jack,
    "Q": Value.Queen,
    "K": Value.King,
    "A": Value.Ace,
}

# The spec says to represent items in console prints as the items that were received from the API
# We could hold the raw values in the cards but that feels ungainly, alternatively we could
# Simply allow the UI printer to contain its own mapping of how to represent how to display those cards
# and while that feels like a much cleaner solution, if the API chooses to change the way it displays cards
# we'll be in violation of the spec. This is usually the point where I ask questions to understand why
# that requirement exists but this will allow us to fill the spec cleanly until we can understand
# the domain logic that leads to that requirement
INVERSE_VALUE_MAPPING = {v: k for k, v in VALUE_MAPPING.items()}

# We could just upper case the enum and resolve it directly with a lookup but this approach provides
# us with a single point of change if the API decides to change the way suits are presented
SUITE_MAPPING = {
    "DIAMONDS": Suit.Diamonds,
    "SPADES": Suit.Spades,
    "CLUBS": Suit.Clubs,
    "HEARTS": Suit.Hearts,
}


def parse_json_cards(raw_cards: str) -> List[Card]:
    validated_cards = map(
        lambda x: Card(SUITE_MAPPING[x["suit"]], VALUE_MAPPING[x["value"]]),
        raw_cards,
    )
    return list(validated_cards)
