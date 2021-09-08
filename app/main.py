"""Naval Fate.

Usage:
  main.py
  main.py --url <URL>
  main.py --name <NAME>
  main.py --url <URL> --name <NAME>

Options:
  -h --help     Show this screen.
 --url          Specify a URL from which to obtain a shuffled set of cards, if no URL is specified this will supply a default
 --name         Set a player name for the first player, if no name is set, this will default to 'Bob'
"""
from docopt import docopt
from constants import DEFAULT_DECK_URL


if __name__ == "__main__":
    arguments = docopt(__doc__, version="Naval Fate 2.0")

    if not arguments["--name"]:
        name = "Bob"
    else:
        name = arguments["<NAME>"]

    if not arguments["--url"]:
        deck_url = DEFAULT_DECK_URL
    else:
        deck_url = arguments["<URL>"]

    print(name)
    print(deck_url)
