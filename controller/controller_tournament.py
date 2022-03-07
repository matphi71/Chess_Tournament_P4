""" controller Tournament"""

from tinydb import TinyDB, Query

from view.view_players import View
from models import model_tournament, model_players
from models.model_tournament import Tournament
from models.model_round import Round
from models import model_round
from controller.controller_round import ControllerRound
from controller.controller_player import ControllerPlayer
from controller.controller_player import PlayersIdentity


db = TinyDB('db.json')
query = Query()


NUMBERS_OF_ROUNDS = 3


class TournamentSetUp:
    
    def __init__(self):
        self.tournament = Tournament
        self.view = View
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
        rounds_list = []
        model_round.round_db.truncate()
        print("\nROUND n°" + str(i))
        ControllerRound().register_first_round_to_db()
        while i < NUMBERS_OF_ROUNDS:
            i += 1
            print("\nROUND N°" + str(i))
            ControllerRound().register_other_rounds_to_db()
        rounds_list.append(model_round.round_db.all())
        return rounds_list

    def add_tournament_to_database(self):
        model_tournament.tournaments_db.truncate()
        return self.collecting_tournament_infos().add_tournament_to_database()

    def print_tournament_results(self):
        return self.view().print_tournament_results()

    def obtaining_report_y_or_n(self):
        return self.view().see_tournament_results_y_or_n()

    def print_report_display(self):
        if self.obtaining_report_y_or_n() in "Yy":
            self.view().report_display()
        else:
            pass

    @staticmethod
    def go():
        TournamentSetUp().add_tournament_to_database()
        TournamentSetUp().print_tournament_results()
        #TournamentSetUp().obtaining_report_y_or_n()



