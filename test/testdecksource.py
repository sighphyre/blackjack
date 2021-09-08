import unittest
import responses
import requests
from app.decksource import RestApiDeckSource
from app.errors import InvalidCardSource
from app.constants import DEFAULT_DECK_URL

MOCK_URL_FOR_CARD_SOURCE = "http://totallynotathing.com"


class TestDeckSource(unittest.TestCase):
    def test_given_a_broken_url_then_raises_an_error_correctly(self):
        self.assertRaises(InvalidCardSource, RestApiDeckSource, "totally not a url")

    @responses.activate
    def test_given_a_valid_url_that_returns_a_404_then_raises_error(self):

        responses.add(
            responses.GET,
            MOCK_URL_FOR_CARD_SOURCE,
            json={"error": "not found"},
            status=404,
        )
        deck_result = RestApiDeckSource(MOCK_URL_FOR_CARD_SOURCE)

        self.assertRaises(InvalidCardSource, deck_result._retrieve_raw_deck_json)

    @responses.activate
    def test_given_a_valid_url_that_returns_a_401_then_raises_error(self):

        responses.add(
            responses.GET,
            MOCK_URL_FOR_CARD_SOURCE,
            json={"error": "unauthorized"},
            status=401,
        )
        deck_result = RestApiDeckSource(MOCK_URL_FOR_CARD_SOURCE)

        self.assertRaises(InvalidCardSource, deck_result._retrieve_raw_deck_json)

    @responses.activate
    def test_given_a_valid_url_that_returns_a_400_range_then_raises_error(self):

        responses.add(
            responses.GET,
            MOCK_URL_FOR_CARD_SOURCE,
            json={"error": "unauthorized"},
            status=402,
        )
        deck_result = RestApiDeckSource(MOCK_URL_FOR_CARD_SOURCE)

        self.assertRaises(InvalidCardSource, deck_result._retrieve_raw_deck_json)

    @responses.activate
    def test_given_a_valid_url_that_returns_a_200_range_then_returns_raw_json(self):

        responses.add(
            responses.GET,
            MOCK_URL_FOR_CARD_SOURCE,
            json={"raw": "json"},
            status=200,
        )
        deck_result = RestApiDeckSource(
            MOCK_URL_FOR_CARD_SOURCE
        )._retrieve_raw_deck_json()

        assert deck_result == {"raw": "json"}
