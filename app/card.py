from enum import Enum
from enum import unique
from dataclasses import dataclass


@unique
class Suite(Enum):
    Spades = 1
    Hearts = 2
    Clubs = 3
    Diamonds = 4


@unique
class Value(Enum):
    Ace = 1
    Two = 2
    Three = 3
    Four = 4
    Five = 5
    Six = 6
    Seven = 7
    Eight = 8
    Nine = 9
    Ten = 10
    Jack = 11
    Queen = 12
    King = 13


@dataclass
class Card:
    suite: Suite
    value: Value
