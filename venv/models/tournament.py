'''model'''

from tinydb import TinyDB, Query

import view
from controller import base

db = TinyDB('db.json')
tournaments_db = db.table('tournaments')
User = Query()



class Tournament:
    
    def __init__(self, name = None):#, place, date, turns_time, rounds, players_index, time_control, managers_notes):
        self.name = base.Controller().new_tournament()
        #self.place = place
        #self.date = date
        #self.turns_time = turns_time
        #self.rounds = rounds
        #self.players_index = players_index
        #self.time_control = time_control
        #self.managers_notes = managers_notes
        
    def new_tournament_infos(self):
        tournaments_db.insert ({'name': self.name})

    def __repr__(self):
        pass

    def __str__(self):
        pass

    def serialize(self):
        pass

    def deserialize(self):
        pass
        