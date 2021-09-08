import urllib.request
from urllib.parse import urlparse
import requests
from app.errors import InvalidCardSource

BACKOFF_TIMEOUTS = [1, 3, 5]


class RestApiDeckSource:
    def __init__(self, url: str):
        self.__validate_url(url)
        self.url = url

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
