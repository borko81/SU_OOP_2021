class Team:

    def __init__(self, name, rating,):
        self.__name = name
        self.__rating = rating
        self.__players = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def rating(self):
        return self.__rating

    @rating.setter
    def rating(self, value):
        self.__rating = value

    @property
    def players(self):
        return self.__players

    @players.setter
    def players(self, value):
        self.__players = value

    def add_player(self, player):
        if player in self.players:
            return "Player %s has already joined" % player.name
        self.players.append(player)
        return "Player %s joined team %s" % (player.name, self.name)

    def remove_player(self, player_name: str):
        try:
            temp_username = [name for name in self.players if name.name == player_name][0]
        except IndexError:
            return "Player %s not found" % player_name
        else:
            self.__players = [
                name for name in self.players if not name.name == player_name
            ]
            return temp_username
