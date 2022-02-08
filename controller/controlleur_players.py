""" controller players """

from tinydb import Query, where

from view.view_players import View
from models import model_players
from models import model_round
from models.model_players import PlayersIdentity

query = Query()

NUMBER_OF_PLAYERS_TO_ADD = 4


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
        return self.collecting_players_infos().serialized_players()

    def deserialized_players(self):
        return self.collecting_players_infos().deserialized_players()

    def sort_players_by_ranking(self):

        """ sorting players to make pairs for first turn, according to the swiss tournament system """

        players_list = []
        for players in model_players.player_db:
            players_list.append(players)
        sorted_players_list = sorted(players_list, key=lambda k: k['ranking'])
        sorted_players_list.reverse()
        return sorted_players_list

    def get_pairs_of_players_first_turn(self):
        half_players_list = int(len(self.sort_players_by_ranking())/2)
        split_in_half_lower_rankings = self.sort_players_by_ranking()[:half_players_list]
        split_in_half_higher_rankings = self.sort_players_by_ranking()[half_players_list:]
        pairs_of_players_first_tour = list(zip(split_in_half_lower_rankings, split_in_half_higher_rankings))
        print(pairs_of_players_first_tour)
        return pairs_of_players_first_tour

    def updating_player_score(self):
        score_list = []
        player_list = []
        for tuples_match in model_round.round_db:
            for pairs in tuples_match['pairs to play']:
                for player in pairs:
                    score_list.append(player[1])
                    player_list.append(player[0])
        for i, score in enumerate(score_list):
            model_players.player_db.update({'score': score}, where('family_name') == player_list[i])
        return model_players.player_db

    def sort_players_by_score(self):

        """ sorting players to make pairs other but first turn, according to the swiss tournament system """

        players_list = []
        for players in self.updating_player_score():
            players_list.append(players)
        sort_by_rank = sorted(players_list, key=lambda k: k['ranking'], reverse=True)
        sort_by_points = sorted(sort_by_rank, key=lambda k: k['score'], reverse=True)
        # rank is preserved by default option
        print(sort_by_points)

    def get_pairs_other_turns(self):
        pass

    #def go(self):
        #ControllerPlayer().add_players_to_database()
        #ControllerPlayer().updating_player_score()
        #ControllerPlayer().sort_players_by_score()






            
    
















