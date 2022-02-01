""" controller Tournament"""

from view.view_players import View
from models import model_tournament, model_round, model_match
from models.model_tournament import Tournament
from models.model_match import Match
from models.model_round import Round
from controller.controlleur_players import ControllerPlayer

from tinydb import TinyDB, Query
db = TinyDB('db.json')
User = Query()


NUMBERS_OF_ROUNDS = 4


class TournamentSetUp:
    
    def __init__(self):
        self.tournament = Tournament
        self.view = View
        self.match = Match
        self.round = Round

    def collecting_tournament_infos(self):

        """ tournament instantiation """

        inputs = self.view().get_tournament_inputs()
        tournament_name = inputs['tournament_name']
        place = inputs['place']
        return self.tournament(tournament_name, place)

    def add_tournament_to_database(self):
        model_tournament.tournaments_db.truncate()
        return self.collecting_tournament_infos().add_tournament_to_database()

    def round_instantiation(self):

        """ match instantiation """

        list_of_pair = []
        for pair_of_players in ControllerPlayer().get_pairs_of_players_first_turn():
            points_award_player_1 = 0
            points_award_player_2 = 0
            player_1 = pair_of_players[0]['family_name']
            player_2 = pair_of_players[1]['family_name']
            input_player_1 = self.view().new_results_match_inputs_player_1()
            input_player_2 = self.view().new_results_match_inputs_player_2()
            if input_player_1 > input_player_2:
                points_award_player_1 += 1
                points_award_player_2 += 0
            elif input_player_2 > input_player_1:
                points_award_player_1 += 0
                points_award_player_2 += 1
            elif input_player_1 == input_player_2 and input_player_1 != 0 and input_player_2 != 0:
                points_award_player_1 += 0.5
                points_award_player_2 += 0.5
            elif input_player_1 and input_player_2 == 0:
                points_award_player_1 += 0
                points_award_player_2 += 0
            match_reference_list = ([[player_1, points_award_player_1], [player_2, points_award_player_2]])
            list_of_pair.append(match_reference_list)
        print(list_of_pair)
        return self.round(list_of_pair)

    def add_round_to_database(self):
        model_round.round_db.truncate()
        self.collecting_round_infos().add_round_to_database()
        return

    def serialized(self):
        return print(self.points_attribution_match().serialized_match())


    def deserialized(self):
        return print(self.points_attribution_match().deserialized_match())

    def add_match_to_database(self):
        model_match.match_db.truncate()
        self.points_attribution_match().add_new_match_to_database()

    def go(self):
        TournamentSetUp().round_instantiation()



