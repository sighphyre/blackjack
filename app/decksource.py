from urllib.parse import urlparse
from typing import List
from types import SimpleNamespace
import requests
import json
from app.errors import InvalidCardSource
from app.card import Card, Suite, Value

BACKOFF_TIMEOUTS = [1, 3, 5]
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
# We could just upper case the enum and resolve it directly with a lookup but this approach provides
# us with a single point of change if the API decides to change the way suites are presented
SUITE_MAPPING = {
    "DIAMONDS": Suite.Diamonds,
    "SPADES": Suite.Spades,
    "CLUBS": Suite.Clubs,
    "HEARTS": Suite.Hearts,
}


def parse_json_cards(json_card_list: str) -> List[Card]:
    raw_card_values = json.loads(
        json_card_list, object_hook=lambda d: SimpleNamespace(**d)
    )
    validated_cards = map(
        lambda x: Card(
            SUITE_MAPPING[x.suit],
            VALUE_MAPPING[x.value],
        ),
        raw_card_values,
    )
    return list(validated_cards)


class RestApiDeckSource:
    def __init__(self, url: str):
        self.__validate_url(url)
        self.url = url

    def load_deck(self):
        serialised_cards = self._retrieve_raw_deck_json()
        cards = parse_json_cards(serialised_cards)
        return Deck(cards)

    def __validate_url(self, url: str):
        # We should pay some consideration to what URL source we're using here. Since BlackJack is a game of gambling
        # we should probably disallow anything that's not coming from an https source, but this is good enough for now
        try:
            result = urlparse(url)
            if not all([result.scheme, result.netloc]):
                raise InvalidCardSource(url, "is not a valid url")
        except:
            raise InvalidCardSource("Cannot parse", url, "as a valid url")

    def _retrieve_raw_deck_json(self):
        deck_response = requests.get(self.url)
        if deck_response.status_code == 200:
            return deck_response.json()
        elif deck_response.status_code == 404:
            raise InvalidCardSource(
                "Got a 404 when trying to retrieve cards from deck source"
            )
        elif deck_response.status_code == 401:
            raise InvalidCardSource(
                "Card source API requires authentication, this is not implemented"
            )
        elif deck_response.status_code >= 400 and deck_response.status_code < 500:
            raise InvalidCardSource(
                "Status code",
                deck_response.status_code,
                "encountered when trying to hit cards",
            )
        elif deck_response.status_code >= 500:
            # Implement backoff
            pass
