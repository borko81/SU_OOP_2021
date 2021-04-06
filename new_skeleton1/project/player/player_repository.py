from project.player.player import Player


class PlayerRepository:

    def __init__(self):
        self.count = 0
        self.players = []

    def add(self, player: Player):
        try:
            player = [p for p in self.players if p.username == player.username][0]
            raise ValueError(f"Player {player.username} already exists!")
        except IndexError:
            self.players.append(player)
            self.count += 1

    def remove(self, player):
        if player == "":
            raise ValueError("Player cannot be an empty string!")

        temp = self.find(player)
        self.players.remove(temp)
        self.count -= 1

    def find(self, username):
        temp = [x for x in self.players if x.username == username][0]
        return temp