import unittest
from random import shuffle
import app.game
from app.card import Card, Suite, Value, Deck
from app.game import Game, HandEvaluator
from app.player import HumanPlayer, DealerPlayer


def generate_mock_deck():
    cards = [[value for value in Value] for suite in Suite]
    return Deck(cards)


class TestStringMethods(unittest.TestCase):
    def test_game_setup(self):
        deck = generate_mock_deck()
        hand_evaluator = HandEvaluator()
        dealer = DealerPlayer(hand_evaluator)
        players = HumanPlayer("john smith", hand_evaluator)
        game = Game(dealer, players, deck, hand_evaluator)

        game.play_first_round()
        game.play_second_round()

        self.assertEqual("foo".upper(), "FOO")
