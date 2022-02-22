""" model Tournament """

from tinydb import TinyDB, Query
import json

User = Query()
db = TinyDB('db.json')
tournaments_db = db.table('TOURNAMENT')


class Tournament:
    
    def __init__(self, tournament_name=None, place=None, date=None, number_of_rounds=0, time_control=None,
                 player_places=None, players_id=None, round_list=None, manager_notes=None):
        self.tournament_name = tournament_name
        self.place = place
        self.date = date
        self. number_of_rounds = number_of_rounds
        self.time_control = time_control
        self.manager_notes = manager_notes
        self.index_players = []  # players_reference dans pl controlleur
        self.players_id = -1
        self.round_list = []  # deserialised round


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
        serialized_tournament_infos['date'] = self.date
        serialized_tournament_infos['number_of_rounds'] = self.number_of_rounds
        serialized_tournament_infos['time_control'] = self.time_control
        serialized_tournament_infos['manager_notes'] = self.manager_notes
        serialized_tournament_infos['index_players'] = self.index_players
        # serialized_tournament_infos['players_id'] = self.players_id
        serialized_tournament_infos['round_list'] = self.round_list
        return serialized_tournament_infos

    def deserialized_tournament_infos(self):
        tournament_name = self.serialized_tournament_infos()['tournament_name']
        place = self.serialized_tournament_infos()['place']
        date = self.serialized_tournament_infos()['date']
        number_of_rounds = self.serialized_tournament_infos()['number_of_rounds']
        time_control = self.serialized_tournament_infos()['time_control']
        manager_notes = self.serialized_tournament_infos()['manager_notes']
        index_players = self.serialized_tournament_infos()['index_players']
        # players_id = self.serialized_tournament_infos()['players_id']
        round_list = self.serialized_tournament_infos()['round_list']
        deserialized_tournament_infos = Tournament(tournament_name=tournament_name, place=place, date=date,
                                                   number_of_rounds=number_of_rounds, time_control=time_control,
                                                   manager_notes=manager_notes, player_places=index_players,
                                                   round_list=round_list)
        return deserialized_tournament_infos

    def add_tournament_to_database(self):

        """ To insert a tournament into the database """

        tournaments_db.insert(self.serialized_tournament_infos())
        return
