""" model match """

import json

from tinydb import TinyDB, Query

db = TinyDB('db.json')
User = Query()


class Match:

    def __init__(self, player_1=None, player_2=None, points_player_1=0, points_player_2=0):
        self.player_1 = player_1
        self.player_2 = player_2
        self.points_player_1 = points_player_1
        self.points_player_2 = points_player_2

    def __str__(self):
        return f"{self.player_1}, {self.player_2}, {self.points_player_1}, {self.points_player_2}"

    def __repr__(self):
        return f"{self.player_1}, {self.player_2}, {self.points_player_1}, {self.points_player_2}"

    '''def serialized_match(self):
        serialized_match = {}
        json.dumps(serialized_match)
        serialized_match['player_1'] = self.player_1
        serialized_match['points_player_1'] = self.points_player_1
        serialized_match['player_2'] = self.player_2
        serialized_match['points_player_2'] = self.points_player_2
        return serialized_match

    def deserialized_match(self):
        player_1 = self.serialized_match()['player_1']
        player_2 = self.serialized_match()['player_2']
        points_player_1 = self.serialized_match()['points_player_1']
        points_player_2 = self.serialized_match()['points_player_2']
        deserialized_match = Match(player_1=player_1, player_2=player_2,
                                   points_player_1=points_player_1, points_player_2=points_player_2)
        return deserialized_match

    def add_new_match_to_database(self):
        pass
        """ insert a match into the database"""

        #match_db.insert(self.serialized_match())
        #return'''







        
        