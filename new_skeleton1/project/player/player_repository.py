from project.player.player import Player


class PlayerRepository:

    def __init__(self):
        self.count = 0
        self.players = []

    def add(self, player: Player):
        if player in self.players:
            raise ValueError(f"Player {player.username} already exists!")
        self.players.append(player)
        self.count += 1

    def remove(self, player: str):
        if not player:
            raise ValueError("Player cannot be an empy string!")
        search_plaer = self.find(player)
        self.players.remove(search_plaer)
        self.count -= 1

    def find(self, username):
        search_plaer = [p for p in self.players if p.username == username][0]
        return search_plaer
