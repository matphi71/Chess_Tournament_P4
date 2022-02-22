""" controller Tournament"""

from operator import attrgetter
import datetime
from tinydb import TinyDB, Query, where
db = TinyDB('db.json')
query = Query()


from view.view_players import View
from models import model_tournament, model_round, model_players
from models.model_tournament import Tournament
from models.model_round import Round
from controller.controller_player import ControllerPlayer
from controller.controller_round import ControllerRound


NUMBERS_OF_ROUNDS = 4


class TournamentSetUp:
    
    def __init__(self):
        self.tournament = Tournament
        self.view = View
        self.round = Round

    def collecting_tournament_infos(self):

        """ tournament instantiation """
        index_players = []
        inputs = self.view().get_tournament_inputs()
        tournament_name = inputs['tournament_name']
        place = inputs['place']
        date = inputs['date']
        number_of_rounds = NUMBERS_OF_ROUNDS
        time_control = inputs['time_control']
        manager_notes = inputs['manager_notes']
        round_list = self.list_of_round()
        # player_id = self.tournament().players_id
        # players = model_players.player_db.all()
        return self.tournament(tournament_name, place, date, number_of_rounds, time_control, manager_notes, round_list)
        # players_index)

    def list_of_round(self):
        print(model_players.player_db.all())
        i = 1
        round_list = []
        print("\nROUND n°" + str(i))
        first_turn_round = ControllerRound().round_instantiation_first_turn().serialized_round()
        round_list.append(first_turn_round)
        model_tournament.tournaments_db.insert({'round_list': first_turn_round})
        while i < NUMBERS_OF_ROUNDS:
            i += 1
            print("\nROUND N°" + str(i))
            other_turns_list = ControllerRound().round_instantiation_other_turns().serialized_round()
            round_list.append(other_turns_list)
            model_tournament.tournaments_db.insert({'round_list': other_turns_list})
        return round_list

    def add_tournament_to_database(self):
        return self.collecting_tournament_infos().add_tournament_to_database()

    def go(self):
        TournamentSetUp().add_tournament_to_database()








