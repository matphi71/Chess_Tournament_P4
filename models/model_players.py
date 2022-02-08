""" model players """

import json

from tinydb import TinyDB, Query

db = TinyDB('db.json')
User = Query()
player_db = db.table('PLAYERS')


class PlayersIdentity:

    def __init__(self, family_name=None, name=None, ranking=None):
        self.family_name = family_name
        self.name = name
        self.ranking = ranking
        self.score = 0

    def __str__(self):
        return f"{self.family_name}, {self.name}, {self.ranking}, {self.score}"

    def __repr__(self):
        return f"{self.family_name}, {self.name}, {self.ranking}, {self.score}"

    def serialized_players(self):
        serialized_players = {}
        json.dumps(serialized_players)
        serialized_players['family_name'] = self.family_name
        serialized_players['name'] = self.name
        serialized_players['ranking'] = self.ranking
        serialized_players['score'] = self.score
        return serialized_players

    def deserialized_players(self):
        family_name = self.serialized_players()["family_name"]
        name = self.serialized_players()['name']
        ranking = self.serialized_players()['ranking']
        score = self.serialized_players()['score']
        deserialized_players = PlayersIdentity(family_name=family_name, name=name, ranking=ranking)
        return deserialized_players

    def add_player_to_database(self):

        """To insert a player into the database"""

        player_db.insert(self.serialized_players())
        return

