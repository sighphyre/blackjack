import unittest
from random import shuffle
import app.game
from app.card import Card, Suit, Value, Deck
from app.game import Game, HandEvaluator
from app.player import HumanPlayer, DealerPlayer, HitStrategy
from app.ui import Tui


# We don't need to mock out the terminal interface but the output makes the tests ugly
class MockUi:
    def take_win_condition(self, *args, **kwargs):
        pass


def generate_mock_deck():
    cards = [Card(suit, value) for value in Value for suit in Suit]
    return Deck(cards)


mock_suit = Suit.Diamonds


class TestStringMethods(unittest.TestCase):
    def setUp(self):
        player_hit_strategy = HitStrategy.default_player_hit_strategy()
        self.hand_evaluator = HandEvaluator()
        self.dealer = DealerPlayer(self.hand_evaluator)
        self.player = HumanPlayer(
            "john smith", self.hand_evaluator, player_hit_strategy
        )
        self.ui = MockUi()

    def test_given_state_where_player_should_bust_on_second_round_dealer_wins(self):
        deck = generate_mock_deck()
        game = Game(self.dealer, self.player, deck, self.hand_evaluator, self.ui)

        winner = game.play_game_and_get_winner()

        self.assertEqual(winner.name, "Dealer")

    def test_given_state_where_dealer_and_player_get_blackjack_should_give_dealer_win(
        self,
    ):
        cards = [
            Card(mock_suit, Value.Ace),
            Card(mock_suit, Value.King),
            Card(mock_suit, Value.Ace),
            Card(mock_suit, Value.King),
        ]

        deck = generate_mock_deck()
        game = Game(self.dealer, self.player, deck, self.hand_evaluator, self.ui)

        winner = game.play_game_and_get_winner()

        self.assertEqual(winner.name, "Dealer")

    def test_given_state_where_dealer_gets_blackjack_should_give_dealer_win(
        self,
    ):
        cards = [
            Card(mock_suit, Value.Two),
            Card(mock_suit, Value.King),
            Card(mock_suit, Value.Ace),
            Card(mock_suit, Value.King),
        ]

        deck = Deck(cards)
        game = Game(self.dealer, self.player, deck, self.hand_evaluator, self.ui)

        winner = game.play_game_and_get_winner()

        self.assertEqual(winner.name, "Dealer")

    def test_given_state_where_player_gets_blackjack_should_give_player_win(
        self,
    ):
        cards = [
            Card(mock_suit, Value.Ace),
            Card(mock_suit, Value.King),
            Card(mock_suit, Value.Two),
            Card(mock_suit, Value.King),
        ]

        deck = Deck(cards)
        game = Game(self.dealer, self.player, deck, self.hand_evaluator, self.ui)

        winner = game.play_game_and_get_winner()

        self.assertEqual(winner.name, "john smith")

    def test_given_state_where_play_second_round_and_player_can_hit_to_21_should_force_player_to_hit_to_21(
        self,
    ):
        cards = [
            Card(mock_suit, Value.Two),
            Card(mock_suit, Value.Two),
            Card(mock_suit, Value.Two),
            Card(mock_suit, Value.Two),
            Card(mock_suit, Value.Ace),
            Card(mock_suit, Value.Six),
            # These should be drawn by dealer
            Card(mock_suit, Value.Ace),
            Card(mock_suit, Value.Ace),
            Card(mock_suit, Value.Ace),
        ]

        deck = Deck(cards)
        game = Game(self.dealer, self.player, deck, self.hand_evaluator, self.ui)

        winner = game.play_game_and_get_winner()

        player_hand_value = self.hand_evaluator.calculate_hand_value(
            self.player.hand
        ).value

        self.assertEqual(winner.name, "john smith")
        self.assertEqual(player_hand_value, 21)

    def test_given_state_where_play_second_round_and_player_hits_to_17_should_force_player_to_stop_hitting(
        self,
    ):
        cards = [
            Card(mock_suit, Value.Two),
            Card(mock_suit, Value.Two),
            Card(mock_suit, Value.Two),
            Card(mock_suit, Value.Two),
            Card(mock_suit, Value.Ace),
            Card(mock_suit, Value.Two),
            # These should be drawn by dealer
            Card(mock_suit, Value.Ace),
            Card(mock_suit, Value.Ace),
            Card(mock_suit, Value.Ace),
        ]

        deck = Deck(cards)
        game = Game(self.dealer, self.player, deck, self.hand_evaluator, self.ui)

        winner = game.play_game_and_get_winner()

        player_hand_value = self.hand_evaluator.calculate_hand_value(
            self.player.hand
        ).value

        self.assertEqual(player_hand_value, 17)

    def test_given_state_where_play_second_round_and_player_hits_to_16_should_force_player_to_hit_again(
        self,
    ):
        cards = [
            Card(mock_suit, Value.Two),
            Card(mock_suit, Value.Two),
            Card(mock_suit, Value.Two),
            Card(mock_suit, Value.Two),
            Card(mock_suit, Value.King),
            Card(mock_suit, Value.Two),
            Card(mock_suit, Value.Two),
            # These should be drawn by dealer
            Card(mock_suit, Value.Ace),
            Card(mock_suit, Value.Ace),
            Card(mock_suit, Value.Ace),
        ]

        deck = Deck(cards)
        game = Game(self.dealer, self.player, deck, self.hand_evaluator, self.ui)

        winner = game.play_game_and_get_winner()

        player_hand_value = self.hand_evaluator.calculate_hand_value(
            self.player.hand
        ).value

        self.assertEqual(player_hand_value, 18)

    def test_given_state_where_play_second_round_and_player_hits_to_18_should_dealer_hits_on_an_18(
        self,
    ):
        cards = [
            Card(mock_suit, Value.Two),
            Card(mock_suit, Value.Two),
            Card(mock_suit, Value.Two),
            Card(mock_suit, Value.Two),
            Card(mock_suit, Value.King),
            Card(mock_suit, Value.Two),
            Card(mock_suit, Value.Two),
            # These should be drawn by dealer
            Card(mock_suit, Value.Ace),
            Card(mock_suit, Value.Three),
            Card(mock_suit, Value.Two),
        ]

        deck = Deck(cards)
        game = Game(self.dealer, self.player, deck, self.hand_evaluator, self.ui)

        winner = game.play_game_and_get_winner()

        dealer_hand_value = self.hand_evaluator.calculate_hand_value(
            self.dealer.hand
        ).value

        self.assertEqual(dealer_hand_value, 20)

    def test_given_state_where_play_second_round_and_player_hits_to_18_should_dealer_stays_on_a_19(
        self,
    ):
        cards = [
            Card(mock_suit, Value.Two),
            Card(mock_suit, Value.Two),
            Card(mock_suit, Value.Two),
            Card(mock_suit, Value.Two),
            Card(mock_suit, Value.King),
            Card(mock_suit, Value.Two),
            Card(mock_suit, Value.Two),
            # These should be drawn by dealer
            Card(mock_suit, Value.Ace),
            Card(mock_suit, Value.Two),
            Card(mock_suit, Value.Two),
        ]

        deck = Deck(cards)
        game = Game(self.dealer, self.player, deck, self.hand_evaluator, self.ui)

        winner = game.play_game_and_get_winner()

        dealer_hand_value = self.hand_evaluator.calculate_hand_value(
            self.dealer.hand
        ).value

        self.assertEqual(dealer_hand_value, 19)
