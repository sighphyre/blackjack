import unittest
from random import shuffle
import app.game
from app.card import Card, Suite, Value
from app.deck import Deck
from app.game import Game, HandEvaluator
from app.player import HumanPlayer, DealerPlayer


def generate_mock_deck():
    cards = [[value for value in Value] for suite in Suite]
    return Deck(cards)


class TestStringMethods(unittest.TestCase):
    def test_game_setup(self):
        deck = generate_mock_deck()
        dealer = DealerPlayer()
        players = [HumanPlayer("john smith")]
        hand_evaluator = HandEvaluator()
        game = Game(dealer, players, deck, hand_evaluator)

        game.first_round()

        self.assertEqual("foo".upper(), "FOO")
