""" model players """

import json

from tinydb import TinyDB, Query

db = TinyDB('db.json')
User = Query()
player_db = db.table('PLAYERS')


class PlayersIdentity:

    def __init__(self, family_name=None, name=None, birth_date=None, gender=None, ranking=None):
        self.family_name = family_name
        self.name = name
        self.birth_date = birth_date
        self.gender = gender
        self.ranking = ranking
        self.score = 0

    def __str__(self):
        return f"{self.family_name}, {self.name},{self.birth_date}, {self.gender}, {self.ranking}, {self.score}"

    def __repr__(self):
        return f"{self.family_name}, {self.name}, {self.birth_date}, {self.gender}, {self.ranking}, {self.score}"

    def serialized_player(self):
        serialized_player = {}
        json.dumps(serialized_player)
        serialized_player['family_name'] = self.family_name
        serialized_player['name'] = self.name
        serialized_player['birth_date'] = self.birth_date
        serialized_player['gender'] = self.gender
        serialized_player['ranking'] = self.ranking
        serialized_player['score'] = self.score
        return serialized_player

    def deserialized_player(self):
        family_name = self.serialized_player()['family_name']
        name = self.serialized_player()['name']
        birth_date = self.serialized_player()['birth_date']
        gender = self.serialized_player()['gender']
        ranking = self.serialized_player()['ranking']
        score = self.serialized_player()['score']
        deserialized_player = PlayersIdentity(family_name=family_name, name=name, birth_date=birth_date, gender=gender,
                                              ranking=ranking)
        return deserialized_player

    def add_player_to_database(self):
        player_db.insert(self.serialized_player())
        return

