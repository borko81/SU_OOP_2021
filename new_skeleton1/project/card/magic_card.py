from project.card.card import Card


class MagicCard(Card):
    def __init__(self, name):
        # damage = 5, health = 80
        super().__init__(name, 5, 80)
