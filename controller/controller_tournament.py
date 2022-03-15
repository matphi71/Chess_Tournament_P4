""" controller Tournament"""

from tinydb import TinyDB, Query

from view.view_tournament import ViewTournament
from models import model_tournament
from models.model_tournament import Tournament
from models.model_round import Round
from models import model_round
from controller.controller_round import ControllerRound
from controller.controller_player import ControllerPlayer


db = TinyDB('db.json')
query = Query()


NUMBERS_OF_ROUNDS = 4


class TournamentSetUp:
    
    def __init__(self):
        self.tournament = Tournament
        self.view = ViewTournament
        self.round = Round

    def collecting_tournament_infos(self):

        """ tournament instantiation """

        inputs = self.view().get_tournament_inputs()
        tournament_name = inputs['tournament_name']
        place = inputs['place']
        date = inputs['date']
        number_of_rounds = NUMBERS_OF_ROUNDS
        time_control = inputs['time_control']
        manager_notes = inputs['manager_notes']
        rounds_list = self.list_of_rounds()
        players_index = ControllerPlayer().players_index()
        return self.tournament(tournament_name, place, date, number_of_rounds, players_index, rounds_list,
                               time_control, manager_notes)

    @staticmethod
    def list_of_rounds():
        i = 1
        list_of_rounds = []
        model_round.round_db.truncate()
        print("\nROUND n°" + str(i))
        ControllerRound().register_first_round_to_db()
        ControllerPlayer().updating_players_score()
        i += 1
        while i < NUMBERS_OF_ROUNDS + 1:
            print("\nROUND N°" + str(i))
            i += 1
            ControllerRound().register_other_rounds_to_db()
        list_of_rounds.append(model_round.round_db.all())
        return list_of_rounds

    def add_tournament_to_database(self):
        model_tournament.tournaments_db.truncate()
        return self.collecting_tournament_infos().add_tournament_to_database()

    def print_tournament_results(self):
        return self.view().print_tournament_results()

    def go(self):
        self.add_tournament_to_database()
        self.print_tournament_results()




