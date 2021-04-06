from project.battle_field import BattleField
from project.card.card_repository import CardRepository
from project.card.magic_card import MagicCard
from project.card.trap_card import TrapCard
from project.player.advanced import Advanced
from project.player.beginner import Beginner
from project.player.player_repository import PlayerRepository


class Controller:
    def __init__(self):
        self.player_repository = PlayerRepository()
        self.card_repository = CardRepository()

    def add_player(self, type: str, username: str):
        if type == 'Beginner':
            player = Beginner(username)
            self.player_repository.players.append(player)
        else:
            player = Advanced(username)
            self.player_repository.players.append(player)
        return f"Successfully added player of type {type} with username: {username}"

    def add_card(self, type: str, name: str):
        if type == 'Magic':
            card = MagicCard(name)
            self.card_repository.cards.append(card)
        else:
            card = TrapCard(name)
            self.card_repository.cards.append(card)
        return f"Successfully added card of type {type} with name: {name}"

    def add_player_card(self, username: str, card_name: str):
        user = self.player_repository.find(username)
        card = self.card_repository.find(card_name)
        user.card_repository.add(card)
        return f"Successfully added card: {card_name} to user: {username}"

    def fight(self, attack_name: str, enemy_name: str):
        a = self.player_repository.find(attack_name)
        e = self.player_repository.find(enemy_name)
        BattleField.fight(a, e)
        return f"Attack user health {a.health} - Enemy user health {e.health}"

    def report(self):
        result = ""
        for user in self.player_repository.players:
            result += f"Username: {user.username} - Health: {user.health} - Cards {user.card_repository.count}\n"
            for card in user.card_repository.cards:
                result += f"### Card: {card.name} - Damage: {card.damage_points}\n"

        return result
