""" model Tournament """

from tinydb import TinyDB, Query
import json

User = Query()
db = TinyDB('db.json')
tournaments_db = db.table('TOURNAMENT')


class Tournament:
    
    def __init__(self, tournament_name=None, place=None, number_of_rounds=0, players_index=None):#date, rounds time_control, managers_notes):
        self.tournament_name = tournament_name
        self.place = place
        self. number_of_rounds = number_of_rounds
        #self.date = date
        #time_control
        self.players_index = players_index
        #self.managers_notes = managers_notes

    def __repr__(self):
        pass
        #return f"{self.tournament_name}, {self.place}"

    def __str__(self):
        pass
        #return f"{self.tournament_name}, {self.place}"

    def serialized_tournament_infos(self):
        serialized_tournament_infos = {}
        json.dumps(serialized_tournament_infos)
        serialized_tournament_infos['tournament_name'] = self.tournament_name
        serialized_tournament_infos['place'] = self.place
        serialized_tournament_infos['number_of_rounds'] = self.number_of_rounds
        serialized_tournament_infos['players_index'] = self.players_index
        return serialized_tournament_infos

    def deserialized_tournament_infos(self):
        tournament_name = self.serialized_tournament_infos()['tournament_name']
        place = self.serialized_tournament_infos()['place']
        number_of_rounds = self.serialized_tournament_infos()['number_of_rounds']
        players_index = self.serialized_tournament_infos()['players_index']
        deserialized_tournament_infos = Tournament(tournament_name=tournament_name, place=place,
                                                   number_of_rounds=number_of_rounds, players_index=players_index)
        return deserialized_tournament_infos

    def add_tournament_to_database(self):

        """ To insert a tournament into the database """

        tournaments_db.insert(self.serialized_tournament_infos())
        return
