from project.card.card import Card


class CardRepository:
    def __init__(self):
        self.count = 0
        self.cards = []

    def add(self, card: Card):
        try:
            temp = [c for c in self.cards if c.name == card.name][0]
            raise ValueError(f"Card {card.name} already exists!")
        except IndexError:
            self.count += 1
            self.cards.append(card)

    def remove(self, card):
        if card == "":
            raise ValueError("Card cannot be an empty string!")
        temp = self.find(card)
        self.cards.remove(temp)
        self.count -= 1

    def find(self, name: str):
        return [c for c in self.cards if c.name == name][0]
