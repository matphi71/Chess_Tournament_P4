""" model round"""

import time
import json
from tinydb import TinyDB, Query

db = TinyDB('db.json')
User = Query()
round_db = db.table('ROUND')

class Round:

    def __init__(self, pairs_to_play=None, beginning_time=None, ending_time=None):
        self.pairs_to_play = pairs_to_play
        #self.beginning_time = beginning_time
        #self.ending_time = ending_time

    def serialized_round(self):
        serialized_round = {}
        json.dumps(serialized_round)
        serialized_round['round_name'] = self.round_name
        serialized_round['pairs_to_play'] = self.pairs_to_play
        #serialized_round['beginning_time'] = self.beginning_time
        #serialized_round['ending_time'] = self.ending_time
        return serialized_round

    def get_points(self):
        pass
        #self.beginning_time = beginning_time
        #self.ending_time = ending_time
        
    def time_start(self):
        beginning_time = time.ctime()
        print(beginning_time)

    def end_notification(self):
        #demander en vue heure démarage et heure fin
        pass
        
    def time_end(self):
        ending_time = time.ctime()
        print(ending_time)

    def add_round_to_database(self):
        round_db.insert(self.serialized_round())
        return

        

    



        