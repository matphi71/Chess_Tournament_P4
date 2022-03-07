""" model Tournament """

from tinydb import TinyDB, Query
import json

User = Query()
db = TinyDB('db.json')
tournaments_db = db.table('TOURNAMENT')


class Tournament:
    
    def __init__(self, tournament_name=None, place=None, date=None, number_of_rounds=0, players_index=None,
                 rounds_list=None, time_control=None, manager_notes=None):
        self.tournament_name = tournament_name
        self.place = place
        self.date = date
        self. number_of_rounds = number_of_rounds
        self.players_index = players_index
        self.rounds_list = rounds_list
        self.time_control = time_control
        self.manager_notes = manager_notes

    def __repr__(self):
        return f"{self.tournament_name}, {self.place}, {self.date}, {self.number_of_rounds}, {self.players_index}," \
               f" {self.rounds_list}, {self.time_control}, {self.manager_notes}"

    def __str__(self):
        return f"{self.tournament_name}, {self.place}, {self.date}, {self.number_of_rounds}, {self.players_index}," \
               f" {self.rounds_list}, {self.time_control}, {self.manager_notes}"

    def serialized_tournament_infos(self):
        serialized_tournament_infos = {}
        json.dumps(serialized_tournament_infos)
        serialized_tournament_infos['tournament_name'] = self.tournament_name
        serialized_tournament_infos['place'] = self.place
        serialized_tournament_infos['date'] = self.date
        serialized_tournament_infos['number_of_rounds'] = self.number_of_rounds
        serialized_tournament_infos['time_control'] = self.time_control
        serialized_tournament_infos['manager_notes'] = self.manager_notes
        serialized_tournament_infos['players_index'] = self.players_index
        serialized_tournament_infos['rounds_list'] = self.rounds_list
        return serialized_tournament_infos

    def deserialized_tournament_infos(self):
        tournament_name = self.serialized_tournament_infos()['tournament_name']
        place = self.serialized_tournament_infos()['place']
        date = self.serialized_tournament_infos()['date']
        number_of_rounds = self.serialized_tournament_infos()['number_of_rounds']
        time_control = self.serialized_tournament_infos()['time_control']
        manager_notes = self.serialized_tournament_infos()['manager_notes']
        players_index = self.serialized_tournament_infos()['players_index']
        rounds_list = self.serialized_tournament_infos()['rounds_list']
        deserialized_tournament_infos = Tournament(tournament_name=tournament_name, place=place, date=date,
                                                   number_of_rounds=number_of_rounds, rounds_list=rounds_list,
                                                   players_index=players_index, time_control=time_control,
                                                   manager_notes=manager_notes)
        return deserialized_tournament_infos

    def add_tournament_to_database(self):

        """ To insert a tournament into the database """

        tournaments_db.insert(self.serialized_tournament_infos())
        return
