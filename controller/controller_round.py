""" controller Round """

from datetime import datetime
from tinydb import TinyDB, Query, where

from models.model_round import Round
from view.view_players import View
from controller.controller_player import ControllerPlayer
from models import model_round

db = TinyDB('db.json')
User = Query()


class ControllerRound:

    def __init__(self):
        self.round = Round
        self.view = View

    def round_instantiation_first_turn(self):

        """ match instantiation first turn"""

        now = datetime.now()
        beginning_time = now.strftime("%m/%d/%Y, %H:%M:%S")
        list_of_pair = []
        i = 1
        for pair_of_players in ControllerPlayer().get_pairs_of_players_first_turn():  # appropriate_turn_list:
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
        ending_time = now.strftime("%m/%d/%Y, %H:%M:%S")
        return self.round(list_of_pair, beginning_time, ending_time)

    def round_instantiation_other_turns(self):

        """ match instantiation first turn"""

        now = datetime.now()
        beginning_time = now.strftime("%m/%d/%Y, %H:%M:%S")
        list_of_pair = []
        i = 1
        for pair_of_players in ControllerPlayer().get_pairs_other_turns():  # appropriate_turn_list:
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
        ending_time = now.strftime("%m/%d/%Y, %H:%M:%S")
        return self.round(list_of_pair, beginning_time, ending_time)

    def add_round_to_database(self):
        #round_number = 0
        #while round_number != NUMBERS_OF_ROUNDS:
        self.round_instantiation().add_round_to_database()
            #round_number += 1
        return

    def serialized(self):
        pass
        #  return print(self.points_attribution_match().serialized_match())

    def deserialized(self):
        pass
        # return print(self.points_attribution_match().deserialized_match())