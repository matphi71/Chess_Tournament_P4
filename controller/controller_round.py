""" controller Round """

from datetime import datetime
from tinydb import TinyDB, Query

from models.model_round import Round
from view.view_tournament import ViewTournament
from controller.controller_player import ControllerPlayer
from models import model_round

db = TinyDB('db.json')
User = Query()


class ControllerRound:

    def __init__(self):
        self.round = Round
        self.view = ViewTournament

    def round_instantiation_first_turn(self):

        """ match instantiation first turn """

        now = datetime.now()
        beginning_time = now.strftime("%m/%d/%Y, %H:%M:%S")
        list_of_pair = []
        i = 1
        for pair_of_players in ControllerPlayer().get_pairs_of_players_first_turn():
            points_award_player_1 = 0
            points_award_player_2 = 0
            player_1 = pair_of_players[0]['family_name']
            player_2 = pair_of_players[1]['family_name']
            print("\nFor match N°" + str(i))
            input_player_1 = int(input(f"enter result of player named {player_1}: "))
            input_player_2 = int(input(f"enter result of player named {player_2}: "))
            #input_player_1 = self.view().new_results_match_inputs_player_1()
            #input_player_2 = self.view().new_results_match_inputs_player_2()
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

    def register_first_round_to_db(self):
        model_round.round_db.truncate()
        self.round_instantiation_first_turn().add_round_to_database()

    def round_instantiation_other_turns(self):

        """ match instantiation other turns """

        now = datetime.now()
        beginning_time = now.strftime("%m/%d/%Y, %H:%M:%S")
        list_of_pair = []
        i = 1
        for pair_of_players in ControllerPlayer().get_pairs_other_turns():
            points_award_player_1 = 0
            points_award_player_2 = 0
            player_1 = pair_of_players[0]['family_name']
            player_2 = pair_of_players[1]['family_name']
            print("\nFor match N°" + str(i))
            input_player_1 = int(input(f"enter result of player named {player_1}: "))
            input_player_2 = int(input(f"enter result of player named {player_2}: "))
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

    def register_other_rounds_to_db(self):
        self.round_instantiation_other_turns().add_round_to_database()
