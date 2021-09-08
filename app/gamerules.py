from app.card import Value, Hand


CARD_VALUES = {
    Value.Two: 2,
    Value.Three: 3,
    Value.Four: 4,
    Value.Five: 5,
    Value.Six: 6,
    Value.Seven: 7,
    Value.Eight: 8,
    Value.Nine: 9,
    Value.Ten: 10,
    Value.Jack: 10,
    Value.Queen: 10,
    Value.King: 10,
    Value.Ace: 11,
}


class HandEvaluator:
    def calculate_hand_value(self, hand: Hand) -> int:
        return sum(CARD_VALUES[card.value] for card in hand.cards)
