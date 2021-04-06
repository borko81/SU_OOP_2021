from project.card.card import Card


class TrapCard(Card):
    def __init__(self, name):
        # damage = 120, health = 5
        super().__init__(name, 120, 5)
