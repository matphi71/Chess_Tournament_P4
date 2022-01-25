""" model Tournament """

from tinydb import TinyDB, Query
import json
User = Query()

db = TinyDB('db.json')
tournaments_db = db.table('tournaments')


class Tournament:
    
    def __init__(self, tournament_name=None, place=None):#, date, turns_time, rounds, players_index, time_control, managers_notes):
        self.tournament_name = tournament_name
        self.place = place
        #self.date = date
        #self.turns_time = turns_time
        #self.rounds = rounds
        #self.players_index = players_index
        #self.time_control = time_control
        #self.managers_notes = managers_notes

    def __repr__(self):
        return f"{self.tournament_name}, {self.place}"

    def __str__(self):
        return f"{self.tournament_name}, {self.place}"

    def serialized_tournament_infos(self):
        serialized_tournament_infos = {}
        json.dumps(serialized_tournament_infos)
        serialized_tournament_infos['tournament_name'] = self.tournament_name
        serialized_tournament_infos['place'] = self.place
        return serialized_tournament_infos

    def deserialized_tournament_infos(self):
        tournament_name = self.serialized_tournament_infos()['tournament_name']
        place = self.serialized_tournament_infos()['place']
        deserialized_tournament_infos = Tournament(tournament_name=tournament_name, place=place)
        return deserialized_tournament_infos

    def add_tournament_to_database(self):

        """ To insert a tournament into the database """
        
        tournaments_db.insert(self.serialized_tournament_infos())
        return tournaments_db
