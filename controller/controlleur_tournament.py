""" controller Tournament"""

from operator import attrgetter
import datetime
from tinydb import TinyDB, Query, where
db = TinyDB('db.json')
User = Query()

from view.view_players import View
from models import model_tournament, model_round, model_players
from models.model_tournament import Tournament
from models.model_round import Round
from controller.controlleur_players import ControllerPlayer


NUMBERS_OF_ROUNDS = 4


class TournamentSetUp:
    
    def __init__(self):
        self.tournament = Tournament
        self.view = View
        self.round = Round

    def collecting_tournament_infos(self):

        """ tournament instantiation """
        index = []
        inputs = self.view().get_tournament_inputs()
        tournament_name = inputs['tournament_name']
        place = inputs['place']
        number_of_rounds = NUMBERS_OF_ROUNDS
        #players_1 = model_players.player_db.get(doc_id=1)
        #players = model_players.player_db.search(User.family_name.any)
        #for players_index in enumerate(players):
            #index.append(players_index)
        #print(players)
        return self.tournament(tournament_name, place, number_of_rounds)#, players_index)

    def add_tournament_to_database(self):
        model_tournament.tournaments_db.truncate()
        return self.collecting_tournament_infos().add_tournament_to_database()

    def round_instantiation(self):

        """ match instantiation """
        print("\n")
        beginning_time = datetime.datetime.now()
        print(beginning_time)
        print("\nThe matches arrangement for this tour will be as follow:")
        list_of_pair = []
        i = 1
        for pair_of_players in ControllerPlayer().get_pairs_of_players_first_turn():
            points_award_player_1 = 0
            points_award_player_2 = 0
            player_1 = pair_of_players[0]['family_name']
            player_2 = pair_of_players[1]['family_name']
            print("\nFor match N°" + str(i))
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
            match_reference_list = ([player_1, points_award_player_1], [player_2, points_award_player_2])
            list_of_pair.append(match_reference_list)
            i += 1
        print("\nThe result of this round is: ")
        print(list_of_pair)
        ending_time = datetime.datetime.now()
        print("\n")
        print(ending_time)
        return self.round(list_of_pair)#, beginning_time, ending_time)

    def add_round_to_database(self):
        model_round.round_db.truncate()
        self.round_instantiation().add_round_to_database()
        return

    def serialized(self):
        pass
        #  return print(self.points_attribution_match().serialized_match())

    def deserialized(self):
        pass
        # return print(self.points_attribution_match().deserialized_match())

    # def go(self):
        # TournamentSetUp().round_instantiation()

        # TournamentSetUp().get_pairs_of_players_other_turns()
        # TournamentSetUp().collecting_tournament_infos()
        # TournamentSetUp().add_round_to_database()
        # TournamentSetUp().sort_players_by_points()
        # TournamentSetUp().updating_player_score()





