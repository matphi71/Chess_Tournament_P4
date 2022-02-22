""" controller player """

from tinydb import Query, where
from tinydb.operations import add
from collections import deque

from view.view_players import View
from models import model_players
from models import model_round
from models import model_tournament
from models.model_players import PlayersIdentity
#from controller.controller_tournament import TournamentSetUp

query = Query()

NUMBER_OF_PLAYERS_TO_ADD = 8


class ControllerPlayer:

    def __init__(self):
        self.view = View
        self.model = PlayersIdentity

    def collecting_players_infos(self):

        """ retrieveing players Identity """

        inputs = self.view().get_players_inputs()
        family_name = inputs['family_name']
        name = inputs['name']
        ranking = inputs['ranking']
        return self.model(family_name, name, ranking)

    def add_players_to_database(self):

        """ inserting players to database """
        
        model_players.player_db.truncate()
        added_players = 0
        while added_players != NUMBER_OF_PLAYERS_TO_ADD:
            self.collecting_players_infos().add_player_to_database()
            added_players += 1
        return

    def players_reference(self):
        for players in enumerate(model_players.player_db):
            print(self.deserialized_players())
            # players = model_players.player_db.get(doc_id=int(i))

    def serialized_players(self):
        return self.collecting_players_infos().serialized_player()

    def deserialized_players(self):
        return self.collecting_players_infos().deserialized_player()

    def sort_players_by_ranking(self):

        """ sorting players to make pairs for first turn, according to the swiss tournament system """

        #self.add_players_to_database()
        players_list = []
        for players in model_players.player_db:
            players_list.append(players)
        sorted_players_list = sorted(players_list, key=lambda k: k['ranking'])
        sorted_players_list.reverse()
        self.updating_player_score()
        return sorted_players_list

    def get_pairs_of_players_first_turn(self):
        half_players_list = int(len(self.sort_players_by_ranking())/2)
        split_in_half_lower_rankings = self.sort_players_by_ranking()[:half_players_list]
        split_in_half_higher_rankings = self.sort_players_by_ranking()[half_players_list:]
        pairs_of_players_first_turn = list(zip(split_in_half_lower_rankings, split_in_half_higher_rankings))
        return pairs_of_players_first_turn

    def updating_player_score(self):
        new_score_list = []
        old_score_list = []
        player_list = []
        players_tuple = []
        rounds_len = []
        for last_score in model_players.player_db:
            old_score_list.append(last_score['score'])
        for number_of_rounds in model_tournament.tournaments_db:
            rounds_len.append(number_of_rounds)
        i = len(rounds_len)
        tuples_to_search = model_tournament.tournaments_db.get(doc_id=i)
        try:
            for tuples_match in tuples_to_search['round_list']['pairs to play']:
                for tuples in tuples_match:
                    players_tuple.append(tuples)
        except TypeError:
            pass
        players_tuple.sort()
        for tuple in players_tuple:
            new_score_list.append(float(tuple[1]))
            player_list.append(tuple[0])
        print(player_list)
        print(old_score_list)
        print(new_score_list)
        for i, val in enumerate(new_score_list):
            model_players.player_db.update(add('score', val), where('family_name') == player_list[i])
        print(model_players.player_db.all())
        print(len(model_tournament.tournaments_db))
        return model_players.player_db

    def sort_players_by_score(self):

        """ sorting players to make pairs other but first turn, according to the swiss tournament system.
            If scores are the same, selection is then by ranking and if a player have already face the other,
            he will face the next to come on the list"""

        players_list = []
        for players in self.updating_player_score():
            players_list.append(players)
        sort_by_rank = sorted(players_list, key=lambda k: k['ranking'], reverse=True)
        sort_by_points = sorted(sort_by_rank, key=lambda k: k['score'], reverse=True)
        # rank is preserved by default option
        return sort_by_points

    def get_pairs_other_turns(self):
        new_pairs_list = []
        last_pairs_list = []
        sorted_players = self.sort_players_by_score()
        if model_tournament.tournaments_db.search(where('round_list').exists()):
            for tuples_match in model_tournament.tournaments_db:
                for pair in tuples_match['round_list']['pairs to play']:
                    last_pairs_list.append(pair)
        else:
            return None
        while len(new_pairs_list) <= len(last_pairs_list) and len(sorted_players) > 0:
            player_1 = sorted_players.pop(0)
            player_2 = sorted_players.pop(0)
            players_pair = (player_1, player_2)
            if (player_1['family_name'], player_2['family_name']) in last_pairs_list \
                    or (player_2['family_name'], player_1['family_name']) in last_pairs_list:
                if len(sorted_players) == 2:
                    player_1 = sorted_players.pop(0)
                    player_2 = sorted_players.pop()
                    players_pair = (player_1, player_2)
                    new_pairs_list.append(players_pair)
                else:
                    player_1 = sorted_players.pop(0)
                    player_2 = sorted_players.pop(1)
                    players_pair = (player_1, player_2)
                    new_pairs_list.append(players_pair)
            else:
                new_pairs_list.append(players_pair)
        return new_pairs_list








            
    
















