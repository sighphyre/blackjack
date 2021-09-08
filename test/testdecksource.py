import unittest
import responses
import requests
from app.decksource import RestApiDeckSource
from app.errors import InvalidCardSource
from app.constants import DEFAULT_DECK_URL


class TestDeckSource(unittest.TestCase):
    def test_given_a_broken_url_then_raises_an_error_correctly(self):
        self.assertRaises(InvalidCardSource, RestApiDeckSource, "totally not a url")

    @responses.activate
    def test_given_a_valid_url_returns_json(self):

        mock_url_for_card_source = "http://totallynotathing.com"
        responses.add(
            responses.GET,
            mock_url_for_card_source,
            json={"error": "not found"},
            status=404,
        )
        deck_source = RestApiDeckSource(mock_url_for_card_source)
        deck_json = deck_source._retrieve_raw_deck_json()

        print(deck_json)

        # assert resp.json() == {"error": "not found"}

        # assert len(responses.calls) == 1
        # assert responses.calls[0].request.url == "http://twitter.com/api/1/foobar"
        # assert responses.calls[0].response.text == '{"error": "not found"}'
