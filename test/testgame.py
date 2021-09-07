import unittest
import app.game
from app.card import Card, Suite, Value
from app.deck import Deck


def generate_mock_deck():
    return [[value for value in Value] for suite in Suite]


class TestStringMethods(unittest.TestCase):
    def test_upper(self):
        print(generate_mock_deck())
        self.assertEqual("foo".upper(), "FOO")
