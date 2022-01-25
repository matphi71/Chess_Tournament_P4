""" model players """

import json

from tinydb import TinyDB, Query

db = TinyDB('db.json')
User = Query()
player_db = db.table('players')


class PlayersIdentity:

    def __init__(self, family_name, name, ranking):
        self.family_name = family_name
        self.name = name

        self.ranking = ranking

    def __str__(self):
        return f"{self.family_name}, {self.name}, {self.ranking}"

    def __repr__(self):
        return f"{self.family_name}, {self.name}, {self.ranking}"

    def serialized_players(self):
        serialized_players = {}
        json.dumps(serialized_players)
        serialized_players['family_name'] = self.family_name
        serialized_players['name'] = self.name
        serialized_players['ranking'] = self.ranking
        return serialized_players

    def deserialized_players(self):
        family_name = self.serialized_players()["family_name"]
        name = self.serialized_players()['name']
        ranking = self.serialized_players()['ranking']
        deserialized_players = PlayersIdentity(family_name=family_name, name=name, ranking=ranking)
        print(deserialized_players)
        return deserialized_players

    def add_player_to_database(self):

        """To insert a player into the database"""

        player_db.insert(self.serialized_players())
        return player_db
