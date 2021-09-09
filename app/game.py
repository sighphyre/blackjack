from typing import List, Tuple
from app.player import DealerPlayer, HumanPlayer, HitStrategy, Player
from app.card import Value, Hand, Deck
from app.gamerules import (
    HandEvaluator,
    GameState,
    HandState,
    BustState,
    BLACKJACK_SCORE,
)
from app.ui import Tui


class Game:
    def __init__(
        self,
        dealer: DealerPlayer,
        player: HumanPlayer,
        deck: Deck,
        hand_evaluator: HandEvaluator,
        ui: Tui,
    ):
        self.player = player
        self.deck = deck
        self.dealer = dealer
        self.hand_evaluator = hand_evaluator
        self.ui = ui

    def play_game_and_get_winner(self) -> Player:
        (
            first_round_state,
            dealer_hand_state,
            player_hand_state,
        ) = self.play_first_round()

        if not first_round_state == GameState.Active:

            if first_round_state == GameState.DealerWin:
                winner = self.dealer
            else:
                winner = self.player
            self.ui.take_win_condition(
                winner,
                self.player.name,
                self.dealer.name,
                dealer_hand_state,
                player_hand_state,
            )
            return winner

        (
            second_round_state,
            dealer_hand_state,
            player_hand_state,
        ) = self.play_second_round()
        if second_round_state == GameState.DealerWin:
            winner = self.dealer
        else:
            winner = self.player
        self.ui.take_win_condition(
            winner,
            self.player.name,
            self.dealer.name,
            dealer_hand_state,
            player_hand_state,
        )
        return winner

    def play_first_round(self) -> Tuple[GameState, HandState, HandState]:
        self.player.take_card(self.deck)
        self.player.take_card(self.deck)

        self.dealer.take_card(self.deck)
        self.dealer.take_card(self.deck)

        dealer_state = self.hand_evaluator.calculate_hand_value(self.dealer.hand)
        player_state = self.hand_evaluator.calculate_hand_value(self.player.hand)

        dealer_score = dealer_state.value
        player_score = player_state.value

        if dealer_score == BLACKJACK_SCORE and player_score == BLACKJACK_SCORE:
            return GameState.DealerWin, dealer_state, player_state
        elif player_score == BLACKJACK_SCORE:
            return GameState.PlayerWin, dealer_state, player_state
        elif dealer_score == BLACKJACK_SCORE:
            return GameState.DealerWin, dealer_state, player_state
        else:
            return GameState.Active, dealer_state, player_state

    def play_second_round(self) -> Tuple[GameState, HandState, HandState]:
        player_state = self.player.play_round(self.deck)
        if player_state.bust_state == BustState.Bust:
            dealer_state = self.hand_evaluator.calculate_hand_value(self.dealer.hand)
            return GameState.DealerWin, dealer_state, player_state

        dealer_hit_strategy = HitStrategy(player_state.value + 1)

        dealer_state = self.dealer.play_round(self.deck, dealer_hit_strategy)

        dealer_score = dealer_state.value
        player_score = player_state.value

        if dealer_state.bust_state == BustState.Bust:
            return GameState.PlayerWin, dealer_state, player_state
        elif dealer_score > player_score:
            return GameState.DealerWin, dealer_state, player_state
        else:
            return GameState.PlayerWin, dealer_state, player_state
