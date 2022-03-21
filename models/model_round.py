""" model round"""

import json
from tinydb import TinyDB, Query

User = Query()
db = TinyDB("db.json")
round_db = db.table("ROUNDS")


class Round:

    """A round is made of pairs to play, a beginning time and an ending time.
    In this class we can add a round to the database"""

    def __init__(self, pairs_to_play=None, beginning_time=None, ending_time=None):
        self.pairs_to_play = pairs_to_play
        self.beginning_time = beginning_time
        self.ending_time = ending_time

    def serialized_round(self):
        serialized_round = {}
        json.dumps(serialized_round)
        serialized_round["pairs_to_play"] = self.pairs_to_play
        serialized_round["beginning_time"] = self.beginning_time
        serialized_round["ending_time"] = self.ending_time
        return serialized_round

    def deserialized_round(self):
        pairs_to_play = self.serialized_round()["pairs_to_play"]
        beginning_time = self.serialized_round()["beginning_time"]
        ending_time = self.serialized_round()["ending_time"]
        deserialized_round = Round(
            pairs_to_play=pairs_to_play,
            beginning_time=beginning_time,
            ending_time=ending_time,
        )
        return deserialized_round

    def add_round_to_database(self):
        round_db.insert(self.serialized_round())
        return
