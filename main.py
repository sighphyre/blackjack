"""BlackJack Example.

Usage:
  main.py
  main.py --url <URL>

Options:
  -h --help     Show this screen.
 --url          Specify a URL from which to obtain a shuffled set of cards, if no URL is specified this will supply a default
"""
from docopt import docopt
from app.constants import DEFAULT_DECK_URL, DEFAULT_PLAYER_NAME
from app.decksource import RestApiDeckSource
from app.game import Game
from app.gamerules import HandEvaluator
from app.player import DealerPlayer, HumanPlayer, HitStrategy
from app.ui import Tui


if __name__ == "__main__":
    arguments = docopt(__doc__, version="BlackJack 1.0")

    if not arguments["--url"]:
        deck_url = DEFAULT_DECK_URL
    else:
        deck_url = arguments["<URL>"]

    deck_source = RestApiDeckSource(deck_url)
    deck = deck_source.load_deck()

    hand_evaluator = HandEvaluator()
    dealer = DealerPlayer(hand_evaluator)
    player_hit_strategy = HitStrategy.default_player_hit_strategy()
    player = HumanPlayer(DEFAULT_PLAYER_NAME, hand_evaluator, player_hit_strategy)

    ui = Tui()

    game = Game(dealer, player, deck, hand_evaluator, ui)

    game.play_game_and_get_winner()
