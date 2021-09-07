from app.card import Card, Suite, Value


class Deck:
    def __init__(self):
        pass

    def draw(self) -> Card:
        return Card(Suite.Clubs, Value.Ace)
