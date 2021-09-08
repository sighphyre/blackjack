"""BlackJack Example.

Usage:
  main.py
  main.py --url <URL>

Options:
  -h --help     Show this screen.
 --url          Specify a URL from which to obtain a shuffled set of cards, if no URL is specified this will supply a default
"""
from docopt import docopt
from constants import DEFAULT_DECK_URL


if __name__ == "__main__":
    arguments = docopt(__doc__, version="Naval Fate 2.0")

    if not arguments["--url"]:
        deck_url = DEFAULT_DECK_URL
    else:
        deck_url = arguments["<URL>"]

    print(name)
    print(deck_url)
